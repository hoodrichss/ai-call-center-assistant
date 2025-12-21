import customtkinter as ctk
import threading
import speech_recognition as sr
from api import AIbrain

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class AssistantGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("AI ASSISTANT")
        self.geometry("950x650")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_rowconfigure(2, weight=0)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="AI OPERATOR", font=("Arial", 20, "bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=20)
        
        self.status_label = ctk.CTkLabel(self.sidebar, text="Загрузка...", text_color="orange")
        self.status_label.grid(row=1, column=0, padx=20)

        self.chat = ctk.CTkTextbox(self, width=600, font=("Segoe UI", 16), wrap="word")
        self.chat.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")
        self.chat.configure(state="disabled")

        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.grid(row=2, column=1, padx=20, pady=20, sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.mic_progress = ctk.CTkProgressBar(self.input_frame, height=10, width=400)
        self.mic_progress.set(0)
        self.mic_progress.grid_remove()

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Напишите вопрос...", height=40)
        self.entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.entry.bind("<Return>", lambda e: self.on_send())

        self.btn_send = ctk.CTkButton(self.input_frame, text="➤", width=50, height=40, command=self.on_send)
        self.btn_send.grid(row=0, column=1, padx=(0, 10))

        self.btn_mic = ctk.CTkButton(self.input_frame, text="🎤", width=50, height=40,fg_color="#D92828", hover_color="#B01E1E", command=self.on_mic)
        self.btn_mic.grid(row=0, column=2)

        self.is_listening = False
        
        self.brain = None
        threading.Thread(target=self.load_brain, daemon=True).start()

    def load_brain(self):
        try:
            self.brain = AIbrain()
            self.status_label.configure(text="● СИСТЕМА ГОТОВА", text_color="#2CC985")
            self.write_chat("System", "База знаний подключена. Жду запросов.")
        except Exception as e:
            self.status_label.configure(text="ОШИБКА API", text_color="red")
            self.write_chat("System", f"Критическая ошибка: {e}")

    def write_chat(self, sender, text):
        self.chat.configure(state="normal")
        
        if sender == "You":
            self.chat.insert("end", f"\n👤 ВЫ: {text}\n")
        elif sender == "Bot":
            self.chat.insert("end", f"\n🤖 AI:\n{text}\n")
            self.chat.insert("end", "—"*40 + "\n")
        else: # system
            self.chat.insert("end", f"\n[INFO]: {text}\n")
            
        self.chat.configure(state="disabled")
        self.chat.see("end")

    def on_send(self):
        text = self.entry.get()
        if not text.strip(): return
        if self.brain is None:
            self.write_chat("System", "Система еще загружается...")
            return
            
        self.entry.delete(0, "end")
        self.write_to_ai(text)

    def on_mic(self):
        if self.is_listening: return  # защита от двойного кликa
        
        self.is_listening = True
        self.btn_mic.configure(state="disabled", text="👂")
        
        self.mic_progress.grid(row=1, column=0, columnspan=3, pady=(10, 0), sticky="ew")
        self.mic_progress.configure(mode="indeterminate")
        self.mic_progress.start()
        
        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        r = sr.Recognizer()
        text = ""
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                self.write_chat("System", "Говорите...")
                
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
                
                self.stop_listening_animation()
                self.write_chat("System", "Обработка голоса...")
                
                text = r.recognize_google(audio, language="ru-RU")
        
        except sr.WaitTimeoutError:
            self.write_chat("System", "Тишина... (Таймаут)")
        except sr.UnknownValueError:
            self.write_chat("System", "Не удалось разобрать речь.")
        except Exception as e:
            self.write_chat("System", f"Ошибка микрофона: {e}")
        finally:
            self.stop_listening_animation()
            self.is_listening = False
            
            self.btn_mic.configure(state="normal", text="🎤", fg_color="#D92828")

        if text:
            self.write_to_ai(text)

    def stop_listening_animation(self):
        """убирает прогресс-бар"""
        self.mic_progress.stop()
        self.mic_progress.grid_forget()

    def write_to_ai(self, text):
        self.write_chat("You", text)
        
        def run():
            response = self.brain.ask(text) 
            self.write_chat("Bot", response)
            
        threading.Thread(target=run, daemon=True).start()

if __name__ == "__main__":
    app = AssistantGUI()
    app.mainloop()
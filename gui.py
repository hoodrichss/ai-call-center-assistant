import customtkinter as ctk
import threading
import speech_recognition as sr
from api import AIbrain

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class AssistantGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("ASSISTANT")
        self.geometry("900x600")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="AI SUPPORT", font=("Arial", 20, "bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=20)
        
        self.status_label = ctk.CTkLabel(self.sidebar, text="Загрузка...", text_color="orange")
        self.status_label.grid(row=1, column=0, padx=20)

        self.chat = ctk.CTkTextbox(self, width=600, font=("Consolas", 14))
        self.chat.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky="nsew")
        self.chat.configure(state="disabled")
      
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.grid(row=2, column=1, padx=20, pady=20, sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Введите запрос...")
        self.entry.grid(row=0, column=0, padx=(0, 10), sticky="ew", ipady=10)
        self.entry.bind("<Return>", lambda e: self.on_send())

        self.btn_send = ctk.CTkButton(self.input_frame, text="➤", width=50, command=self.on_send)
        self.btn_send.grid(row=0, column=1, padx=(0, 10))

        self.btn_mic = ctk.CTkButton(self.input_frame, text="🎤", width=50, fg_color="#D92828", 
                                     hover_color="#B01E1E", command=self.on_mic)
        self.btn_mic.grid(row=0, column=2)

        self.brain = None
        threading.Thread(target=self.load_brain).start()



    def load_brain(self):
        try:
            self.brain = AIbrain()
            self.status_label.configure(text="● ГОТОВ", text_color="#00FF00")
            self.write_chat("System", "Ассистент готов к работе")
        except Exception as e:
            self.status_label.configure(text="ОШИБКА", text_color="red")
            self.write_chat("System", f"Ошибка запуска: {e}")

    def write_chat(self, sender, text):
        self.chat.configure(state="normal")
        if sender == "You":
            self.chat.insert("end", f"\n👤 ВЫ: {text}\n")
        elif sender == "Bot":
            self.chat.insert("end", f"\n🤖 Робот:\n{text}\n" + "—"*30 + "\n")
        else:
            self.chat.insert("end", f"\n[INFO]: {text}\n")
        self.chat.configure(state="disabled")
        self.chat.see("end")

    def on_send(self):
        text = self.entry.get()
        if not text: return
        if self.brain is None:
            self.write_chat("System", "Еще не загрузился, ожидайте...")
            return
            
        self.entry.delete(0, "end")
        self.write_to_ai(text)

    def on_mic(self):
        threading.Thread(target=self.listen).start()

    def listen(self):
        r = sr.Recognizer()
        self.btn_mic.configure(state="disabled", text="👂")
        try:
            with sr.Microphone() as source:
                self.write_chat("System", "Слушаю...")
                audio = r.listen(source, timeout=5)
                text = r.recognize_google(audio, language="ru-RU")
                self.write_to_ai(text)
        except Exception as e:
            self.write_chat("System", "Не расслышал.")
        finally:
            self.btn_mic.configure(state="normal", text="🎤")

    def write_to_ai(self, text):
        """Отправляем текст в api.py"""
        self.write_chat("You", text)
        
        def run():
            response = self.brain.ask(text) 
            self.write_chat("Bot", response)
            
        threading.Thread(target=run).start()

if __name__ == "__main__":
    app = AssistantGUI()
    app.mainloop()
import google.generativeai as genai
import config

class AIbrain:
    def __init__(self):
        self._configure()
        self.system_prompt = self._load_file(config.PROMPT_PATH)
        self.knowledge_base = self._load_file(config.KB_PATH)
        
        self.model = genai.GenerativeModel(
            config.MODEL_NAME,
            generation_config={"temperature": 0.1}
        )

    def _configure(self):
        if not config.API_KEY:
            raise ValueError("Нет API ключа!")
        genai.configure(api_key=config.API_KEY)

    def _load_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Ошибка: Файл не найден."

    def ask(self, user_query):
        """Главная функция: Вопрос -> Ответ"""
        try:
            full_request = f"""
            {self.system_prompt}

            === БАЗА ЗНАНИЙ ===
            {self.knowledge_base}
            === КОНЕЦ БАЗЫ ===

            ВОПРОС ОПЕРАТОРА: {user_query}
            """
            
            response = self.model.generate_content(full_request)
            return response.text
            
        except Exception as e:
            return f"Ошибка нейросети: {e}"

#только если запустить файл напрямую (для теста)
if __name__ == "__main__":
    brain = AIbrain()
    print(brain.ask("Тестовый вопрос: завис cisco"))
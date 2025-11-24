# 📞 AI Contact Center Copilot (Enterprise MVP)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/LLM-Google%20Gemini-orange)
![Architecture](https://img.shields.io/badge/Architecture-RAG-purple)
![Status](https://img.shields.io/badge/Status-Prototype-green)

[🇺🇸 English](#-english-version) | [🇷🇺 Русский](#-русская-версия)

---

## 🇺🇸 English Version

Next-generation AI Assistant for Support Operators.
Designed to act as a "Second Brain" for the operator, integrated directly into the CRM interface (Ozon/Bitrix/Custom) via an overlay/extension architecture.

The Goal: Transform every junior operator into a Senior Specialist instantly by providing real-time, context-aware hints and strict compliance control.

### 🚀 Core Features (Implemented & Vision)

#### 1. 🧠 The "Centaur" Brain (RAG)
*   Context-Aware Answers: The AI doesn't just chat; it searches the corporate Knowledge Base (`knowledgebase.txt`) to provide 100% accurate, script-compliant answers.
*   No Hallucinations: Strict system prompting ensures the bot never invents facts.

#### 2. 🎙️ Voice & Chat Modules
*   Real-time Transcription: Listens to the call via microphone, converts Speech-to-Text, and generates answers before the client finishes speaking.
*   Smart Scripts: For chat support, the AI generates ready-to-paste responses.
    *   *Example:* "Client missing tomatoes for $2" -> AI calculates refund + generates apology script automatically.

#### 3. 🛡️ AI Supervisor (Compliance Guardrails)
*   Real-time Monitoring: The AI analyzes operator intent.
*   Safety Checks: If an operator tries to drop a call or refuse a refund illegally, the AI intervenes: *"Warning: Critical Error. Do not hang up. Offer compensation X according to protocol."*

#### 4. 🧩 Seamless Integration (Roadmap)
*   Overlay Interface: Designed to work as a browser extension or embedded widget within the CRM (e.g., Ozon Admin), eliminating "Alt+Tab" switching.
*   SSO (Single Sign-On): Automatic authorization linked to the operator's ID.

### 🗺️ Technical Roadmap
- [x] Core Logic: Python backend with Google Gemini API integration.
- [x] RAG Engine: Retrieval from local text-based Knowledge Base.
- [x] GUI: Modern Dark-Mode interface (`customtkinter`) for testing.
- [ ] Browser Extension: Migrating UI to Chrome Extension for CRM injection.
- [ ] Admin Panel: Web-interface for Team Leads to update scripts without coding.
- [ ] X-Wiki Sync: Auto-updating Knowledge Base via corporate Wiki API.

### 🛠 Tech Stack
*   Backend: Python, Google Generative AI, SpeechRecognition.
*   Frontend (MVP): CustomTkinter (Desktop App).
*   Target Frontend: JavaScript/React (Chrome Extension or etc).

---

## 🇷🇺 Русская Версия

Интеллектуальный Копилот для операторов Колл-центра (Enterprise решение).

Система, работающая по принципу «Экзоскелет для мозга». Бот интегрируется в рабочий процесс оператора и берет на себя поиск информации, расчеты компенсаций и контроль соблюдения регламентов.

Цель: Снижение AHT (среднего времени звонка), уменьшение ошибок новичков и предотвращение выгорания ОП.

### ⚡️ Ключевые возможности (текущие и планируемые)

#### 1. 🧠 Гибридный интеллект (RAG)
*   Бот использует Retrieval Augmented Generation: он ищет ответы строго в утвержденной Базе Знаний.
*   Минимизация «отсебятины»: оператор читает проверенный, юридически верный скрипт.

#### 2. 🗣️ Модули: голос и чат
*   Анализ звонка: Бот слушает диалог в реальном времени, транскрибирует речь клиента и выводит подсказки на экран быстрее, чем оператор успеет найти их вручную.
*   Умные сценарии: Для чатов бот сам выполняет рутинные действия.
    *   *Кейс:* «Недовоз товара». Бот сам считает сумму, проверяет лимиты компенсации и выдает готовый текст с промокодом.

#### 3. 🛡️ AI-супервайзер (Контроль качества)
*   Превентивная защита: Бот анализирует намерения оператора.
*   Блокировка ошибок: Если оператор хочет совершить критическую ошибку (сброс звонка, грубость, отказ в законном возврате), бот выдает предупреждение: *«Стоп! Это нарушение регламента №5. Сделай вот так...»*.

#### 4. 🧩 Бесшовная интеграция (Архитектура)
*   Продукт проектируется как Overlay (Наложение) поверх рабочих окон CRM (Ozon, Cisco), чтобы оператору не приходилось переключаться между окнами.
*   Ролевая модель: Разграничение прав доступа (Оператор / Тимлид / Админ).

### ⚙️ Установка и запуск прототипа

1.  Клонируйте репозиторий:
   
    git clone https://github.com/hoodrichss/ai-call-center-assistant.git
    
2.  Установите зависимости:
   
    pip install -r requirements.txt
    
3.  API Ключ:
    *   Получите ключ в Google AI Studio.
    *   Создайте файл .env и добавьте: GEMINI_API_KEY=ваш_ключ.
4.  Запуск:
   
    python bot/gui.py
    
### ⚠️ Важное примечание
Проект использует API Google Gemini. В РФ для работы требуется VPN.
База знаний (`knowledgebase.txt`) содержит синтетические (вымышленные) данные. Любые совпадения с реальными компаниями, тарифами или скриптами случайны. Конфиденциальные данные не используются.

---

Author & Architect: hoodrichss

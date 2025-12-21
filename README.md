# 📞 AI Contact Center Copilot (Enterprise MVP)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/LLM-Google%20Gemini-orange)
![Architecture](https://img.shields.io/badge/Architecture-RAG-purple)
![Status](https://img.shields.io/badge/Status-Prototype-green)

[🇺🇸 English](#-english-version) | [🇷🇺 Русский](#-русская-версия)

---

## 🇺🇸 English Version

Next-generation AI Assistant for Support Operators.
Designed to act as a "Second Brain" for the operator, integrated directly into the CRM interface (Azone/Bitrix/Custom) via an overlay/extension architecture.

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

AI-ассистент нового поколения для операторов поддержки.
Спроектирован как **«Второй мозг»** оператора, интегрируемый напрямую в интерфейс CRM (Azone/Bitrix/др) через архитектуру overlay/расширения.

**Главная цель:** Мгновенно трансформировать любого оператора-новичкаа в опытного специалиста за счет контекстных подсказок в реальном времени и жесткого контроля соблюдения регламентов.

### 🚀 Ключевой функционал

#### 1. 🧠 Мозг «Кентавра» (RAG Архитектура)
*   **Контекстные ответы:** ИИ не просто ведет диалог, он выполняет поиск по корпоративной Базе Знаний (`knowledgebase.txt`), предоставляя 100% точные ответы, соответствующие скриптам.
*   **Никаких галлюцинаций:** Строгий системный промптинг гарантирует, что бот опирается только на факты компании и не выдумывает отсебятину.

#### 2. 🎙️ Модули Голоса и Чата
*   **Транскрибация (STT) в реальном времени:** Слушает звонок через микрофон, переводит речь в текст и генерирует ответ еще до того, как клиент закончил фразу.
*   **Умные скрипты:** Для чат-поддержки ИИ генерирует готовые ответы для вставки (Ready-to-paste).
*   *Пример кейса:* «Клиенту не доложили помидоры на 200 руб.» -> ИИ сам считает сумму возврата, проверяет лимиты и генерирует текст извинения с промокодом.

#### 3. 🛡️ AI-Супервайзер (Compliance Guardrails)
*   **Мониторинг намерений:** ИИ анализирует, что собирается сделать оператор.
*   **Предохранители (Safety Checks):** Если оператор пытается сбросить звонок или отказать в возврате, ИИ вмешивается: *"Внимание: Критическая ошибка. Не вешайте трубку. Предложите компенсацию X согласно протоколу №4."*

#### 4. 🧩 Бесшовная интеграция (Roadmap)
*   **Overlay-интерфейс:** Проектируется как браузерное расширение или виджет поверх рабочей CRM, чтобы исключить переключение окон ("Alt+Tab").
*   **SSO (Single Sign-On):** Автоматическая авторизация, привязанная к ID оператора.

### 🗺️ Техническая карта (Roadmap)
- [x] **Core Logic:** Python бэкенд с интеграцией Google Gemini API.
- [x] **RAG Engine:** Механизм поиска (Retrieval) по локальной текстовой Базе Знаний.
- [x] **GUI:** Современный Dark-Mode интерфейс (`customtkinter`).
- [ ] **Browser Extension:** Миграция UI в расширение Chrome для инъекции скрипта в CRM.
- [ ] **Admin Panel:** Веб-интерфейс для Тимлидов (обновление скриптов и БЗ без участия разработчиков).
- [ ] **Wiki Sync:** Автоматическая синхронизация Базы Знаний через API корпоративной XWiki (Confluence/Notion).

### 🛠 Стек технологий
*   **Backend:** Python 3.10+, Google Generative AI (LLM), SpeechRecognition.
*   **Frontend (MVP):** CustomTkinter (Desktop App).
*   **Target Frontend:** JavaScript/React (Chrome Extension).

### ⚙️ Установка и запуск прототипа

1.  Клонируйте репозиторий:
```  
git clone https://github.com/hoodrichss/ai-call-center-assistant.git
```
   
2.  Установите зависимости:
```
   pip install -r requirements.txt
```
   
3.  API Ключ:
    *   Получите ключ в Google AI Studio.
    *   Создайте файл .env и добавьте: GEMINI_API_KEY=ваш_ключ.
4.  Запуск:
```
   python bot/gui.py
```
    
### ⚠️ Важное примечание
Проект использует API Google Gemini. В РФ для работы требуется VPN.
База знаний (`knowledgebase.txt`) содержит синтетические (вымышленные) данные. Любые совпадения с реальными компаниями, тарифами или скриптами случайны. Конфиденциальные данные не используются.

---

Author & Architect: hoodrichss

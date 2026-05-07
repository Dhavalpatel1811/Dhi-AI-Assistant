# 🤖 Dhi — Personal AI Assistant

A fully free, Jarvis-like personal AI assistant built with Python.  
No paid services. Runs entirely on your PC with free cloud AI when online.

> Built phase by phase as a deep-learning journey into AI agents, memory, voice, and automation.

---

# ✨ Current Features (Phases 1 & 2)

- 🎤 Voice input — speak naturally, Dhi listens
- 🔊 Voice output — Dhi speaks back to you
- 🧠 AI brain — powered by Groq API (online) with Ollama local fallback (offline)
- 🔍 Web search — real-time information using DuckDuckGo
- 🤖 Agentic behavior — Dhi decides when to search and when to answer directly
- 💬 Conversation memory — remembers context within a session
- ⌨️ Text fallback — type when voice input is unavailable
- 🌐 Smart mode switching — uses Groq API online and Ollama offline

---

# 🛠️ Tech Stack

- **Python 3.13**
- **Groq API** — free cloud LLM (`llama-3.1-8b-instant`)
- **Ollama** — local LLM fallback (`gemma3:1b`)
- **DuckDuckGo Search** — free real-time web search
- **SpeechRecognition** — speech-to-text
- **pyttsx3** — offline text-to-speech
- **PyAudio** — microphone access

---

# 💻 System Requirements

- OS: Windows 10/11
- RAM: 8GB+
- Python 3.10+
- Ollama installed (for offline fallback)

---

# 🚀 Setup & Installation

## 1. Clone the repository

```bash
git clone https://github.com/Dhavalpatel1811/Dhi-AI-Assistant.git
cd Dhi-AI-Assistant
```

## 2. Create a virtual environment

```bash
python -m venv dhi
dhi\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and add your free Groq API key from:

https://console.groq.com

Example:

```env
GROQ_API_KEY=your_api_key_here
```

## 5. Set up Ollama (offline fallback)

Download Ollama from:

https://ollama.com

Then run:

```bash
ollama pull gemma3:1b
ollama serve
```

## 6. Run Dhi

```bash
python main.py
```

---

# 📁 Project Structure

```text
Dhi/
├── main.py                  # Entry point
├── config.py                # Settings and personality
├── requirements.txt         # Dependencies
├── .env.example             # Environment variables template
├── README.md
│
├── core/
│   ├── agent.py             # Smart agent (Groq + Ollama fallback)
│   ├── groq_engine.py       # Groq API engine (primary)
│   ├── llm.py               # Ollama local engine (fallback)
│   ├── voice_input.py       # Speech-to-text
│   └── voice_output.py      # Text-to-speech
│
└── tools/
    ├── __init__.py
    └── web_search.py        # DuckDuckGo web search tool
```

---

# 🏗️ Architecture

```text
You Speak / Type
        ↓
   Voice Input
        ↓
      Agent
    ↙       ↘
 Online?   Offline?
    ↓          ↓
 Groq API   Ollama
    ↓
Needs Tool?
    ↓
Web Search (DuckDuckGo)
    ↓
    Response
        ↓
   Voice Output
```

---

# 🗺️ Roadmap

- [x] Phase 1 — The Brain & Voice (Foundation)
- [x] Phase 2 — Give It Tools (Agentic Core)
- [ ] Phase 3 — Memory (It Remembers You)
- [ ] Phase 4 — Whisper Voice Upgrade
- [ ] Phase 5 — Computer Control
- [ ] Phase 6 — App Integrations
- [ ] Phase 7 — The Orchestrator (True Agentic Brain)
- [ ] Phase 8 — Polish & Productize

---

# 🔑 Environment Variables

| Variable       | Description                         | Required |
| -------------- | ----------------------------------- | -------- |
| `GROQ_API_KEY` | Free API key from console.groq.com | Yes      |

---

# 👨‍💻 Author

## Dhaval Patel

Building Dhi as a deep-dive portfolio project into AI agents, memory, and automation.  
Follow the journey on LinkedIn!

---

# 📜 License

MIT License — free to use, modify, and learn from.

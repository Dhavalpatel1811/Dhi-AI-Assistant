# 🤖 Dhi — Personal AI Assistant

A fully local, 100% free, Jarvis-like personal AI assistant built with Python.
No cloud APIs. No paid services. Runs entirely on your PC.

---

## ✨ Features (Phase 1)
- 🎤 Voice input — speak naturally, Dhi listens
- 🔊 Voice output — Dhi speaks back to you
- 🧠 Local LLM — powered by Gemma 3 via Ollama (no internet needed)
- 💬 Persistent conversation — remembers context within a session
- ⌨️ Text fallback — type if voice isn't available

---

## 🛠️ Tech Stack
- **Python 3.13**
- **Ollama** — local LLM runner
- **Gemma 3 1B** — lightweight, fast local language model
- **SpeechRecognition** — voice to text
- **pyttsx3** — text to voice (offline)
- **PyAudio** — microphone access

---

## 💻 System Requirements
- OS: Windows 10/11
- RAM: 8GB+
- GPU: NVIDIA GTX 1650 (4GB VRAM)
- Python 3.10+
- Ollama installed

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Dhavalpatel1811/Dhi-AI-Assistant.git
cd Dhi-AI-Assistant
```

### 2. Create virtual environment
```bash
python -m venv dhi
dhi\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama
Download Ollama from https://ollama.com then run:
```bash
ollama pull gemma3:1b
ollama serve
```

### 5. Run Dhi
```bash
python main.py
```

---

## 📁 Project Structure
Dhi/
├── main.py              # Entry point
├── config.py            # Settings and personality
├── requirements.txt     # Dependencies
├── README.md
└── core/
├── llm.py           # LLM engine (Ollama)
├── voice_input.py   # Speech to text
└── voice_output.py  # Text to speech
---

## 🗺️ Roadmap
- [x] Phase 1 — The Brain & Voice (Foundation)
- [ ] Phase 2 — Give it Tools (Agentic Core)
- [ ] Phase 3 — Memory (It Remembers You)
- [ ] Phase 4 — Whisper Voice Upgrade
- [ ] Phase 5 — Computer Control
- [ ] Phase 6 — App Integrations
- [ ] Phase 7 — The Orchestrator (True Agentic Brain)
- [ ] Phase 8 — Polish & Productize

---

## 👨‍💻 Author
**Dhaval Patel**
Building Dhi as a portfolio project to learn AI agents deeply.
Follow the journey on LinkedIn!

---

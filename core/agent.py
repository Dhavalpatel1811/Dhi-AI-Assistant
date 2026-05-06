# core/agent.py — Smart agent with Groq primary + Ollama fallback

import socket
from config import ASSISTANT_NAME


def check_internet() -> bool:
    """Check if internet is available."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect(("8.8.8.8", 53))
        sock.close()
        return True
    except OSError:
        return False


class Agent:
    def __init__(self):
        self.engine = None
        self.mode = None
        self._initialize()

    def _initialize(self):
        if check_internet():
            try:
                from core.groq_engine import GroqEngine
                self.engine = GroqEngine()
                self.mode = "groq"
                print("🌐 Mode: Groq API (online)\n")
            except Exception as e:
                print(f"⚠️  Groq failed: {e}")
                self._fallback_to_local()
        else:
            self._fallback_to_local()

    def _fallback_to_local(self):
        from core.llm import LLMEngine
        self.engine = LLMEngine()
        self.mode = "local"
        print("💻 Mode: Local Ollama (offline)\n")

    def chat(self, user_input: str) -> str:
        return self.engine.chat(user_input)
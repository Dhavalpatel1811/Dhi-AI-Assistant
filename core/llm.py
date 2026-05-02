# core/llm.py — Handles communication with local LLM via Ollama

import ollama
from config import MODEL_NAME, SYSTEM_PROMPT


class LLMEngine:
    def __init__(self):
        self.model = MODEL_NAME
        self.conversation_history = []
        # Inject Dhi's personality as system message
        self.conversation_history.append({
            "role": "system",
            "content": SYSTEM_PROMPT
        })

    def chat(self, user_input: str) -> str:
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Send full conversation to Ollama
        response = ollama.chat(
            model=self.model,
            messages=self.conversation_history
        )

        assistant_reply = response["message"]["content"]

        # Add Dhi's reply to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        return assistant_reply
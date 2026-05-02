# main.py — Entry point for Dhi

from core.llm import LLMEngine
from core.voice_input import VoiceInput
from core.voice_output import VoiceOutput
from config import ASSISTANT_NAME


def main():
    print(f"Starting {ASSISTANT_NAME}...\n")

    llm = LLMEngine()
    voice_in = VoiceInput()
    voice_out = VoiceOutput()

    voice_out.speak(f"Hello Sir! I am {ASSISTANT_NAME}, your personal assistant. How can I help you today?")

    while True:
        try:
            # Get input — voice or text fallback
            user_input = voice_in.listen()

            # If voice failed, fallback to text
            if not user_input:
                user_input = input("You (type): ").strip()

            if not user_input:
                continue

            # Exit commands
            if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                voice_out.speak("Goodbye Sir! Have a great day!")
                break

            # Get response from LLM
            response = llm.chat(user_input)

            # Speak the response
            voice_out.speak(response)

        except KeyboardInterrupt:
            voice_out.speak("Goodbye Sir!")
            break


if __name__ == "__main__":
    main()
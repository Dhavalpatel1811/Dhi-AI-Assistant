# main.py — Entry point for Dhi

from core.agent import Agent
from core.voice_input import VoiceInput
from core.voice_output import VoiceOutput
from config import ASSISTANT_NAME


def main():
    print(f"Starting {ASSISTANT_NAME}...\n")

    agent = Agent()
    voice_in = VoiceInput()
    voice_out = VoiceOutput()

    voice_out.speak(f"Hello Sir! I am {ASSISTANT_NAME}, your personal assistant. How can I help you today?")

    while True:
        try:
            user_input = voice_in.listen()

            if not user_input:
                user_input = input("You (type): ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                voice_out.speak("Goodbye Sir! Have a great day!")
                break

            response = agent.chat(user_input)
            voice_out.speak(response)

        except KeyboardInterrupt:
            voice_out.speak("Goodbye Sir!")
            break


if __name__ == "__main__":
    main()
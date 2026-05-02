# core/voice_output.py — Text to Speech (Dhi speaks)

import pyttsx3


class VoiceOutput:
    def speak(self, text: str):
        print(f"\nDhi: {text}\n")
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", 175)
            engine.setProperty("volume", 1.0)

            # Pick male voice for Jarvis feel
            voices = engine.getProperty("voices")
            for voice in voices:
                if "david" in voice.name.lower() or "male" in voice.name.lower():
                    engine.setProperty("voice", voice.id)
                    break

            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"⚠️ Voice output error: {e}")
import pyttsx3


def speech_to_text(text, rate=100, volume=1, voice_type="F"):
    engine = pyttsx3.init()  # object creation
    engine.setProperty("rate", rate)  # setting up new voice rate
    engine.setProperty("volume", volume)  # setting up volume level  between 0 and 1
    voices = engine.getProperty("voices")  # getting details of current voice
    if voice_type == "M":
        engine.setProperty("voice", voices[0].id)
    elif voice_type == "F":
        # changing index, changes voices. 1 for female
        engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":
    speech_to_text("PROGRAM STARTED, PRESS BUTTON TO CAPTURE")

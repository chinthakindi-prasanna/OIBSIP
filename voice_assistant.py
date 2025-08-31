import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    print(f"[Assistant]: {text}")   # Debug print
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to user command and convert to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("🔎 Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"✅ You said: {query}")
    except Exception:
        print("❌ Sorry, could not understand. Please say again.")
        return None
    return query.lower()

def main():
    print("🚀 Voice assistant started!")   # Debug message
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        print("👉 Waiting for your command...")
        query = take_command()

        if query is None:
            continue

        if "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\Public\\Music"  # change to your music folder
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music")
                else:
                    speak("No music found in your folder")
            else:
                speak("Music folder does not exist")

        elif "exit" in query or "quit" in query or "stop" in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I can't do that yet.")

# ✅ Correct entry point
if __name__ == "__main__":
    main()

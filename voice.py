import speech_recognition as sr
from datetime import datetime
import pyttsx3
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    return recognizer.recognize_google(audio)

def handle_command(command):
    if "hello" in command.lower():
        speak("Hello! How can I help you?")
    elif "time" in command.lower():
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command.lower():
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command.lower():
        query = command.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        try:
            command = get_audio()
            print(f"You said: {command}")
            handle_command(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

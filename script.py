
import speech_recognition as sr
import openai

from os import system
openai.api_key = 'API_KEY'

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")

    while True:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)

            if text == 'stop':
                print("Program stopped.")
                break
            response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"Responce in a paragrapgh on the follofing question: {text}\n",
            max_tokens=100
        )
            answer = response.choices[0].text.strip()

            print("ChatGPT response:", answer)
            system(f"say -v Samantha {answer}")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error:", e)
   
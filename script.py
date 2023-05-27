# import time

# import speech_recognition as sr


# # this is called from the background thread
# def callback(recognizer, audio):
#     # received audio data, now we'll recognize it using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


# r = sr.Recognizer()
# m = sr.Microphone()
# with m as source:
#     r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# # start listening in the background (note that we don't have to do this inside a `with` statement)
# stop_listening = r.listen_in_background(m, callback)
# # `stop_listening` is now a function that, when called, stops background listening

# # do some unrelated computations for 5 seconds
# for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

# # calling this function requests that the background listener stop listening
# stop_listening(wait_for_stop=False)

# # do some more unrelated things
# while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping
import speech_recognition as sr
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Create a recognizer object
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    # Adjust for ambient noise levels
    r.adjust_for_ambient_noise(source)
    # Listen for audio input from the user
    audio = r.listen(source)

    try:
        # Convert speech to text using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said:", text)

        # Make an API request to ChatGPT
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"What is the answer to life, the universe, and everything?\nUser: {text}\n",
            max_tokens=50
        )
        
        # Get the generated answer from the API response
        answer = response.choices[0].text.strip()
        
        print("ChatGPT response:", answer)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error:", e)


import streamlit as st
from elevenlabs import generate, set_api_key
import openai
import requests

# Global variables

AUDIOS_PATH = "frontend/src/audios/"
AUDIO_PATH = "/audios/"
OPENAI_API_KEY = "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"

def premade_voice(prompt, voice):
    audio_path = f'{AUDIO_PATH}{voice}.mp3'

    audio = generate(
        text=prompt,
        voice=voice,
        model="eleven_monolingual_v1"
    )

    try:
        with open(audio_path, 'wb') as f:
            f.write(audio)

        return audio_path

    except Exception as e:
        print(e)

        return ""

def get_correction_prompt(user_input):
    prompt = f"""
    You are an AI system that serves as a tutor, offering efficient learning methods to help users achieve fluency in English. It should initiate dialogues in English and provide continuous corrections for learning enhancement.
    In each step of conversion fix the sentences in order to improve the English skill. 

    User : "So during my English test, I would like to describe my daily routine in the office and my hobbies during my free time"

    Tutor : 

    "Here's feedback on your previous message:

    Original: "So during my English test, I would like to describe my daily routine in the office and my hobbies during my free time."

    Corrected: "During my English test, I would like to describe my daily routine at the office and my hobbies in my free time."

    Feedback:

        Removed "So" from the beginning of the sentence as it's not necessary.
        Changed "in the office" to "at the office" for more natural phrasing.
        Changed "during my free time" to "in my free time" for a more natural expression.

    Now, let's help you prepare to describe your daily routine at the office and your hobbies in your free time:

    Daily routine at the office: Start by outlining the main tasks and responsibilities you have at work. Then, create a few sentences to describe your typical day, including when you arrive at the office, any meetings you attend, tasks you complete, and when you finish work for the day.

    Example: "I usually arrive at the office around 9 am and start by checking my emails. I often have meetings in the morning to discuss ongoing projects with my team. After lunch, I focus on my main tasks, such as analyzing data or writing reports. I finish work around 6 pm."

    Hobbies in your free time: Make a list of your favorite hobbies or activities that you enjoy doing during your free time. Then, create a few sentences to describe each hobby, including why you enjoy it and how often you do it.

    Example: "In my free time, I enjoy reading novels, especially in the science fiction and mystery genres. I find it relaxing and a great way to escape from daily stress. I also like hiking on weekends, as it allows me to explore nature and stay active."

    Remember to practice speaking these sentences out loud to become more comfortable describing your daily routine and hobbies in English."

    User : "{user_input}"
    """
    return prompt


def main():
    st.title("Virtual Tutor for Learning English")

    user_input = st.text_input("Enter a sentence in English")

    if st.button('Submit'):
        # GPT-4 for language translation and teaching
        # The API key and model name should be updated according to GPT-4
        openai.api_key = f"{OPENAI_API_KEY}"  

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": get_correction_prompt(user_input)}
                ]
            )

            lesson = response['choices'][0]['message']['content']
            st.write(lesson)

            # Generate voice
            voice = 'Bella' # Update voice as per requirement
            audio_path = premade_voice(lesson, voice)
            
            if audio_path:
                audio_file = open(audio_path, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


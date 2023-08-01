# AI English Tutor : ElevenLabs AI Hackathon Project


AI English Tutor is an innovative solution designed to improve English fluency through advanced artificial intelligence technologies. Utilizing the capabilities of OpenAI's GPT-3.5-Turbo, ElevenLabs's Speech Synthesis with multiple voice options, and Streamlit, this application provides interactive and constructive dialogues for an optimized language learning experience.

## Technologies Used

1. **OpenAI's GPT-3.5-Turbo**: The AI tutor is powered by OpenAI's cutting-edge language model that underpins the dialogue and correction mechanisms. It's equipped to comprehend context, deliver accurate responses, and offer extensive language corrections.

   Example:
   ```python
   openai.ChatCompletion.create(
       model="gpt-3.5-turbo-16k",
       messages=[
           {"role": "system", "content": "You are an AI English tutor..."},
           {"role": "user", "content": '"I want to be better to speaking English"'}
       ]
   )
   ```
   
2. **ElevenLabs Speech Synthesis**: This advanced text-to-speech model is capable of converting the tutor's textual output into lifelike speech. With the added option of selecting between multiple voices, it brings an auditory learning dimension to the application, thereby creating an immersive language learning environment.

   Example:
   ```python
   from elevenlabs import generate, play

   audio = generate(
       text="Hello, my name is Arnold",
       voice="Arnold",
       model='eleven_multilingual_v1'
   )

   play(audio)
   ```

3. **Streamlit**: Our AI tutor is deployed within an intuitive and user-friendly interface developed using Streamlit. This Python framework enables rapid prototyping, deployment, and user engagement.

   Example:
   ```python
   import streamlit as st

   st.title('AI English Tutor')
   user_input = st.text_input("Enter your text")
   ```

## Running the Application

Before running the application, make sure to install the necessary packages:

```bash
pip install -r requirements.txt
```

You need to set up your OpenAI and ElevenLabs API keys as environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export XI_API_KEY="your-elevenlabs-api-key"
```

Then, to run the application, use:

```bash
streamlit run api.py
```

## Conclusion

AI English Tutor signifies the transformative role of artificial intelligence in education. Through interactive dialogues and real-time feedback, it assures users of substantial improvements in their English proficiency.

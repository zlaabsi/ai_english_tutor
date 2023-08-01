# AI English Tutor : ElevenLabs AI Hackathon Project

![8 5(2)](https://github.com/zlaabsi/ai_english_tutor/assets/52045850/0420b604-1a05-46d4-a5cf-5b48f022b2f9)


AI English Tutor is an innovative application that aims to bolster English proficiency through interactive dialogues, correction prompts, and real-time feedback. The application combines OpenAI's GPT-3.5-Turbo, ElevenLabs's Speech Synthesis, and Streamlit to deliver a potent, user-friendly language learning platform.


## Technologies Used

1. **OpenAI's GPT-3.5-Turbo**: OpenAI's language model serves as the backbone of our AI tutor. It generates dialogue and provides corrections to user input. Below is a snippet demonstrating the request to the GPT-3.5-Turbo model.

    ```python
    correction_prompts = get_correction_prompt(user_input)
    for prompt in correction_prompts:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "system", "content": prompt}
                ]
            )
    ```
   
2. **ElevenLabs Speech Synthesis**: After obtaining the response from the AI tutor, it is converted into audible speech using ElevenLabs's Text to Speech capability. Users can choose from a variety of voices for the output audio.

   ```python
   voice = st.selectbox(
       "Select Voice",
       ["Rachel", "Domi", "Bella", "Antoni", "Elli", "Josh", "Arnold", "Adam", "Sam"]
   )

   # Generate voice
   audio = generate(
       text=lesson,
       voice=voice,
       model='eleven_monolingual_v1'
   )
                
   if audio:
       st.audio(audio, format='audio/mp3')
   ```
   
3. **Streamlit**: Streamlit provides the user interface for our AI tutor. It enables users to input their sentences and interact with the AI tutor. 

   ```python
   st.title("AI Tutor for Learning English 😎 🇬🇧 🇺🇸")
   user_input = st.text_input("Enter a sentence in English")
   if st.button('Submit'):
       # Code to process the input and generate response
   ```

## Running the Application

Before running the application, install the necessary packages:

```bash
pip install -r requirements.txt
```

Ensure to set up your OpenAI and ElevenLabs API keys as environment variables:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export XI_API_KEY="your-elevenlabs-api-key"
```

Finally, to run the application:

```bash
streamlit run api.py
```

## Conclusion

AI English Tutor offers a blend of advanced AI technologies to provide a robust and interactive platform for English language learning. It demonstrates the potential of AI in revolutionizing education, offering immersive and personalized learning experiences.

## Bonus

The Midjourney prompt used to generate the project illustration : `an android steampunk robot with stereotypically British Victorian clothes and features, drinking English tea and levitating against the backdrop of steampunk London , by Albert Bierstadt, by Annibale Carracci, by Wangechi Mutu, Illustration, Artwork, Golden Hour, First-Person, 4k, HDR, Flare, Rembrandt Lighting, Felt, Fibers, VFX --uplight --ar 4:3`

# Return the code that uses the Groq client to get a response from the LLM
import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Function to get a response from the LLM using Groq
def get_llm_response(user_input):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a world class fitness coach and nutritionist and you are helping people achieve their fitness goals. Give them a diet and training plan based on eating habits, health conditions and lifestyle. Check whether the goals are realistic and if they aren't specify it"
            },
            {
                "role": "user",
                "content": user_input
            },
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        stream=False,
        stop=None,
    )
    return response.choices[0].message.content
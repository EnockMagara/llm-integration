from together import Together
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("TOGETHER_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. Please set the TOGETHER_API_KEY environment variable."
    )

client = Together(api_key=api_key)

response = client.chat.completions.create(
    model="meta-llama/Llama-Vision-Free",
    messages=[
        {"role": "user", "content": "What are some fun things to do in New York?"}
    ],
)
print(response.choices[0].message.content)

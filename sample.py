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

def suggest_activity(location):
    """
    Suggest activities for a given location.
    
    Args:
        location (str): The location where activities should take place
    
    Returns:
        str: Activity recommendations
    """
    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[{"role": "user", "content": f"What are some fun things to do in {location}?"}]
    )
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    location = input("Where would you like to find activities? ")
    recommendations = suggest_activity(location)
    print("\nHere are some activities you can do:")
    print(recommendations)

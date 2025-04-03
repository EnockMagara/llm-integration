from together import Together
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get the API key from environment variables
api_key = os.getenv("TOGETHER_API_KEY")

# hard coding user profile here for simplicity
# in a real setting, this would be retrieved
# from a database for example based on the logged in user
user_profile = {
    "name": "Amina Zein",
    "age": 25,
    "location": "New York",
    "interests": ["hiking", "movies", "restaurants", "technology", "fitness"],
    "style": "adventurous",
}


def get_user_input():
    user_preference = input(
        "What are you in the mood for today? (e.g., 'outdoor activities', 'restaurants', 'relaxing activity'): "
    )
    return user_preference


def suggest_activity(user_profile, user_preference):

    prompt = f"""
The user is {user_profile['name']}, a {user_profile['age']}-year-old who lives in {user_profile['location']}. 
Their interests include {', '.join(user_profile['interests'])}. 
They are in the mood for {user_preference}. 
Based on this information, provide some fun and personalized recommendations.
Provide your recommendations as a single numbered list without further details or titles. Do not provide recommendations for activities other than what they asked for.
"""
    client = Together(api_key=api_key)
    if not api_key:
        raise ValueError(
            "API key not found. Please set the TOGETHER_API_KEY environment variable."
        )
    response = client.chat.completions.create(
        model="meta-llama/Llama-Vision-Free",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    user_preference = get_user_input()
    activity_suggestions = suggest_activity(user_profile, user_preference)
    print(f"{activity_suggestions}")

    # Ask for user feedback
    # we don't do anything with this right now but this can be
    # the basis for gather performance info on the usefulness of the suggestions
    feedback = (
        input("Was this recommendation useful to you? (yes/no): ").strip().lower()
    )

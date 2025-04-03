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

    ## construct the prompt as you see fit and query the model here
    ## this function should return the list of suggestions from the model
    return ""


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

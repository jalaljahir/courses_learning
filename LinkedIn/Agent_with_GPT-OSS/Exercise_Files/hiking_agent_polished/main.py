import ollama
from weather import get_weather, get_todays_weather_summary
from parks import get_parks, get_trails
from location import get_current_location
from config import NPS_API_KEY

def query_model(system_prompt, user_prompt):
    """Generic function to query the Ollama model."""
    try:
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
        
        print("Asking model...")
        response = ollama.chat(model='gpt-oss:20b', messages=messages)
        return response['message']['content'].strip()
    except Exception as e:
        print(f"An error occurred while querying the model: {e}")
        return ""

def main():
    if NPS_API_KEY == "YOUR_API_KEY_HERE":
        print("Please set your NPS_API_KEY in config.py before running the script.")
        return

    # --- Step 1: Get Location and Analyze Weather ---
    print("Detecting your location...")
    latitude, longitude, state = get_current_location()
    if not latitude:
        print("Could not detect your location. Please restart and try again.")
        return

    print("Checking the weather near you...")
    weather_data = get_weather(latitude, longitude)
    if not weather_data:
        print("Could not retrieve weather data. Please try again later.")
        return
    weather_summary = get_todays_weather_summary(weather_data)
    print(f"Weather Summary: {weather_summary}")

    if "Could not get" in weather_summary:
        print("Could not get a valid weather summary. Exiting.")
        return

    weather_prompt = f"Based on this forecast, is it a good day for a hike? {weather_summary}"
    weather_system_prompt = "You are an assistant that determines if the weather is good for hiking. Respond with only 'yes' or 'no'."
    model_decision = query_model(weather_system_prompt, weather_prompt).lower()
    
    if not model_decision:
        print("The model failed to provide a weather decision. Please try again later.")
        return
    
    print(f"Model decision: {model_decision}")

    if "no" in model_decision:
        print("\nThe model determined the weather is not suitable for hiking today.")
        return
    
    # --- Step 2: Gather Park and Trail Data ---
    print("\nWeather looks good! Searching for nearby parks and trails...")
    parks_data = get_parks(NPS_API_KEY, state)

    if not parks_data.get("data"):
        print(f"Could not find any National Parks in {state}.")
        return

    parks_and_trails = {}
    for park in parks_data["data"]:
        park_name = park['fullName']
        trails_data = get_trails(NPS_API_KEY, park["parkCode"])
        
        if trails_data.get("data"):
            # Simplified trail filtering
            trails_list = [
                trail['title'] for trail in trails_data["data"]
                if "hiking" in trail.get("tags", []) or "trail" in trail.get("title", "").lower()
            ]
            parks_and_trails[park_name] = trails_list

    if not parks_and_trails:
        print("No parks with hiking trails found in your area.")
        return

    # --- Step 3: Get Opinionated Recommendations from Model ---
    recommendations_system_prompt = "You are an expert hiking guide. Your task is to analyze the following list of parks and trails and recommend the top 2-3 options for a hike today. Provide a brief, opinionated reason for each recommendation, explaining why it's a good choice (e.g., 'Best for views,' 'Great for a challenge,' 'Perfect for a relaxing walk')."
    
    prompt_data = ""
    for park_name, trails in parks_and_trails.items():
        prompt_data += f"\nPark: {park_name}\n"
        if trails:
            for trail in trails:
                prompt_data += f"  - Trail: {trail}\n"
        else:
            prompt_data += "  - No specific trails listed.\n"
            
    recommendations = query_model(recommendations_system_prompt, f"Here are the available parks and trails:\n{prompt_data}")
    print("\n--- Hiking Recommendations ---")
    print(recommendations)

if __name__ == '__main__':
    main()

import requests

def get_parks(api_key, state_code):
    url = f"https://developer.nps.gov/api/v1/parks?stateCode={state_code}&api_key={api_key}"
    response = requests.get(url)
    return response.json()
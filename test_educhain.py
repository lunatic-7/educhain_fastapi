import requests

url = "http://localhost:8000/generate-mcq/"

# Define the query parameters
params = {
    "topic": "Physics",
    "level": "Easy",
    "num": 5,
    "api_key": "Your_OpenAI_API_Key_Here",
}

# Make a POST request to the endpoint
response = requests.post(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response data
    print(response.json())
else:
    # Print the error message
    print("Error:", response.text)

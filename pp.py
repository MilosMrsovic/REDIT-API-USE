import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path="mycodes.env")

# Fetch API credentials from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")

# Function to authenticate and get the access token
def get_access_token():
    # Authenticate using client_id and client_secret
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {'grant_type': 'client_credentials'} # Set the grant type to 'client_credentials'
    headers = {'User-Agent': user_agent} # Set the user-agent in the header
    
    try:
        # Send POST request to get the access token
        response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for HTTP errors
        return response.json()['access_token'] # Return the access token
    except requests.exceptions.RequestException as e:
        # If there's an error, print the error message
        print("Error during authentication:")
        print(e)
        return None
    
# Function to fetch the latest posts from a given subreddit
def fetch_latest_posts(subreddit, token):
    headers = {
        'Authorization': f'bearer {token}', # Authorization header with bearer token
        'User-Agent': user_agent  # Include user-agent in the header
    }
    url = f'https://oauth.reddit.com/r/{subreddit}/new?limit=5' # URL to fetch the latest posts from the subreddit
    
    try:
        # Send GET request to fetch the posts
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for HTTP errors
        
        # Parse the response to get the posts
        posts = response.json()['data']['children']
        for post in posts:
            data = post['data']
            print(f"Title: {data['title']}")
            print(f"Author: {data['author']}")
            print(f"Upvotes: {data['ups']}")
            print("\n")

    except requests.exceptions.RequestException as e:
        # If there's an error, print the error message
        print("Error while fetching posts:")
        print(e)

# Main program entry point
if __name__ == "__main__":
    token = get_access_token()   # Get the access token
    if token:
        subreddit = 'python'  # Subreddit to fetch posts from (can be changed)
        fetch_latest_posts(subreddit, token)  # Fetch and display the latest posts

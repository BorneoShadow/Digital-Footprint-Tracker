import requests
from bs4 import BeautifulSoup
import tweepy

# Twitter API authentication (replace with your own keys)
TWITTER_API_KEY = "your_api_key"
TWITTER_API_SECRET = "your_api_secret"
TWITTER_ACCESS_TOKEN = "your_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Setup Twitter API
def twitter_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

# Function to scrape public social media data
def scrape_social_media(username):
    try:
        twitter_data = scrape_twitter(username)
        return twitter_data
    except Exception as e:
        return {"error": str(e)}

# Function to scrape Twitter data
def scrape_twitter(username):
    api = twitter_api()
    try:
        user = api.get_user(screen_name=username)
        return {
            "username": user.screen_name,
            "name": user.name,
            "followers": user.followers_count,
            "description": user.description
        }
    except Exception as e:
        return {"error": str(e)}

# Example use of the scraper
if __name__ == "__main__":
    username = input("Enter the Twitter username to scrape: ")
    data = scrape_social_media(username)
    print(data)

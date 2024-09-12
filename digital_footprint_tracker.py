import os
import pandas as pd
from extract_metadata import extract_metadata
from social_media_scraper import scrape_social_media

# Function to analyze digital footprints
def analyze_footprints(file_path, username):
    print(f"Analyzing digital footprint for: {username}")
    
    # Step 1: Extract metadata from a file
    metadata = extract_metadata(file_path)
    print("\nExtracted Metadata:")
    print(metadata)

    # Step 2: Scrape public social media information
    social_data = scrape_social_media(username)
    print("\nScraped Social Media Data:")
    print(social_data)

    # Step 3: Analyze behavior
    analyze_behavior(social_data)

# Function to analyze online behaviors based on social data
def analyze_behavior(social_data):
    if social_data.get('followers') and social_data['followers'] > 1000:
        print("\nUser is influential based on followers count.")
    else:
        print("\nUser has a moderate digital presence.")

if __name__ == "__main__":
    file_path = input("Enter the file path to analyze metadata: ")
    username = input("Enter the social media username to scrape: ")
    analyze_footprints(file_path, username)

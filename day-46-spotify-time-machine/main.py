import os
import requests
from bs4 import BeautifulSoup as bs
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_APP_CLIENT_ID = os.getenv("SPOTIFY_APP_CLIENT_ID")
SPOTIFY_APP_CLIENT_SECRET = os.getenv("SPOTIFY_APP_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

chosen_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")


# Parse Billboard website


response = requests.get(f"https://www.billboard.com/charts/hot-100/{chosen_date}/")
web_data = response.text
soup = bs(web_data, "html.parser")

rows_song_name = soup.select(selector="li h3")
song_titles = [row.getText().strip("\n,\t") for row in rows_song_name[:100]]
print(song_titles)


# Connect to Spotify using Spotipy


sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(
    client_id=SPOTIFY_APP_CLIENT_ID,
    client_secret=SPOTIFY_APP_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    cache_path="token.txt",
))


# Create a List of top 100 songs


song_year = chosen_date[:4]
song_uris = []

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{song_year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(uri)
    except IndexError:
        print(f"'{song}' doesn't exist in Spotify. Skipped.")


# Create a new playlist for a user and fill it with songs


user_id = sp.current_user()['id']
new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{chosen_date} Billboard Top 100",
    public=False,
    collaborative=False,
    description='Auto-created Spotify playlist using Billboard Top 100'
    )

sp.playlist_add_items(new_playlist["id"], song_uris)

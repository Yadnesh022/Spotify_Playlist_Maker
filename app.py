from flask import Flask, render_template, request, redirect, url_for, flash
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Spotify API credentials
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:3036/callback'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    mood = request.form['mood']
    num_songs = int(request.form['num_songs'])
    language = request.form['language']

    # Mapping of language to Spotify genre
    language_to_genre = {
        "hindi": "indian",
        "english": "pop",
        "spanish": "latin",
    }

    # Validate input language
    if language.lower() not in language_to_genre:
        flash("Error: Language not supported.")
        return redirect(url_for('index'))

    genre = language_to_genre[language.lower()]

    # Initialize Spotipy with user authentication
    scope = "playlist-modify-private playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=scope))

    # Create a new playlist
    user_id = sp.me()["id"]
    playlist_name = f"{language.capitalize()} {mood} Recommendations"
    playlist_description = f"A playlist based on {language.capitalize()} {mood} mood"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)

    # Get recommendations based on mood and genre
    recommendations = sp.recommendations(seed_genres=[genre], limit=num_songs)

    # Add tracks to the playlist
    track_uris = [track['uri'] for track in recommendations['tracks']]
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

    flash(f"Playlist '{playlist_name}' has been created with {len(track_uris)} tracks!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

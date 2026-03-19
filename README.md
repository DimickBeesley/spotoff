# SpotOff

Exports all your Spotify playlists and tracks to CSV.

## Setup

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create an app (or use an existing one).
2. In the app settings, add a Redirect URI: `http://127.0.0.1:8080/callback`
3. If your app is in **Development Mode**, add your Spotify account email under **User Management**.
4. Copy your Client ID and Client Secret.

Create a `.env` file in the project root:

```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/callback
```

## Usage

```bash
pip install -r requirements.txt
python3 spotoff.py > playlists.csv
```

On first run, a browser window will open asking you to authorize the app. After authorizing, the export will begin.

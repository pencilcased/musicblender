import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "f41fbd8cfe0e34f9cc5fd0d464aed3af"  # this is a sample key
API_SECRET = "488551532b42d9636b615aa5a7e3ab90"

# In order to perform a write operation you need to authenticate yourself
username = "kmurpo"
password_hash = pylast.md5("Yingqi1234!")

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=username,
    password_hash=password_hash,
)
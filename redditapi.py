import requests, ctypes, urllib.request, winreg
from pathlib import Path


desktop_wallpaper = 20

subreddit = "ProgrammingHumor"

reddit = requests.get(
    "https://www.reddit.com/r/programminghumor/hot/.json?count=1",
    headers = {
        "User-agent":"NCIGF_Bot"
    }
)

if reddit.status_code != 200:
    exit()

response = reddit.json()

first_post = response["data"]["children"][0]["data"]
title = first_post["title"]
image_url = first_post["url"]
link_to_post = first_post["permalink"]

home_directory = str(Path.home()) + "/"
image_name = image_url.split("/")[-1]

image_local = home_directory + image_name

urllib.request.urlretrieve(image_url, image_local)

ctypes.windll.user32.SystemParametersInfoW(desktop_wallpaper, 0, image_local, 0)

exit(0)
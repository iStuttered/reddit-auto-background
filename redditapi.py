import requests, ctypes, urllib.request, os
from pathlib import Path

def getPostImageFromReddit(subreddit:str = "programminghumor", sort_by:str = "hot") -> str:
    reddit = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/" + sort_by + "/.json?count=1",
        headers = {
            "User-agent":"Hi_Reddit_Bot"
        }
    )

    if reddit.status_code != 200:
        print("Couldn't query reddit.")

    response = reddit.json()

    first_post = response["data"]["children"][0]["data"]
    return first_post["url"]

def downloadImage(external_image_path:str) -> str:

    home_directory = str(Path.home())
    image_name = external_image_path.split("/")[-1]

    image_folder = home_directory + "/Pictures/Reddit/"
    image_local = image_folder + image_name

    if not os.path.exists(image_folder):
        os.mkdir(image_folder)

    urllib.request.urlretrieve(external_image_path, image_local)
    return image_local

def setImageAsWindowsBackground(local_image_path:str) -> str:
    desktop_wallpaper = 20
    ctypes.windll.user32.SystemParametersInfoW(desktop_wallpaper, 0, local_image_path, 0)

external_image = getPostImageFromReddit("programminghumor", "hot")

local_image = downloadImage(external_image)

setImageAsWindowsBackground(local_image)

exit(0)

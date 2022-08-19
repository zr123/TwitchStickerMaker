from bs4 import BeautifulSoup
import wget


if __name__ == '__main__':
    # step 1 -> turn channel name into channel id

    # TODO - get channel id automaticall
    channel_id = 40972890 # admiral bahroo

    # step 2: download index.html from channel-page

    wget.download(f"https://www.twitchemotes.com/channels/{channel_id}/", "downloads/channel_index.html")

    with open("downloads/channel_index.html", "r") as file:
        channel_index = "".join(file.readlines())

    # step 3: parse
    soup = BeautifulSoup(channel_index, 'html.parser')
    images = soup.find_all("img")

    # step 4: download
    for image in images:
        emote_id = image.get("data-image-id")
        emote_name = image.get("data-regex")
        if emote_id is not None:
            # download sticker
            print(f"Downloading {emote_name}")
            wget.download(f"https://static-cdn.jtvnw.net/emoticons/v1/{emote_id}/3.0", f"stickers/{emote_name}.png")

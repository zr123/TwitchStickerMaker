from bs4 import BeautifulSoup
import wget
import os


if __name__ == '__main__':
    # step 1 -> turn channel name into channel id

    # TODO - get channel id automaticall
    channel_id = 40972890 # admiral bahroo

    # step 2: download index.html from channel-page

    filename = wget.download(f"https://www.twitchemotes.com/channels/{channel_id}/", "downloads/index.html")

    with open(filename, "r") as file:
        channel_index = "".join(file.readlines())

    # step 3: parse
    soup = BeautifulSoup(channel_index, 'html.parser')
    images = soup.find_all("img")

    # cleanup
    os.remove(filename)

    # step 4: download
    for image in images[1:]:
        emote_id = image.get("data-image-id")
        emote_name = image.get("data-regex")
        emote_src = image.get("src")
        emote_src = emote_src.replace("/2.0", "/3.0") # get high resolution image
        if emote_id is not None:
            # download sticker
            print(f"Downloading {emote_name}")
            if emote_src.count("animated") > 0:
                wget.download(emote_src, f"stickers/{emote_name}.gif")
            else:
                wget.download(emote_src, f"stickers/{emote_name}.png")
        else:
            pass    # TODO: could be a badge!

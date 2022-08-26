from bs4 import BeautifulSoup
import wget
import os
import time


def resolve_channel_name(channel_name):
    # step 1 -> turn channel name into channel id

    # TODO - get channel id automatically
    channel_id = 40972890  # "admiralbahroo"
    return channel_id


def get_main_page(channel_id):
    # step 2: download index.html from channel-page
    assert(type(channel_id) == int)

    filename = wget.download(f"https://www.twitchemotes.com/channels/{channel_id}/", "index.html")

    with open(filename, "r") as file:
        channel_index_html = "".join(file.readlines())

    # cleanup
    os.remove(filename)

    if channel_index_html == "Channel not found":
        raise Exception("Channel not found")

    return channel_index_html


def download_emote():
    pass


def parse_channel_html(index_html):
    # step 3: parse
    soup = BeautifulSoup(index_html, 'html.parser')
    images = soup.find_all("img")

    savepath = "downloads/" + time.ctime().replace(":", "-")
    os.mkdir(savepath)
    os.mkdir(f"{savepath}/stickers")

    # step 4: download
    for image in images[1:]:
        emote_id = image.get("data-image-id")
        emote_name = image.get("data-regex")
        emote_src = image.get("src")
        emote_src = emote_src.replace("/2.0", "/3.0")  # get high resolution image
        if emote_id is not None:
            # download sticker
            print(f"Downloading {emote_name}")
            if emote_src.count("animated") > 0:
                wget.download(emote_src, f"{savepath}/stickers/{emote_name}.gif")
            else:
                wget.download(emote_src, f"{savepath}/stickers/{emote_name}.png")
        else:
            pass  # TODO: could be a badge!

from bs4 import BeautifulSoup
import wget
import os
import time


def resolve_channel_name(channel_name):
    # TODO
    pass


def get_main_page(channel_id):
    """
    Download index.html from channel-page.

    :param channel_id:
    :return html of the channel page:
    """
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
    os.mkdir(f"{savepath}/badges")
    os.mkdir(f"{savepath}/cheers")

    # step 4: download
    for image in images[1:]:
        emote_id = image.get("data-image-id")
        emote_src = image.get("src")

        if emote_id is not None:
            # sticker
            emote_name = image.get("data-regex")
            emote_src = emote_src.replace("/2.0", "/3.0")  # get high resolution image
            print(f"Downloading {emote_name}")
            if emote_src.count("animated") > 0:
                wget.download(emote_src, f"{savepath}/stickers/{emote_name}.gif")
            else:
                wget.download(emote_src, f"{savepath}/stickers/{emote_name}.png")
        else:
            # badge or cheer
            emote_name = image.parent.text.replace("\n", "")
            if emote_src.count("badge") > 0:
                # badge
                print(f"Downloading badge: {emote_src}")
                wget.download(emote_src, f"{savepath}/badges/{emote_name}.png")
            else:
                # cheer
                print(f"Downloading cheer: {emote_src}")
                file_extension = emote_src.split(".")[-1]
                wget.download(emote_src, f"{savepath}/cheers/{emote_name}.{file_extension}")

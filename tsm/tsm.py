from bs4 import BeautifulSoup
import wget
import os
import time


def download_channel_emotes(channel_name=None, channel_id=None):
    if channel_name is not None:
        channel_id = resolve_channel_name(channel_name)
    else:
        channel_index_html = get_main_page(channel_id)
        parsed_data = parse_channel_html(channel_index_html)
        download_all_emotes(parsed_data)


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


def parse_channel_html(index_html):
    soup = BeautifulSoup(index_html, 'html.parser')
    images = soup.find_all("img")

    results = []
    for image in images[1:]:
        emote_id = image.get("data-image-id")
        emote_src = image.get("src")
        if emote_id is not None:
            emote_type = "sticker"
            emote_name = image.get("data-regex")
            emote_src = emote_src.replace("/2.0", "/3.0")  # get high resolution image
            if emote_src.count("animated") > 0:
                extension = ".gif"
            else:
                extension = ".png"
        else:
            emote_name = image.parent.text.replace("\n", "")
            if emote_src.count("badge") > 0:
                emote_type = "badge"
                extension = "png"
            else:
                emote_type = "cheer"
                extension = emote_src.split(".")[-1]

        results.append({"name": emote_name, "src": emote_src, "type": emote_type, "ext": extension})

    return results


def download_all_emotes(parsed_data, base_path="downloads"):
    savepath = f"{base_path}/" + time.ctime().replace(":", "-")
    os.mkdir(savepath)
    os.mkdir(f"{savepath}/sticker")
    os.mkdir(f"{savepath}/badge")
    os.mkdir(f"{savepath}/cheer")

    for emote in parsed_data:
        download_emote(emote["src"], savepath + "/" + emote["type"], emote["name"], emote["ext"])

    return savepath


def download_emote(src, path, name, extension):
    wget.download(src, f"{path}/{name}.{extension}")

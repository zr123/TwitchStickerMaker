[![Python Package using Conda](https://github.com/zr123/TwitchStickerMaker/actions/workflows/python-package-conda.yml/badge.svg?branch=main)](https://github.com/zr123/TwitchStickerMaker/actions/workflows/python-package-conda.yml)

# Twitch Sticker Maker

Download emotes from a Twitch.tv-channel to be used as stickers in your messenger apps. This code currently scrapes https://www.twitchemotes.com, rather than using the Twitch-API.

# How to use

Install prequisites with `conda env create -f environment.yml` or install them manually.

Afterwards you can use this project from the command line:

```
python tsm.py <channel_id>
```

You can get the channel_id via sites like https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/. The channel id can currently not be automatically resolved.

# Disclaimer

This project is personal usage only! Image copyright lies with Twitch.tv or the respective copyright holders.

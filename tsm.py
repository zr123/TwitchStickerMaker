from sys import argv
import tsm


if __name__ == '__main__':
    channel_id = int(argv[1])
    tsm.download_channel_emotes(channel_id=channel_id)

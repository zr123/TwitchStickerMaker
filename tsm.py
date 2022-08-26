from sys import argv
import tsm


if __name__ == '__main__':
    channel_id = int(argv[1])
    channel_index_html = tsm.get_main_page(channel_id)
    tsm.parse_channel_html(channel_index_html)

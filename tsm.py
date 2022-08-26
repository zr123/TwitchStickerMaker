import tsm


if __name__ == '__main__':
    channel_id = tsm.resolve_channel_name("admiralbahroo")
    channel_index_html = tsm.get_main_page(channel_id)
    tsm.parse_channel_html(channel_index_html)

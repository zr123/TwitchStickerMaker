import subprocess
import pytest
import tsm


def test_get_main_page():
    html = tsm.get_main_page(40972890)
    assert(html.startswith("<!DOCTYPE html>"))


def test_get_main_page_fail():
    with pytest.raises(AssertionError) as e_info:
        tsm.get_main_page(None)


def test_get_main_page_channel_not_found():
    with pytest.raises(Exception) as e_info:
        tsm.get_main_page(0)


def test_parse_channel_html():
    html = """<!DOCTYPE html>
<html lang="en">
<body>
<img src="/derp.png">

</div>>
<div>
<center><a href="/channels/40972890/emotes/305148231"><img src="https://static-cdn.jtvnw.net/emoticons/v2/305148231/static/light/2.0" data-toggle="popover" data-image-id="305148231" class="emote expandable-emote" data-tooltip="<strong>roo1</strong>" data-regex="roo1" /></a><br />roo1</center><br />
</div>

<div class="col-md-2">
<center>
<img src="https://static-cdn.jtvnw.net/badges/v1/20c06547-f205-4b87-8620-966fb6c77ebd/3" />
<br />2000000 Bits
</center><br />
</div> </div>

<div class="col-md-2">
<center>
<img src="https://d3aqoihi2n8ty8.cloudfront.net/partner-actions/40972890/f6f90a40-89d3-4dcf-93be-d6160f5e0c55/10000/light/animated/3.gif" />
<br />10000 Bits
</center><br />
</div>

</body>
</html>
    """
    result = tsm.parse_channel_html(html)
    assert len(result) == 3


def test_download_all_emotes():
    data = [
        {"name": "herp", "src": "https://static-cdn.jtvnw.net/emoticons/v2/305148231/static/light/3.0", "type": "sticker", "ext": "png"},
        {"name": "derp", "src": "https://static-cdn.jtvnw.net/badges/v1/20c06547-f205-4b87-8620-966fb6c77ebd/3", "type": "badge", "ext": "png"},
        {"name": "lulz", "src": "https://d3aqoihi2n8ty8.cloudfront.net/partner-actions/40972890/f6f90a40-89d3-4dcf-93be-d6160f5e0c55/10000/light/animated/3.gif", "type": "cheer", "ext": "gif"},
    ]
    tsm.download_all_emotes(data)


def test_download_channel_emotes():
    tsm.download_channel_emotes(channel_id=40972890)

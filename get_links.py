import urllib.request
import json

def get_all_video_in_channel(channel_id):
    api_key = "AIzaSyBGtA1sEnGJAlIO80c2JaoX1X3jbEk0Zn4"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    print(video_links)
    with open("video_links.txt", "w") as file:
        for link in video_links:
            file.write(link + "\n")
    
    return video_links

get_all_video_in_channel("UCcefcZRL2oaA_uBNeo5UOWg")
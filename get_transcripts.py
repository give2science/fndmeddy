import json
import os
from youtube_transcript_api import YouTubeTranscriptApi


# set the output directory for the transcript files
output_dir = 'transcripts'

# create a folder to store the transcripts
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



# read the list of video URLs from a file
with open("video_links.txt", "r") as file:
    video_links = file.read().splitlines()

# iterate over the list of video URLs
for link in video_links:
    # extract the video ID from the URL
    video_id = link.split('=')[1]
    print(video_id)

    try:
        # retrieve the available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # iterate over all available transcripts
        for transcript in transcript_list:
            # fetch the actual transcript data
            transcript_data = transcript.fetch()


            # write the transcript data to a file in the output directory
            output_file = os.path.join(output_dir, f'{video_id}.json')
            with open(output_file, 'w') as f:
                json.dump(transcript_data, f)
    except:
        pass


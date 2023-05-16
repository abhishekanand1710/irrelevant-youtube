import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import pandas as pd

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_video_details(youtube, ids):

    details = []
    for i in range(0, len(ids), 50):
        temp_ids = ids[i:i+50]
        ids_string = ",".join(temp_ids)
        request = youtube.videos().list(
            part="snippet,contentDetails", id=ids_string
        )
        response = request.execute()

        temp_details = []
        if response["items"]:
            for item in response["items"]:
                if item and item["snippet"]:
                    temp_details.append({"id": item["id"], "title": item["snippet"]["title"], "description": item["snippet"]["description"]})
        details.extend(temp_details)
    return details

def read_csv(file_path):
    df = pd.read_csv(file_path, on_bad_lines="skip")
    return df.video_id.values

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    gb_ids = read_csv("youtube-dataset/GBvideos.csv")
    gb_details = get_video_details(youtube, gb_ids)
    gb_text_details_df = pd.DataFrame(gb_details)
    gb_text_details_df.to_csv("youtube-dataset/GBtext-details.csv")

    us_ids = read_csv("youtube-dataset/USvideos.csv")
    us_details = get_video_details(youtube, us_ids)
    us_text_details_df = pd.DataFrame(us_details)
    us_text_details_df.to_csv("youtube-dataset/UStext-details.csv")

    

if __name__ == "__main__":
    main()
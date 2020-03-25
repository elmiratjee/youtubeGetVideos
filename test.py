import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_839737400366-16nm7ouve15fg7usoccjtoamovd5vjm7.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id="UCLGe0PxyRFWmXVGJKq_gGvw"
    )
    global response
    response= request.execute()
    print(response)


if __name__ == "__main__":
    main()

def getInformation():
    response_json = json.dumps(response)
    title = json.loads(response_json)["items"][0]["snippet"]["title"]
    subCount = json.loads(response_json)["items"][0]["statistics"]["subscriberCount"]
    viewcount = json.loads(response_json)["items"][0]["statistics"]["viewCount"]
    print("Channel: " + title)
    print("Subcribers: " + subCount)
    print("Views: " + viewcount)

getInformation()

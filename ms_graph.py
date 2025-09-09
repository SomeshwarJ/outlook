import os
import webbrowser
import msal
from dotenv import load_dotenv

MS_GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"

def get_access_token(application_id, client_secret, scopes):
    client = msal.ConfidentialClientApplication(
        client_id=application_id,
        client_credential=client_secret,
        authority="https://login.microsoftonline.com/consumers",
    )
    refresh_token = None
    if os.path.exists("referesh_token.txt"):
        with open("referesh_token.txt", "r") as token_file:
            refresh_token = token_file.read().strip()
    
    if refresh_token:
        token_response = client.acquire_token_by_refresh_token(
            refresh_token=refresh_token,
            scopes=scopes
        )
    else:
        auth_request_url = client.get_authorization_request_url(
            scopes=scopes
        )
        webbrowser.open(auth_request_url)
        auth_code = input("Enter the authorization code: ")
        if not auth_code:
            raise ValueError("Authorization code is required.")
        token_response = client.acquire_token_by_authorization_code(
            code=auth_code,
            scopes=scopes
        )
    if 'access_token' in token_response:
        if 'refresh_token' in token_response:
            with open("referesh_token.txt", "w") as token_file:
                token_file.write(token_response['refresh_token'])
        return token_response['access_token']
    else:
        raise Exception("Could not obtain access token: " + str(token_response))

def main():
    load_dotenv()
    application_id = os.getenv("APPLICATION_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    SCOPES = ['User.Read', 'Mail.Send', 'Mail.ReadWrite']
    try:
        access_token = get_access_token(application_id, client_secret, SCOPES)
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        print("Access Token:", headers)
    except Exception as e:
        print("Error obtaining access token:", str(e))

if __name__ == "__main__":
    main()

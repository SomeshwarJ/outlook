import os
from pathlib import Path
import httpx
from dotenv import load_dotenv
from ms_graph import get_access_token, MS_GRAPH_BASE_URL
from outlook import create_attachment

def draft_email(subject):
    email_data = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": "This is a draft email with attachments."
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": "senthilsomeshwar2002@gmail.com"
                    }
                }
            ],
        },
        "saveToSentItems": "false"
    }
    return email_data


def main():
    load_dotenv()
    APPLICATION_ID = os.getenv( 'APPLICATION_ID')
    CLIENT_SECRET = os.getenv( 'CLIENT_SECRET')
    SCOPES = ['User.Read',' Mail.ReadWrite' ]
    
    try:
        access_token = get_access_token(
            application_id=APPLICATION_ID,
            client_secret=CLIENT_SECRET,
            scopes=SCOPES
        )
        headers = {'Authorization': 'Bearer' + access_token}

        email_data = draft_email("Draft Email with Attachments")
        response = httpx.post(
            f"{MS_GRAPH_BASE_URL}/me/sendMail",
            headers=headers,
            json=email_data
        )
        if response.status_code != 202:
            raise httpx.HTTPStatusError(f"Failed to create draft email: {response.text}", request=response.request, response=response)
        print("Draft email created successfully.")
        
    except httpx.HTTPStatusError as e:
        print(f'HTTP Error: {e}' )
    except Exception as e:
        print(f'Error: {e}' )

if __name__ == "__main__":
    main()
import os
import base64
import mimetypes
from pathlib import Path
import httpx
from ms_graph import get_access_token, MS_GRAPH_BASE_URL

def create_attachment(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode('utf-8')
    mime_type = get_mime_type(file_path)
    attachment = {
        "@odata.type": "#microsoft.graph.fileAttachment",
        "name": Path(file_path).name,
        "contentType": mime_type,
        "contentBytes": encoded_content
    }
    return attachment


def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type
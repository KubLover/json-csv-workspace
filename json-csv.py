from __future__ import print_function

import os.path
import csv
import json


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']


def main():
    
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
   
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'path/clientID.json', SCOPES)
            creds = flow.run_local_server(port=0)
    
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('admin', 'directory_v1', credentials=creds)


    json_file_path = 'input.json'
    csv_file_path = 'converted.csv'

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            create_user(service, row)


def create_user(service, user_data):
    user = {
        'primaryEmail': user_data['email'],
        'name': {
            'givenName': user_data['first_name'],
            'familyName': user_data['last_name']
        },
        'password': user_data['password'],
        'changePasswordAtNextLogin': True
    } 
    try:
        created_user = service.users().insert(body=user).execute()
        print(f"User created: {created_user['primaryEmail']} ({created_user['givenName']['fullName']})")
    except Exception as error:
        print(f"Error creating user {user_data['email']}: {error}")

if __name__ == '__main__':
    main()

    
# json-csv-workspace
Simple python script that converts JSON to CSV and creates users in Google Workspace

The script works with Admin SDK: Directory API.

Steps before running the script:

1. Create GCP project - enable Admin SDK: Directory API - https://console.cloud.google.com/apis/enableflow

2. Authorize credentials for the application.
   * Create Credentials https://console.cloud.google.com/apis/credentials 
   * Pick "Desktop app" and download JSON file. 
   * In the code replace line 29 "path/clientID.json" with your credentials.json file.

3. Replace data in input.json file with desired user information.
  * You can add other attributes in JSON and update the code as required.

4. Install google client library for python "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"

5. Run the code - python3 quickstart.py
  * If you are running the code first time, the prompt will ask you to sign in to your workspace admin account.


If you are getting permission error or want to create users without super admin account credentials, do the following:
   
   * Create service account in GCP
   * In the admin.google.com navigate to "API controls"
   * Click "Manage Domain Wide Delegation"
   * Add new client, in the "client ID" field add your service account client ID
   * In OAuth scopes add "https://www.googleapis.com/auth/admin.directory.user" and save
     NOTE: This may take up some time to enable access to your Google services.
     
    
WARNING!

Be careful with the script, if you try to run it several times, Google may disallow creation of users in your directory. "potentially abusive behavior"
In order to get unban, you will need to contact Google Support.

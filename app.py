from flask import Flask, request, jsonify, render_template
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
import os

app = Flask(__name__)

# Path to the service account key file
key_path = '/app/wedding-uploader-412016-5f9a11ebbdac.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

# Scopes for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Authenticate and construct the Drive API client
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Google Drive folder ID where the files will be uploaded
FOLDER_ID = '1TsAFLyG6cB7YejXBtpJqprNFY_DFBjaG'

@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    uploaded_files = request.files.getlist('file')

    if not uploaded_files:
        return jsonify({'error': 'No files uploaded'}), 400

    for file in uploaded_files:
        file_metadata = {
            'name': file.filename,
            'parents': [FOLDER_ID]  # ID of the Google Drive folder to upload into
        }
        media_body = MediaIoBaseUpload(file.stream, mimetype=file.mimetype)

        try:
            drive_service.files().create(
                body=file_metadata,
                media_body=media_body,
                fields='id'
            ).execute()
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Upload successful'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# from flask import Flask, request, jsonify, render_template
# from google.cloud import storage
# from datetime import timedelta
# from google.oauth2 import service_account
# import os
#
# app = Flask(__name__)
#
# key_path = '/app/wedding-uploader-412016-5f9a11ebbdac.json'
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
#
# SCOPES = ['https://www.googleapis.com/auth/drive.file']
# # Initialize Google Cloud Storage client with OAuth 2.0 credentials
# client = storage.Client()
#
# # Initialize Google Cloud Storage client
# bucket_name = 'wedding-uploader-412016_cloudbuild'
# bucket = client.bucket(bucket_name)
#
#
# @app.route('/')
# def upload_form():
#     return render_template('upload.html')
#
#
# @app.route('/upload-image', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#
#     # Define your bucket name
#     blob = bucket.blob(file.filename)
#
#     # Upload the file to Google Cloud Storage
#     blob.upload_from_file(file, content_type=file.content_type)
#
#     return jsonify({'message': 'File uploaded successfully', 'fileName': file.filename})
#
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

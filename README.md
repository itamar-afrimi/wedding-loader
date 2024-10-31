
# Image Upload Script

## About
This Python script enables guests to easily upload images to a designated Google Drive folder. It simplifies the process of collecting images from users without requiring direct access to the Drive account.

## Features
- **User-Friendly**: Allows guests to upload images through a simple interface.
- **Secure Uploads**: Ensures that uploaded images are stored securely in the specified Google Drive folder.
- **Flexible**: Easily customizable to adapt to various project needs.

## Requirements
- Python 3.x
- Google Drive API access
- Necessary libraries:
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-api-python-client`
  
## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Google Drive API:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the Google Drive API.
   - Create credentials (OAuth 2.0 Client IDs) and download the `credentials.json` file.
   - Place the `credentials.json` file in the project directory.

## Usage
1. Run the script:
   ```bash
   python app.py
   ```

2. Follow the on-screen instructions to upload images.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Google Drive API](https://developers.google.com/drive)
- [Python](https://www.python.org/)
```

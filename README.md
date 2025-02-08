# YouTube Audio Downloader

A simple Python-based GUI application using **Flet** that allows users to download audio from YouTube by entering song names or YouTube links. The actual downloading is handled by a Node.js script using **ytdl-core**.

## Features
- Enter song names (comma-separated) or YouTube links
- Automatically finds YouTube links for song names
- Downloads audio in **WebM** format
- Simple and intuitive Flet-based UI

---

## Installation
### 1. Install Python Dependencies
Ensure you have **Python 3.8+** installed, then run:
```sh
pip install -r requirements.txt
```

### 2. Install Node.js Dependencies
Ensure you have **Node.js** installed (download from [nodejs.org](https://nodejs.org/)).
Then, navigate to the `js` folder and run:
```sh
npm install
```

---

## Usage
### Run the Application
```sh
python main.py
```

### How It Works
1. Open the application
2. Enter a **song name** or **YouTube link** (multiple songs can be separated by commas)
3. Click **Download**
4. The downloaded audio files will be saved in the same directory

---

## File Structure
```
/your_project_directory
│── js/
│   ├── downloader.js    # Node.js script for downloading audio
│   ├── package.json     # Node dependencies
│── main.py              # Python GUI using Flet
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
```

---

## Dependencies
### Python
- `flet`
- `requests`

### Node.js
- `ytdl-core`

---

## License
This project is open-source under the **MIT License**.

---

## Author
Developed by **Basil Benny**.


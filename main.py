from __future__ import unicode_literals  # Enables support for Unicode literals in Python 2/3 compatibility
import requests  # For making HTTP requests
import subprocess  # To run external commands
import flet as ft  # GUI framework

# Global variables
completed = False  # Flag to track completion status
currently_downloading_song = ""  # Stores the current song being downloaded


def check_string(char):
    """Checks if a character is not a backslash or forward slash."""
    if char in r"\\" or char in r"//":
        return False
    else:
        return True


def song_by_name(song_name: str):
    """Searches for a song on YouTube and returns the first video link."""
    song = song_name
    search_word = '+'.join(song.split())  # Replaces spaces with '+' for search
    search_link = f"https://www.youtube.com/results?search_query={search_word}"
    response = requests.get(search_link)  # Sends a GET request to YouTube
    char = ""
    index = response.text.index(r"/watch?v=")  # Finds the first video link
    link = ""
    while char != '%':  # Extracts the video ID until a '%' character is found
        link += response.text[index]
        char = response.text[index]
        if char in r"\\":  # Stops if a backslash is encountered
            break
        index += 1
    url = "https://www.youtube.com/" + link  # Constructs the full video URL
    new_url = url[:-1]  # Removes the last character (possibly an unwanted '%')
    return new_url


def run_javascript(js_file_path="JS/downloader.js", video_url="", video_name=""):
    """Runs a JavaScript file using Node.js with given arguments."""
    try:
        command = ["node", js_file_path, video_url, video_name]  # Command to execute
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # print("JavaScript Output:", result.stdout)  # Uncomment for debugging
    except subprocess.CalledProcessError as e:
        print(f"Error running JavaScript: {e}")
    except FileNotFoundError:
        print("Error: Node.js not found. Make sure it's installed and in your PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")


def process_values(text_field_data: str):
    """Processes the input text, extracts song names, and initiates downloads."""
    global completed, currently_downloading_song
    song_names = text_field_data.split(',')  # Splits input into a list of songs
    for song in song_names:
        if "youtube" in song:  # Direct YouTube link handling
            currently_downloading_song = song
            update_ui_downloading(page)
            run_javascript(video_url=song, video_name=song)
        else:  # Search for the song on YouTube
            currently_downloading_song = song
            update_ui_downloading(page)
            new_url = song_by_name(song)
            run_javascript(video_url=new_url)
    completed = True  # Marks download as completed
    update_ui_downloading(page)


def update_ui_downloading(page: ft.Page):
    """Updates the UI to show download progress or completion."""
    if not completed:
        page.clean()  # Clears the page
        song_input.value = data  # Sets input field value
        page.add(ft.Row([song_input, download_button]))  # Re-adds UI elements
        downloading_label.value = f"Downloading {currently_downloading_song}"  # Shows download status
        page.add(ft.Column([downloading_label, pb]))  # Adds label and progress bar
        page.update()
    else:
        page.clean()
        song_input.value = data
        page.add(ft.Row([song_input, download_button]))
        downloading_label.value = "Download completed"  # Shows completion message
        page.add(downloading_label)
        page.update()


def main(p: ft.Page):
    """Initializes the UI components and event handlers."""
    global pb, downloading_label, song_input, download_button, page

    def values_submitted(e):
        """Handles the submission of song input."""
        global data
        data = song_input.value
        process_values(data)

    page = p
    pb = ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee")  # Progress bar setup
    downloading_label = ft.Text(f"Downloading {currently_downloading_song}")  # Status label
    page.title = "test window"
    page.window.height = 300
    page.window.width = 500
    song_input = ft.TextField(hint_text="Song name, youtube link, or songs separated by a ','", width=200,
                              autofocus=True, on_submit=values_submitted)  # Input field
    download_button = ft.ElevatedButton(text="Download", color=ft.colors.BLUE,
                                        on_click=values_submitted)  # Download button
    page.add(ft.Row([song_input, download_button]))  # Adds UI elements


# Runs the app with the main function
ft.app(main)

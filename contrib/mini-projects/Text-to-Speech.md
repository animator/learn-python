
``` python
from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # for Windows
    # os.system("mpg123 output.mp3")  # for Linux (requires mpg123 to be installed)

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

if __name__ == "__main__":
    print("Choose text source:")
    print("1. Text file")
    print("2. User input")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        file_path = input("Enter the path to the text file: ")
        text_content = read_text_file(file_path)
    elif choice == "2":
        input_text = input("Enter the text to convert to speech: ")
        text_content = input_text
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        exit()

    if text_content:
        text_to_speech(text_content)
```

The above code uses a library **gTTS**.

gTTS (Google Text-to-Speech) is a Python library and CLI tool to
interface with Google Translate\'s text-to-speech API. It allows you to
convert text into speech in various languages using Google\'s natural
language processing capabilities.

**Features:**

*Simple Interface:* gTTS provides a simple and easy-to-use interface for
converting text to speech. You only need to provide the text you want to
convert, and gTTS handles the rest.

*Support for Multiple Languages:* gTTS supports a wide range of
languages for text-to-speech conversion. You can specify the language of
the input text, and gTTS will generate speech in the corresponding
language.

*Customizable Speed and Pitch:* You can adjust the speed and pitch of
the generated speech to suit your preferences or requirements. This
allows for some customization of the output speech.

*Offline Usage:* While gTTS requires an internet connection to fetch the
audio data from Google\'s servers, once the audio file is generated, it
can be saved locally and played offline.

*CLI Tool:* In addition to the Python library, gTTS also provides a
command-line interface (CLI) tool, allowing you to convert text to
speech directly from the terminal without writing any Python code.

*Free and Open Source*: gTTS is free to use and open source, making it
accessible to developers for various projects and applications.


Above code prompts to enter the text source either by giving input
through command line interface or by providing the path for specific
text file.
Then it saves the file in your current folder


# QR Code Encoder and Decoder Application

## Overview

This project is a QR code encoder and decoder application built using Python and Tkinter. The application allows users to:

1. Encode text into a QR code and save it as an image file.
2. Decode QR codes using a webcam and save the decoded text to a file.

## Features

- **Encode Text to QR Code**: Converts user-provided text into a QR code and saves it as a PNG image.
- **Decode QR Code from Camera**: Captures QR codes using the webcam, decodes the text, and allows saving the decoded text to a file.

## Requirements

- Python 3.x
- Tkinter
- qrcode
- Pillow (PIL)
- OpenCV
- pyzbar

## Installation

1. **Install Python**: Make sure you have Python 3.x installed on your system.

2. **Install Required Libraries**:
    ```bash
    pip install qrcode[pil]
    pip install pillow
    pip install opencv-python
    pip install pyzbar
    ```

## Usage

1. **Run the Application**:
    ```bash
    python QRCodeApp.py
    ```

2. **Encode Text to QR Code**:
    - Click the "Encode Text to QR Code" button.
    - Enter the text you want to encode in the text box.
    - Click the "Convert" button.
    - Save the generated QR code image.

3. **Decode QR Code from Camera**:
    - Click the "Decode QR Code from Camera" button.
    - Click "Start Camera" to begin scanning.
    - The application will decode the QR code and display the text.
    - Save the decoded text to a file.

## Project Structure

- `qr_code_project.py`: Main application script containing the Tkinter GUI and logic for encoding and decoding QR codes.
- `readme.md`: Project documentation.

## Libraries Used

- **Tkinter**: For the graphical user interface.
- **qrcode**: To generate QR codes from text.
- **Pillow (PIL)**: For handling image files.
- **OpenCV**: For capturing video from the webcam and processing frames.
- **pyzbar**: For decoding QR codes from images.

## How It Works

### Encoding QR Code

1. The user enters text into a text box.
2. The text is converted to a QR code using the `qrcode` library.
3. The generated QR code is saved as a PNG image.

### Decoding QR Code

1. The user starts the camera using the OpenCV library.
2. Frames from the webcam are captured and processed to detect QR codes.
3. Detected QR codes are decoded using the `pyzbar` library.
4. The decoded text is displayed to the user and can be saved to a text file.

## License

This project is licensed under the MIT License.

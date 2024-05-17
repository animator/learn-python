import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import cv2
from pyzbar.pyzbar import decode

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Encoder and Decoder")

        # Main frame that contains the primary buttons
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)
        self.main_frame.pack(padx=30)

        # Button to show the encode screen
        self.button1 = tk.Button(self.main_frame, text="Encode Text to QR Code", command=self.show_encode_screen)
        self.button1.pack(pady=10)

        # Button to show the decode screen
        self.button2 = tk.Button(self.main_frame, text="Decode QR Code from Camera", command=self.show_decode_screen)
        self.button2.pack(pady=10)

        self.encode_frame = None
        self.decode_frame = None

    def show_encode_screen(self):
        # Clear the main frame and show the encode frame
        self.clear_frame()
        self.encode_frame = tk.Frame(self.root)
        self.encode_frame.pack(pady=20)
        self.encode_frame.pack(padx=30)

        # Text box to enter text for QR code
        self.text_box = tk.Entry(self.encode_frame, width=50)
        self.text_box.pack(pady=10)

        # Button to convert text to QR code
        self.convert_button = tk.Button(self.encode_frame, text="Convert", command=self.convert_to_qr)
        self.convert_button.pack(pady=10)

        # Button to go back to the main screen
        self.back_button = tk.Button(self.encode_frame, text="Back", command=self.show_main_screen)
        self.back_button.pack(pady=10)

    def convert_to_qr(self):
        text = self.text_box.get()
        if text:
            # Generate QR code from text
            qr = qrcode.make(text)
            # Save the QR code as an image file
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                qr.save(file_path)
                messagebox.showinfo("Success", "QR Code saved successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter text to convert to QR Code.")

    def show_decode_screen(self):
        # Clear the main frame and show the decode frame
        self.clear_frame()
        self.decode_frame = tk.Frame(self.root)
        self.decode_frame.pack(pady=10)
        self.decode_frame.pack(padx=50)

        # Button to start the camera for QR code scanning
        self.start_camera_button = tk.Button(self.decode_frame, text="Start Camera", command=self.start_camera)
        self.start_camera_button.pack(pady=0)

        # Button to go back to the main screen
        self.back_button = tk.Button(self.decode_frame, text="Back", command=self.show_main_screen)
        self.back_button.pack(pady=10)

    def start_camera(self):
        cap = cv2.VideoCapture(0)
        found_qr = False

        while not found_qr:
            ret, frame = cap.read()
            if not ret:
                break

            # Decode QR code from the camera frame
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(points, returnPoints=True)
                else:
                    hull = points

                n = len(hull)
                for j in range(0, n):
                    cv2.line(frame, tuple(hull[j]), tuple(hull[(j+1) % n]), (255, 0, 0), 3)

                # Extract and display the decoded text
                qr_text = obj.data.decode("utf-8")
                found_qr = True
                cv2.putText(frame, qr_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                self.display_decoded_text(qr_text)

            cv2.imshow("QR Code Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def display_decoded_text(self, text):
        # Show the decoded text in a message box
        messagebox.showinfo("Decoded Text", text)
        # Save the decoded text to a text file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(text)
        messagebox.showinfo("Success", "Decoded text saved successfully!")

    def show_main_screen(self):
        # Clear the current frame and show the main frame
        self.clear_frame()
        self.main_frame.pack(pady=20)
        self.main_frame.pack(padx=30)

        # Re-create the buttons for encoding and decoding
        self.button1 = tk.Button(self.main_frame, text="Encode Text to QR Code", command=self.show_encode_screen)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.main_frame, text="Decode QR Code from Camera", command=self.show_decode_screen)
        self.button2.pack(pady=10)

        self.encode_frame = None
        self.decode_frame = None

    def clear_frame(self):
        # Clear all widgets from the current frame
        for widget in self.root.winfo_children():
            widget.pack_forget()
            widget.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()

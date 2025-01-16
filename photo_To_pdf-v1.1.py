import os
from tkinter import Tk, Button, Label, filedialog
from PIL import Image
from reportlab.pdfgen import canvas
from tkinter import messagebox

class ImageToPDFConverter:
    def __init__(self, master):
        self.master = master
        master.title("Image to PDF Converter")
        
        # Set a fixed window size and make it resizable
        master.geometry("400x200")  # Initial size (width x height)
        master.resizable(True, True)  # Allow resizing

        self.label = Label(master, text="SELECT AN IMAGE FILE")
        self.label.pack(pady=10)

        self.select_button = Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=5)

        self.convert_button = Button(master, text="Convert to PDF", command=self.convert_to_pdf, state='disabled')
        self.convert_button.pack(pady=5)

        self.image_path = None  # Initialize image path to None.

    def select_image(self):
        """Allows the user to select an image and updates the label."""
        file_path = filedialog.askopenfilename(
            title="Select an image file", 
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        if file_path:
            self.image_path = file_path
            self.convert_button.config(state='normal')
            self.label.config(text=f"Selected image {os.path.basename(self.image_path)}")

    def convert_to_pdf(self):
        """Converts the selected image to PDF and saves it."""
        if self.image_path:
            try:
                # Open the image
                image = Image.open(self.image_path)
                pdf_filename = os.path.splitext(os.path.basename(self.image_path))[0] + '.pdf'
                pdf_path = os.path.join(os.path.expanduser("~"), "Downloads", pdf_filename)

                # Create PDF using reportlab
                pdf = canvas.Canvas(pdf_path, pagesize=(image.width, image.height))
                pdf.drawInlineImage(self.image_path, 0, 0, width=image.width, height=image.height)
                pdf.save()

                # Inform user about successful conversion
                self.label.config(text=f"Conversion successful! PDF saved at: {pdf_path}")
                messagebox.showinfo("Success", f"PDF saved successfully at: {pdf_path}")
            except Exception as e:
                # Handle errors (e.g., unsupported image format, file not found, etc.)
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            # In case no image is selected
            messagebox.showwarning("Warning", "Please select an image first.")

if __name__ == "__main__":
    root = Tk()
    app = ImageToPDFConverter(root)
    root.mainloop()

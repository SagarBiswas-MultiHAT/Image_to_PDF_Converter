
### README:

```markdown
# Image to PDF Converter

This Python application allows you to easily convert image files to PDF format. It supports multiple image formats, including PNG, JPG, BMP, and others. The conversion process is simple and fast, and the resulting PDF is saved in your Downloads folder.

## Features:
- Select an image file to convert
- Convert supported image formats to PDF
- Save the PDF in the Downloads folder
- Simple and easy-to-use GUI built with Tkinter

## Requirements:
- Python 3.x
- Pillow for image processing
- reportlab for creating PDFs
- Tkinter for the graphical user interface (GUI)

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Installation:
1. Clone the repository or download the script.
2. Install the required dependencies using pip:

   pip install pillow reportlab
   ```

## Usage

To use the tool:

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the following command:

   ```bash
   python image_to_pdf_converter.py
   ```

### Example Workflow:
1. Click **Select Image** to choose an image from your computer.
2. After selecting the image, click **Convert to PDF** to convert the image to a PDF.
3. The PDF will be saved to your Downloads folder with the same name as the image file.

### Example Output:

When a successful conversion is made, the GUI will display a message similar to:

```
Conversion successful! PDF saved at: /home/user/Downloads/your_image.pdf
```

## Code Explanation

### Main Script

- **GUI Layout**: The app provides a simple window with two buttons: one for selecting an image file and another for converting the image to PDF.
- **Image Selection**: The `select_image` method opens a file dialog that allows the user to select an image.
- **Image Conversion**: The `convert_to_pdf` method converts the selected image into a PDF format using the `reportlab` library.
- **Error Handling**: If the user tries to convert without selecting an image or if an error occurs during the conversion, an error message is shown.

### Error Handling
- **No Image Selected**: If no image is selected, a warning message prompts the user to select an image.
- **Conversion Errors**: If there’s an issue with the conversion (e.g., unsupported format), an error message will display.

## Contributing

Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. This license permits anyone to use, modify, and distribute the software with minimal restrictions. See the [LICENSE](LICENSE) file for details.

---

**Note**: This script is designed for educational and personal use.

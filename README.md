Wi-Fi & URL QR Code Generator
This Python-based tool simplifies sharing Wi-Fi credentials or URLs by generating scannable QR codes. Users can easily share network details with friends, guests, or colleagues without exposing sensitive data directly. The tool supports various customization options for QR codes, enhancing flexibility and ease of use.

Features:
Wi-Fi QR Code Generation: Quickly generate QR codes for Wi-Fi credentials, enabling seamless connection with a simple scan.
URL QR Code Creation: Generate QR codes for any URL to share links easily.
Customizable QR Code Appearance: Options to customize the size, color, and file format of the QR code.
User-friendly Output: Save QR codes as image files to share digitally or print.
How to Use:
Clone the repository to your local machine.
Run the script with the desired Wi-Fi credentials or URL input.
Save or share the generated QR code image.
Requirements:
Python 3.x
qrcode and pillow libraries
Installation:
bash
Copy code
pip install qrcode[pil]
Example Usage:
python
Copy code
# Generate a Wi-Fi QR code
python qr_generator.py --wifi "SSID_NAME" --password "WIFI_PASSWORD"

# Generate a URL QR code
python qr_generator.py --url "https://example.com"
Contributions:
Contributions are welcome! Please feel free to submit pull requests or report issues to help improve the tool.

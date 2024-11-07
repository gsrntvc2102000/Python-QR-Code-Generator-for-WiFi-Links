import qrcode

# Function to generate WiFi QR code
def generate_wifi_qr(ssid, password, encryption, filename='wifi_qr.png'):
    wifi_string = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_string)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"WiFi QR code generated and saved as {filename}")

# Function to generate a QR code for a URL
def generate_link_qr(link, filename='link_qr.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"Link QR code generated and saved as {filename}")

# Main function to provide a menu and input interface
def main():
    print("Welcome to the QR Code Generator!")
    print("What would you like to generate a QR code for?")
    print("1. WiFi Network")
    print("2. Link (URL)")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        ssid = input("Enter the WiFi network SSID: ")
        password = input("Enter the WiFi network password: ")
        encryption = input("Enter the WiFi network encryption type (WPA/WEP/etc.): ")
        filename = input("Enter the desired filename for the QR code image (default: wifi_qr.png): ")
        filename = filename if filename else 'wifi_qr.png'
        generate_wifi_qr(ssid, password, encryption, filename)
        
    elif choice == "2":
        link = input("Enter the link (URL): ")
        filename = input("Enter the desired filename for the QR code image (default: link_qr.png): ")
        filename = filename if filename else 'link_qr.png'
        generate_link_qr(link, filename)
        
    else:
        print("Invalid choice. Please try again.")
        main()  # Retry if input is invalid

# Ensure the script runs when executed
if __name__ == "__main__":
    main()

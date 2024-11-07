import qrcode

# Function to generate WiFi QR code
def generate_wifi_qr(ssid, password, encryption):
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
    img.save('wifi_qr.png')

# Function to generate a QR code for a URL
def generate_link_qr(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('link_qr.png')

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
        generate_wifi_qr(ssid, password, encryption)
        print("WiFi QR code generated and saved as wifi_qr.png")
    elif choice == "2":
        link = input("Enter the link (URL): ")
        generate_link_qr(link)
        print("Link QR code generated and saved as link_qr.png")
    else:
        print("Invalid choice. Please try again.")

# Ensure the script runs when executed
if __name__ == "__main__":
    main()

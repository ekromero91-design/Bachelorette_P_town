#!/usr/bin/env python3

import qrcode

def update_qr_code():
    print("Enter your live URL (from GitHub Pages, Netlify, etc.):")
    print("Example: https://username.github.io/olivias-bachelorette/olivias-bachelorette.html")
    url = input("URL: ").strip()
    
    if not url:
        print("No URL provided!")
        return
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR code image with purple color scheme
    qr_img = qr.make_image(fill_color="purple", back_color="white")
    
    # Save the QR code
    qr_img.save('olivias_bachelorette_qr_final.png')
    print(f"\n✅ QR code updated successfully!")
    print(f"📱 QR code saved as: olivias_bachelorette_qr_final.png")
    print(f"🔗 Points to: {url}")
    print(f"\n🎉 Now anyone can scan this QR code with their phone!")

if __name__ == "__main__":
    update_qr_code()

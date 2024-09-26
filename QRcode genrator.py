import qrcode
import os

qr = qrcode.QRCode(
    version=15,  # Higher version increases the complexity of the QR code
    box_size=10,  # Size of each box in pixels
    border=5      # Thickness of the border around the QR code
)

data = "Enjoy The Universe"  # Data to encode or you can paste a link 

qr.add_data(data)  # Add data to the QR code
qr.make(fit=True)  # Adjust QR code size

# Create the image for the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the generated QR code as an image file
img.save("test.png")


os.startfile("test.png")

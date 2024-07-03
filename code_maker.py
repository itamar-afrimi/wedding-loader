# import qrcode
#
# # Replace with your actual Cloud Run service URL
# upload_url = "https://wedding-upload-vldxf7fcdq-wn.a.run.app"
#
# # Generate the QR code
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(upload_url)
# qr.make(fit=True)
#
# # Create an image from the QR Code instance
# img = qr.make_image(fill='black', back_color='white')
#
# # Save the image
# img.save("wedding_upload_qr_code.png")
import qrcode

# URL to the shared Google Drive folder
shared_folder_url = 'https://wedding-upload-vldxf7fcdq-wn.a.run.app'

# Generate QR code
qr = qrcode.make(shared_folder_url)
qr.save('wedding_photos_qr_code.png')

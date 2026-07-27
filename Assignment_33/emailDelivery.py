import os
import smtplib
import mimetypes
from email.message import EmailMessage
import traceback

def SendEmail(receiverEmail, file, body):
    print("receiverEmail:", receiverEmail)
    # print(file)
    # print(body)
    # 1. Define configurations
    SMTP_SERVER = "smtp.gmail.com"  # e.g., Gmail SMTP
    SMTP_PORT = 465                 # TLS port
    SENDER_EMAIL = "vpulsbhagwat@gmail.com"
    SENDER_PASSWORD = "wjpqyceeawaxzmft"  # Use a secure App Password
    RECEIVER_EMAIL = receiverEmail

    # 2. Build the email headers and body
    msg = EmailMessage()
    msg["Subject"] = "Duplicate file removal status"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(body)
    
    # 3. Read and attach the file
    file_path = file  # Replace with your local file path
    file_name = os.path.basename(file_path)
    print("file_name:", file_name)

    # Automatically detect the file type (e.g., application/pdf)
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = "application/octet-stream"
    main_type, sub_type = mime_type.split("/", 1)

    # Open the file in binary mode and add it to the email object
    with open(file_path, "rb") as f:
        file_data = f.read()
        msg.add_attachment(
            file_data,
            maintype=main_type,
            subtype=sub_type,
            filename=file_name
        )

    # 4. Connect to the server and send the email
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            # server.starttls()  # Upgrade connection to secure TLS
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully with the attachment!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        # traceback.print_exc()
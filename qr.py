import qrcode
from PIL import Image, ImageDraw, ImageFont

def add_rounded_rectangle(draw, position, size, radius, fill):
    """Draw a rounded rectangle"""
    x0, y0, x1, y1 = position
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.pieslice([x0, y0, x0 + 2 * radius, y0 + 2 * radius], 180, 270, fill=fill)
    draw.pieslice([x1 - 2 * radius, y0, x1, y0 + 2 * radius], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - 2 * radius, x0 + 2 * radius, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - 2 * radius, y1 - 2 * radius, x1, y1], 0, 90, fill=fill)

def generate_qr_with_logo_in_rounded_rectangle(data, logo_path, output_path, text):
    # Step 1: Generate basic QR code
    qr = qrcode.QRCode(
        version=1,  # Version 1: 21x21 matrix
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (allows for logo insertion)
        box_size=30,  # Size of each box in pixels
        border=3  # Thickness of the border
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Step 2: Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Step 3: Open the logo and resize it to fit inside the QR code
    logo = Image.open(logo_path)
    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 8  # Resize logo to 1/4th of the QR code size
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Step 4: Create a rounded rectangle behind the logo
    rounded_rect_size = (logo_size + 20, logo_size + 20)  # Add padding around the logo
    rounded_rect = Image.new("RGBA", rounded_rect_size, (255, 255, 255, 0))  # Transparent background
    draw = ImageDraw.Draw(rounded_rect)

    # Draw the rounded rectangle
    add_rounded_rectangle(draw, (0, 0, rounded_rect_size[0], rounded_rect_size[1]), rounded_rect_size[0] // 5, radius=20, fill="white")

    # Step 5: Paste the logo onto the rounded rectangle
    logo_pos = ((rounded_rect_size[0] - logo_size) // 2, (rounded_rect_size[1] - logo_size) // 2)
    rounded_rect.paste(logo, logo_pos, mask=logo if logo.mode == 'RGBA' else None)

    # Step 6: Calculate the position to paste the rounded rectangle onto the QR code
    qr_pos = ((qr_width - rounded_rect_size[0]) // 2, (qr_height - rounded_rect_size[1]) // 2)
    qr_img.paste(rounded_rect, qr_pos, mask=rounded_rect)

    # Step 7: Add text to the bottom of the QR code
    if text:
        draw_qr = ImageDraw.Draw(qr_img)
        font = ImageFont.truetype("assets/font/Roboto/Roboto-Bold.ttf", 60)  # Use a suitable font and size

        # Calculate text size and position (center-bottom)
        text_width, text_height = draw_qr.textbbox((0, 0), text, font=font)[2:]
        text_pos = ((qr_width - text_width) // 2, qr_height - text_height - 20)  # 10px above bottom edge

        # Draw the text
        draw_qr.text(text_pos, text, font=font, fill="black")

    # Step 8: Save the final image
    qr_img.save(output_path)
    print(f"QR code saved at {output_path}")

# Usage example
generate_qr_with_logo_in_rounded_rectangle(
    data="http://example.com",
    logo_path="assets/logo.png",  # Path to your logo image
    output_path="output/qr.png",  # Output file
    text="Hello world!"  # Text to add
)

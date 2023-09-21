import streamlit as st
from PIL import Image, ImageDraw, ImageFont


def draw_text(draw, text, position, font, max_width):
    # Split the text into lines that fit within the specified width.
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and font.getsize(line + words[0])[0] <= max_width:
            line += (words.pop(0) + ' ')
        lines.append(line)

    # Draw each line of text.
    y = position[1]
    for line in lines:
        width, height = draw.textsize(line, font=font)
        # Draw text
        draw.text(((max_width - width) / 2, y), line, font=font, fill="white")
        y += height
    return y  # Return the Y coordinate after the last line.


st.title("Meme Generator")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    top_text = st.text_input("Top Text", "")
    bottom_text = st.text_input("Bottom Text", "")

    if st.button("Generate Meme"):
        # Load image
        img_width, img_height = image.size
        draw = ImageDraw.Draw(image)

        # Define font and max width for text
        font_size = int(img_height / 15)  # Base font size on image height
        font = ImageFont.truetype("arial.ttf", font_size)
        max_width = img_width - 40  # Leave 20 pixels padding on each side

        # Draw top text
        draw_text(draw, top_text, (20, 10), font, max_width)

        # Draw bottom text
        _, text_height = draw.textsize(bottom_text, font=font)
        draw_text(draw, bottom_text, (20, img_height - text_height - 10), font, max_width)

        st.image(image, caption='Your Meme.', use_column_width=True)
        st.balloons()
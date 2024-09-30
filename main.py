import streamlit as st
from transformers import AutoModel, AutoTokenizer
import re
from PIL import Image
import torch

# Load tokenizer and model for OCR
tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)
model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, low_cpu_mem_usage=True, use_safetensors=True, pad_token_id=tokenizer.eos_token_id)

# Set model to evaluation mode and move to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.eval().to(device)

# Streamlit application
st.title("OCR Application")
st.write("Upload an image to extract text in both English and Hindi.")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file to an image that can be processed by the model
    image = Image.open(uploaded_file)

    # Convert image to RGB if it's not already in that format
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image.save("temp_image.jpg", "JPEG")  # Save the uploaded image temporarily

    # Perform OCR using the model (pass the file path to the tokenizer and model)
    with torch.no_grad():
        res = model.chat(tokenizer, "temp_image.jpg", ocr_type='ocr')

    # Text formatting
    res = re.sub(' +', ' ', res)  # Replace multiple spaces with a single space
    res = re.sub(r'(?<=[.,!?])(?=[^\s])', r' ', res)  # Add spaces after punctuation
    res = re.sub(r'(?<=[.!?]) +', r'\g<0>\n', res)  # Add line breaks after sentence endings

    st.subheader("Extracted Text:")

    # Search functionality
    search_term = st.text_input("Enter keywords to search within the extracted text:")

    if search_term:
        # Highlight the matching text
        highlighted_text = re.sub(f'({search_term})', r'**\1**', res, flags=re.IGNORECASE)

        # Display search results with highlighted keywords
        st.markdown(f"{highlighted_text}", unsafe_allow_html=True)
    else:
        # Display extracted text without highlighting
        st.text(res)


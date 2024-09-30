

---

# OCR Application with English and Hindi Support

This is a web-based OCR (Optical Character Recognition) application that allows users to upload images and extract text in both English and Hindi. The app uses **GOT-OCR** for English text extraction and **EasyOCR** for Hindi text extraction. Additionally, it provides a keyword search feature that highlights specific words within the extracted text.

## Features

- Extract text from images in both **English** and **Hindi**.
- **Search** for keywords in the extracted text.
- **Highlight** keywords for easy identification.
- Simple **web interface** built using Streamlit.
- Deployed via **ngrok** for easy remote access.

## Requirements

- Python 3.x
- Packages: 
  - `streamlit`
  - `easyocr`
  - `transformers`
  - `Pillow`
  - `pyngrok`

## Installation and Setup

Follow these steps to install and run the OCR application locally.

### Step 1: Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/ocr-app.git
cd ocr-app
```

### Step 2: Create a Virtual Environment (Optional but recommended)

It's a good idea to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install the Required Dependencies

Install the necessary Python packages using `pip`:

```bash
pip install streamlit easyocr transformers Pillow pyngrok
```

### Step 4: Set Up `ngrok`

You need an `ngrok` account to generate a public URL for the Streamlit app. 

1. Sign up at [ngrok.com](https://ngrok.com/) and get your auth token.
2. Set the auth token in your environment:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

Replace `YOUR_AUTH_TOKEN` with the token from your ngrok dashboard.

### Step 5: Run the Application

To run the application, execute the following command in the terminal:

```bash
streamlit run app.py
```

This will start the Streamlit server locally on port 8501. Ngrok will provide a public URL for remote access.

### Step 6: Access the App via Ngrok

Once the app is running, start `ngrok` to create a public tunnel to the Streamlit app:

```bash
ngrok http 8501
```

Ngrok will generate a public URL (like `https://your-ngrok-url.ngrok.io`) that you can share with others to access the app from any device.

## Usage

1. **Upload an Image**: On the main screen, upload an image in `.jpg`, `.jpeg`, or `.png` format.
2. **Extract Text**: The app will extract text in both English and Hindi from the image.
3. **Search Keywords**: You can enter a keyword in the provided text box to search within the extracted text. The keyword will be highlighted in the results.

## Example

- Upload an image containing English and Hindi text.
- The extracted text will be displayed.
- Enter a keyword like "example", and the app will highlight this word wherever it appears in the extracted text.

## Technologies Used

- **Streamlit**: For the web interface.
- **EasyOCR**: For Hindi text extraction.
- **GOT-OCR**: For English text extraction using a pre-trained transformer-based model.
- **Pillow**: For image processing.
- **Ngrok**: For exposing the local Streamlit app to the web.

## Troubleshooting

- **Model loading issue**: If you encounter any issues loading the models (GOT-OCR, EasyOCR), ensure that your system supports GPU (CUDA) for optimal performance. If you don't have a GPU, remove the `.cuda()` calls in the code.
- **Ngrok error**: If you get an error from `ngrok`, make sure you've set the correct auth token and that the `ngrok` command is properly installed and configured.

## License

This project is licensed under the MIT License.

---


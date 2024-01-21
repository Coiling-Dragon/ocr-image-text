# OCR Script Setup

This guide will help you set up an OCR (Optical Character Recognition) script using Tesseract and Python.

## Prerequisites

- Python 3.12.1
- Tesseract OCR

## Installation

### Tesseract

Tesseract is an open-source OCR engine that our script uses to convert images to text. You can install it using either Homebrew (for macOS) or Chocolatey (for Windows).

#### macOS:

To install Tesseract on macOS, use the following command in your terminal:

```bash
brew install tesseract
```

#### Windows:

In this example, we're using Chocolatey and setting the path to the Tesseract executable.

```bash
choco install tesseract
```

### Python Virtual Environment

It's a good practice to create a virtual environment for your Python projects. This keeps the dependencies used by different projects separate.

Create a new virtual environment using the following command:

```bash
python -m venv venv
```

### Activate the Virtual Environment

After creating the virtual environment, you need to activate it.

#### Windows:

To activate the virtual environment on Windows, use the following command in your terminal:

```bash
.\venv\Scripts\activate
```

#### macOS/Linux:

To activate the virtual environment on macOS or Linux, use the following command in your terminal:

```bash
source venv/bin/activate
```

### Install the Required Python Packages

We have a `requirements.txt` file that lists all the Python packages that our script needs. You can install all of them using the following command:

```bash
pip install -r requirements.txt
```

Now you're all set to run the script!


### Run it

```bash
python main.py
```
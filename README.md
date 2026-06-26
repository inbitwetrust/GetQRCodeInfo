# QR Code & Barcode Image Decoder v1.6

A lightweight Python command‑line tool for detecting and decoding **QR Codes** and **Barcodes** from image files.  
It includes automatic image preprocessing, transparency handling, grayscale fallback, and selective decoding based on the desired code type.

Designed for anyone who needs a fast and reliable QRcode or Barcode inspection utility directly from the terminal.

---

## Features

- **Decode QR Codes and Barcodes** from common image formats.
- **Automatic preprocessing**:
  - Converts transparent PNGs to white‑background RGB.
  - Converts images to grayscale when needed.
  - Attempts inverted‑grayscale decoding if normal decoding fails.
- **Selective decoding**:
  - Mode `1` → decode **only QR Codes**
  - Mode `2` → decode **only Barcodes**
- **Clear error reporting** to stderr.
- **Simple CLI interface** suitable for scripting and automation.

---

## How It Works

The decoder performs the following operations:

1. Loads the target image.
2. Converts the image to grayscale.
3. Generates an inverted version of the image.
4. Attempts QR code detection against the inverted image.
5. Falls back to the original image if no QR code is found.
6. Extracts all detected QR code objects.
7. Decodes payloads using UTF-8, with automatic Latin-1 fallback.
8. Presents results in a clean, structured terminal layout.

This dual-pass detection method significantly improves readability for QR codes that may be affected by unusual color schemes, image processing artifacts, or inversion.

---

## 📦 Requirements

- Python 3.x
- Dependencies:
  - `Pillow`
  - `pyzbar`

Install them with:

```bash
pip install pillow pyzbar
```

---

## Usage

### Single Image

```bash
python getQRcodeInfo-v1.6.py <mode> <image_path>
```

---

## Author

**George W. Aravidis**


---

## License

This project is provided for educational, research, automation, and operational purposes.

You may modify and distribute it according to the license included in this repository.

---

## Disclaimer

This tool is intended for legitimate QR code analysis and decoding activities. Users are responsible for ensuring compliance with applicable laws, regulations, organizational policies, and security requirements when using this software.

# QRcode Decoder v1.3

A tiny command-line QR code analysis and decoding utility written in Python.  
This tool extracts and displays QR code contents from image files using an enhanced detection workflow, supporting both standard and inverted QR code matrices.

Designed for anyone who needs a fast and reliable QR code inspection utility directly from the terminal.

---

## Features

- Decode QR codes from image files
- Automatic fallback detection using inverted image processing
- Support for multiple QR codes within a single image
- UTF-8 and Latin-1 character decoding support
- Unicode-aware output formatting
- Professional terminal interface with colorized output
- Structured visualization of decoded data
- Batch processing of multiple image files
- Robust exception handling and error reporting
- Lightweight and easy to integrate into automation workflows

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

## Requirements

### Python Version

- Python 3.8+

### Dependencies

- Pillow
- pyzbar

Install required packages:

```bash
pip install pillow pyzbar
```

---

## System Dependencies

### Linux

Install the ZBar shared library:

#### Debian / Ubuntu

```bash
sudo apt update
sudo apt install libzbar0
```

#### Kali Linux

```bash
sudo apt install libzbar0
```

#### Fedora

```bash
sudo dnf install zbar
```

#### Arch Linux

```bash
sudo pacman -S zbar
```

---

## Usage

### Single Image

```bash
python3 getQRcodeInfo-v1.3.py qr_code.png
```

### Multiple Images

```bash
python3 getQRcodeInfo-v1.3.py image1.png image2.jpg image3.bmp
```

---

## Example Output

```text
QRcode decoder v1.3
Created by George W. Aravidis | June 2026

[*] Scanning target file: sample.png...

[+] ACCESS GRANTED: Found 1 QR code(s)!

┌── [ OBJECT #1 ] ──────────────────────────┐
│ TYPE   : QRCODE                           │
├── [ DECRYPTED DATA ] ─────────────────────┤
│ https://github.com/example/repository     │
└───────────────────────────────────────────┘
```

---

## Supported Formats

The application supports any image format recognized by Pillow, including:

- PNG
- JPG / JPEG
- BMP
- TIFF
- GIF
- WEBP

---

## Error Handling

The tool gracefully handles:

- Missing files
- Invalid image formats
- Corrupted image files
- QR codes containing non-UTF-8 data
- Images without detectable QR codes
- Runtime decoding exceptions

---

## Use Cases

### Security Analysis

Inspect QR codes embedded in documents, screenshots, phishing samples, and digital artifacts.

### Digital Forensics

Extract QR code payloads during evidence analysis and incident response investigations.

### Automation Pipelines

Integrate QR code extraction into batch processing, CI/CD workflows, or security tooling.

### General QR Inspection

Quickly view the contents of QR codes without requiring mobile devices or graphical applications.

---

## Technical Overview

| Component | Purpose |
|------------|-----------|
| Pillow | Image loading and preprocessing |
| ImageOps | Image inversion processing |
| pyzbar | QR code detection and decoding |
| Unicode Width Calculation | Proper alignment of multilingual content |
| ANSI Terminal Colors | Enhanced readability and professional output |

---

## Project Structure

```text
getQRcodeInfo-v1.3.py
```

Single-file implementation with no unnecessary complexity, making it easy to audit, customize, and deploy.

---

## Performance Notes

- Supports detection of multiple QR codes within a single image.
- Efficient grayscale preprocessing minimizes unnecessary computation.
- Inversion fallback increases detection success rates for difficult QR code samples.
- Suitable for both interactive and scripted environments.

---

## Future Enhancements

Potential future improvements include:

- Barcode support (Code128, EAN, UPC, etc.)
- Recursive directory scanning
- JSON output mode
- CSV export
- Detection confidence reporting
- Image metadata analysis
- Parallel processing for large datasets

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

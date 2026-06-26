#!/usr/bin/env python3

# --------------------------------------------------------------
#  QR Code & Barcode Image Decoder
#  A tool for detecting and decoding QR codes and Barcodes.
#  Created by George W. A. | June 2026
# --------------------------------------------------------------

import sys
from PIL import Image, ImageOps
from pyzbar.pyzbar import decode


def prepare_image(path):
    try:
        img = Image.open(path)
        
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert('RGBA')
            # Δημιουργία λευκού φόντου (απαραίτητο για τα barcodes)
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            return background
        else:
            return img.convert("RGB")
            
    except Exception as e:
        print(f"{path}: cannot open ({e})", file=sys.stderr)
        return None


def process(path, mode):

    image = prepare_image(path)
    if image is None:
        return 3


    decoded = decode(image)

    if not decoded:
        gray = image.convert("L")
        decoded = decode(gray)

    if not decoded:
        inverted = ImageOps.invert(image.convert("L"))
        decoded = decode(inverted)

    if not decoded:
        print(f"{path}: no code found", file=sys.stderr)
        return 2

    found = False

    for obj in decoded:
        t = obj.type
        d = obj.data.decode("utf-8", errors="ignore")

        # Αν θέλουμε ΜΟΝΟ QR (Mode 1) και βρήκε κάτι άλλο, το προσπερνάμε
        if mode == "1" and t != "QRCODE":
            continue
            
        if mode == "2" and t == "QRCODE":
            continue

        print(f"{t}:{d}")
        found = True

    if not found:
        code_type = "QR Code" if mode == "1" else "Barcode"
        print(f"{path}: no matching {code_type} found in image", file=sys.stderr)
        return 2

    return 0


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <1=QR | 2=BARCODE> <image_path>", file=sys.stderr)
        return 1
        
    mode = sys.argv[1]
    if mode not in ["1", "2"]:
        print("Error: Invalid mode. Use 1 for QR Codes or 2 for Barcodes.", file=sys.stderr)
        return 1

    return process(sys.argv[2], mode)


if __name__ == "__main__":
    sys.exit(main())

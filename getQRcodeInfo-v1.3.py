import sys
import unicodedata
from PIL import Image, ImageOps
from pyzbar.pyzbar import decode

GREEN = '\033[92m'
BRIGHT_GREEN = '\033[1;92m'
WHITE = '\033[97m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

def print_banner():
    print(f"\n{BRIGHT_GREEN}QRcode decoder v1.3{RESET}")
    print(f"{GREEN}Created by George W. Aravidis | June 2026 {RESET}\n")

def get_visual_length(text):
    return sum(2 if unicodedata.east_asian_width(c) in ('F', 'W') else 1 for c in text)

def read_qr(image_path):
    print(f"{CYAN}[*] Scanning target file: {image_path}...{RESET}")
    
    try:
        img = Image.open(image_path)
        img_gray = img.convert('L')
        img_inverted = ImageOps.invert(img_gray)
    except FileNotFoundError:
        print(f"{RED}[-] SYSTEM ERROR: File '{image_path}' not found.{RESET}\n")
        return
    except Exception as e:
        print(f"{RED}[-] CRITICAL ERROR: {e}{RESET}\n")
        return

    decoded_objects = decode(img_inverted)
    if not decoded_objects:
        decoded_objects = decode(img)

    if not decoded_objects:
        print(f"{RED}[-] NO DATA FOUND: No valid QR code detected in the matrix.{RESET}\n")
        return

    print(f"{BRIGHT_GREEN}[+] ACCESS GRANTED: Found {len(decoded_objects)} QR code(s)!{RESET}\n")
    
    for idx, obj in enumerate(decoded_objects, 1):
        try:
            data = obj.data.decode('utf-8')
        except UnicodeDecodeError:
            data = obj.data.decode('latin-1')
            
        lines = data.splitlines()
        
        type_str = f"TYPE   : {obj.type}"
        max_content_len = max(max((get_visual_length(line) for line in lines), default=0), get_visual_length(type_str))
        
        box_width = max(max_content_len + 4, 40) 
        
        top_title = f" [ OBJECT #{idx} ] "
        mid_title = f" [ DECRYPTED DATA ] "
        
        top_border = f"┌──{top_title}" + "─" * (box_width - get_visual_length(top_title) - 3) + "┐"
        mid_border = f"├──{mid_title}" + "─" * (box_width - get_visual_length(mid_title) - 3) + "┤"
        bottom_border = "└" + "─" * (box_width - 1) + "┘"
        
        print(f"{GREEN}{top_border}{RESET}")
        
        type_line = f" TYPE   : {obj.type}"
        padding_type = box_width - get_visual_length(type_line) - 2
        print(f"{GREEN}│{RESET}{WHITE}{type_line}{RESET}" + " " * padding_type + f"{GREEN}│{RESET}")
        
        print(f"{GREEN}{mid_border}{RESET}")
        
        for line in lines:
            vis_len = get_visual_length(line)
            padding = box_width - vis_len - 3
            print(f"{GREEN}│{RESET} {WHITE}{line}{RESET}" + " " * padding + f"{GREEN}│{RESET}")
            
        print(f"{GREEN}{bottom_border}{RESET}\n")

if __name__ == "__main__":
    print_banner()
    
    if len(sys.argv) < 2:
        print(f"{RED}[!] USAGE ERROR:{RESET} Missing payload argument.\n")
        print(f"{WHITE}Syntax:{RESET} python getQRcodeInfo.py <path_to_image1> [path_to_image2 ...]")
        print(f"\n")

    else:
        target_files = sys.argv[1:]
        for file_path in target_files:
            read_qr(file_path)

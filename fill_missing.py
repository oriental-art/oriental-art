import os
import urllib.request
import ssl
import urllib.parse

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

MISSING = {
    "calligraphy/wang_xizhi_orchid.jpg": ("1280", "800", "Wang Xizhi", "Orchid Pavilion Preface"),
    "jade/qing_jade.jpg": ("800", "600", "Qing Dynasty", "Jade Carving"),
    "jade/jadeite.jpg": ("800", "600", "Imperial", "Jadeite"),
}

def download_image(local_path, width, height, line1, line2):
    base_dir = '/home/kai/.openclaw/workspace/images'
    full_path = os.path.join(base_dir, local_path)
    dir_path = os.path.dirname(full_path)
    os.makedirs(dir_path, exist_ok=True)
    
    # Remove SVG if exists
    svg_path = full_path.replace('.jpg', '.svg')
    if os.path.exists(svg_path):
        os.remove(svg_path)
    
    text = urllib.parse.quote(f"{line1}\n{line2}")
    url = f"https://placehold.co/{width}x{height}/f5f2ed/5a4a3a?text={text}"
    
    try:
        print(f"Downloading {local_path}...")
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            data = response.read()
            with open(full_path, 'wb') as f:
                f.write(data)
        print(f"  ✓ {len(data)} bytes")
        return True
    except Exception as e:
        print(f"  ✗ Failed: {str(e)[:60]}")
        return False

def main():
    for local_path, (w, h, l1, l2) in MISSING.items():
        download_image(local_path, w, h, l1, l2)

if __name__ == '__main__':
    main()

import os
import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Try different Chinese image sources
SOURCES_TO_TRY = [
    # Baidu image search results (may work)
    ("painting/test_baidu.jpg", "https://pics7.baidu.com/feed/9f510fb30f2442a7d02b81c97c5e4e3f5243c5c5.jpeg"),
    # Placeholder image services
    ("painting/test_placeholder.jpg", "https://placehold.co/800x600/f5f2ed/666?text=Chinese+Art"),
]

def try_download(local_path, url):
    base_dir = '/home/kai/.openclaw/workspace/images'
    full_path = os.path.join(base_dir, local_path)
    
    try:
        print(f"Trying {url}...")
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Bot/0.1)'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ssl_context, timeout=15) as response:
            data = response.read()
            with open(full_path, 'wb') as f:
                f.write(data)
        print(f"  ✓ Success! {len(data)} bytes")
        return True
    except Exception as e:
        print(f"  ✗ Failed: {str(e)[:60]}")
        return False

def main():
    for local_path, url in SOURCES_TO_TRY:
        try_download(local_path, url)

if __name__ == '__main__':
    main()

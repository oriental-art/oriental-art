import os
import urllib.request
import ssl
import urllib.parse

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Image definitions with placehold.co
IMAGES = {
    # Painting - landscape format (1280x800)
    "painting/fan_kuan_travelers.jpg": ("1280", "800", "Fan Kuan", "Travelers Among Mountains"),
    "painting/guo_xi_early_spring.jpg": ("1280", "800", "Guo Xi", "Early Spring"),
    "painting/ni_zan_cold_mountain.jpg": ("1280", "800", "Ni Zan", "Cold Mountain Pavilion"),
    "painting/shen_zhou_lofty_mount.jpg": ("800", "600", "Shen Zhou", "Lofty Mount Lu"),
    "painting/ma_yuan_spring.jpg": ("800", "600", "Ma Yuan", "Walking on Path in Spring"),
    "painting/dong_qichang_landscape.jpg": ("1280", "800", "Dong Qichang", "Landscape"),
    "painting/huizong_birds_flowers.jpg": ("800", "600", "Emperor Huizong", "Birds and Flowers"),
    "painting/gu_kaizhi_luo_river.jpg": ("1280", "800", "Gu Kaizhi", "Nymph of Luo River"),
    "painting/wang_ximeng_rivers_mountains.jpg": ("1280", "800", "Wang Ximeng", "Rivers and Mountains"),
    "painting/zhang_zeduan_qingming.jpg": ("1280", "800", "Zhang Zeduan", "Qingming Festival"),
    "painting/qi_baishi_shrimp.jpg": ("800", "600", "Qi Baishi", "Shrimp"),
    
    # Calligraphy
    "calligraphy/wang_xizhi_orchid.jpg": ("1280", "800", "Wang Xizhi", "Orchid Pavilion"),
    "calligraphy/huaisu_autobiography.jpg": ("800", "600", "Huaisu", "Autobiography"),
    "calligraphy/brushes.jpg": ("800", "600", "Four Treasures", "Brushes"),
    "calligraphy/seal_script.jpg": ("800", "600", "Small Seal", "Script"),
    
    # Ceramics
    "ceramics/blue_white_vase.jpg": ("800", "600", "Blue and White", "Porcelain"),
    "ceramics/longquan_celadon.jpg": ("800", "600", "Longquan", "Celadon"),
    "ceramics/jian_tea_bowl.jpg": ("800", "600", "Jian Ware", "Tea Bowl"),
    
    # Jade
    "jade/jade_bi_disc.jpg": ("800", "600", "Jade Bi", "Disc"),
    "jade/qing_jade.jpg": ("800", "600", "Qing Dynasty", "Jade"),
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
    
    if os.path.exists(full_path):
        print(f"Skipping {local_path} - exists")
        return True
    
    # Create URL with encoded text
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
    success = 0
    failed = 0
    
    for local_path, (w, h, l1, l2) in IMAGES.items():
        if download_image(local_path, w, h, l1, l2):
            success += 1
        else:
            failed += 1
    
    print(f"\nDone: {success} success, {failed} failed")
    
    # Update HTML files to use .jpg
    print("\nUpdating HTML files to use .jpg extension...")
    os.system("sed -i 's/\\.svg\"/.jpg\"/g' /home/kai/.openclaw/workspace/articles/*/*.html")
    print("HTML files updated!")

if __name__ == '__main__':
    main()

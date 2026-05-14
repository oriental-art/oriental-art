import os
import urllib.request
import ssl

# Create SSL context that ignores certificate verification
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Try different image sources
IMAGE_SOURCES = {
    # Using placeholder.com for testing
    "painting/fan_kuan_travelers.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Fan+Kuan+Travelers",
    "painting/guo_xi_early_spring.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Guo+Xi+Early+Spring",
    "painting/ni_zan_cold_mountain.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Ni+Zan+Cold+Mountain",
    "painting/shen_zhou_lofty_mount.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Shen+Zhou+Lofty+Mount",
    "painting/ma_yuan_spring.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Ma+Yuan+Spring",
    "painting/dong_qichang_landscape.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Dong+Qichang+Landscape",
    "painting/huizong_birds_flowers.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Huizong+Birds+Flowers",
    "painting/gu_kaizhi_luo_river.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Gu+Kaizhi+Luo+River",
    "painting/wang_ximeng_rivers_mountains.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Wang+Ximeng+Rivers",
    "painting/zhang_zeduan_qingming.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Zhang+Zeduan+Qingming",
    "painting/qi_baishi_shrimp.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Qi+Baishi+Shrimp",
    
    "calligraphy/wang_xizhi_orchid.jpg": "https://via.placeholder.com/1280x800/f5f2ed/666?text=Wang+Xizhi+Orchid",
    "calligraphy/huaisu_autobiography.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Huaisu+Autobiography",
    "calligraphy/brushes.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Chinese+Brushes",
    "calligraphy/seal_script.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Seal+Script",
    
    "ceramics/blue_white_vase.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Blue+White+Vase",
    "ceramics/longquan_celadon.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Longquan+Celadon",
    "ceramics/jian_tea_bowl.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Jian+Tea+Bowl",
    
    "jade/jade_bi_disc.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Jade+Bi+Disc",
    "jade/qing_jade.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Qing+Jade",
    "jade/jadeite.jpg": "https://via.placeholder.com/800x600/f5f2ed/666?text=Imperial+Jadeite",
}

def download_image(local_path, url):
    full_path = os.path.join('/home/kai/.openclaw/workspace/images', local_path)
    dir_path = os.path.dirname(full_path)
    os.makedirs(dir_path, exist_ok=True)
    
    if os.path.exists(full_path):
        print(f"Skipping {local_path} - already exists")
        return True
    
    try:
        print(f"Downloading {local_path}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ssl_context, timeout=30) as response:
            with open(full_path, 'wb') as f:
                f.write(response.read())
        print(f"  ✓ Saved {local_path}")
        return True
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        return False

def main():
    success = 0
    failed = 0
    
    for local_path, url in IMAGE_SOURCES.items():
        if download_image(local_path, url):
            success += 1
        else:
            failed += 1
    
    print(f"\nDone: {success} success, {failed} failed")

if __name__ == '__main__':
    main()

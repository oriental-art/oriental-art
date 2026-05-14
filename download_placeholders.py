import os
import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Image definitions with placehold.co
IMAGES = {
    # Painting - landscape format (1280x800)
    "painting/fan_kuan_travelers.jpg": ("1280", "800", "范宽《溪山行旅图》", "Fan Kuan - Travelers Among Mountains"),
    "painting/guo_xi_early_spring.jpg": ("1280", "800", "郭熙《早春图》", "Guo Xi - Early Spring"),
    "painting/ni_zan_cold_mountain.jpg": ("1280", "800", "倪瓒《容膝斋图》", "Ni Zan - Cold Mountain Pavilion"),
    "painting/shen_zhou_lofty_mount.jpg": ("800", "600", "沈周《庐山高图》", "Shen Zhou - Lofty Mount Lu"),
    "painting/ma_yuan_spring.jpg": ("800", "600", "马远《山径春行图》", "Ma Yuan - Walking on Path in Spring"),
    "painting/dong_qichang_landscape.jpg": ("1280", "800", "董其昌《山水图》", "Dong Qichang - Landscape"),
    "painting/huizong_birds_flowers.jpg": ("800", "600", "宋徽宗《花鸟图》", "Emperor Huizong - Birds and Flowers"),
    "painting/gu_kaizhi_luo_river.jpg": ("1280", "800", "顾恺之《洛神赋图》", "Gu Kaizhi - Nymph of Luo River"),
    "painting/wang_ximeng_rivers_mountains.jpg": ("1280", "800", "王希孟《千里江山图》", "Wang Ximeng - Rivers and Mountains"),
    "painting/zhang_zeduan_qingming.jpg": ("1280", "800", "张择端《清明上河图》", "Zhang Zeduan - Qingming Festival"),
    "painting/qi_baishi_shrimp.jpg": ("800", "600", "齐白石《虾》", "Qi Baishi - Shrimp"),
    
    # Calligraphy
    "calligraphy/wang_xizhi_orchid.jpg": ("1280", "800", "王羲之《兰亭序》", "Wang Xizhi - Orchid Pavilion"),
    "calligraphy/huaisu_autobiography.jpg": ("800", "600", "怀素《自叙帖》", "Huaisu - Autobiography"),
    "calligraphy/brushes.jpg": ("800", "600", "文房四宝", "Four Treasures - Brushes"),
    "calligraphy/seal_script.jpg": ("800", "600", "小篆", "Small Seal Script"),
    
    # Ceramics
    "ceramics/blue_white_vase.jpg": ("800", "600", "青花瓷器", "Blue and White Porcelain"),
    "ceramics/longquan_celadon.jpg": ("800", "600", "龙泉青瓷", "Longquan Celadon"),
    "ceramics/jian_tea_bowl.jpg": ("800", "600", "建窑茶盏", "Jian Ware Tea Bowl"),
    
    # Jade
    "jade/jade_bi_disc.jpg": ("800", "600", "玉璧", "Jade Bi Disc"),
    "jade/qing_jade.jpg": ("800", "600", "清代玉雕", "Qing Dynasty Jade"),
    "jade/jadeite.jpg": ("800", "600", "翡翠", "Imperial Jadeite"),
}

def download_image(local_path, width, height, cn_title, en_title):
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
    
    # Create URL with text
    text = f"{cn_title}%0A{en_title}"
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
    
    for local_path, (w, h, cn, en) in IMAGES.items():
        if download_image(local_path, w, h, cn, en):
            success += 1
        else:
            failed += 1
    
    print(f"\nDone: {success} success, {failed} failed")
    
    # List files
    print("\nFiles created:")
    for root, dirs, files in os.walk('/home/kai/.openclaw/workspace/images'):
        for f in sorted(files):
            if f.endswith('.jpg'):
                filepath = os.path.join(root, f)
                size = os.path.getsize(filepath)
                print(f"  {filepath.replace('/home/kai/.openclaw/workspace/images/', '')}: {size/1024:.1f} KB")

if __name__ == '__main__':
    main()

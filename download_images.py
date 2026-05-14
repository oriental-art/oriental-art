import os
import requests
import urllib.parse

# Image mappings: (local_filename, wikimedia_url)
IMAGES = {
    # Painting
    "painting/fan_kuan_travelers.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg/1280px-Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg",
    "painting/guo_xi_early_spring.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg/1280px-Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg",
    "painting/ni_zan_cold_mountain.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg",
    "painting/shen_zhou_lofty_mount.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg/800px-Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg",
    "painting/ma_yuan_spring.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg/800px-Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg",
    "painting/dong_qichang_landscape.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg/1280px-Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg",
    "painting/huizong_birds_flowers.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg/800px-Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg",
    "painting/gu_kaizhi_luo_river.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg/1280px-Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg",
    "painting/wang_ximeng_rivers_mountains.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg",
    "painting/zhang_zeduan_qingming.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg/1280px-Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg",
    "painting/qi_baishi_shrimp.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Qi_Baishi_-_Shrimp.jpg/800px-Qi_Baishi_-_Shrimp.jpg",
    
    # Calligraphy
    "calligraphy/wang_xizhi_orchid.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg",
    "calligraphy/huaisu_autobiography.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Huaisu_Autobiography.jpg/800px-Huaisu_Autobiography.jpg",
    "calligraphy/brushes.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chinese_writing_brushes.jpg/800px-Chinese_writing_brushes.jpg",
    "calligraphy/seal_script.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Small_Seal_Script.jpg/800px-Small_Seal_Script.jpg",
    
    # Ceramics
    "ceramics/blue_white_vase.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg",
    "ceramics/longquan_celadon.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Longquan_celadon_Song_Dynasty.jpg/800px-Longquan_celadon_Song_Dynasty.jpg",
    "ceramics/jian_tea_bowl.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jian_tea_bowl_Song_dynasty.jpg/800px-Jian_tea_bowl_Song_dynasty.jpg",
    
    # Jade
    "jade/jade_bi_disc.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg",
    "jade/qing_jade.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jade_carving_Qing_dynasty.jpg/800px-Jade_carving_Qing_dynasty.jpg",
    "jade/jadeite.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jadeite_Ching_dynasty.jpg/800px-Jadeite_Ching_dynasty.jpg",
}

def download_image(local_path, url):
    full_path = os.path.join('/home/kai/.openclaw/workspace/images', local_path)
    if os.path.exists(full_path):
        print(f"Skipping {local_path} - already exists")
        return True
    
    try:
        print(f"Downloading {local_path}...")
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; Bot/0.1)'}
        response = requests.get(url, headers=headers, timeout=60)
        if response.status_code == 200:
            with open(full_path, 'wb') as f:
                f.write(response.content)
            print(f"  ✓ Saved {local_path} ({len(response.content)} bytes)")
            return True
        else:
            print(f"  ✗ Failed: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    success = 0
    failed = 0
    
    for local_path, url in IMAGES.items():
        if download_image(local_path, url):
            success += 1
        else:
            failed += 1
    
    print(f"\nDone: {success} success, {failed} failed")

if __name__ == '__main__':
    main()

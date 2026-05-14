import os
import re
import glob

# Simple replacement map: (old_pattern, new_path)
REPLACEMENTS = [
    # Painting
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg/1280px-Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg", "../images/painting/fan_kuan_travelers.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg/1280px-Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg", "../images/painting/guo_xi_early_spring.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg", "../images/painting/ni_zan_cold_mountain.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg/800px-Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg", "../images/painting/shen_zhou_lofty_mount.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg/800px-Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg", "../images/painting/ma_yuan_spring.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg/1280px-Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg", "../images/painting/dong_qichang_landscape.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg/800px-Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg", "../images/painting/huizong_birds_flowers.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg/1280px-Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg", "../images/painting/gu_kaizhi_luo_river.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg", "../images/painting/wang_ximeng_rivers_mountains.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg/1280px-Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg", "../images/painting/zhang_zeduan_qingming.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Qi_Baishi_-_Shrimp.jpg/800px-Qi_Baishi_-_Shrimp.jpg", "../images/painting/qi_baishi_shrimp.jpg"),
    
    # Calligraphy
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "../images/calligraphy/wang_xizhi_orchid.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Huaisu_Autobiography.jpg/800px-Huaisu_Autobiography.jpg", "../images/calligraphy/huaisu_autobiography.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chinese_writing_brushes.jpg/800px-Chinese_writing_brushes.jpg", "../images/calligraphy/brushes.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Small_Seal_Script.jpg/800px-Small_Seal_Script.jpg", "../images/calligraphy/seal_script.jpg"),
    
    # Ceramics
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "../images/ceramics/blue_white_vase.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Longquan_celadon_Song_Dynasty.jpg/800px-Longquan_celadon_Song_Dynasty.jpg", "../images/ceramics/longquan_celadon.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jian_tea_bowl_Song_dynasty.jpg/800px-Jian_tea_bowl_Song_dynasty.jpg", "../images/ceramics/jian_tea_bowl.jpg"),
    
    # Jade
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "../images/jade/jade_bi_disc.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jade_carving_Qing_dynasty.jpg/800px-Jade_carving_Qing_dynasty.jpg", "../images/jade/qing_jade.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jadeite_Ching_dynasty.jpg/800px-Jadeite_Ching_dynasty.jpg", "../images/jade/jadeite.jpg"),
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old_url, new_path in REPLACEMENTS:
        content = content.replace(old_url, new_path)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = '/home/kai/.openclaw/workspace/articles'
    categories = ['painting', 'calligraphy', 'ceramics', 'jade']
    
    updated = 0
    for category in categories:
        pattern = os.path.join(base_dir, category, '*.html')
        files = glob.glob(pattern)
        for filepath in sorted(files):
            if process_file(filepath):
                updated += 1
                print(f"Updated: {os.path.basename(filepath)}")
    
    print(f"\nTotal updated: {updated} files")

if __name__ == '__main__':
    main()

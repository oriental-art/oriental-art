import os
import re
import glob

# Additional images for each article (to be inserted at different positions)
ADDITIONAL_IMAGES = {
    # Painting articles
    "02_brush_techniques": [
        ("../images/painting/ni_zan_cold_mountain.jpg", "Ni Zan - The Cold Mountain Pavilion", "Ni Zan (1301-1374), demonstrating masterful brushwork and ink modulation"),
    ],
    "03_bird_flower": [
        ("../images/painting/huizong_birds_flowers.jpg", "Emperor Huizong - Birds and Flowers", "Emperor Huizong (1082-1135), masterpiece of bird-and-flower painting"),
    ],
    "04_song_masters": [
        ("../images/painting/ma_yuan_spring.jpg", "Ma Yuan - Walking on Path in Spring", "Ma Yuan (c. 1160-1225), Southern Song dynasty master"),
        ("../images/painting/guo_xi_early_spring.jpg", "Guo Xi - Early Spring", "Guo Xi (c. 1020-1090), Northern Song dynasty"),
    ],
    "05_literati_painting": [
        ("../images/painting/shen_zhou_lofty_mount.jpg", "Shen Zhou - Lofty Mount Lu", "Shen Zhou (1427-1509), Ming dynasty literati painting"),
        ("../images/painting/ni_zan_cold_mountain.jpg", "Ni Zan - The Cold Mountain Pavilion", "Ni Zan (1301-1374), Yuan dynasty literati style"),
    ],
    "06_figure_painting": [
        ("../images/painting/gu_kaizhi_luo_river.jpg", "Gu Kaizhi - Nymph of the Luo River", "Gu Kaizhi (c. 344-406), Eastern Jin dynasty"),
    ],
    "07_color_painting": [
        ("../images/painting/wang_ximeng_rivers_mountains.jpg", "Wang Ximeng - A Thousand Li of Rivers and Mountains", "Wang Ximeng (1096-1119), blue-green landscape masterpiece"),
    ],
    "08_handscroll": [
        ("../images/painting/zhang_zeduan_qingming.jpg", "Zhang Zeduan - Along the River During the Qingming Festival", "Zhang Zeduan (1085-1145), famous handscroll painting"),
    ],
    "09_modern_painting": [
        ("../images/painting/qi_baishi_shrimp.jpg", "Qi Baishi - Shrimp", "Qi Baishi (1864-1957), modern master of bird-and-flower painting"),
    ],
    "10_appreciation": [
        ("../images/painting/dong_qichang_landscape.jpg", "Dong Qichang - Landscape", "Dong Qichang (1555-1636), Ming dynasty theorist and painter"),
        ("../images/painting/fan_kuan_travelers.jpg", "Fan Kuan - Travelers Among Mountains and Streams", "Fan Kuan (c. 960-1030), Northern Song masterpiece"),
    ],
    
    # Calligraphy articles
    "01_soul_of_brush": [
        ("../images/calligraphy/huaisu_autobiography.jpg", "Huaisu - Autobiography", "Huaisu (737-799), Tang dynasty master of cursive script"),
        ("../images/calligraphy/brushes.jpg", "Chinese Writing Brushes", "The Four Treasures of the Study - brushes"),
    ],
    "02_wang_xizhi": [
        ("../images/calligraphy/huaisu_autobiography.jpg", "Huaisu - Autobiography", "Huaisu (737-799), Tang dynasty cursive script"),
    ],
    "03_five_shades_ink": [
        ("../images/painting/ni_zan_cold_mountain.jpg", "Ni Zan - The Cold Mountain Pavilion", "Ni Zan, demonstrating the five shades of ink"),
    ],
    "04_cursive_script": [
        ("../images/calligraphy/huaisu_autobiography.jpg", "Huaisu - Autobiography", "Huaisu (737-799), wild cursive script masterpiece"),
    ],
    "05_four_treasures": [
        ("../images/calligraphy/brushes.jpg", "Chinese Writing Brushes", "Traditional brushes, one of the Four Treasures"),
        ("../images/calligraphy/seal_script.jpg", "Small Seal Script", "Seal script example"),
    ],
    "06_seal_script": [
        ("../images/calligraphy/seal_script.jpg", "Small Seal Script", "Small Seal Script, standardized by Li Si"),
    ],
    "07_tang_masters": [
        ("../images/calligraphy/huaisu_autobiography.jpg", "Huaisu - Autobiography", "Huaisu, Tang dynasty master"),
    ],
    "08_meditative_art": [
        ("../images/calligraphy/wang_xizhi_orchid.jpg", "Wang Xizhi - Preface to the Orchid Pavilion", "The meditative quality of calligraphy"),
    ],
    "09_women_calligraphy": [
        ("../images/calligraphy/wang_xizhi_orchid.jpg", "Wang Xizhi - Preface to the Orchid Pavilion", "Historical calligraphy traditions"),
    ],
    "10_digital_age": [
        ("../images/calligraphy/brushes.jpg", "Chinese Writing Brushes", "Traditional tools in the digital age"),
    ],
    
    # Ceramics articles
    "01_ceramics_overview": [
        ("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Ming dynasty blue and white porcelain"),
        ("../images/ceramics/longquan_celadon.jpg", "Longquan Celadon", "Song dynasty celadon with jade-green glaze"),
    ],
    "02_blue_white": [
        ("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Blue and white porcelain, Ming dynasty"),
    ],
    "03_song_celadon": [
        ("../images/ceramics/longquan_celadon.jpg", "Longquan Celadon", "Longquan celadon, Song dynasty"),
    ],
    "04_jingdezhen": [
        ("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Jingdezhen porcelain, the pinnacle of Chinese ceramics"),
    ],
    "05_tea_ceramics": [
        ("../images/ceramics/jian_tea_bowl.jpg", "Jian Ware Tea Bowl", "Jian ware with hare's fur glaze, Song dynasty"),
    ],
    "06_monochrome": [
        ("../images/ceramics/longquan_celadon.jpg", "Longquan Celadon", "Monochrome celadon glaze"),
    ],
    "07_export_porcelain": [
        ("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Chinese export porcelain"),
    ],
    "08_collecting_ceramics": [
        ("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Ming blue and white, prized by collectors"),
    ],
    "09_contemporary_ceramics": [
        ("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Contemporary ceramic traditions"),
    ],
    "10_marks": [
        ("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Imperial reign marks on porcelain"),
    ],
    
    # Jade articles
    "01_jade_overview": [
        ("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Neolithic jade bi disc, symbol of heaven"),
        ("../images/jade/qing_jade.jpg", "Qing Dynasty Jade", "Qing dynasty jade carving"),
    ],
    "02_jade_carving": [
        ("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Jade carving example"),
    ],
    "03_cong_bi": [
        ("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Jade bi and cong, Neolithic Liangzhu culture"),
    ],
    "04_qing_jade": [
        ("../images/jade/qing_jade.jpg", "Qing Dynasty Jade", "Qing dynasty jade carving, peak of refinement"),
    ],
    "05_collecting_jade": [
        ("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Ancient jade, highly valued by collectors"),
    ],
    "06_jadeite": [
        ("../images/jade/jadeite.jpg", "Imperial Jadeite", "Imperial green jadeite"),
    ],
    "07_jade_medicine": [
        ("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Jade in traditional Chinese medicine"),
    ],
    "08_symbolism": [
        ("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Jade symbolism in Chinese culture"),
    ],
    "09_jade_jewelry": [
        ("../images/jade/jadeite.jpg", "Imperial Jadeite", "Jadeite jewelry"),
    ],
    "10_future_jade": [
        ("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Ancient jade traditions"),
    ],
}

def make_image_html(img_path, alt, caption):
    return f'''<div class="inline-image">
    <img src="{img_path}" alt="{alt}" loading="lazy">
    <div class="caption">{caption}</div>
</div>
'''

def process_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    article_id = filename.replace('.html', '')
    
    images = ADDITIONAL_IMAGES.get(article_id, [])
    if not images:
        return
    
    # Check current image count
    current_count = content.count('<div class="inline-image">')
    if current_count >= len(images) + 1:
        print(f"Skipping {article_id} - already has {current_count} images")
        return
    
    # Find article content
    match = re.search(r'(<article class="article-content">)(.*?)(</article>)', content, re.DOTALL)
    if not match:
        return
    
    article_body = match.group(2)
    
    # Split by paragraphs
    paragraphs = re.split(r'(</p>)', article_body)
    
    # Insert additional images after some paragraphs
    insert_positions = [4, 8, 12]  # Insert at roughly these paragraph positions
    
    new_body_parts = []
    img_idx = 0
    para_count = 0
    
    for i, part in enumerate(paragraphs):
        new_body_parts.append(part)
        if part == '</p>':
            para_count += 1
            # Insert image at designated positions
            if para_count in insert_positions and img_idx < len(images):
                img_html = make_image_html(images[img_idx][0], images[img_idx][1], images[img_idx][2])
                new_body_parts.append(img_html)
                img_idx += 1
    
    # If we haven't inserted all images, add at the end
    while img_idx < len(images):
        img_html = make_image_html(images[img_idx][0], images[img_idx][1], images[img_idx][2])
        new_body_parts.append(img_html)
        img_idx += 1
    
    new_body = ''.join(new_body_parts)
    content = content.replace(match.group(2), new_body)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_count = content.count('<div class="inline-image">')
    print(f"Updated {article_id}: {current_count} -> {new_count} images")

def main():
    base_dir = '/home/kai/.openclaw/workspace/articles'
    categories = ['painting', 'calligraphy', 'ceramics', 'jade']
    
    for category in categories:
        pattern = os.path.join(base_dir, category, '*.html')
        files = glob.glob(pattern)
        for filepath in sorted(files):
            process_article(filepath)

if __name__ == '__main__':
    main()

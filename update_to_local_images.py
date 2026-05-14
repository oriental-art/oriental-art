import os
import re
import glob
import shutil

# Map article IDs to local image paths
ARTICLE_IMAGES = {
    "01_shan_shui": [
        ("../images/painting/fan_kuan_travelers.jpg", "Fan Kuan - Travelers Among Mountains and Streams", "Fan Kuan (c. 960-1030), Travelers Among Mountains and Streams, Northern Song dynasty"),
        ("../images/painting/guo_xi_early_spring.jpg", "Guo Xi - Early Spring", "Guo Xi (c. 1020-1090), Early Spring, Northern Song dynasty"),
        ("../images/painting/ni_zan_cold_mountain.jpg", "Ni Zan - The Cold Mountain Pavilion", "Ni Zan (1301-1374), The Cold Mountain Pavilion, Yuan dynasty"),
        ("../images/painting/shen_zhou_lofty_mount.jpg", "Shen Zhou - Lofty Mount Lu", "Shen Zhou (1427-1509), Lofty Mount Lu, Ming dynasty"),
        ("../images/painting/ma_yuan_spring.jpg", "Ma Yuan - Walking on Path in Spring", "Ma Yuan (c. 1160-1225), Walking on Path in Spring, Southern Song dynasty"),
        ("../images/painting/dong_qichang_landscape.jpg", "Dong Qichang - Landscape", "Dong Qichang (1555-1636), Landscape, Ming dynasty"),
    ],
    "02_brush_techniques": [("../images/painting/ni_zan_cold_mountain.jpg", "Brushwork Example", "Ni Zan, demonstrating masterful brushwork")],
    "03_bird_flower": [("../images/painting/huizong_birds_flowers.jpg", "Emperor Huizong - Birds and Flowers", "Emperor Huizong (1082-1135), Birds and Flowers, Northern Song dynasty")],
    "04_song_masters": [("../images/painting/ma_yuan_spring.jpg", "Ma Yuan - Walking on Path in Spring", "Ma Yuan (c. 1160-1225), Walking on Path in Spring, Southern Song dynasty")],
    "05_literati_painting": [("../images/painting/shen_zhou_lofty_mount.jpg", "Shen Zhou - Lofty Mount Lu", "Shen Zhou (1427-1509), Lofty Mount Lu, Ming dynasty literati painting")],
    "06_figure_painting": [("../images/painting/gu_kaizhi_luo_river.jpg", "Gu Kaizhi - Nymph of the Luo River", "Gu Kaizhi (c. 344-406), Nymph of the Luo River, Eastern Jin dynasty")],
    "07_color_painting": [("../images/painting/wang_ximeng_rivers_mountains.jpg", "Wang Ximeng - A Thousand Li of Rivers and Mountains", "Wang Ximeng (1096-1119), A Thousand Li of Rivers and Mountains, Northern Song dynasty")],
    "08_handscroll": [("../images/painting/zhang_zeduan_qingming.jpg", "Zhang Zeduan - Along the River During the Qingming Festival", "Zhang Zeduan (1085-1145), Along the River During the Qingming Festival, Northern Song dynasty")],
    "09_modern_painting": [("../images/painting/qi_baishi_shrimp.jpg", "Qi Baishi - Shrimp", "Qi Baishi (1864-1957), Shrimp, modern master")],
    "10_appreciation": [("../images/painting/dong_qichang_landscape.jpg", "Dong Qichang - Landscape", "Dong Qichang (1555-1636), Landscape, Ming dynasty")],
    
    "01_soul_of_brush": [("../images/calligraphy/wang_xizhi_orchid.jpg", "Wang Xizhi - Preface to the Orchid Pavilion", "Wang Xizhi (303-361), Preface to the Poems Composed at the Orchid Pavilion")],
    "02_wang_xizhi": [("../images/calligraphy/wang_xizhi_orchid.jpg", "Wang Xizhi - Preface to the Orchid Pavilion", "Wang Xizhi (303-361), Preface to the Poems Composed at the Orchid Pavilion")],
    "03_five_shades_ink": [("../images/painting/ni_zan_cold_mountain.jpg", "Five Shades of Ink", "Ni Zan, demonstrating the five shades of ink")],
    "04_cursive_script": [("../images/calligraphy/huaisu_autobiography.jpg", "Huaisu - Autobiography", "Huaisu (737-799), Autobiography in wild cursive script, Tang dynasty")],
    "05_four_treasures": [("../images/calligraphy/brushes.jpg", "Chinese Writing Brushes", "Traditional Chinese writing brushes, one of the Four Treasures of the Study")],
    "06_seal_script": [("../images/calligraphy/seal_script.jpg", "Small Seal Script", "Small Seal Script, standardized by Li Si during the Qin dynasty")],
    "07_tang_masters": [("../images/calligraphy/huaisu_autobiography.jpg", "Huaisu - Tang Master", "Huaisu, Tang dynasty master of cursive script")],
    "08_meditative_art": [("../images/calligraphy/wang_xizhi_orchid.jpg", "Meditative Calligraphy", "The meditative quality of classical calligraphy")],
    "09_women_calligraphy": [("../images/calligraphy/wang_xizhi_orchid.jpg", "Historical Calligraphy", "Historical calligraphy traditions")],
    "10_digital_age": [("../images/calligraphy/brushes.jpg", "Traditional Tools", "Traditional tools in the digital age")],
    
    "01_ceramics_overview": [("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Blue and white porcelain vase, Jingdezhen, Ming dynasty Yongle period (1403-1424)")],
    "02_blue_white": [("../images/ceramics/blue_white_vase.jpg", "Blue and White Porcelain", "Blue and white porcelain vase, Ming dynasty Yongle period")],
    "03_song_celadon": [("../images/ceramics/longquan_celadon.jpg", "Longquan Celadon", "Longquan celadon, Song dynasty, showing the characteristic jade-green glaze")],
    "04_jingdezhen": [("../images/ceramics/blue_white_vase.jpg", "Jingdezhen Porcelain", "Jingdezhen blue and white porcelain, the pinnacle of Chinese ceramic art")],
    "05_tea_ceramics": [("../images/ceramics/jian_tea_bowl.jpg", "Jian Tea Bowl", "Jian ware tea bowl with hare's fur glaze, Song dynasty")],
    "06_monochrome": [("../images/ceramics/longquan_celadon.jpg", "Monochrome Celadon", "Monochrome celadon glaze, Song dynasty")],
    "07_export_porcelain": [("../images/ceramics/blue_white_vase.jpg", "Export Porcelain", "Chinese export porcelain that influenced global ceramic traditions")],
    "08_collecting_ceramics": [("../images/ceramics/blue_white_vase.jpg", "Ming Blue and White", "Ming dynasty blue and white, highly prized by collectors")],
    "09_contemporary_ceramics": [("../images/ceramics/blue_white_vase.jpg", "Ceramic Tradition", "Contemporary artists continue the ceramic tradition")],
    "10_marks": [("../images/ceramics/blue_white_vase.jpg", "Imperial Marks", "Imperial reign marks on Chinese porcelain")],
    
    "01_jade_overview": [("../images/jade/jade_bi_disc.jpg", "Jade Bi Disc", "Jade bi disc, Neolithic period, representing heaven in ancient Chinese cosmology")],
    "02_jade_carving": [("../images/jade/jade_bi_disc.jpg", "Jade Carving", "Intricate jade carving demonstrating technical mastery")],
    "03_cong_bi": [("../images/jade/jade_bi_disc.jpg", "Cong and Bi", "Jade bi disc and cong, Neolithic Liangzhu culture")],
    "04_qing_jade": [("../images/jade/qing_jade.jpg", "Qing Jade", "Qing dynasty jade carving, representing the peak of technical refinement")],
    "05_collecting_jade": [("../images/jade/jade_bi_disc.jpg", "Ancient Jade", "Ancient jade bi disc, highly valued by collectors")],
    "06_jadeite": [("../images/jade/jadeite.jpg", "Imperial Jadeite", "Imperial green jadeite, the most precious variety of jade")],
    "07_jade_medicine": [("../images/jade/jade_bi_disc.jpg", "Jade in Medicine", "Jade was believed to have healing properties in traditional Chinese medicine")],
    "08_symbolism": [("../images/jade/jade_bi_disc.jpg", "Jade Symbolism", "Jade bi disc symbolizing heaven and cosmic order")],
    "09_jade_jewelry": [("../images/jade/jadeite.jpg", "Jade Jewelry", "Jadeite jewelry, prized for its color and translucency")],
    "10_future_jade": [("../images/jade/jade_bi_disc.jpg", "Jade Tradition", "Ancient jade traditions continue to inspire contemporary artists")],
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
    
    images = ARTICLE_IMAGES.get(article_id, [])
    if not images:
        return
    
    # Replace existing inline images with local paths
    # Find all inline-image divs
    pattern = r'<div class="inline-image">\s*<img src="[^"]*" alt="([^"]*)"[^>]*>\s*<div class="caption">([^<]*)</div>\s*</div>'
    
    def replace_image(match, img_list=images):
        alt = match.group(1)
        # Find matching image in our list
        for img_path, img_alt, caption in img_list:
            if img_alt in alt or alt in img_alt:
                return make_image_html(img_path, img_alt, caption)
        # If no match, use first image
        if img_list:
            return make_image_html(img_list[0][0], img_list[0][1], img_list[0][2])
        return match.group(0)
    
    new_content = re.sub(pattern, replace_image, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {article_id}")

def main():
    base_dir = '/home/kai/.openclaw/workspace/articles'
    categories = ['painting', 'calligraphy', 'ceramics', 'jade']
    
    for category in categories:
        pattern = os.path.join(base_dir, category, '*.html')
        files = glob.glob(pattern)
        for filepath in sorted(files):
            process_article(filepath)
    
    print("\nDone! Now copy actual images to images/ folder")

if __name__ == '__main__':
    main()

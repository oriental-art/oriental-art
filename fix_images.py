import os
import re
import glob

# Article-specific image mappings from Wikimedia Commons
ARTICLE_IMAGES = {
    "01_shan_shui": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg/1280px-Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg", "Fan Kuan - Travelers Among Mountains and Streams", "Fan Kuan (c. 960-1030), Travelers Among Mountains and Streams, Northern Song dynasty"),
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg/1280px-Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg", "Guo Xi - Early Spring", "Guo Xi (c. 1020-1090), Early Spring, Northern Song dynasty"),
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg", "Ni Zan - The Cold Mountain Pavilion", "Ni Zan (1301-1374), The Cold Mountain Pavilion, Yuan dynasty"),
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg/800px-Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg", "Shen Zhou - Lofty Mount Lu", "Shen Zhou (1427-1509), Lofty Mount Lu, Ming dynasty"),
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg/800px-Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg", "Ma Yuan - Walking on Path in Spring", "Ma Yuan (c. 1160-1225), Walking on Path in Spring, Southern Song dynasty"),
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg/1280px-Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg", "Dong Qichang - Landscape", "Dong Qichang (1555-1636), Landscape, Ming dynasty"),
    ],
    "02_brush_techniques": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg", "Brushwork Example", "Ni Zan (1301-1374), The Cold Mountain Pavilion, demonstrating masterful brushwork"),
    ],
    "03_bird_flower": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg/800px-Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg", "Emperor Huizong - Birds and Flowers", "Emperor Huizong (1082-1135), Birds and Flowers, Northern Song dynasty"),
    ],
    "04_song_masters": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg/800px-Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg", "Ma Yuan - Walking on Path in Spring", "Ma Yuan (c. 1160-1225), Walking on Path in Spring, Southern Song dynasty"),
    ],
    "05_literati_painting": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg/800px-Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg", "Shen Zhou - Lofty Mount Lu", "Shen Zhou (1427-1509), Lofty Mount Lu, Ming dynasty literati painting"),
    ],
    "06_figure_painting": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg/1280px-Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg", "Gu Kaizhi - Nymph of the Luo River", "Gu Kaizhi (c. 344-406), Nymph of the Luo River, Eastern Jin dynasty"),
    ],
    "07_color_painting": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg", "Wang Ximeng - A Thousand Li of Rivers and Mountains", "Wang Ximeng (1096-1119), A Thousand Li of Rivers and Mountains, Northern Song dynasty blue-green landscape"),
    ],
    "08_handscroll": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg/1280px-Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg", "Zhang Zeduan - Along the River During the Qingming Festival", "Zhang Zeduan (1085-1145), Along the River During the Qingming Festival, Northern Song dynasty handscroll"),
    ],
    "09_modern_painting": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Qi_Baishi_-_Shrimp.jpg/800px-Qi_Baishi_-_Shrimp.jpg", "Qi Baishi - Shrimp", "Qi Baishi (1864-1957), Shrimp, modern master"),
    ],
    "10_appreciation": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg/1280px-Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg", "Dong Qichang - Landscape", "Dong Qichang (1555-1636), Landscape, Ming dynasty"),
    ],
    "01_soul_of_brush": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "Wang Xizhi - Preface to the Orchid Pavilion", "Wang Xizhi (303-361), Preface to the Poems Composed at the Orchid Pavilion"),
    ],
    "02_wang_xizhi": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "Wang Xizhi - Preface to the Orchid Pavilion", "Wang Xizhi (303-361), Preface to the Poems Composed at the Orchid Pavilion"),
    ],
    "03_five_shades_ink": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg", "Five Shades of Ink", "Ni Zan, demonstrating the five shades of ink"),
    ],
    "04_cursive_script": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Huaisu_Autobiography.jpg/800px-Huaisu_Autobiography.jpg", "Huaisu - Autobiography", "Huaisu (737-799), Autobiography in wild cursive script, Tang dynasty"),
    ],
    "05_four_treasures": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chinese_writing_brushes.jpg/800px-Chinese_writing_brushes.jpg", "Chinese Writing Brushes", "Traditional Chinese writing brushes, one of the Four Treasures of the Study"),
    ],
    "06_seal_script": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Small_Seal_Script.jpg/800px-Small_Seal_Script.jpg", "Small Seal Script", "Small Seal Script, standardized by Li Si during the Qin dynasty"),
    ],
    "07_tang_masters": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Huaisu_Autobiography.jpg/800px-Huaisu_Autobiography.jpg", "Huaisu - Tang Master", "Huaisu, Tang dynasty master of cursive script"),
    ],
    "08_meditative_art": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "Meditative Calligraphy", "The meditative quality of classical calligraphy"),
    ],
    "09_women_calligraphy": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "Historical Calligraphy", "Historical calligraphy traditions"),
    ],
    "10_digital_age": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chinese_writing_brushes.jpg/800px-Chinese_writing_brushes.jpg", "Traditional Tools", "Traditional tools in the digital age"),
    ],
    "01_ceramics_overview": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Blue and White Porcelain", "Blue and white porcelain vase, Jingdezhen, Ming dynasty Yongle period (1403-1424)"),
    ],
    "02_blue_white": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Blue and White Porcelain", "Blue and white porcelain vase, Ming dynasty Yongle period"),
    ],
    "03_song_celadon": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Longquan_celadon_Song_Dynasty.jpg/800px-Longquan_celadon_Song_Dynasty.jpg", "Longquan Celadon", "Longquan celadon, Song dynasty, showing the characteristic jade-green glaze"),
    ],
    "04_jingdezhen": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Jingdezhen Porcelain", "Jingdezhen blue and white porcelain, the pinnacle of Chinese ceramic art"),
    ],
    "05_tea_ceramics": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jian_tea_bowl_Song_dynasty.jpg/800px-Jian_tea_bowl_Song_dynasty.jpg", "Jian Tea Bowl", "Jian ware tea bowl with hare's fur glaze, Song dynasty"),
    ],
    "06_monochrome": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Longquan_celadon_Song_Dynasty.jpg/800px-Longquan_celadon_Song_Dynasty.jpg", "Monochrome Celadon", "Monochrome celadon glaze, Song dynasty"),
    ],
    "07_export_porcelain": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Export Porcelain", "Chinese export porcelain that influenced global ceramic traditions"),
    ],
    "08_collecting_ceramics": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Ming Blue and White", "Ming dynasty blue and white, highly prized by collectors"),
    ],
    "09_contemporary_ceramics": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Ceramic Tradition", "Contemporary artists continue the ceramic tradition"),
    ],
    "10_marks": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Imperial Marks", "Imperial reign marks on Chinese porcelain"),
    ],
    "01_jade_overview": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade Bi Disc", "Jade bi disc, Neolithic period, representing heaven in ancient Chinese cosmology"),
    ],
    "02_jade_carving": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade Carving", "Intricate jade carving demonstrating technical mastery"),
    ],
    "03_cong_bi": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Cong and Bi", "Jade bi disc and cong, Neolithic Liangzhu culture"),
    ],
    "04_qing_jade": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jade_carving_Qing_dynasty.jpg/800px-Jade_carving_Qing_dynasty.jpg", "Qing Jade", "Qing dynasty jade carving, representing the peak of technical refinement"),
    ],
    "05_collecting_jade": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Ancient Jade", "Ancient jade bi disc, highly valued by collectors"),
    ],
    "06_jadeite": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jadeite_Ching_dynasty.jpg/800px-Jadeite_Ching_dynasty.jpg", "Imperial Jadeite", "Imperial green jadeite, the most precious variety of jade"),
    ],
    "07_jade_medicine": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade in Medicine", "Jade was believed to have healing properties in traditional Chinese medicine"),
    ],
    "08_symbolism": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade Symbolism", "Jade bi disc symbolizing heaven and cosmic order"),
    ],
    "09_jade_jewelry": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jadeite_Ching_dynasty.jpg/800px-Jadeite_Ching_dynasty.jpg", "Jade Jewelry", "Jadeite jewelry, prized for its color and translucency"),
    ],
    "10_future_jade": [
        ("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade Tradition", "Ancient jade traditions continue to inspire contemporary artists"),
    ],
}

def make_image_html(url, alt, caption):
    return f'''<div class="inline-image">
    <img src="{url}" alt="{alt}" loading="lazy">
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
        print(f"No images for {article_id}")
        return
    
    # Check if already has inline images
    if '<div class="inline-image">' in content:
        print(f"Already has inline images: {article_id}")
        return
    
    # Find article content
    match = re.search(r'(<article class="article-content">)(.*?)(</article>)', content, re.DOTALL)
    if not match:
        print(f"No article content found: {article_id}")
        return
    
    article_start = match.group(1)
    article_body = match.group(2)
    article_end = match.group(3)
    
    # Split by paragraphs
    paragraphs = re.split(r'(</p>)', article_body)
    
    # Insert images after certain paragraphs
    new_body_parts = []
    img_idx = 0
    
    for i, para in enumerate(paragraphs):
        new_body_parts.append(para)
        
        # Insert image after every 4th closing </p> tag
        if para == '</p>' and img_idx < len(images):
            if (i // 2) % 4 == 2:  # Every 4th paragraph
                img_html = make_image_html(images[img_idx][0], images[img_idx][1], images[img_idx][2])
                new_body_parts.append(img_html)
                img_idx += 1
    
    # If we haven't inserted all images, add them at the end
    while img_idx < len(images):
        img_html = make_image_html(images[img_idx][0], images[img_idx][1], images[img_idx][2])
        new_body_parts.append(img_html)
        img_idx += 1
    
    new_body = ''.join(new_body_parts)
    
    # Replace article content
    new_article = article_start + new_body + article_end
    content = content.replace(match.group(0), new_article)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {article_id} with {len(images)} image(s)")

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

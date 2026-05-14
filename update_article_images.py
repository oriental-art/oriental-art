import os
import re
import glob

# Article-specific image mappings from Wikimedia Commons (museum collections)
ARTICLE_IMAGES = {
    # Painting articles
    "01_shan_shui": [
        ("Fan Kuan", "Fan Kuan - Travelers Among Mountains and Streams", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg/1280px-Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg", "Fan Kuan (c. 960-1030), Travelers Among Mountains and Streams, Northern Song dynasty"),
        ("Guo Xi", "Early Spring", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg/1280px-Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg", "Guo Xi (c. 1020-1090), Early Spring, Northern Song dynasty"),
        ("Ni Zan", "The Cold Mountain Pavilion", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg", "Ni Zan (1301-1374), The Cold Mountain Pavilion, Yuan dynasty"),
    ],
    "02_brush_techniques": [
        ("brushwork", "Chinese brush painting technique", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Chinese_Brush_Painting.jpg/800px-Chinese_Brush_Painting.jpg", "Traditional Chinese brush painting demonstrating various stroke techniques"),
    ],
    "03_bird_flower": [
        ("bird and flower", "Bird and Flower Painting", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg/800px-Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg", "Emperor Huizong (1082-1135), Birds and Flowers, Northern Song dynasty"),
    ],
    "04_song_masters": [
        ("Song dynasty", "Song Dynasty Landscape", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg/800px-Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg", "Ma Yuan (c. 1160-1225), Walking on Path in Spring, Southern Song dynasty"),
    ],
    "05_literati_painting": [
        ("literati", "Literati Painting", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg/800px-Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg", "Shen Zhou (1427-1509), Lofty Mount Lu, Ming dynasty"),
    ],
    "06_figure_painting": [
        ("figure", "Chinese Figure Painting", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg/1280px-Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg", "Gu Kaizhi (c. 344-406), Nymph of the Luo River, Eastern Jin dynasty"),
    ],
    "07_color_painting": [
        ("color", "Blue Green Landscape", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg", "Wang Ximeng (1096-1119), A Thousand Li of Rivers and Mountains, Northern Song dynasty"),
    ],
    "08_handscroll": [
        ("handscroll", "Handscroll Format", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg/1280px-Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg", "Zhang Zeduan (1085-1145), Along the River During the Qingming Festival, Northern Song dynasty"),
    ],
    "09_modern_painting": [
        ("modern", "Modern Chinese Painting", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Qi_Baishi_-_Shrimp.jpg/800px-Qi_Baishi_-_Shrimp.jpg", "Qi Baishi (1864-1957), Shrimp, modern master"),
    ],
    "10_appreciation": [
        ("appreciation", "Painting Appreciation", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg/1280px-Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg", "Dong Qichang (1555-1636), Landscape, Ming dynasty"),
    ],
    
    # Calligraphy articles
    "01_soul_of_brush": [
        ("calligraphy", "Wang Xizhi Calligraphy", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "Wang Xizhi (303-361), Preface to the Poems Composed at the Orchid Pavilion, the most celebrated masterpiece of Chinese calligraphy"),
    ],
    "02_wang_xizhi": [
        ("Wang Xizhi", "Wang Xizhi", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "Wang Xizhi (303-361), Preface to the Poems Composed at the Orchid Pavilion"),
    ],
    "03_five_shades_ink": [
        ("ink", "Ink Wash Painting", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg", "Ni Zan, demonstrating the five shades of ink"),
    ],
    "04_cursive_script": [
        ("cursive", "Cursive Script", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Huaisu_Autobiography.jpg/800px-Huaisu_Autobiography.jpg", "Huaisu (737-799), Autobiography in wild cursive script, Tang dynasty"),
    ],
    "05_four_treasures": [
        ("treasures", "Four Treasures", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chinese_writing_brushes.jpg/800px-Chinese_writing_brushes.jpg", "Traditional Chinese writing brushes, one of the Four Treasures of the Study"),
    ],
    "06_seal_script": [
        ("seal", "Seal Script", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Small_Seal_Script.jpg/800px-Small_Seal_Script.jpg", "Small Seal Script, standardized by Li Si during the Qin dynasty"),
    ],
    "07_tang_masters": [
        ("Tang", "Tang Calligraphy", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Huaisu_Autobiography.jpg/800px-Huaisu_Autobiography.jpg", "Huaisu, Tang dynasty master of cursive script"),
    ],
    "08_meditative_art": [
        ("meditative", "Meditative Calligraphy", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "The meditative quality of classical calligraphy"),
    ],
    "09_women_calligraphy": [
        ("women", "Women Calligraphers", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg", "Historical calligraphy by women artists"),
    ],
    "10_digital_age": [
        ("digital", "Digital Calligraphy", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chinese_writing_brushes.jpg/800px-Chinese_writing_brushes.jpg", "Traditional tools in the digital age"),
    ],
    
    # Ceramics articles
    "01_ceramics_overview": [
        ("ceramics", "Chinese Ceramics", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Blue and white porcelain vase, Jingdezhen, Ming dynasty Yongle period (1403-1424)"),
    ],
    "02_blue_white": [
        ("blue white", "Blue and White Porcelain", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Blue and white porcelain vase, Ming dynasty Yongle period"),
    ],
    "03_song_celadon": [
        ("celadon", "Song Celadon", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Longquan_celadon_Song_Dynasty.jpg/800px-Longquan_celadon_Song_Dynasty.jpg", "Longquan celadon, Song dynasty, showing the characteristic jade-green glaze"),
    ],
    "04_jingdezhen": [
        ("Jingdezhen", "Jingdezhen Porcelain", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Jingdezhen blue and white porcelain, the pinnacle of Chinese ceramic art"),
    ],
    "05_tea_ceramics": [
        ("tea", "Tea Ceramics", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jian_tea_bowl_Song_dynasty.jpg/800px-Jian_tea_bowl_Song_dynasty.jpg", "Jian ware tea bowl with hare's fur glaze, Song dynasty"),
    ],
    "06_monochrome": [
        ("monochrome", "Monochrome Glazes", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Longquan_celadon_Song_Dynasty.jpg/800px-Longquan_celadon_Song_Dynasty.jpg", "Monochrome celadon glaze, Song dynasty"),
    ],
    "07_export_porcelain": [
        ("export", "Export Porcelain", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Chinese export porcelain that influenced global ceramic traditions"),
    ],
    "08_collecting_ceramics": [
        ("collecting", "Ceramic Collection", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Ming dynasty blue and white, highly prized by collectors"),
    ],
    "09_contemporary_ceramics": [
        ("contemporary", "Contemporary Ceramics", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Contemporary artists continue the ceramic tradition"),
    ],
    "10_marks": [
        ("marks", "Ceramic Marks", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg", "Imperial reign marks on Chinese porcelain"),
    ],
    
    # Jade articles
    "01_jade_overview": [
        ("jade", "Chinese Jade", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade bi disc, Neolithic period, representing heaven in ancient Chinese cosmology"),
    ],
    "02_jade_carving": [
        ("carving", "Jade Carving", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Intricate jade carving demonstrating technical mastery"),
    ],
    "03_cong_bi": [
        ("cong bi", "Cong and Bi", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade bi disc and cong, Neolithic Liangzhu culture"),
    ],
    "04_qing_jade": [
        ("Qing", "Qing Dynasty Jade", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jade_carving_Qing_dynasty.jpg/800px-Jade_carving_Qing_dynasty.jpg", "Qing dynasty jade carving, representing the peak of technical refinement"),
    ],
    "05_collecting_jade": [
        ("collecting", "Jade Collection", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Ancient jade bi disc, highly valued by collectors"),
    ],
    "06_jadeite": [
        ("jadeite", "Jadeite", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jadeite_Ching_dynasty.jpg/800px-Jadeite_Ching_dynasty.jpg", "Imperial green jadeite, the most precious variety of jade"),
    ],
    "07_jade_medicine": [
        ("medicine", "Jade in Medicine", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade was believed to have healing properties in traditional Chinese medicine"),
    ],
    "08_symbolism": [
        ("symbolism", "Jade Symbolism", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Jade bi disc symbolizing heaven and cosmic order"),
    ],
    "09_jade_jewelry": [
        ("jewelry", "Jade Jewelry", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jadeite_Ching_dynasty.jpg/800px-Jadeite_Ching_dynasty.jpg", "Jadeite jewelry, prized for its color and translucency"),
    ],
    "10_future_jade": [
        ("future", "Future of Jade", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg", "Ancient jade traditions continue to inspire contemporary artists"),
    ],
}

def extract_content_sections(html_content):
    """Extract the main content sections from HTML"""
    # Find content between article tags
    article_match = re.search(r'<article class="article-content">(.*?)</article>', html_content, re.DOTALL)
    if not article_match:
        return None, None
    
    content = article_match.group(1)
    
    # Split by h2 headings
    sections = re.split(r'(<h2>.*?</h2>)', content)
    return sections, content

def insert_images_into_content(content, images, article_id):
    """Insert images at appropriate positions in content"""
    if not images:
        return content
    
    # Split content by paragraphs and headings
    parts = re.split(r'(</p>|</h2>)', content)
    
    result = []
    image_idx = 0
    
    for i, part in enumerate(parts):
        result.append(part)
        
        # Insert image after every 3rd paragraph or after certain headings
        if image_idx < len(images) and (part == '</p>' or part == '</h2>'):
            if i % 4 == 2:  # Insert roughly every 4th closing tag
                img_html = f'''
<div class="inline-image">
    <img src="{images[image_idx][2]}" alt="{images[image_idx][1]}" loading="lazy">
    <div class="caption">{images[image_idx][3]}</div>
</div>
'''
                result.append(img_html)
                image_idx += 1
    
    return ''.join(result)

def process_article(filepath):
    """Process a single article file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract article ID from filename
    filename = os.path.basename(filepath)
    article_id = filename.replace('.html', '')
    
    # Get images for this article
    images = ARTICLE_IMAGES.get(article_id, [])
    
    if not images:
        print(f"No images defined for {article_id}")
        return
    
    # Check if already has inline images
    if 'class="inline-image"' in content:
        print(f"Skipping {article_id} - already has inline images")
        return
    
    # Extract article content
    article_match = re.search(r'(<article class="article-content">)(.*?)(</article>)', content, re.DOTALL)
    if not article_match:
        print(f"Could not find article content in {article_id}")
        return
    
    article_start = article_match.group(1)
    article_body = article_match.group(2)
    article_end = article_match.group(3)
    
    # Insert images into content
    new_body = insert_images_into_content(article_body, images, article_id)
    
    # Add inline-image CSS if not present
    if '.inline-image' not in content:
        css_to_add = '''        .inline-image {
            margin: 32px 0;
            text-align: center;
        }
        .inline-image img {
            max-width: 100%; height: auto;
            border-radius: 4px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .inline-image .caption {
            font-size: 0.85rem;
            color: var(--ink-gray);
            margin-top: 12px;
            font-style: italic;
        }
'''
        # Insert before the @media query
        content = content.replace('@media (max-width: 768px)', css_to_add + '        @media (max-width: 768px)')
    
    # Replace article content
    new_article = article_start + new_body + article_end
    content = content.replace(article_match.group(0), new_article)
    
    # Remove gallery section if present
    gallery_pattern = r'    <section class="gallery-section">.*?</section>\n'
    content = re.sub(gallery_pattern, '', content, flags=re.DOTALL)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {article_id} with {len(images)} images")

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

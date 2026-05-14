import os

# SVG templates for different artwork types
LANDSCAPE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="800" viewBox="0 0 1280 800">
  <rect width="1280" height="800" fill="#f5f2ed"/>
  <path d="M0 600 Q320 400 640 500 T1280 450 L1280 800 L0 800 Z" fill="#d4c4b0" opacity="0.5"/>
  <path d="M0 500 Q400 300 800 400 T1280 350 L1280 800 L0 800 Z" fill="#c4b4a0" opacity="0.4"/>
  <text x="640" y="380" font-family="serif" font-size="32" fill="#5a4a3a" text-anchor="middle" font-style="italic">{title}</text>
  <text x="640" y="420" font-family="sans-serif" font-size="16" fill="#8a7a6a" text-anchor="middle">{subtitle}</text>
</svg>'''

PORTRAIT_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <rect width="800" height="600" fill="#f5f2ed"/>
  <text x="400" y="280" font-family="serif" font-size="28" fill="#5a4a3a" text-anchor="middle" font-style="italic">{title}</text>
  <text x="400" y="320" font-family="sans-serif" font-size="14" fill="#8a7a6a" text-anchor="middle">{subtitle}</text>
</svg>'''

CALLIGRAPHY_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="800" viewBox="0 0 1280 800">
  <rect width="1280" height="800" fill="#faf8f5"/>
  <text x="640" y="380" font-family="serif" font-size="36" fill="#1a1a1a" text-anchor="middle">{title}</text>
  <text x="640" y="430" font-family="sans-serif" font-size="16" fill="#4a4a4a" text-anchor="middle">{subtitle}</text>
</svg>'''

CERAMICS_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <rect width="800" height="600" fill="#f0f0f0"/>
  <ellipse cx="400" cy="350" rx="120" ry="150" fill="#e8e8e8" stroke="#ccc" stroke-width="2"/>
  <text x="400" y="280" font-family="serif" font-size="24" fill="#5a5a5a" text-anchor="middle">{title}</text>
  <text x="400" y="540" font-family="sans-serif" font-size="14" fill="#888" text-anchor="middle">{subtitle}</text>
</svg>'''

JADE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
  <rect width="800" height="600" fill="#f5f5f0"/>
  <circle cx="400" cy="300" r="100" fill="#7a9a8a" opacity="0.6"/>
  <text x="400" y="280" font-family="serif" font-size="24" fill="#fff" text-anchor="middle">{title}</text>
  <text x="400" y="450" font-family="sans-serif" font-size="14" fill="#5a8a7f" text-anchor="middle">{subtitle}</text>
</svg>'''

# Image definitions
IMAGES = {
    # Painting - landscape format
    "painting/fan_kuan_travelers.jpg": ("Fan Kuan", "Travelers Among Mountains and Streams, Northern Song", LANDSCAPE_SVG),
    "painting/guo_xi_early_spring.jpg": ("Guo Xi", "Early Spring, Northern Song", LANDSCAPE_SVG),
    "painting/ni_zan_cold_mountain.jpg": ("Ni Zan", "The Cold Mountain Pavilion, Yuan", LANDSCAPE_SVG),
    "painting/shen_zhou_lofty_mount.jpg": ("Shen Zhou", "Lofty Mount Lu, Ming", PORTRAIT_SVG),
    "painting/ma_yuan_spring.jpg": ("Ma Yuan", "Walking on Path in Spring, Southern Song", PORTRAIT_SVG),
    "painting/dong_qichang_landscape.jpg": ("Dong Qichang", "Landscape, Ming", LANDSCAPE_SVG),
    "painting/huizong_birds_flowers.jpg": ("Emperor Huizong", "Birds and Flowers, Northern Song", PORTRAIT_SVG),
    "painting/gu_kaizhi_luo_river.jpg": ("Gu Kaizhi", "Nymph of the Luo River, Eastern Jin", LANDSCAPE_SVG),
    "painting/wang_ximeng_rivers_mountains.jpg": ("Wang Ximeng", "A Thousand Li of Rivers and Mountains, Northern Song", LANDSCAPE_SVG),
    "painting/zhang_zeduan_qingming.jpg": ("Zhang Zeduan", "Along the River During Qingming Festival, Northern Song", LANDSCAPE_SVG),
    "painting/qi_baishi_shrimp.jpg": ("Qi Baishi", "Shrimp, Modern Master", PORTRAIT_SVG),
    
    # Calligraphy
    "calligraphy/wang_xizhi_orchid.jpg": ("Wang Xizhi", "Preface to the Orchid Pavilion, Jin Dynasty", CALLIGRAPHY_SVG),
    "calligraphy/huaisu_autobiography.jpg": ("Huaisu", "Autobiography, Tang Dynasty", PORTRAIT_SVG),
    "calligraphy/brushes.jpg": ("Four Treasures", "Chinese Writing Brushes", PORTRAIT_SVG),
    "calligraphy/seal_script.jpg": ("Seal Script", "Small Seal Script, Qin Dynasty", PORTRAIT_SVG),
    
    # Ceramics
    "ceramics/blue_white_vase.jpg": ("Blue & White Porcelain", "Ming Dynasty, Jingdezhen", CERAMICS_SVG),
    "ceramics/longquan_celadon.jpg": ("Longquan Celadon", "Song Dynasty, Jade-green Glaze", CERAMICS_SVG),
    "ceramics/jian_tea_bowl.jpg": ("Jian Ware Tea Bowl", "Song Dynasty, Hare's Fur Glaze", CERAMICS_SVG),
    
    # Jade
    "jade/jade_bi_disc.jpg": ("Jade Bi Disc", "Neolithic Period, Liangzhu Culture", JADE_SVG),
    "jade/qing_jade.jpg": ("Qing Jade Carving", "Qing Dynasty, Peak of Refinement", JADE_SVG),
    "jade/jadeite.jpg": ("Imperial Jadeite", "The Most Precious Variety", JADE_SVG),
}

def create_image(path, title, subtitle, template):
    full_path = os.path.join('/home/kai/.openclaw/workspace/images', path.replace('.jpg', '.svg'))
    dir_path = os.path.dirname(full_path)
    os.makedirs(dir_path, exist_ok=True)
    
    svg_content = template.format(title=title, subtitle=subtitle)
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"Created: {path.replace('.jpg', '.svg')}")

def main():
    for path, (title, subtitle, template) in IMAGES.items():
        create_image(path, title, subtitle, template)
    
    print("\nAll SVG images created!")
    print("\nNow updating HTML files to use .svg extension...")

if __name__ == '__main__':
    main()

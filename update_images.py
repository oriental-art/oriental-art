#!/usr/bin/env python3
"""
更新所有文章中的图片链接为可靠的Unsplash图片
"""

import os
import re

# 图片配置 - 每个分类使用相关的Unsplash图片
category_images = {
    "calligraphy": {
        "img1": ("https://images.unsplash.com/photo-1516961642265-531546e84af2?w=800&q=80", "王羲之《兰亭序》书法"),
        "img2": ("https://images.unsplash.com/photo-1584448082978-4553a877b910?w=800&q=80", "毛笔书写艺术")
    },
    "painting": {
        "img1": ("https://images.unsplash.com/photo-1578926288207-a90a5366759d?w=800&q=80", "中国传统山水画"),
        "img2": ("https://images.unsplash.com/photo-1580136608260-4eb11f4b64fe?w=800&q=80", "水墨画艺术")
    },
    "ceramics": {
        "img1": ("https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=800&q=80", "青花瓷艺术"),
        "img2": ("https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?w=800&q=80", "中国瓷器")
    },
    "jade": {
        "img1": ("https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=800&q=80", "玉石雕刻艺术"),
        "img2": ("https://images.unsplash.com/photo-1603569283847-aa295f0d016a?w=800&q=80", "精美玉器")
    }
}

def update_article_images(file_path, category):
    """更新单个文章的图片链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取该分类的图片
        img1_url, img1_alt = category_images[category]["img1"]
        img2_url, img2_alt = category_images[category]["img2"]
        
        # 找到所有 gallery-item 块
        gallery_pattern = r'(<div class="gallery-item">\s*<img src=")([^"]+)(" alt=")([^"]*)(" loading="lazy">\s*<div class="gallery-caption">)([^<]*)(</div>\s*</div>)'
        
        matches = list(re.finditer(gallery_pattern, content))
        if len(matches) >= 2:
            # 替换第一张图片
            match1 = matches[0]
            old_text1 = match1.group(0)
            new_text1 = f'{match1.group(1)}{img1_url}{match1.group(3)}{img1_alt}{match1.group(5)}{img1_alt}{match1.group(7)}'
            content = content.replace(old_text1, new_text1, 1)
            
            # 重新查找第二张图片（因为内容已改变）
            matches = list(re.finditer(gallery_pattern, content))
            if len(matches) >= 2:
                match2 = matches[1]
                old_text2 = match2.group(0)
                new_text2 = f'{match2.group(1)}{img2_url}{match2.group(3)}{img2_alt}{match2.group(5)}{img2_alt}{match2.group(7)}'
                content = content.replace(old_text2, new_text2, 1)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"  错误: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    base_dir = "/home/kai/.openclaw/workspace/articles"
    
    for category in ["calligraphy", "painting", "ceramics", "jade"]:
        category_dir = os.path.join(base_dir, category)
        if not os.path.exists(category_dir):
            print(f"目录不存在: {category_dir}")
            continue
        
        print(f"\n处理 {category} 类文章...")
        
        for filename in os.listdir(category_dir):
            if filename.endswith('.html'):
                file_path = os.path.join(category_dir, filename)
                print(f"  更新: {filename}")
                if update_article_images(file_path, category):
                    print(f"    ✓ 完成")
                else:
                    print(f"    ✗ 失败")

if __name__ == "__main__":
    main()
    print("\n所有文章图片链接更新完成！")

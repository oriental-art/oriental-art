# Image Setup Instructions

## Current Status
All article HTML files have been updated to use local image paths:
- `../images/painting/` - for painting articles
- `../images/calligraphy/` - for calligraphy articles  
- `../images/ceramics/` - for ceramics articles
- `../images/jade/` - for jade articles

## Required Images

### Painting Images (images/painting/)
1. `fan_kuan_travelers.jpg` - Fan Kuan, Travelers Among Mountains and Streams
2. `guo_xi_early_spring.jpg` - Guo Xi, Early Spring
3. `ni_zan_cold_mountain.jpg` - Ni Zan, The Cold Mountain Pavilion
4. `shen_zhou_lofty_mount.jpg` - Shen Zhou, Lofty Mount Lu
5. `ma_yuan_spring.jpg` - Ma Yuan, Walking on Path in Spring
6. `dong_qichang_landscape.jpg` - Dong Qichang, Landscape
7. `huizong_birds_flowers.jpg` - Emperor Huizong, Birds and Flowers
8. `gu_kaizhi_luo_river.jpg` - Gu Kaizhi, Nymph of the Luo River
9. `wang_ximeng_rivers_mountains.jpg` - Wang Ximeng, A Thousand Li of Rivers and Mountains
10. `zhang_zeduan_qingming.jpg` - Zhang Zeduan, Along the River During the Qingming Festival
11. `qi_baishi_shrimp.jpg` - Qi Baishi, Shrimp

### Calligraphy Images (images/calligraphy/)
1. `wang_xizhi_orchid.jpg` - Wang Xizhi, Preface to the Orchid Pavilion
2. `huaisu_autobiography.jpg` - Huaisu, Autobiography
3. `brushes.jpg` - Chinese writing brushes
4. `seal_script.jpg` - Small Seal Script

### Ceramics Images (images/ceramics/)
1. `blue_white_vase.jpg` - Blue and white porcelain vase
2. `longquan_celadon.jpg` - Longquan celadon
3. `jian_tea_bowl.jpg` - Jian ware tea bowl

### Jade Images (images/jade/)
1. `jade_bi_disc.jpg` - Jade bi disc
2. `qing_jade.jpg` - Qing dynasty jade carving
3. `jadeite.jpg` - Imperial jadeite

## How to Add Images

### Option 1: Download from Wikimedia Commons
Visit these URLs and download the images:
- https://commons.wikimedia.org/wiki/File:Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg
- https://commons.wikimedia.org/wiki/File:Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg
- (and so on for each image)

### Option 2: Use Your Own Images
Replace the files in the `images/` folder with your own artwork images. Just keep the same filenames.

### Option 3: Use Placeholder Images
Create simple placeholder images with the artwork titles until you can obtain the actual images.

## After Adding Images
1. Add the images to git: `git add images/`
2. Commit: `git commit -m "Add artwork images"`
3. Push: `git push origin main`
4. GitHub Pages will automatically update

## Note
The current setup uses relative paths (`../images/...`) which work correctly with GitHub Pages. The images folder is at the repository root level, and articles reference them using `../images/` from their location in `articles/{category}/`.

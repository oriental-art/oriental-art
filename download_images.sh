#!/bin/bash
# Download script for Oriental Art images
# Run this script on a machine with internet access to Wikimedia Commons

set -e

BASE_DIR="images"
mkdir -p $BASE_DIR/{painting,calligraphy,ceramics,jade}

echo "Downloading Chinese Art images from Wikimedia Commons..."
echo ""

# Painting images
echo "Downloading Painting images..."
curl -L -o "$BASE_DIR/painting/fan_kuan_travelers.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg/1280px-Fan_Kuan_-_Travelers_Among_Mountains_and_Streams_-_Google_Art_Project.jpg" && echo "✓ Fan Kuan"
curl -L -o "$BASE_DIR/painting/guo_xi_early_spring.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg/1280px-Guo_Xi_-_Early_Spring_-_Google_Art_Project.jpg" && echo "✓ Guo Xi"
curl -L -o "$BASE_DIR/painting/ni_zan_cold_mountain.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg/1280px-Ni_Zan_-_The_Cold_Mountain_Pavilion_-_Google_Art_Project.jpg" && echo "✓ Ni Zan"
curl -L -o "$BASE_DIR/painting/shen_zhou_lofty_mount.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg/800px-Shen_Zhou_-_Lofty_Mount_Lu_-_Google_Art_Project.jpg" && echo "✓ Shen Zhou"
curl -L -o "$BASE_DIR/painting/ma_yuan_spring.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg/800px-Ma_Yuan_-_Walking_on_Path_in_Spring_-_Google_Art_Project.jpg" && echo "✓ Ma Yuan"
curl -L -o "$BASE_DIR/painting/dong_qichang_landscape.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg/1280px-Dong_Qichang_-_Landscape_-_Google_Art_Project.jpg" && echo "✓ Dong Qichang"
curl -L -o "$BASE_DIR/painting/huizong_birds_flowers.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg/800px-Emperor_Huizong_-_Birds_and_Flowers_-_Google_Art_Project.jpg" && echo "✓ Emperor Huizong"
curl -L -o "$BASE_DIR/painting/gu_kaizhi_luo_river.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg/1280px-Gu_Kaizhi_-_Nymph_of_the_Luo_River_-_Google_Art_Project.jpg" && echo "✓ Gu Kaizhi"
curl -L -o "$BASE_DIR/painting/wang_ximeng_rivers_mountains.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg" && echo "✓ Wang Ximeng"
curl -L -o "$BASE_DIR/painting/zhang_zeduan_qingming.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg/1280px-Zhang_Zeduan_-_Along_the_River_During_the_Qingming_Festival_-_Google_Art_Project.jpg" && echo "✓ Zhang Zeduan"
curl -L -o "$BASE_DIR/painting/qi_baishi_shrimp.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Qi_Baishi_-_Shrimp.jpg/800px-Qi_Baishi_-_Shrimp.jpg" && echo "✓ Qi Baishi"

# Calligraphy images
echo ""
echo "Downloading Calligraphy images..."
curl -L -o "$BASE_DIR/calligraphy/wang_xizhi_orchid.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg/1280px-Wang_Xizhi_Preface_to_the_Poems_Composed_at_the_Orchid_Pavilion.jpg" && echo "✓ Wang Xizhi"
curl -L -o "$BASE_DIR/calligraphy/huaisu_autobiography.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Huaisu_Autobiography.jpg/800px-Huaisu_Autobiography.jpg" && echo "✓ Huaisu"
curl -L -o "$BASE_DIR/calligraphy/brushes.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Chinese_writing_brushes.jpg/800px-Chinese_writing_brushes.jpg" && echo "✓ Brushes"
curl -L -o "$BASE_DIR/calligraphy/seal_script.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Small_Seal_Script.jpg/800px-Small_Seal_Script.jpg" && echo "✓ Seal Script"

# Ceramics images
echo ""
echo "Downloading Ceramics images..."
curl -L -o "$BASE_DIR/ceramics/blue_white_vase.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg/800px-Blue_and_white_vase_Jingdezhen_Ming_Yongle_1403_1424.jpg" && echo "✓ Blue & White Vase"
curl -L -o "$BASE_DIR/ceramics/longquan_celadon.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Longquan_celadon_Song_Dynasty.jpg/800px-Longquan_celadon_Song_Dynasty.jpg" && echo "✓ Longquan Celadon"
curl -L -o "$BASE_DIR/ceramics/jian_tea_bowl.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jian_tea_bowl_Song_dynasty.jpg/800px-Jian_tea_bowl_Song_dynasty.jpg" && echo "✓ Jian Tea Bowl"

# Jade images
echo ""
echo "Downloading Jade images..."
curl -L -o "$BASE_DIR/jade/jade_bi_disc.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jade_bi_disc_Neolithic.jpg/800px-Jade_bi_disc_Neolithic.jpg" && echo "✓ Jade Bi Disc"
curl -L -o "$BASE_DIR/jade/qing_jade.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jade_carving_Qing_dynasty.jpg/800px-Jade_carving_Qing_dynasty.jpg" && echo "✓ Qing Jade"
curl -L -o "$BASE_DIR/jade/jadeite.jpg" "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jadeite_Ching_dynasty.jpg/800px-Jadeite_Ching_dynasty.jpg" && echo "✓ Jadeite"

echo ""
echo "========================================"
echo "Download complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Remove old SVG files: rm images/*/*.svg"
echo "2. Update HTML to use .jpg: sed -i 's/\\.svg\"/.jpg\"/g' articles/*/*.html"
echo "3. Add to git: git add images/"
echo "4. Commit: git commit -m 'Add artwork images'"
echo "5. Push: git push origin main"

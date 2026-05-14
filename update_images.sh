#!/bin/bash

# 更新文章图片链接为更可靠的源

# 书法类文章图片
calligraphy_images=(
    "01_soul_of_brush.html:https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/LantingXu_copy_by_Feng_Chengsu.jpg/1280px-LantingXu_copy_by_Feng_Chengsu.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chinese_Brush_Pen.jpg/800px-Chinese_Brush_Pen.jpg"
    "02_wang_xizhi.html:https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/LantingXu_copy_by_Feng_Chengsu.jpg/1280px-LantingXu_copy_by_Feng_Chengsu.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Wang_Xizhi_Portrait.jpg/600px-Wang_Xizhi_Portrait.jpg"
    "03_five_shades_ink.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Mi_Fu_001.jpg/800px-Mi_Fu_001.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chinese_Brush_Pen.jpg/800px-Chinese_Brush_Pen.jpg"
    "04_cursive_script.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Huaisu_Autobiography.jpg/1280px-Huaisu_Autobiography.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Zhang_Xu_cursive_script.jpg/800px-Zhang_Xu_cursive_script.jpg"
    "05_four_treasures.html:https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chinese_Brush_Pen.jpg/800px-Chinese_Brush_Pen.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Ink_stone_with_dragon.jpg/800px-Ink_stone_with_dragon.jpg"
    "06_seal_script.html:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Qin_Script_Bronze.jpg/1280px-Qin_Script_Bronze.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Seal_script_stone.jpg/800px-Seal_script_stone.jpg"
    "07_tang_masters.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Yan_Zhenqing_Duobao_Pagoda.jpg/800px-Yan_Zhenqing_Duobao_Pagoda.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Liu_Gongquan_Calligraphy.jpg/800px-Liu_Gongquan_Calligraphy.jpg"
    "08_meditative_art.html:https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/LantingXu_copy_by_Feng_Chengsu.jpg/1280px-LantingXu_copy_by_Feng_Chengsu.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chinese_Brush_Pen.jpg/800px-Chinese_Brush_Pen.jpg"
    "09_women_calligraphy.html:https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/LantingXu_copy_by_Feng_Chengsu.jpg/1280px-LantingXu_copy_by_Feng_Chengsu.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chinese_Brush_Pen.jpg/800px-Chinese_Brush_Pen.jpg"
    "10_digital_age.html:https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/LantingXu_copy_by_Feng_Chengsu.jpg/1280px-LantingXu_copy_by_Feng_Chengsu.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Chinese_Brush_Pen.jpg/800px-Chinese_Brush_Pen.jpg"
)

# 绘画类文章图片
painting_images=(
    "01_essence_painting.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Along_the_River_During_the_Qingming_Festival_%28Qing_Court_Version%29.jpg/1280px-Along_the_River_During_the_Qingming_Festival_%28Qing_Court_Version%29.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg"
    "02_shan_shui.html:https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Shan_shui_painting.jpg/800px-Shan_shui_painting.jpg"
    "03_bird_flower.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Bird_and_flower_painting.jpg/800px-Bird_and_flower_painting.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Bird_flower_detail.jpg/800px-Bird_flower_detail.jpg"
    "04_song_masters.html:https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Song_painting.jpg/800px-Song_painting.jpg"
    "05_literati_painting.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Su_Shi_Bamboo.jpg/800px-Su_Shi_Bamboo.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Literati_painting.jpg/800px-Literati_painting.jpg"
    "06_figure_painting.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Along_the_River_During_the_Qingming_Festival_%28Qing_Court_Version%29.jpg/1280px-Along_the_River_During_the_Qingming_Festival_%28Qing_Court_Version%29.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Figure_painting.jpg/800px-Figure_painting.jpg"
    "07_ink_wash.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Mi_Fu_001.jpg/800px-Mi_Fu_001.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ink_wash.jpg/800px-Ink_wash.jpg"
    "08_painting_theory.html:https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Painting_theory.jpg/800px-Painting_theory.jpg"
    "09_modern_painting.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Modern_chinese_painting.jpg/800px-Modern_chinese_painting.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Contemporary_ink.jpg/800px-Contemporary_ink.jpg"
    "10_collecting.html:https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg/1280px-Wang_Ximeng_-_A_Thousand_Li_of_Rivers_and_Mountains_-_Google_Art_Project.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Scroll_mounting.jpg/800px-Scroll_mounting.jpg"
)

# 瓷器类文章图片
ceramics_images=(
    "01_art_porcelain.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Blue_and_white_porcelain_vase.jpg/800px-Blue_and_white_porcelain_vase.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ming_porcelain.jpg/800px-Ming_porcelain.jpg"
    "02_blue_white.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Blue_and_white_porcelain_vase.jpg/800px-Blue_and_white_porcelain_vase.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Yuan_blue_white.jpg/800px-Yuan_blue_white.jpg"
    "03_celadon.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Longquan_celadon.jpg/800px-Longquan_celadon.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Song_celadon.jpg/800px-Song_celadon.jpg"
    "04_tang_sancai.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Tang_sancai_camel.jpg/800px-Tang_sancai_camel.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Tang_sancai_figures.jpg/800px-Tang_sancai_figures.jpg"
    "05_song_dynasty.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Ru_ware.jpg/800px-Ru_ware.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ding_ware.jpg/800px-Ding_ware.jpg"
    "06_ming_porcelain.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Ming_vase.jpg/800px-Ming_vase.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Xuande_porcelain.jpg/800px-Xuande_porcelain.jpg"
    "07_qing_porcelain.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Qing_porcelain.jpg/800px-Qing_porcelain.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Famille_rose.jpg/800px-Famille_rose.jpg"
    "08_kilns.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jingdezhen_kiln.jpg/800px-Jingdezhen_kiln.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Longquan_kiln.jpg/800px-Longquan_kiln.jpg"
    "09_teapots.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Yixing_teapot.jpg/800px-Yixing_teapot.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Zisha_teapot.jpg/800px-Zisha_teapot.jpg"
    "10_collecting_ceramics.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Ming_vase.jpg/800px-Ming_vase.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Porcelain_collection.jpg/800px-Porcelain_collection.jpg"
)

# 玉雕类文章图片
jade_images=(
    "01_jade_carving.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jade_burial_suit.jpg/800px-Jade_burial_suit.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ancient_jade.jpg/800px-Ancient_jade.jpg"
    "02_hetian_jade.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Hetian_jade.jpg/800px-Hetian_jade.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/White_jade.jpg/800px-White_jade.jpg"
    "03_jade_ritual.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jade_bi.jpg/800px-Jade_bi.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Jade_cong.jpg/800px-Jade_cong.jpg"
    "04_han_jade.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Han_jade_dragon.jpg/800px-Han_jade_dragon.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Han_jade_pendant.jpg/800px-Han_jade_pendant.jpg"
    "05_jade_techniques.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jade_carving_tools.jpg/800px-Jade_carving_tools.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Jade_workshop.jpg/800px-Jade_workshop.jpg"
    "06_jadeite.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jadeite_bangle.jpg/800px-Jadeite_bangle.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Imperial_jadeite.jpg/800px-Imperial_jadeite.jpg"
    "07_master_carvers.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jade_masterpiece.jpg/800px-Jade_masterpiece.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Jade_sculpture.jpg/800px-Jade_sculpture.jpg"
    "08_symbolism.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jade_dragon_pendant.jpg/800px-Jade_dragon_pendant.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Jade_symbols.jpg/800px-Jade_symbols.jpg"
    "09_jade_jewelry.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Jade_jewelry.jpg/800px-Jade_jewelry.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Jade_pendant_modern.jpg/800px-Jade_pendant_modern.jpg"
    "10_future_jade.html:https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Contemporary_jade.jpg/800px-Contemporary_jade.jpg:https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Modern_jade_art.jpg/800px-Modern_jade_art.jpg"
)

echo "开始更新图片链接..."

# 更新书法类文章
echo "更新书法类文章..."
cd articles/calligraphy
for item in "${calligraphy_images[@]}"; do
    IFS=':' read -r file img1 img2 <<< "$item"
    if [ -f "$file" ]; then
        # 替换第一张图片
        sed -i "s|<img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/[^\"]*/[^\"]*\" alt=\"[^\"]*\"|<img src=\"$img1\" alt=\"Featured Artwork 1\"|g" "$file"
        echo "  更新: $file"
    fi
done
cd ../..

# 更新绘画类文章
echo "更新绘画类文章..."
cd articles/painting
for item in "${painting_images[@]}"; do
    IFS=':' read -r file img1 img2 <<< "$item"
    if [ -f "$file" ]; then
        sed -i "s|<img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/[^\"]*/[^\"]*\" alt=\"[^\"]*\"|<img src=\"$img1\" alt=\"Featured Artwork 1\"|g" "$file"
        echo "  更新: $file"
    fi
done
cd ../..

# 更新瓷器类文章
echo "更新瓷器类文章..."
cd articles/ceramics
for item in "${ceramics_images[@]}"; do
    IFS=':' read -r file img1 img2 <<< "$item"
    if [ -f "$file" ]; then
        sed -i "s|<img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/[^\"]*/[^\"]*\" alt=\"[^\"]*\"|<img src=\"$img1\" alt=\"Featured Artwork 1\"|g" "$file"
        echo "  更新: $file"
    fi
done
cd ../..

# 更新玉雕类文章
echo "更新玉雕类文章..."
cd articles/jade
for item in "${jade_images[@]}"; do
    IFS=':' read -r file img1 img2 <<< "$item"
    if [ -f "$file" ]; then
        sed -i "s|<img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/[^\"]*/[^\"]*\" alt=\"[^\"]*\"|<img src=\"$img1\" alt=\"Featured Artwork 1\"|g" "$file"
        echo "  更新: $file"
    fi
done
cd ../..

echo "图片链接更新完成！"

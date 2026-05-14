const pptxgen = require("pptxgenjs");

let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.author = '专业马拉松教练';
pres.title = '半程马拉松训练计划';

const colors = {
    primary: "667eea",
    secondary: "764ba2", 
    accent: "f093fb",
    dark: "1a1a2e",
    light: "f8f9fa",
    success: "28a745",
    warning: "ffc107",
    danger: "dc3545"
};

// 第1页：封面
let slide1 = pres.addSlide();
slide1.background = { color: colors.dark };
slide1.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 5.625, fill: { color: colors.primary, transparency: 20 } });
slide1.addShape(pres.shapes.OVAL, { x: 7, y: -1, w: 4, h: 4, fill: { color: colors.secondary, transparency: 30 } });
slide1.addShape(pres.shapes.OVAL, { x: -1, y: 3, w: 3, h: 3, fill: { color: colors.accent, transparency: 20 } });
slide1.addText("专业半程马拉松训练计划", { x: 0.5, y: 1.5, w: 9, h: 1, fontSize: 44, fontFace: "Microsoft YaHei", bold: true, color: "FFFFFF", align: "center" });
slide1.addText("从100分钟突破到95分钟", { x: 0.5, y: 2.6, w: 9, h: 0.6, fontSize: 28, fontFace: "Microsoft YaHei", color: colors.accent, align: "center" });
slide1.addShape(pres.shapes.RECTANGLE, { x: 2, y: 3.5, w: 6, h: 1.5, fill: { color: "FFFFFF", transparency: 10 }, line: { color: "FFFFFF", width: 1 } });
slide1.addText("当前成绩：100分钟 (4:45/km)\n目标成绩：95分钟 (4:30/km)\n训练周期：12周 (3个月)", { x: 2, y: 3.6, w: 6, h: 1.3, fontSize: 16, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center", valign: "middle" });

// 第2页：目录
let slide2 = pres.addSlide();
slide2.background = { color: "FFFFFF" };
slide2.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 1.2, fill: { color: colors.primary } });
slide2.addText("目录", { x: 0.5, y: 0.3, w: 9, h: 0.6, fontSize: 32, fontFace: "Microsoft YaHei", bold: true, color: "FFFFFF" });
const tocItems = ["01  训练计划概述与目标分析", "02  运动员评估与训练区间", "03  周期化训练架构", "04  12周详细训练计划", "05  力量训练方案", "06  营养与补给策略", "07  恢复与损伤预防", "08  比赛日执行策略"];
let yPos = 1.5;
tocItems.forEach((item, index) => {
    slide2.addShape(pres.shapes.RECTANGLE, { x: 0.8, y: yPos, w: 0.15, h: 0.5, fill: { color: index % 2 === 0 ? colors.primary : colors.secondary } });
    slide2.addText(item, { x: 1.1, y: yPos, w: 8, h: 0.5, fontSize: 20, fontFace: "Microsoft YaHei", color: colors.dark, valign: "middle" });
    yPos += 0.55;
});

// 第3页：目标分析
let slide3 = pres.addSlide();
slide3.background = { color: "FFFFFF" };
slide3.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 1, fill: { color: colors.primary } });
slide3.addText("01  训练计划概述与目标分析", { x: 0.5, y: 0.25, w: 9, h: 0.5, fontSize: 28, fontFace: "Microsoft YaHei", bold: true, color: "FFFFFF" });
slide3.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.3, w: 9, h: 1.8, fill: { color: "f8f9fa" }, line: { color: colors.primary, width: 2 } });
slide3.addText("挑战目标", { x: 0.7, y: 1.4, w: 2, h: 0.4, fontSize: 18, fontFace: "Microsoft YaHei", bold: true, color: colors.primary });
slide3.addText("半马成绩：100分钟 → 95分钟\n配速提升：4:45/km → 4:30/km\n时间框架：12周（3个月）", { x: 0.7, y: 1.9, w: 8.6, h: 1, fontSize: 16, fontFace: "Microsoft YaHei", color: colors.dark });
slide3.addText("成功关键因素", { x: 0.5, y: 3.3, w: 4, h: 0.4, fontSize: 20, fontFace: "Microsoft YaHei", bold: true, color: colors.secondary });
const factors = ["有氧基础：当前成绩表明具备扎实基础", "乳酸阈值：需提升阈值配速10-15秒/公里", "跑步经济性：通过力量和技巧训练改善", "配速执行：培养精确的配速感知能力"];
yPos = 3.8;
factors.forEach(factor => {
    slide3.addShape(pres.shapes.OVAL, { x: 0.6, y: yPos + 0.1, w: 0.15, h: 0.15, fill: { color: colors.success } });
    slide3.addText(factor, { x: 0.9, y: yPos, w: 4, h: 0.4, fontSize: 14, fontFace: "Microsoft YaHei", color: colors.dark });
    yPos += 0.45;
});
slide3.addText("周期化训练架构", { x: 5.5, y: 3.3, w: 4, h: 0.4, fontSize: 20, fontFace: "Microsoft YaHei", bold: true, color: colors.secondary });
const phases = [{ name: "基础强化期", weeks: "1-4周", color: colors.primary }, { name: "专项提升期", weeks: "5-8周", color: colors.secondary }, { name: "巅峰竞技期", weeks: "9-11周", color: colors.warning }, { name: "taper减量期", weeks: "12周", color: colors.success }];
let xPos = 5.5;
phases.forEach((phase) => {
    slide3.addShape(pres.shapes.RECTANGLE, { x: xPos, y: 3.8, w: 1, h: 1.2, fill: { color: phase.color } });
    slide3.addText(phase.name, { x: xPos, y: 3.9, w: 1, h: 0.5, fontSize: 11, fontFace: "Microsoft YaHei", bold: true, color: "FFFFFF", align: "center" });
    slide3.addText(phase.weeks, { x: xPos, y: 4.4, w: 1, h: 0.4, fontSize: 10, fontFace: "Microsoft YaHei", color: "FFFFFF", align: "center" });
    xPos += 1.1;
});

// 保存
pres.writeFile({ fileName: "专业半程马拉松训练计划.pptx" });
console.log("PPT生成成功！");

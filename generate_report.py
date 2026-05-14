#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
光互联/OCS深度研究报告 PDF生成器
使用reportlab生成专业投研报告
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from datetime import datetime
import os

# 注册中文字体
try:
    # 尝试使用系统中文字体
    font_paths = [
        '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
        '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
        '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    
    chinese_font = None
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont('ChineseFont', font_path))
                chinese_font = 'ChineseFont'
                print(f"Registered font: {font_path}")
                break
            except Exception as e:
                print(f"Failed to register {font_path}: {e}")
                continue
    
    if chinese_font is None:
        # 使用默认Helvetica字体，但中文会显示为方框
        chinese_font = 'Helvetica'
        print("Warning: No Chinese font found, using Helvetica")
        
except Exception as e:
    print(f"Font registration error: {e}")
    chinese_font = 'Helvetica'

class PDFReportGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm
        )
        self.story = []
        self.styles = self._create_styles()
        
    def _create_styles(self):
        """创建自定义样式"""
        styles = getSampleStyleSheet()
        
        # 标题样式
        styles.add(ParagraphStyle(
            name='CustomTitle',
            fontName=chinese_font,
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            spaceAfter=30,
            textColor=colors.HexColor('#1a1a1a')
        ))
        
        # 副标题样式
        styles.add(ParagraphStyle(
            name='CustomSubtitle',
            fontName=chinese_font,
            fontSize=14,
            leading=18,
            alignment=TA_CENTER,
            spaceAfter=20,
            textColor=colors.HexColor('#666666')
        ))
        
        # 一级标题
        styles.add(ParagraphStyle(
            name='Heading1Custom',
            fontName=chinese_font,
            fontSize=16,
            leading=22,
            alignment=TA_LEFT,
            spaceBefore=20,
            spaceAfter=12,
            textColor=colors.HexColor('#2c5aa0'),
            borderPadding=5
        ))
        
        # 二级标题
        styles.add(ParagraphStyle(
            name='Heading2Custom',
            fontName=chinese_font,
            fontSize=13,
            leading=18,
            alignment=TA_LEFT,
            spaceBefore=15,
            spaceAfter=8,
            textColor=colors.HexColor('#1a1a1a'),
            leftIndent=10
        ))
        
        # 三级标题
        styles.add(ParagraphStyle(
            name='Heading3Custom',
            fontName=chinese_font,
            fontSize=11,
            leading=15,
            alignment=TA_LEFT,
            spaceBefore=10,
            spaceAfter=6,
            textColor=colors.HexColor('#333333'),
            leftIndent=20
        ))
        
        # 正文样式
        styles.add(ParagraphStyle(
            name='BodyTextCustom',
            fontName=chinese_font,
            fontSize=10,
            leading=14,
            alignment=TA_JUSTIFY,
            spaceBefore=6,
            spaceAfter=6,
            leftIndent=20,
            rightIndent=20
        ))
        
        # 表格标题样式
        styles.add(ParagraphStyle(
            name='TableTitle',
            fontName=chinese_font,
            fontSize=10,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.white
        ))
        
        # 表格内容样式
        styles.add(ParagraphStyle(
            name='TableText',
            fontName=chinese_font,
            fontSize=9,
            leading=11,
            alignment=TA_CENTER
        ))
        
        # 页脚样式
        styles.add(ParagraphStyle(
            name='Footer',
            fontName=chinese_font,
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
            textColor=colors.grey
        ))
        
        return styles
    
    def add_title_page(self):
        """添加封面页"""
        # 主标题
        self.story.append(Spacer(1, 4*cm))
        self.story.append(Paragraph("光互联/OCS行业", self.styles['CustomTitle']))
        self.story.append(Paragraph("深度研究报告", self.styles['CustomTitle']))
        self.story.append(Spacer(1, 1*cm))
        
        # 副标题
        self.story.append(Paragraph("AI数据中心驱动下的光通信产业投资机遇", self.styles['CustomSubtitle']))
        self.story.append(Spacer(1, 3*cm))
        
        # 报告信息
        info_data = [
            ["报告日期", "2026年4月4日"],
            ["研究范围", "7家核心上市公司"],
            ["投资评级", "增持/买入"],
            ["分析师", "AI投研团队"]
        ]
        
        info_table = Table(info_data, colWidths=[6*cm, 8*cm])
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), chinese_font),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        
        self.story.append(info_table)
        self.story.append(PageBreak())
    
    def add_table_of_contents(self):
        """添加目录"""
        self.story.append(Paragraph("目录", self.styles['Heading1Custom']))
        self.story.append(Spacer(1, 0.5*cm))
        
        toc_items = [
            ("第一部分  行业深度分析", "3"),
            ("    1.1 OCS技术路线对比", "3"),
            ("    1.2 市场规模与增长预测", "4"),
            ("    1.3 产业链分析", "5"),
            ("    1.4 竞争格局与壁垒", "6"),
            ("第二部分  公司深度分析", "7"),
            ("    2.1 光迅科技 (002281.SZ)", "7"),
            ("    2.2 新易盛 (300502.SZ)", "9"),
            ("    2.3 光库科技 (300620.SZ)", "11"),
            ("    2.4 腾景科技 (688195.SH)", "12"),
            ("    2.5 赛微电子 (300456.SZ)", "13"),
            ("    2.6 聚光科技 (300203.SZ)", "14"),
            ("    2.7 德科立 (688205.SH)", "15"),
            ("第三部分  对比分析与投资建议", "16"),
            ("    3.1 7家公司对比矩阵", "16"),
            ("    3.2 投资评级汇总表", "17"),
            ("    3.3 风险提示", "18"),
        ]
        
        for item, page in toc_items:
            self.story.append(Paragraph(f"{item} .................................................... {page}", 
                                      self.styles['BodyTextCustom']))
        
        self.story.append(PageBreak())
    
    def add_section_title(self, title):
        """添加章节标题"""
        self.story.append(Paragraph(title, self.styles['Heading1Custom']))
        self.story.append(Spacer(1, 0.3*cm))
    
    def add_subsection_title(self, title):
        """添加小节标题"""
        self.story.append(Paragraph(title, self.styles['Heading2Custom']))
        self.story.append(Spacer(1, 0.2*cm))
    
    def add_body_text(self, text):
        """添加正文"""
        self.story.append(Paragraph(text, self.styles['BodyTextCustom']))
        self.story.append(Spacer(1, 0.1*cm))
    
    def add_table(self, headers, data, col_widths=None):
        """添加表格"""
        table_data = [headers] + data
        
        if col_widths is None:
            col_widths = [16*cm / len(headers)] * len(headers)
        
        table = Table(table_data, colWidths=col_widths)
        
        # 表格样式
        style_commands = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), chinese_font),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTNAME', (0, 1), (-1, -1), chinese_font),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]
        
        # 交替行背景色
        for i in range(1, len(table_data)):
            if i % 2 == 0:
                style_commands.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor('#f5f5f5')))
        
        table.setStyle(TableStyle(style_commands))
        self.story.append(table)
        self.story.append(Spacer(1, 0.3*cm))
    
    def generate_report(self):
        """生成完整报告"""
        # 封面
        self.add_title_page()
        
        # 目录
        self.add_table_of_contents()
        
        # 第一部分：行业深度分析
        self.add_section_title("第一部分  行业深度分析")
        
        self.add_subsection_title("1.1 OCS技术路线对比")
        self.add_body_text("光交换（OCS, Optical Circuit Switching）是下一代数据中心网络的核心技术。当前主要技术路线包括MEMS OCS、液晶OCS、热光OCS和SOA阵列四种方案。")
        
        ocs_headers = ["技术路线", "原理", "优势", "劣势", "代表厂商"]
        ocs_data = [
            ["MEMS OCS", "微机电系统驱动", "低功耗、高可靠性", "响应速度较慢", "赛微电子、华为"],
            ["液晶OCS", "液晶分子取向控制", "无机械部件、响应快", "温度敏感", "日本厂商"],
            ["热光OCS", "热光效应", "结构简单", "功耗高、速度慢", "研究机构"],
            ["SOA阵列", "半导体光放大器", "增益补偿、可集成", "功耗较高", "光迅科技"],
        ]
        self.add_table(ocs_headers, ocs_data, [3*cm, 3.5*cm, 3.5*cm, 3*cm, 3*cm])
        
        self.add_subsection_title("1.2 市场规模与增长预测")
        self.add_body_text("根据LightCounting和Yole最新数据，全球光模块市场正处于AI驱动的爆发式增长期。2024年市场规模约120亿美元，预计2027年将突破200亿美元，年复合增长率达18%。")
        
        market_headers = ["年份", "市场规模(亿美元)", "同比增速", "主要驱动力"]
        market_data = [
            ["2024", "120", "+25%", "800G光模块放量"],
            ["2025E", "150", "+25%", "AI数据中心建设"],
            ["2027E", "200", "+18%", "1.6T光模块商用"],
            ["2030E", "300", "+15%", "CPO技术普及"],
        ]
        self.add_table(market_headers, market_data, [4*cm, 4*cm, 4*cm, 4*cm])
        
        self.add_subsection_title("1.3 产业链分析")
        self.add_body_text("光互联产业链可分为上游光芯片/电芯片、中游光模块/光纤器件、下游云厂商/设备商三个环节。上游光芯片是核心壁垒，中游光模块竞争激烈，下游需求由AI算力投资驱动。")
        
        chain_headers = ["环节", "细分领域", "代表企业", "价值占比"]
        chain_data = [
            ["上游", "光芯片", "源杰科技、Lumentum", "30%"],
            ["上游", "电芯片", "Marvell、Broadcom", "25%"],
            ["中游", "光模块", "中际旭创、新易盛、光迅", "35%"],
            ["中游", "光纤器件", "光库科技、德科立", "10%"],
        ]
        self.add_table(chain_headers, chain_data, [3*cm, 3*cm, 6*cm, 4*cm])
        
        self.add_subsection_title("1.4 竞争格局与壁垒")
        self.add_body_text("光模块行业具有较高的技术壁垒和客户认证壁垒。全球竞争格局中，中国厂商占据主导地位，中际旭创、新易盛、光迅科技等跻身全球前五。行业壁垒主要体现在技术迭代能力、客户资源和规模效应三个方面。")
        
        self.story.append(PageBreak())
        
        # 第二部分：公司深度分析
        self.add_section_title("第二部分  公司深度分析")
        
        # 2.1 光迅科技
        self.add_subsection_title("2.1 光迅科技 (002281.SZ) - 光模块龙头")
        
        company_info = """
        <b>基本信息：</b>最新股价90.39元，市值约730亿元，PE-TTM 79.58倍。<br/>
        <b>投资亮点：</b>国内光模块龙头，中国信科集团旗下，拥有完整的光芯片、光器件、光模块全产业链布局。<br/>
        <b>财务表现：</b>2024年营收82.72亿元（+36.49%），净利润6.61亿元，毛利率22.46%，ROE 7.55%。<br/>
        <b>成长驱动：</b>800G光模块量产、CPO技术布局、激光雷达业务拓展。<br/>
        <b>投资评级：</b>增持 | 目标价：85元
        """
        self.add_body_text(company_info)
        
        # 2.2 新易盛
        self.add_subsection_title("2.2 新易盛 (300502.SZ) - 高速光模块领军者")
        
        company_info2 = """
        <b>基本信息：</b>最新股价455.30元，市值约4500亿元，PE-TTM 60.19倍。<br/>
        <b>投资亮点：</b>高速光模块领先厂商，800G产品放量，海外云厂商客户占比超80%。<br/>
        <b>财务表现：</b>2024年营收86.47亿元（+179%），净利润28.38亿元，毛利率44.72%，ROE 41%。<br/>
        <b>成长驱动：</b>1.6T光模块研发、LPO/CPO技术布局、硅光技术。<br/>
        <b>投资评级：</b>买入 | 目标价：500元
        """
        self.add_body_text(company_info2)
        
        # 2.3 光库科技
        self.add_subsection_title("2.3 光库科技 (300620.SZ) - 光纤器件专家")
        
        company_info3 = """
        <b>投资亮点：</b>光纤器件细分龙头，铌酸锂调制器技术领先，CPO概念核心标的。<br/>
        <b>核心优势：</b>保偏光纤器件全球领先，薄膜铌酸锂技术突破，收购Lumentum相关资产。<br/>
        <b>成长驱动：</b>薄膜铌酸锂调制器放量、CPO应用拓展。<br/>
        <b>投资评级：</b>增持
        """
        self.add_body_text(company_info3)
        
        # 2.4 腾景科技
        self.add_subsection_title("2.4 腾景科技 (688195.SH) - 精密光学新秀")
        
        company_info4 = """
        <b>投资亮点：</b>科创板上市，专注精密光学元件，光通信与激光雷达双轮驱动。<br/>
        <b>核心优势：</b>精密光学元件制造能力，光学薄膜技术，微光学元件加工。<br/>
        <b>成长驱动：</b>CPO光学元件、激光雷达光学组件。<br/>
        <b>投资评级：</b>增持
        """
        self.add_body_text(company_info4)
        
        # 2.5 赛微电子
        self.add_subsection_title("2.5 赛微电子 (300456.SZ) - MEMS代工龙头")
        
        company_info5 = """
        <b>投资亮点：</b>全球领先的MEMS代工能力，瑞典Silex母公司，可用于MEMS OCS制造。<br/>
        <b>核心优势：</b>全球MEMS代工前三，广泛的MEMS工艺平台。<br/>
        <b>成长驱动：</b>MEMS OCS代工、国产替代。<br/>
        <b>风险提示：</b>地缘政治风险，业绩波动较大。<br/>
        <b>投资评级：</b>中性
        """
        self.add_body_text(company_info5)
        
        # 2.6 聚光科技
        self.add_subsection_title("2.6 聚光科技 (300203.SZ) - 环境监测龙头")
        
        company_info6 = """
        <b>投资亮点：</b>环境监测仪器龙头，光谱技术积累深厚。<br/>
        <b>说明：</b>光通信业务占比相对较小，非纯正光互联标的。<br/>
        <b>投资评级：</b>中性
        """
        self.add_body_text(company_info6)
        
        # 2.7 德科立
        self.add_subsection_title("2.7 德科立 (688205.SH) - 长距离传输专家")
        
        company_info7 = """
        <b>投资亮点：</b>科创板上市，专注长距离传输光模块，相干光模块能力领先。<br/>
        <b>核心优势：</b>长距离传输技术领先，相干DSP技术。<br/>
        <b>成长驱动：</b>800G长距离模块、DCI应用。<br/>
        <b>投资评级：</b>增持
        """
        self.add_body_text(company_info7)
        
        self.story.append(PageBreak())
        
        # 第三部分：对比分析与投资建议
        self.add_section_title("第三部分  对比分析与投资建议")
        
        self.add_subsection_title("3.1 7家公司对比矩阵")
        
        compare_headers = ["公司", "代码", "主营业务", "PE-TTM", "毛利率", "ROE", "评级"]
        compare_data = [
            ["光迅科技", "002281", "光模块龙头", "79.58", "22.46%", "7.55%", "增持"],
            ["新易盛", "300502", "高速光模块", "60.19", "44.72%", "41.00%", "买入"],
            ["光库科技", "300620", "光纤器件", "-", "-", "-", "增持"],
            ["腾景科技", "688195", "精密光学", "-", "-", "-", "增持"],
            ["赛微电子", "300456", "MEMS代工", "-", "-", "-", "中性"],
            ["聚光科技", "300203", "环境监测", "-", "-", "-", "中性"],
            ["德科立", "688205", "长距离光模块", "-", "-", "-", "增持"],
        ]
        self.add_table(compare_headers, compare_data, [2.5*cm, 2*cm, 3*cm, 2*cm, 2*cm, 2*cm, 2.5*cm])
        
        self.add_subsection_title("3.2 投资评级汇总表")
        
        rating_headers = ["公司", "评级", "目标价", "当前价", "上涨空间", "核心逻辑"]
        rating_data = [
            ["光迅科技", "增持", "85元", "90.39元", "-6%", "行业龙头，估值偏高"],
            ["新易盛", "买入", "500元", "455.30元", "+10%", "业绩高增长，盈利领先"],
            ["光库科技", "增持", "-", "-", "-", "技术壁垒高，受益CPO"],
            ["腾景科技", "增持", "-", "-", "-", "CPO+激光雷达双景气"],
            ["赛微电子", "中性", "-", "-", "-", "前景广阔但波动大"],
            ["聚光科技", "中性", "-", "-", "-", "非纯正光互联标的"],
            ["德科立", "增持", "-", "-", "-", "长距离技术壁垒高"],
        ]
        self.add_table(rating_headers, rating_data, [2.5*cm, 1.5*cm, 2*cm, 2.5*cm, 2*cm, 5.5*cm])
        
        self.add_subsection_title("3.3 风险提示")
        
        risk_text = """
        <b>1. 技术风险：</b>光模块技术迭代快，存在技术路线风险；CPO技术可能改变行业格局。<br/><br/>
        <b>2. 市场风险：</b>AI投资可能不及预期，云厂商资本开支波动。<br/><br/>
        <b>3. 竞争风险：</b>行业竞争加剧，毛利率下滑；新进入者冲击。<br/><br/>
        <b>4. 地缘政治风险：</b>中美科技竞争；供应链安全。<br/><br/>
        <b>5. 估值风险：</b>板块估值较高；业绩不及预期可能引发估值回调。
        """
        self.add_body_text(risk_text)
        
        self.story.append(Spacer(1, 1*cm))
        
        # 免责声明
        disclaimer = """
        <b>免责声明：</b>本报告仅供参考，不构成投资建议。投资者应独立判断，自行承担投资风险。
        报告中的数据来源于公开信息，分析师不对其准确性和完整性作出保证。
        """
        self.add_body_text(disclaimer)
        
        # 生成PDF
        self.doc.build(self.story)
        print(f"PDF报告已生成: {self.filename}")

if __name__ == "__main__":
    output_file = "/home/kai/.openclaw/workspace/光互联OCS深度研究报告_专业版.pdf"
    generator = PDFReportGenerator(output_file)
    generator.generate_report()

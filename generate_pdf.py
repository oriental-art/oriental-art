# Simple PDF generation using basic libraries
try:
    from fpdf import FPDF
    has_fpdf = True
except:
    has_fpdf = False

import yaml

# Load YAML
with open('half_marathon_advanced_plan.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

if has_fpdf:
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 16)
            self.cell(0, 10, 'Half Marathon Training Plan', 0, 1, 'C')
            self.ln(5)
        
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, 'Half Marathon: 100min -> 95min', 0, 1, 'C')
    pdf.cell(0, 10, '12-Week Advanced Training Plan', 0, 1, 'C')
    pdf.ln(10)
    
    # Athlete Info
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Athlete Profile', 0, 1)
    pdf.set_font('Arial', '', 11)
    athlete = data['athlete']
    pdf.cell(0, 8, f"Current: {athlete['current_half_marathon_time']} ({athlete['current_pace']}/km)", 0, 1)
    pdf.cell(0, 8, f"Goal: {athlete['goal']['target_time']} ({athlete['goal']['target_pace']}/km)", 0, 1)
    pdf.ln(5)
    
    # Training Zones
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Training Paces', 0, 1)
    pdf.set_font('Arial', '', 10)
    zones = athlete['zones']['pace']
    for name, pace in zones.items():
        pdf.cell(0, 7, f"{name.capitalize()}: {pace}/km", 0, 1)
    pdf.ln(5)
    
    # Weekly Plan
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '12-Week Training Schedule', 0, 1)
    pdf.ln(5)
    
    # Phase 1
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Phase 1: Base Building (Weeks 1-4)', 0, 1)
    pdf.set_font('Arial', '', 10)
    phase1_data = [
        ['Week', 'Volume', 'Long Run', 'Key Workouts'],
        ['1', '50km', '16km', 'Tempo 25min + 1000mx5'],
        ['2', '52km', '17km', 'Tempo 30min + 1000mx6'],
        ['3', '48km', '14km', 'Recovery Week'],
        ['4', '55km', '18km', 'Tempo 30min + 1200mx5'],
    ]
    for row in phase1_data:
        for item in row:
            pdf.cell(40, 8, item, 1)
        pdf.ln()
    pdf.ln(5)
    
    # Phase 2
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Phase 2: Build (Weeks 5-8)', 0, 1)
    pdf.set_font('Arial', '', 10)
    phase2_data = [
        ['Week', 'Volume', 'Long Run', 'Key Workouts'],
        ['5', '58km', '19km', 'Tempo 35min + 8km@race pace'],
        ['6', '60km', '20km', 'Tempo 40min + 10km@race pace'],
        ['7', '52km', '15km', 'Recovery Week'],
        ['8', '62km', '21km', 'Tempo 40min + 12km@race pace'],
    ]
    for row in phase2_data:
        for item in row:
            pdf.cell(40, 8, item, 1)
        pdf.ln()
    pdf.ln(5)
    
    # Phase 3
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Phase 3: Peak (Weeks 9-11)', 0, 1)
    pdf.set_font('Arial', '', 10)
    phase3_data = [
        ['Week', 'Volume', 'Long Run', 'Key Workouts'],
        ['9', '55km', '18km', '10km race pace run'],
        ['10', '50km', '15km', 'Light recovery'],
        ['11', '45km', '12km', '8km race pace tune-up'],
    ]
    for row in phase3_data:
        for item in row:
            pdf.cell(40, 8, item, 1)
        pdf.ln()
    pdf.ln(5)
    
    # Phase 4
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Phase 4: Taper (Week 12)', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 8, 'Week 12: 28km total -> RACE DAY (Target: 95 minutes)', 0, 1)
    pdf.ln(10)
    
    # Race Strategy
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Race Day Strategy', 0, 1)
    pdf.ln(5)
    
    race = data['race_day']
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Target: {race['target_time']} ({race['target_pace']})", 0, 1)
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, 'Pacing Strategy:', 0, 1)
    pdf.set_font('Arial', '', 10)
    for s in race['strategy']:
        pdf.cell(0, 7, f"- {s}", 0, 1)
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 8, 'Nutrition:', 0, 1)
    pdf.set_font('Arial', '', 10)
    for n in race['nutrition']:
        pdf.cell(0, 7, f"- {n}", 0, 1)
    pdf.ln(10)
    
    # Weekly Schedule
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Typical Week Schedule', 0, 1)
    pdf.ln(5)
    
    schedule = [
        ['Day', 'Workout', 'Notes'],
        ['Monday', 'Easy Run 40min', 'Recovery from weekend'],
        ['Tuesday', 'Intervals', 'Key workout - VO2max'],
        ['Wednesday', 'Easy Run 45-50min', 'Active recovery'],
        ['Thursday', 'Tempo Run', 'Key workout - Threshold'],
        ['Friday', 'Rest', 'Complete rest'],
        ['Saturday', 'Easy Run 30-35min', 'Preparation for long run'],
        ['Sunday', 'Long Run 16-21km', 'Endurance building'],
    ]
    pdf.set_font('Arial', '', 9)
    for row in schedule:
        pdf.cell(35, 8, row[0], 1)
        pdf.cell(50, 8, row[1], 1)
        pdf.cell(80, 8, row[2], 1)
        pdf.ln()
    pdf.ln(10)
    
    # Key Points
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Key Points', 0, 1)
    pdf.set_font('Arial', '', 10)
    for note in data['notes'][:5]:
        pdf.cell(0, 7, f"- {note}", 0, 1)
    
    pdf.output('half_marathon_advanced_plan.pdf')
    print("PDF generated: half_marathon_advanced_plan.pdf")
else:
    # Generate markdown as fallback
    print("Generating markdown version...")
    with open('half_marathon_advanced_plan.md', 'w', encoding='utf-8') as f:
        f.write("# 半程马拉松进阶训练计划\n\n")
        f.write("## 目标：100分钟 → 95分钟（12周）\n\n")
        
        athlete = data['athlete']
        f.write(f"**当前成绩：** {athlete['current_half_marathon_time']}（{athlete['current_pace']}/km）\n\n")
        f.write(f"**目标成绩：** {athlete['goal']['target_time']}（{athlete['goal']['target_pace']}/km）\n\n")
        
        f.write("## 训练配速区间\n\n")
        zones = athlete['zones']['pace']
        for name, pace in zones.items():
            f.write(f"- **{name.capitalize()}:** {pace}/km\n")
        f.write("\n")
        
        f.write("## 12周训练计划\n\n")
        
        for phase in data['plan']['phases']:
            f.write(f"### {phase['name']}（第{phase['weeks']}周）\n\n")
            f.write(f"**重点：** {phase['focus']}\n\n")
            if 'progression' in phase:
                f.write("| 周次 | 周跑量 | 长距离 | 关键训练 |\n")
                f.write("|------|--------|--------|----------|\n")
                for week, details in phase['progression'].items():
                    week_num = week.replace('week_', '')
                    vol = details.get('volume', '-')
                    long = details.get('long_run', '-')
                    key = details.get('tempo', '') or details.get('race_pace', '') or details.get('intervals', '')
                    if '恢复' in str(details) or week_num in ['3', '7', '10']:
                        key = '恢复周'
                    f.write(f"| 第{week_num}周 | {vol}km | {long}km | {key} |\n")
            f.write("\n")
        
        f.write("## 比赛日策略\n\n")
        race = data['race_day']
        f.write(f"**目标时间：** {race['target_time']}\n\n")
        f.write(f"**目标配速：** {race['target_pace']}\n\n")
        f.write("**配速策略：**\n")
        for s in race['strategy']:
            f.write(f"- {s}\n")
        f.write("\n")
        
        f.write("## 重要提醒\n\n")
        for note in data['notes']:
            f.write(f"- {note}\n")
    
    print("Markdown generated: half_marathon_advanced_plan.md")

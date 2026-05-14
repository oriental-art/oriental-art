#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os

# 创建输出目录
output_dir = '/home/kai/.openclaw/workspace/exports/images'
os.makedirs(output_dir, exist_ok=True)

# 设置样式
plt.style.use('default')

# 1. 营收与净利润趋势图
years = ['2022', '2023', '2024', '2025E']
revenue = [60.6, 82.7, 110.2, 145.0]
profit = [6.2, 6.6, 9.5, 14.0]

fig, ax1 = plt.subplots(figsize=(10, 6))
color1 = '#2E86AB'
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Revenue (Billion RMB)', color=color1, fontsize=12)
line1 = ax1.plot(years, revenue, color=color1, marker='o', linewidth=2.5, markersize=8, label='Revenue')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, alpha=0.3)

ax2 = ax1.twinx()
color2 = '#A23B72'
ax2.set_ylabel('Net Profit (Billion RMB)', color=color2, fontsize=12)
line2 = ax2.plot(years, profit, color=color2, marker='s', linewidth=2.5, markersize=8, label='Net Profit')
ax2.tick_params(axis='y', labelcolor=color2)

for i, (r, p) in enumerate(zip(revenue, profit)):
    ax1.annotate(f'{r}', (years[i], r), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    ax2.annotate(f'{p}', (years[i], p), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9)

plt.title('Guangxun Technology: Revenue & Profit Trend (2022-2025E)', fontsize=14, fontweight='bold')
fig.legend(loc='upper left', bbox_to_anchor=(0.12, 0.88))
plt.tight_layout()
plt.savefig(f'{output_dir}/guangxun_revenue_profit.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1: Revenue & Profit Trend - Saved")

# 2. 季度营收增长图
quarters = ['2025Q1', '2025Q2', '2025Q3']
quarterly_revenue = [22.5, 28.3, 34.5]
quarterly_profit = [1.8, 2.4, 3.0]

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(quarters))
width = 0.35

bars1 = ax.bar(x - width/2, quarterly_revenue, width, label='Revenue', color='#2E86AB', alpha=0.8)
bars2 = ax.bar(x + width/2, quarterly_profit, width, label='Net Profit', color='#A23B72', alpha=0.8)

ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Amount (Billion RMB)', fontsize=12)
ax.set_title('Guangxun Technology: Quarterly Performance (2025)', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(quarters)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(f'{output_dir}/guangxun_quarterly.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2: Quarterly Performance - Saved")

# 3. 盈利能力指标图
years_metrics = ['2022', '2023', '2024', '2025E']
gross_margin = [22.6, 22.5, 23.5, 24.5]
net_margin = [10.2, 8.0, 8.6, 9.7]
roe = [8.0, 7.6, 9.8, 12.5]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years_metrics, gross_margin, marker='o', linewidth=2.5, markersize=8, label='Gross Margin', color='#2E86AB')
ax.plot(years_metrics, net_margin, marker='s', linewidth=2.5, markersize=8, label='Net Margin', color='#A23B72')
ax.plot(years_metrics, roe, marker='^', linewidth=2.5, markersize=8, label='ROE', color='#F18F01')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_title('Guangxun Technology: Profitability Metrics (2022-2025E)', fontsize=14, fontweight='bold')
ax.legend(loc='best')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'{output_dir}/guangxun_profitability.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3: Profitability Metrics - Saved")

# 4. 可比公司估值对比图
companies = ['Guangxun', 'Zhongji', 'Xinyisheng', 'Tianfu']
pe_values = [76.06, 45.50, 35.20, 42.30]
pb_values = [7.46, 8.20, 8.50, 6.80]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

colors_pe = ['#E74C3C' if x == max(pe_values) else '#3498DB' for x in pe_values]
bars1 = ax1.bar(companies, pe_values, color=colors_pe, alpha=0.8)
ax1.set_ylabel('PE Ratio', fontsize=12)
ax1.set_title('PE Ratio Comparison', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='y')
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

colors_pb = ['#E74C3C' if x == max(pb_values) else '#3498DB' for x in pb_values]
bars2 = ax2.bar(companies, pb_values, color=colors_pb, alpha=0.8)
ax2.set_ylabel('PB Ratio', fontsize=12)
ax2.set_title('PB Ratio Comparison', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')
for bar in bars2:
    height = bar.get_height()
    ax2.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.suptitle('Valuation Comparison: Guangxun vs Peers', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(f'{output_dir}/guangxun_valuation_comparison.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4: Valuation Comparison - Saved")

# 5. DCF敏感性分析热力图
wacc_range = [8, 9, 10, 11, 12]
terminal_growth_range = [1.5, 2.0, 2.5, 3.0, 3.5]

dcf_values = np.array([
    [98.5, 92.3, 86.8, 81.9, 77.5],
    [88.2, 83.1, 78.5, 74.4, 70.7],
    [79.5, 75.2, 71.3, 67.8, 64.6],
    [72.0, 68.3, 65.0, 62.0, 59.3],
    [65.5, 62.3, 59.4, 56.8, 54.4]
])

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(dcf_values, cmap='RdYlGn', aspect='auto', vmin=50, vmax=100)

ax.set_xticks(np.arange(len(terminal_growth_range)))
ax.set_yticks(np.arange(len(wacc_range)))
ax.set_xticklabels([f'{x}%' for x in terminal_growth_range])
ax.set_yticklabels([f'{x}%' for x in wacc_range])

for i in range(len(wacc_range)):
    for j in range(len(terminal_growth_range)):
        text = ax.text(j, i, f'{dcf_values[i, j]:.1f}', ha="center", va="center", color="black", fontweight='bold')

ax.set_xlabel('Terminal Growth Rate', fontsize=12)
ax.set_ylabel('WACC', fontsize=12)
ax.set_title('DCF Sensitivity Analysis: Fair Value per Share', fontsize=14, fontweight='bold')

cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Fair Value (RMB)', rotation=270, labelpad=20)
ax.plot(1, 2, 'r*', markersize=20, label='Current Price (90.39)')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig(f'{output_dir}/guangxun_dcf_sensitivity.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5: DCF Sensitivity Analysis - Saved")

# 6. 收入结构饼图
segments = ['Datacom\n(45%)', 'Telecom\n(35%)', 'Optical Chips\n(15%)', 'Others\n(5%)']
sizes = [45, 35, 15, 5]
colors_pie = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
explode = (0.05, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=segments, colors=colors_pie,
                                   autopct='%1.0f%%', shadow=True, startangle=90, textprops={'fontsize': 11})

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

ax.set_title('Guangxun Technology: Revenue Structure (2025E)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f'{output_dir}/guangxun_revenue_structure.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 6: Revenue Structure - Saved")

# 7. 股价与估值区间图
fig, ax = plt.subplots(figsize=(12, 6))

valuation_scenarios = ['Bear\n(65)', 'Base\n(75)', 'Bull\n(85)', 'Current\n(90.39)']
values = [65, 75, 85, 90.39]
colors_val = ['#E74C3C', '#F39C12', '#27AE60', '#3498DB']

bars = ax.bar(valuation_scenarios, values, color=colors_val, alpha=0.8, edgecolor='black', linewidth=1.5)

ax.axhline(y=90.39, color='#E74C3C', linestyle='--', linewidth=2, label='Current Price: 90.39')
ax.axhline(y=75, color='#27AE60', linestyle='--', linewidth=2, label='Base Case: 75')

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_ylabel('Price (RMB)', fontsize=12)
ax.set_title('Guangxun Technology: Valuation Scenarios vs Current Price', fontsize=14, fontweight='bold')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3, axis='y')

ax.text(3.5, 70, 'Current price is\n15-30% above\nbase case', 
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5), fontsize=10, ha='center')

plt.tight_layout()
plt.savefig(f'{output_dir}/guangxun_valuation_scenarios.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 7: Valuation Scenarios - Saved")

print("\n✅ All 7 charts generated successfully!")
print(f"Output directory: {output_dir}/")

# -*- coding: utf-8 -*-
"""
酒店预订数据清洗、分析与可视化
数据集：hotel_bookings.csv (来自Kaggle)
输出图片：保存到 outputs/ 文件夹
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# ------------------------------
# 1. 数据加载与初步查看
# ------------------------------
def load_data(filepath="data/hotel_bookings.csv"):
    """加载CSV数据并显示基本信息"""
    df = pd.read_csv(filepath)
    print("数据形状:", df.shape)
    print("\n前5行:")
    print(df.head())
    print("\n列信息:")
    print(df.info())
    print("\n缺失值统计:")
    print(df.isnull().sum())
    return df

# ------------------------------
# 2. 数据清洗
# ------------------------------
def clean_data(df):
    """处理缺失值、转换日期类型、派生新特征"""
    df_clean = df.copy()

    # 2.1 处理缺失值
    # children 用中位数填充（假设0为无儿童）
    df_clean['children'].fillna(df_clean['children'].median(), inplace=True)
    # country 用众数填充
    df_clean['country'].fillna(df_clean['country'].mode()[0], inplace=True)
    # agent 和 company 用0填充（表示未知/无代理）
    df_clean['agent'].fillna(0, inplace=True)
    df_clean['company'].fillna(0, inplace=True)

    # 2.2 转换日期列
    df_clean['reservation_status_date'] = pd.to_datetime(
        df_clean['reservation_status_date'], errors='coerce'
    )
    df_clean['arrival_date'] = pd.to_datetime(
        df_clean['arrival_date_year'].astype(str) + '-' +
        df_clean['arrival_date_month'].str[:3] + '-' +
        df_clean['arrival_date_day_of_month'].astype(str),
        errors='coerce'
    )

    # 2.3 派生新特征：总人数、是否取消、停留天数
    df_clean['total_guests'] = (df_clean['adults'] + df_clean['children'] +
                                df_clean['babies'])
    df_clean['is_canceled'] = df_clean['is_canceled'].astype(int)
    df_clean['stays_total'] = (df_clean['stays_in_weekend_nights'] +
                               df_clean['stays_in_week_nights'])

    # 2.4 删除对分析无用的列（可选）
    # 这里保留所有列，后续按需使用

    # 2.5 去除异常值（例如总人数为0的记录）
    df_clean = df_clean[df_clean['total_guests'] > 0]

    print("\n清洗后数据形状:", df_clean.shape)
    print("缺失值已处理:", df_clean.isnull().sum().sum() == 0)
    return df_clean

# ------------------------------
# 3. 数据分析与可视化
# ------------------------------
def analyze_and_visualize(df):
    """生成多张分析图表并保存到outputs/"""
    # 创建输出目录
    os.makedirs("outputs", exist_ok=True)

    # 设置中文显示（视操作系统而定，可改为英文标签）
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

    # 3.1 预订取消比例（饼图）
    plt.figure(figsize=(6, 6))
    cancel_ratio = df['is_canceled'].value_counts()
    labels = ['未取消', '已取消']
    plt.pie(cancel_ratio, labels=labels, autopct='%1.1f%%', startangle=90,
            colors=['#66b3ff', '#ff9999'])
    plt.title('预订取消比例')
    plt.savefig('outputs/cancel_pie.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3.2 每月预订数量（折线图）
    plt.figure(figsize=(12, 5))
    # 提取月份数字
    month_map = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
                 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    df['month_num'] = df['arrival_date_month'].map(month_map)
    monthly_bookings = df.groupby('month_num').size().sort_index()
    plt.plot(monthly_bookings.index, monthly_bookings.values, marker='o', linestyle='-')
    plt.xticks(range(1,13), ['Jan','Feb','Mar','Apr','May','Jun',
                             'Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.xlabel('月份')
    plt.ylabel('预订数量')
    plt.title('各月预订数量趋势')
    plt.grid(True, alpha=0.3)
    plt.savefig('outputs/monthly_bookings.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3.3 不同酒店类型的取消率（柱状图）
    plt.figure(figsize=(8, 5))
    hotel_cancel = df.groupby('hotel')['is_canceled'].mean() * 100
    sns.barplot(x=hotel_cancel.index, y=hotel_cancel.values, palette='pastel')
    plt.ylabel('取消率 (%)')
    plt.title('不同酒店类型的取消率')
    for i, v in enumerate(hotel_cancel.values):
        plt.text(i, v+1, f'{v:.1f}%', ha='center')
    plt.savefig('outputs/hotel_cancel_rate.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3.4 预订渠道分布（水平条形图，取前10）
    plt.figure(figsize=(10, 6))
    market_seg = df['market_segment'].value_counts().head(10)
    sns.barplot(x=market_seg.values, y=market_seg.index, palette='viridis')
    plt.xlabel('预订数量')
    plt.ylabel('渠道')
    plt.title('预订渠道分布（前10）')
    plt.savefig('outputs/market_segment.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3.5 客人国籍分布（前10）
    plt.figure(figsize=(10, 6))
    country_counts = df['country'].value_counts().head(10)
    sns.barplot(x=country_counts.values, y=country_counts.index, palette='rocket')
    plt.xlabel('预订数量')
    plt.ylabel('国家代码')
    plt.title('客人国籍分布（前10）')
    plt.savefig('outputs/country_dist.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3.6 入住天数分布（直方图）
    plt.figure(figsize=(10, 5))
    sns.histplot(df['stays_total'], bins=30, kde=True, color='skyblue')
    plt.xlabel('总入住天数')
    plt.ylabel('频次')
    plt.title('总入住天数分布')
    plt.savefig('outputs/stays_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3.7 热力图：数值特征相关性
    plt.figure(figsize=(12, 8))
    numeric_cols = ['lead_time', 'stays_total', 'adults', 'children', 'babies',
                    'total_guests', 'is_canceled', 'booking_changes', 'days_in_waiting_list']
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('数值特征相关性热力图')
    plt.savefig('outputs/correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("所有图表已保存到 outputs/ 目录")

# ------------------------------
# 4. 主程序（执行流程）
# ------------------------------
def main():
    print("="*50)
    print("酒店预订数据分析流程开始")
    print("="*50)

    # 加载数据
    df = load_data("data/hotel_bookings.csv")

    # 清洗
    df_clean = clean_data(df)

    # 分析与可视化
    analyze_and_visualize(df_clean)

    # 输出清洗后数据的描述统计
    print("\n清洗后数据描述统计:")
    print(df_clean.describe())
    output_csv_path = "outputs/hotel_bookings_clean.csv"
    df_clean.to_excel(output_csv_path, index=False)
    print(f"清洗后的数据已保存至: {output_csv_path}")
    # 可选：保存清洗后的数据
    # df_clean.to_csv("outputs/cleaned_hotel_bookings.csv", index=False)
    print("\n分析完成！")

if __name__ == "__main__":
    main()


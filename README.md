# 🏨 酒店预订数据分析项目 (Hotel Booking Analysis)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![PowerBI](https://img.shields.io/badge/PowerBI-Ready-yellow)

## 📖 项目简介
本项目基于 **Kaggle 经典酒店预订数据集（Hotel Bookings）**，使用 **Python** 完成全流程数据清洗与探索性数据分析（EDA），并输出标准化数据源，最终无缝对接 **Excel 验证** 与 **Power BI 动态仪表板**，实现从“脏数据”到“业务洞察”的完整链路。

> **核心目标**：探索酒店预订取消率的影响因素，分析客源分布、淡旺季趋势及房价规律，为运营策略提供数据支撑。

---

## 🗂️ 数据集说明
- **文件来源**：`data/hotel_bookings.csv`（含 32 个字段，约 12 万条记录）
- **关键字段**：
  - `hotel`：酒店类型（Resort Hotel / City Hotel）
  - `is_canceled`：是否取消（核心标签）
  - `lead_time`：提前预订天数
  - `adr`（Average Daily Rate）：日均房价
  - `arrival_date_year / month / day`：抵达日期
  - `country`、`market_segment`、`customer_type` 等维度字段

---

## 🛠️ 技术栈与工具链
| 工具 | 职责 |
| :--- | :--- |
| **Python (Pandas/NumPy)** | 数据清洗、缺失值处理、特征工程、复杂计算 |
| **Python (Matplotlib/Seaborn)** | 生成基础静态可视化图表（暂存 `outputs/`） |
| **Excel** | 样本数据抽查、轻量级透视验证、异常值人工复核 |
| **Power BI** | 制作动态交互仪表板、业务监控看板、最终汇报交付 |

---

## 📁 项目文件结构

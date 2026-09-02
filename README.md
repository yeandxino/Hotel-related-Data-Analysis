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
hotel-booking-analysis/
├── data/
│ └── hotel_bookings.csv # 原始数据集
├── outputs/ # 输出目录（自动生成）
│ ├── cleaned_hotel_data.xlsx # 清洗后的数据源（核心产出）
│ ├── cancel_pie.png # 取消比例饼图
│ ├── monthly_bookings.png # 月度趋势折线图
│ ├── hotel_cancel_rate.png # 酒店类型取消率柱状图
│ ├── market_segment.png # 渠道分布条形图
│ ├── country_dist.png # 客源国籍分布图
│ ├── stays_distribution.png # 入住天数分布直方图
│ ├── correlation_heatmap.png # 数值特征相关性热力图
│ ├── adr_distribution.png # 房价分布图（新增）
│ └── lead_time_cancel_rate.png # 提前预订天数与取消率关系图
├── jiudian.py # 主程序脚本
├── requirements.txt # Python 依赖清单
└── README.md # 项目说明文档

---

## ⚙️ 核心功能实现（Python）

### 1. 数据清洗 (Data Cleaning)
- ✅ **缺失值智能填充**：
  - `children` → 中位数填充（若无数据则填 0）
  - `country` → 众数填充（最常见国籍）
  - `agent` / `company` → 填充 `0`（代表“无代理/无公司”，有业务含义）
- ✅ **日期标准化**：合并年月日字段为统一的 `arrival_date` 时间格式。
- ✅ **特征工程**：派生 `total_guests`（总人数）、`stays_total`（总入住天数）等新列。
- ✅ **异常值过滤**：剔除 `total_guests <= 0` 的无效录入记录。

### 2. 探索性分析 (EDA) 与可视化
- 📊 **核心指标监控**：整体取消率、平均房价（ADR）、平均提前预订天数。
- 📈 **趋势洞察**：月度预订量变化趋势、不同酒店类型的取消率对比。
- 🌍 **客群画像**：Top 10 客源国分布、主流市场渠道（Online TA / Offline TA / Direct）占比。
- 🔗 **相关性分析**：`lead_time`、`stays_total`、`adr` 等数值变量间的关联热力图。
- 🎯 **进阶分析**：提前预订天数与取消率的单调关系（分箱折线图），验证“预订越早，取消概率越高”的业务假设。

### 3. 数据导出
- 💾 清洗后的完整数据自动保存为 `outputs/cleaned_hotel_data.xlsx`，便于 Excel 二次验证及 **Power BI 直接挂载**。

---

## 🚀 快速开始（运行指南）

### 环境配置
确保已安装 Python 3.8+，在项目根目录下执行：
```bash
pip install -r requirements.txt
执行脚本
bash
python jiudian.py
程序将自动：

读取 data/hotel_bookings.csv

执行清洗与特征工程

生成所有图表至 outputs/ 文件夹

输出清洗后的 Excel 文件

📊 下一步：Power BI 仪表板接入
打开 Power BI Desktop，选择 获取数据 → Excel。

导入 outputs/cleaned_hotel_data.xlsx。

在 Power BI 中创建以下核心度量值（DAX）：

总预订数 = COUNTROWS('cleaned_hotel_data')

取消率 = DIVIDE(CALCULATE([总预订数], 'cleaned_hotel_data'[is_canceled]=1), [总预订数])

平均房价 = AVERAGE('cleaned_hotel_data'[adr])

拖拽生成动态看板（包含卡片图、折线趋势、地图、切片器等），实现业务自助分析。

📝 依赖库清单（requirements.txt）
text
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
openpyxl>=3.1.0
🤝 贡献与反馈
欢迎提交 Issue 或 Pull Request 来优化数据分析逻辑或新增可视化维度。

📌 版权声明
本项目仅供学习与数据分析研究使用，数据集来源于 Kaggle Hotel Booking Demand。

text

---

### 附加建议（针对 GitHub 仓库）

1. **关于 `image.png` 文件**：你之前截图中有两个图片文件（IDE 界面截图和数据样本截图），建议将它们重命名并放入 `docs/` 或根目录，在 README 中引用展示：
   ```markdown
   ## 📸 项目截图
   ![项目结构](image.png)
如果你想把 Power BI 仪表板的截图也放进去，等你在 Power BI 做完后，截一张全屏图放到 README 末尾，会让项目看起来更完整、更有说服力。

Git 提交信息建议：

第一次提交：feat: 初始化酒店预订数据分析项目

更新代码：fix: 修正 df_clean 作用域问题及 seaborn 弃用警告


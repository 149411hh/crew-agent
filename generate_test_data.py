import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 生成模拟销售数据
dates = [datetime(2026, 3, 1) + timedelta(days=i) for i in range(30)]
data = {
    "日期": dates,
    "产品": np.random.choice(["A产品", "B产品", "C产品", "D产品"], 30),
    "销售额": np.random.randint(5000, 50000, 30),
    "销量": np.random.randint(10, 200, 30),
    "地区": np.random.choice(["北京", "上海", "广州", "深圳", "东京"], 30)
}

df = pd.DataFrame(data)
df.to_excel("data/sales_data.xlsx", index=False)
print(" 测试数据 sales_data.xlsx 已生成！")
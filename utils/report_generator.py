import os
from datetime import datetime

def save_final_report(result: str, user_input: str) -> str:
    """保存结构化的最终 Markdown 报告"""
    os.makedirs("outputs", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/office_report_{timestamp}.md"
    
    content = f"""# OfficeAI-Crew 任务报告
**生成时间**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**用户原始需求**：{user_input}

---

{result}

---
报告由 OfficeAI-Crew 多 Agent 团队自动生成
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filename
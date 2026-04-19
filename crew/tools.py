from crewai_tools import FileReadTool, SerperDevTool
import pandas as pd
from pypdf2 import PdfReader
import markdown
from weasyprint import HTML
import os
from datetime import datetime, timedelta
from typing import List

# 基础工具
file_read_tool = FileReadTool()

# Serper 搜索工具（需在 .env 配置 SERPER_API_KEY）
search_tool = SerperDevTool() if os.getenv("SERPER_API_KEY") else None

# ==================== 自定义工具 ====================

def read_pdf_file(file_path: str) -> str:
    """读取 PDF 文件内容"""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return f"PDF 内容预览（前1000字符）：\n{text[:1000]}...\n总页数：{len(reader.pages)}"
    except Exception as e:
        return f"读取 PDF 失败: {str(e)}"

def generate_email_draft(subject: str, recipient: str, content: str, tone: str = "professional") -> str:
    """生成专业邮件草稿"""
    signature = "\n\n最佳 regards,\n[你的名字]\n[你的职位]\n[公司名称]"
    email = f"""主题: {subject}

尊敬的 {recipient}：

{content}

{signature}"""
    return email

def suggest_meeting_time(preferred_date: str = None, duration_minutes: int = 60) -> str:
    """建议会议时间（简单模拟，避免早晚高峰）"""
    if not preferred_date:
        preferred_date = datetime.now().strftime("%Y-%m-%d")
    
    suggestions = [
        f"{preferred_date} 10:00-11:00（上午黄金时段）",
        f"{preferred_date} 14:00-15:00（下午精力较好）",
        f"{preferred_date} 15:30-16:30（避免午后困倦）"
    ]
    return "推荐会议时间：\n" + "\n".join(suggestions)

def markdown_to_html_report(markdown_content: str, title: str = "OfficeAI-Crew 报告") -> str:
    """将 Markdown 转为 HTML 并保存"""
    html = markdown.markdown(markdown_content)
    full_html = f"""
    <html>
    <head><meta charset="utf-8"><title>{title}</title></head>
    <body style="font-family: Arial, sans-serif; padding: 40px;">
        <h1>{title}</h1>
        {html}
    </body>
    </html>
    """
    os.makedirs("outputs", exist_ok=True)
    path = f"outputs/report_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(full_html)
    return f"HTML 报告已生成：{path}"

# 工具列表
def get_all_tools():
    tools = [file_read_tool, read_pdf_file, generate_email_draft, suggest_meeting_time, markdown_to_html_report]
    if search_tool:
        tools.append(search_tool)
    return tools
from crew.crew import create_office_crew
from utils.report_generator import save_final_report
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from dotenv import load_dotenv
import os
import sys

load_dotenv()

console = Console()

def main():
    console.print(Panel.fit(
        "OfficeAI-Crew - 智能办公助手团队\n"
        "多Agent协作完成办公任务",
        title="启动",
        border_style="blue"
    ))
    
    # 获取用户输入
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        console.print("\n请输入你的办公需求（例如：帮我准备明天下午的项目周会）：")
        user_input = input("> ").strip()
    
    if not user_input:
        console.print("输入不能为空！")
        return
    
    console.print(f"\n任务已接收：{user_input}\n")
    console.print("正在启动 Agent 团队（研究员、文案、日程、演示、主管）...\n")
    
    try:
        crew = create_office_crew(user_input)
        result = crew.kickoff()
        
        # 保存 Markdown 报告
        report_path = save_final_report(str(result), user_input)
        
        # 生成 HTML 美观报告
        from crew.tools import markdown_to_html_report
        html_path = markdown_to_html_report(str(result), "OfficeAI-Crew 办公任务报告")
        
        # 输出最终结果
        console.print("\n" + "=" * 80)
        console.print(Panel(
            Markdown(str(result)),
            title="任务完成 - 最终交付成果",
            border_style="green",
            padding=(1, 2)
        ))
        
        console.print(f"\nMarkdown 报告已保存：{report_path}")
        console.print(f"HTML 美观报告已生成：{html_path}")
        console.print("\n感谢使用 OfficeAI-Crew！")
        
    except Exception as e:
        console.print(f"执行过程中出现错误：{str(e)}")
        console.print("建议检查 .env 文件中的 OPENAI_API_KEY 是否正确设置。")
        if "Serper" in str(e):
            console.print("如果使用了搜索功能，请确认 SERPER_API_KEY 已正确配置。")

if __name__ == "__main__":
    main()
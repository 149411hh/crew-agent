from crewai import Task
from .agents import researcher, writer, scheduler, presenter, manager

# ==================== 定义 Tasks ====================

def create_tasks(user_input: str):
    """根据用户输入动态创建任务"""
    
    research_task = Task(
        description=f"""分析用户需求中的数据相关部分：
        用户需求: {user_input}
        请从 data/ 目录下的文件中提取必要信息，并进行数据分析。""",
        expected_output="详细的数据分析报告，包括关键指标、趋势和洞察。用中文输出。",
        agent=researcher
    )

    writing_task = Task(
        description=f"""根据用户需求和研究员提供的数据，撰写专业文档：
        用户需求: {user_input}
        请生成合适的办公文档（邮件、周报、总结等）。""",
        expected_output="专业的中文办公文档，包括标题、正文和适当的礼貌用语。",
        agent=writer
    )

    presentation_task = Task(
        description=f"""为用户需求生成演示材料：
        用户需求: {user_input}
        请生成清晰的PPT大纲或汇报要点。""",
        expected_output="PPT大纲或汇报结构（用Markdown格式），包含标题、关键点和建议演讲顺序。",
        agent=presenter
    )

    final_task = Task(
        description=f"""汇总所有团队成员的输出，为用户提供完整的最终结果。
        用户原始需求: {user_input}
        请以清晰、专业的格式呈现最终交付物，包括数据分析、文案和演示材料。""",
        expected_output="完整的办公任务交付成果，包含多个部分，并给出使用建议。用中文输出。",
        agent=manager,
        context=[research_task, writing_task, presentation_task]
    )

    return [research_task, writing_task, presentation_task, final_task]
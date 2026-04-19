from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from .tools import file_read_tool, get_all_tools, read_pdf_file, generate_email_draft, suggest_meeting_time

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    temperature=float(os.getenv("TEMPERATURE", 0.7))
)

# ==================== Agents ====================

researcher = Agent(
    role="资深数据与信息研究员",
    goal="准确读取文件（Excel/PDF）、分析数据、搜索必要信息，并提供深度洞察",
    backstory="你是一位严谨的分析师，擅长处理 Excel、PDF，并结合最新信息给出业务建议。",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    tools=[file_read_tool, read_pdf_file] + ([search_tool] if 'search_tool' in globals() else [])
)

writer = Agent(
    role="专业办公文案专家",
    goal="撰写高质量的邮件、周报、总结等办公文档，语气得体专业",
    backstory="你有10年行政助理经验，精通中国职场沟通规范。",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    tools=[generate_email_draft, file_read_tool]
)

scheduler = Agent(
    role="日程与会议协调专家",
    goal="合理安排会议时间、生成日程建议，避免冲突",
    backstory="你是一位高效的时间管理高手，熟悉高管日程安排。",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    tools=[suggest_meeting_time]
)

presenter = Agent(
    role="汇报与演示专家",
    goal="生成清晰的 PPT 大纲、汇报要点和演讲提示",
    backstory="你擅长将复杂内容提炼成逻辑清晰、说服力强的演示材料。",
    llm=llm,
    verbose=True,
    allow_delegation=False
)

manager = Agent(
    role="智能办公项目主管",
    goal="协调团队、分解任务、确保最终输出完整专业且实用",
    backstory="你是一位经验丰富的项目经理，擅长把模糊办公需求转化为高质量成果，并把控整体质量。",
    llm=llm,
    verbose=True,
    allow_delegation=True
)
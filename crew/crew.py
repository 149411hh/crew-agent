from crewai import Crew, Process
from .agents import researcher, writer, scheduler, presenter, manager
from .tasks import create_tasks
from dotenv import load_dotenv

load_dotenv()

def create_office_crew(user_input: str):
    tasks = create_tasks(user_input)
    
    office_crew = Crew(
        agents=[researcher, writer, scheduler, presenter, manager],
        tasks=tasks,
        manager_agent=manager,
        process=Process.hierarchical,
        verbose=2,                    # 更详细日志
        memory=True,
        cache=True,
        max_rpm=30,
        output_log_file="outputs/crew_log.txt",
        # 可选：单独指定 manager 模型
        # manager_llm=ChatOpenAI(model="gpt-4o")
    )
    return office_crew
# OfficeAI-Crew —— 智能办公助手团队

一个基于CrewAI的多 Agent 办公自动化 Demo，模拟真实办公小团队（研究员、文案、日程专家、演示专家、项目主管）协作，帮助用户快速完成数据分析、周报撰写、邮件起草、会议安排和汇报准备等办公任务。

## ✨ 项目亮点

- 支持自然语言输入办公需求，一句话即可启动整个团队
- 多 Agent 角色化分工 + Hierarchical（主管协调）模式
- 支持读取 Excel 销售数据和 PDF 文件
- 自动生成专业邮件草稿、日程建议、PPT 大纲
- 输出 Markdown + 美观 HTML 报告（可直接分享）
- 集成 Serper 网页搜索（可选），可获取最新行业信息
- 详细的 Agent 协作过程日志，便于调试和演示

##  快速开始

1. 克隆项目
```bash
git clone https://github.com/你的用户名/OfficeAI-Crew.git
cd OfficeAI-Crew

2. 安装依赖
Bashpip install -r requirements.txt

3. 配置环境变量
Bashcp .env.example .env
编辑 .env 文件，填入你的密钥：
envOPENAI_API_KEY=sk-你的OpenAI密钥
SERPER_API_KEY=你的Serper密钥（可选，用于联网搜索）
LLM_MODEL=gpt-4o-mini

4. 生成测试数据
Bashpython generate_test_data.py

5. 运行 Demo
Bashpython main.py

示例输入：
text帮我准备明天下午的项目周会：分析 sales_data.xlsx 中的上周销售数据，生成周报要点，并起草给老板的总结邮件，同时搜索一下2026年AI办公工具的最新趋势

📁 项目结构
textOfficeAI-Crew/
├── crew/
│   ├── agents.py          # 定义所有 Agent 角色和工具
│   ├── tasks.py           # 定义任务流程
│   ├── crew.py            # Crew 编排与 Hierarchical 模式
│   └── tools.py           # 自定义工具（Excel、PDF、邮件、日程、HTML报告等）
├── utils/
│   └── report_generator.py # Markdown 报告生成
├── data/
│   └── sales_data.xlsx    # 测试销售数据
├── outputs/               # 生成的报告和日志（.gitignore）
├── main.py                # CLI 入口
├── generate_test_data.py  # 生成测试数据
├── requirements.txt
├── .env.example
└── README.md
🛠️ 核心功能与工具

数据分析：读取并分析 Excel 销售数据（总销售额、产品/地区表现等）
文件读取：支持 Excel 和 PDF 文件
邮件生成：自动生成专业中文邮件草稿（含主题、正文、签名）
日程安排：智能建议会议时间
演示材料：生成 Markdown 格式的 PPT 大纲和汇报要点
联网搜索（可选）：通过 Serper 获取最新网页信息
报告输出：自动生成 Markdown + HTML 美观报告

技术栈

CrewAI（多 Agent 编排框架）
LangChain + crewai-tools
OpenAI GPT 系列模型（gpt-4o-mini / gpt-4o）
pandas（数据分析）
PyPDF2（PDF 读取）
Rich（终端美化输出）
markdown + weasyprint（报告生成）

未来计划（欢迎贡献）
添加 Streamlit 网页交互界面
支持本地模型（Ollama / LM Studio）
集成 RAG 公司知识库
支持生成 Word 文档（.docx）
集成 Gmail / 企业微信邮件发送
Docker 一键部署


欢迎 Star ⭐ 和 Fork！
如果你在使用过程中有任何问题或改进建议，欢迎提交 Issue 或 Pull Request。
# OfficeAI-Crew

基于 **CrewAI** 的多 Agent 智能办公助手系统。通过一句自然语言指令，即可自动完成数据分析、周报撰写、邮件起草、会议总结等办公任务。

## ✨ 项目亮点

- **多 Agent 协作**：支持 Hierarchical（层级）模式，模拟真实团队工作流。
- **全能工具集成**：集成数据分析、PDF 处理、邮件生成等多种实用工具。
- **高质量输出**：自动生成结构化的 Markdown 报告和 HTML 格式结果。
- **透明化执行**：提供详细的任务执行日志，便于调试和过程演示。
- **极简操作**：专为日常办公自动化设计，上手即用。

---

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/149411hh/crew-agent.git
cd crew-agent
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
复制模板并编辑 `.env` 文件，填入你的 API 密钥：
```bash
cp .env.example .env
```
**配置内容示例：**
```env
OPENAI_API_KEY=sk-你的OpenAI_API密钥
# 可选（用于联网搜索功能）
SERPER_API_KEY=你的Serper密钥
LLM_MODEL=gpt-4o-mini
```

### 4. 生成测试数据并运行
```bash
python generate_test_data.py
python main.py
```

> **示例输入：** > *“帮我准备明天下午的项目周会：分析 sales_data.xlsx 的上周销售数据，生成周报要点，并起草给老板的总结邮件。”*

---

## 📁 项目结构

```text
crew/          # Agent 角色、任务和 Crew 定义
tools/         # 自定义工具（Excel、PDF、邮件等）
utils/         # 报告生成和辅助功能
data/          # 测试数据
outputs/       # 生成的报告和日志
main.py        # 项目入口
```

---

## 🛠️ 技术栈

* **核心框架**：[CrewAI](https://www.crewai.com/) + [LangChain](https://www.langchain.com/)
* **大语言模型**：OpenAI GPT 系列（推荐 `gpt-4o-mini` 或 `gpt-4o`）
* **处理工具**：Pandas (数据), PyPDF2 (PDF), Rich (终端美化), Serper (搜索)
* **开发语言**：Python 3.13

---

## 💡 使用场景

* **报表自动化**：销售/项目周报一键生成。
* **深度分析**：Excel 数据分析与初步可视化。
* **会议提效**：会议纪要整理与总结邮件撰写。
* **流程简化**：各种繁琐的日常办公任务自动化。

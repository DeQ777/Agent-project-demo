# Agent-project-demo
利用Langchain框架进行搭建的简单Agent智能体

# 说明
该项目仅为本人学习Agent过程的记录，并非原创
感谢黑马程序员开源免费项目、高德地图等开放平台

# 项目简介
智扫通机器人智能客服是一个面向扫地机器人使用用户的问答聊天应用。
整体由前端（使用streamlit搭建）和后端（利用Langchain构建的Agent）组成

# 目录结构
Agent-project-demo/
├── agent/
│   ├── react_agent.py            # Agent执行程序
│   └── tools/
│       ├── agent_tools.py        # Agent所需调用的工具
│       └── middleware.py         # Agent中间件，用来反馈运行过程的信息
├── chroma_db/                    # Chroma向量库，用于向量化存储数据信息
├── config/
│   ├── agent.yml                 # Agent的基础配置
│   ├── rag.yml                   # 模型名称的配置
│   ├── chroma.yml                # 向量库相关配置
│   └── prompts.yml               # 各种提示词文件路径
├── data/
│   ├── 扫地机器人100问.pdf
│   ├── 扫地机器人100问2.txt
│   ├── 扫拖一体机器人100问.txt
│   ├── 故障排除.txt
│   ├── 维护保养.txt
│   ├── 选购指南.txt
│   └── external/
│       └── records.csv           # 用户使用记录
├── logs/                         # 日志文件目录（自动生成）
├── model/
│   └── factory.py                # 用于加载聊天模型与嵌入模型
├── prompts/
│   ├── main_prompt.txt           # 主 ReAct 提示词
│   ├── rag_summarize.txt         # RAG 摘要提示词
│   └── report_prompt.txt         # 报告生成提示词
├── rag/
│   ├── rag_service.py            # RAG 检索摘要服务
│   └── vector_store.py           # Chroma 向量库管理
├── utils/
│   ├── config_handler.py         # 加载各项配置
│   ├── logger_handler.py         # 用于生成日志
│   ├── prompt_loader.py          # 加载各部分的提示词
│   ├── file_handler.py           # 用于加载文档数据
│   └── path_tool.py              # 获取文件的路径
├── app.py                        # 网页搭建，用于用户的直接使用
└── md5.text                      # MD5文档，用于校核向量库中数据是否重复


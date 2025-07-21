from autogen_agentchat.agents import CodeExecutorAgent

def getCodeExecutorAgent(code_executor):

    agent = CodeExecutorAgent(
        name="code_executor_agent",
        code_executor=code_executor
    )

    return agent
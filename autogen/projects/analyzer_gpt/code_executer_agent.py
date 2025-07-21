import asyncio
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_agentchat.messages import TextMessage

async def main():
    docker = DockerCommandLineCodeExecutor(
        image="python:3-slim",
        container_name="CodeExecuterContainer",
        work_dir="/temp",
        timeout=20,
    )

    code_executer_agent = CodeExecutorAgent(
        name="CodeExecuterAgent",
        code_executor=docker,
    )

    python_code = """
```python
print("hello world")
```
    """
    task = TextMessage(content=python_code, source="user")

    await docker.start()

    result = await code_executer_agent.run(task=task)

    print(result)

if __name__ == "__main__":
    asyncio.run(main())
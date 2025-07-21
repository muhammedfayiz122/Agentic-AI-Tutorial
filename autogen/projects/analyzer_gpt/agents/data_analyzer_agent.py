from autogen_agentchat.agents import AssistantAgent
from prompts.agent_prompts import DATA_ANALYZER_MESSAGE

def getDataAnalayzerAgent(model_client):
    """
    Agent for analyze data
    """
    data_analyzer_agent = AssistantAgent(
        name="data_analyzer_agent",
        model_client=model_client,
        description="",
        system_message=DATA_ANALYZER_MESSAGE
    )
    return data_analyzer_agent
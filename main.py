import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor


from tools import search_tool, wiki_tool, save_tool


# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Pydantic model for structured output
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Language model configuration
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
)

# Output parser using the model schema
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Define the prompt template with placeholders and formatting
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         "You are a research assistant that helps generate research papers.\n"
         "You must use any tools necessary. Format the output as:\n{format_instructions}"),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())


# Define available tools
tools = [search_tool, wiki_tool, save_tool]

# Create agent and executor
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Prompt user input
query = input("What can I help you research? ")

# Run the agent and handle output
try:
    raw_response = agent_executor.invoke({"query": query})
    structured_response = parser.parse(raw_response)
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e)
    print("Raw response:\n", raw_response)

# Buddy my AI Research Assistant
This project is an intelligent agent powered by OpenAI's GPT that can perform autonomous research using search tools, Wikipedia, and local saving mechanisms. It is designed to assist in generating structured summaries, sources, and contextual information for academic or general topics using LangChain and LangChain-compatible tools.


### Requirements

Ensure you have Python 3.9+ and the following packages installed:

- pip install langchain langchain-openai python-dotenv pydantic

#### Create a .env file in the root directory with the following content:

- OPENAI_API_KEY="your_openai_api_key_here"



ser Query → AgentExecutor (LangChain Tool-Calling Agent)
         ↘︎                 ↙︎
        [LLM] ———→ [Search Tools, Wiki, Save Tool]
                          ↓
           Structured Response via Pydantic


The agent:
- Accepts a user query
- Decides which tools to use
- Executes tools to gather data
- Formats the response using a Pydantic schema
- Returns a rich, structured summary

### Example Output
{
  "topic": "Artificial Intelligence in Healthcare",
  "summary": "AI is transforming healthcare through diagnostics, personalised treatment, and administrative automation...",
  "sources": [
    "https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC..."
  ],
  "tools_used": ["search_tool", "wiki_tool"]
}


### Uasage: 
- python main.py



#### Query input type:
What are the latest advancements in quantum computing?


### Future Enhancements
- Add support for citations with DOI metadata
- Integrate vector-based memory storage (e.g., FAISS)
- Enable auto-saving reports as PDF/Markdown
- Add multi-turn memory via LangChain's ConversationBufferMemory

### License:
IT License – free to use and modify for educational and research purposes.

### Autor:
Rashid

### Date:20225

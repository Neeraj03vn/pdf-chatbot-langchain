# agent_builder.py
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.tools import Tool

from tools import calculator

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def build_agent(vectorstore, llm):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )

    pdf_qa_tool = Tool(
        name="PDF_QA",
        func=qa_chain.run,
        description="Use this tool to answer questions about the uploaded PDF."
    )

    agent = initialize_agent(
        tools=[pdf_qa_tool, calculator],
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
    return qa_chain, agent

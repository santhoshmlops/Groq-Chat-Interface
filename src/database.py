# Importing necessary modules
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from chain import get_model

# Function to initialize the database connection
def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    # Constructing the database URI
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    # Returning SQLDatabase object initialized with the URI
    return SQLDatabase.from_uri(db_uri)

# Function to create a chain for generating SQL queries
def get_sql_chain(db):
    # Template for generating prompts to write SQL queries
    template = """
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
        
        <SCHEMA>{schema}</SCHEMA>
        
        Conversation History: {chat_history}
        
        Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
        
        For example:
        Question: which 3 artists have the most tracks?
        SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
        Question: Name 10 artists
        SQL Query: SELECT Name FROM Artist LIMIT 10;
        
        Your turn:
        
        Question: {question}
        SQL Query:
        """
        
    # Creating a ChatPromptTemplate from the template
    prompt = ChatPromptTemplate.from_template(template)
    
    # Getting the language model
    llm = get_model()
    
    # Function to retrieve the schema of the database
    def get_schema(_):
        return db.get_table_info()
    
    # Creating a chain of operations
    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
    )

# Function to generate natural language responses to user queries
def get_database_text(user_query: str, db: SQLDatabase, chat_history: list):
    
    # Creating a SQL chain
    sql_chain = get_sql_chain(db)
    
    # Template for generating prompts for natural language responses
    template = """
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, question, sql query, and sql response, write a natural language response.
        <SCHEMA>{schema}</SCHEMA>

        Conversation History: {chat_history}
        SQL Query: <SQL>{query}</SQL>
        User question: {question}
        SQL Response: {response}"""
    
    # Creating a ChatPromptTemplate from the template
    prompt = ChatPromptTemplate.from_template(template)
    
    # Getting the language model
    llm = get_model()
    
    # Creating a chain of operations
    chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
        schema=lambda _: db.get_table_info(),
        response=lambda vars: db.run(vars["query"]),
        )
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # Invoking the chain with necessary variables
    return chain.invoke({
        "question": user_query,
        "chat_history": chat_history,
    })
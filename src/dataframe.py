# Importing necessary libraries
import pandas as pd 
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent 
from chain import get_model  

# Function to process user query on uploaded CSV file
def get_dataframe_text(file_uploads, user_query):
    if not file_uploads:
        return None

    df = pd.concat([pd.read_csv(file) for file in file_uploads])

    # Getting the language model
    model = get_model()

    # Creating a pandas DataFrame agent with the model and DataFrame
    agent = create_pandas_dataframe_agent(model, df, verbose=True)

    # Invoking the agent with user query
    response = agent.invoke(user_query)

    # Returning the response
    return response['output']
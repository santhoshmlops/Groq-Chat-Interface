# Groq Chat Interface

The "Groq Chat Interface" project is a comprehensive interactive assistant designed to facilitate seamless communication between users and the system through various interfaces such as ChatBot, Image processing, PDF parsing, website content analysis, YouTube video content, DataFrame analysis, and Database interactions.

The project begins by offering users a sidebar menu where they can select their desired interface. Each interface caters to different user needs and scenarios, providing a versatile platform for interaction. For instance, the ChatBot interface allows users to engage in conversational interactions, while the Image processing interface enables the system to analyze images uploaded by the user.

Users can upload files or input URLs depending on the selected interface. For interfaces like Image processing, PDF parsing, and DataFrame analysis, users can upload files, whereas for interfaces like website content analysis and YouTube video content, users can input URLs. This flexibility accommodates a wide range of use cases, from analyzing textual data to processing multimedia content.

A notable feature of the system is its ability to maintain a chat history, which displays both user inputs and system responses. This feature not only provides users with a record of their interactions but also facilitates context retention, ensuring a smoother conversational experience.

Real-time response generation is another key aspect of the system. Utilizing various processing methods depending on the selected interface, the system generates responses promptly, enhancing the user experience. Additionally, the system measures response time, allowing users to gauge the efficiency of their interactions with the interface.

One of the most significant functionalities of the system is its Database interaction capability. Users can connect to a database by providing credentials, enabling them to execute queries directly from the interface. This functionality opens up possibilities for data-driven interactions, empowering users to leverage existing data resources seamlessly.

In summary, the "Groq Chat Interface" project offers a robust and user-friendly platform for interactive communication and data analysis. With its diverse set of interfaces, chat history maintenance, real-time response generation, and Database interaction capabilities, the system caters to a wide range of user needs, making it a valuable tool for various applications across different domains.


# How to Download and Run Project?

### You will need to copy and paste the following code into your terminal :

### STEP 01 - Clone this repository:

```bash
https://github.com/santhoshmlops/Groq-Chat-Interface.git
```

### STEP 02 - Create a conda environment or python environment:

```bash
conda create -p venv python=3.11 -y
```

```bash
conda activate venv/
```
or

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### STEP 03 - Install the Requirements : 
```bash
pip install -r requirements.txt
```
### STEP 04 - Download and install Ollama for Embeddings: 

Download and install Ollama.exe [Download link](https://ollama.com/download)

```bash
ollama run nomic-embed-text
```
### STEP 05 - Run the Streamlit Application : 
```bash
streamlit run app.py
```



![Screenshot (39)](https://github.com/santhoshmlops/Groq-Chat-Interface/assets/133121635/ad00ec00-a0ee-4d46-98a4-2a380645ba6a)
![Screenshot (40)](https://github.com/santhoshmlops/Groq-Chat-Interface/assets/133121635/5c05761a-2e74-4b82-80c6-2c4a57e1ac1a)
![Screenshot (41)](https://github.com/santhoshmlops/Groq-Chat-Interface/assets/133121635/7a6ecaa1-e221-4bdb-b881-290f04b6dbb3)

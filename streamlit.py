import streamlit as st
st.set_page_config(page_title="CareConnect - Empathetic Mental Health Companion", layout="wide")
import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Retrieve the OpenAI API key from environment variables
openai_api_key = os.getenv('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')

# Initialize the OpenAI model with the retrieved API key
llm = OpenAI(
    openai_api_key='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',
    temperature=0.7  # Adjust temperature for more creative responses
)

# Chat interface
st.title("CareConnect")

# Define a more detailed prompt template for dialect understanding
prompt_template = PromptTemplate(
    input_variables=["data_description", "question"],
    template="""
    You are a health expert with expertise in understanding various dialects and mental health issues. Your task is to interpret the following data and answer the question in a manner that respects dialect nuances and also provide health-related issues and health centres to the user.
    
    Data:
    {data_description}
    
    Question:
    {question}
    
    Please consider any dialect variations in your response.
    """
)

# Create a LangChain
chain = LLMChain(llm=llm, prompt=prompt_template)

def normalize_dialect(input_text):
    # Example function to normalize common dialect-specific phrases
    # Extend this function as needed
    normalized_text = input_text.replace("y'all", "you all").replace("gonna", "going to")
    return normalized_text

def get_response(data_description, question):
    # Normalize the question for dialect
    normalized_question = normalize_dialect(question)
    
    # Running the chain to get a response
    response = chain.run(data_description=data_description, question=normalized_question)
    
    return response

# Streamlit application
def main():
    

    # Input fields
    data_description = st.text_area("Enter Data Description", "Data includes various facts about Health, Mental health challenges, and Health centers in St.Kitts.")
    question = st.text_input("Enter Your Question")
    
    # Submit button
    if st.button("Get Response"):
        if question:
            answer = get_response(data_description, question)
            st.write(f"*Answer:* {answer}")
        else:
            st.warning("Please enter a question.")

if _name_ == "_main_":
    main()


# Streamlit layout

st.markdown("""
<style>
body {
    background-color:blue;
}
</style>
""", unsafe_allow_html=True)
# Sidebar for mood checkboxes
st.sidebar.title("How are you feeling today?")
feeling_anxious = st.sidebar.checkbox("Feeling Anxious")
feeling_depressed = st.sidebar.checkbox("Feeling Depressed")
feeling_stressed = st.sidebar.checkbox("Feeling Stressed")
trouble_sleeping = st.sidebar.checkbox("Trouble Sleeping")



# Chat history container
chat_history = st.empty()

# Placeholder for chat history
messages = []




# Display the chat history
with chat_history.container():
    for message in messages:
        st.write(message)

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 336px; /* Adjust this value to match the width of your sidebar */
        width: calc(100% - 336px); /* Adjust this value to match the width of your sidebar */
        text-align: center; /* Center text within the available width */
        color: grey;
        padding: 10px;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        background: white; /* Ensure footer background is white to match the page background */
    }
    </style>
    <div class="footer">
        Created by Code Brawlers. This chatbot does not replace human interaction. Seek help from nearby health centres.
    </div>
    """,
    unsafe_allow_html=True
)

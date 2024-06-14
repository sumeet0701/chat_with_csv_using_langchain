import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from dotenv import load_dotenv

def main():
    load_dotenv()

    if os.getenv("GOOGLE_API_KEY") is None or os.getenv("GOOGLE_API_KEY") == "":
        print("google api key is not exists")
    else:
        print("google api key is available")

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    st.set_page_config(page_title = "Ask any from your csv")
    st.header("Ask your csv")

    csv_file = st.file_uploader("Upload a csv file", type="csv")
    if csv_file is not None:
        agent = create_csv_agent(
            ChatGoogleGenerativeAI(model="gemini-pro" ),csv_file, verbose=True
        )                                                   

        user_question = st.text_input("Ask a question about your csv")

        if user_question is not None and user_question == "":
            with st.spinner(text = "In Progress....."):
                st.write(agent.run(user_question))







if __name__ == '__main__':
    main()
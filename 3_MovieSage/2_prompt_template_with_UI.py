import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Initialize Mistral AI Model
model = ChatMistralAI(model="mistral-small-2603")


# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:
Carefully analyze the given movie paragraph and extract the most useful and relevant information from it.

Rules:
- Extract information only from the provided paragraph.
- Do NOT add explanations or extra commentary.
- Do NOT guess or invent unknown facts.
- If any information is not available, write "Not Mentioned".
- Keep the information clear, concise, and accurate.
- Keep the quick summary short (2-3 sentences maximum).
- Each field MUST be displayed on a separate line.
- Add a blank line between each field for better readability.
- Follow the exact output format given below.

Output Format:

**Movie Title:** 
**Release Year:** 
**Genre:** 
**Director:** 
**Main Cast:** 
**Plot:** 
**IMDb Rating:** 
**Music Composer:** 
**Notable Features:** 
**Recognition / Achievements:** 

### Summary
"""
    ),
    (
        "human",
        """
Extract the information from the following paragraph:

{paragraph}
"""
    )
])


# Streamlit UI
st.title("Movie Information Extractor")


# User Input
para = st.text_area(
    "Enter Movie Paragraph:",
    height=250
)


# Extract Information Button
if st.button("Extract Information"):

    if para.strip():

        # Insert paragraph into prompt
        final_prompt = prompt.invoke(
            {"paragraph": para}
        )

        # Send prompt to Mistral AI
        response = model.invoke(final_prompt)

        # Display Result
        st.subheader("Extracted Information")

        # Display each item with proper line breaks
        st.markdown(
            response.content.replace("\n", "  \n")
        )

    else:
        st.warning("Please enter a movie paragraph.")
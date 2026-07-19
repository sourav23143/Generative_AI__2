import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel
from typing import List, Optional


# Load environment variables
load_dotenv()


# --------------------------------------------------
# PYDANTIC SCHEMA
# --------------------------------------------------

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# --------------------------------------------------
# PYDANTIC OUTPUT PARSER
# --------------------------------------------------

parser = PydanticOutputParser(pydantic_object=Movie)


# --------------------------------------------------
# MISTRAL AI MODEL
# --------------------------------------------------

model = ChatMistralAI(model="mistral-small-2603")


# --------------------------------------------------
# PROMPT TEMPLATE
# --------------------------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the paragraph.

{format_instructions}
"""
        ),
        (
            "human",
            "{paragraph}"
        )
    ]
)


# --------------------------------------------------
# STREAMLIT UI
# --------------------------------------------------

st.title("Movie Information Extractor")


# User Input
para = st.text_area(
    "Enter Movie Paragraph:",
    height=250
)


# Extract Data Button
if st.button("Extract Data"):

    if para.strip():

        # Put paragraph and format instructions inside prompt
        final_prompt = prompt.invoke(
            {
                "paragraph": para,
                "format_instructions": parser.get_format_instructions()
            }
        )


        # --------------------------------------------------
        # GET RAW MODEL OUTPUT
        # --------------------------------------------------

        response = model.invoke(final_prompt)

        # Since we are able to invoke this prompt,
        # this thing is known as Runnable (Chains)


        # --------------------------------------------------
        # CONVERT RAW OUTPUT TO STRUCTURED OUTPUT
        # --------------------------------------------------

        # Parse the output of an LLM call to a Pydantic object
        movie_data = parser.parse(response.content)


        # --------------------------------------------------
        # RAW MODEL OUTPUT
        # --------------------------------------------------

        st.header("Raw Model Output")

        st.code(
            response.content,
            language="json"
        )


        # --------------------------------------------------
        # STRUCTURED OUTPUT
        # --------------------------------------------------

        st.header("Structured Output")

        st.json(
            movie_data.model_dump()
        )


    else:

        st.warning("Please enter a movie paragraph.")
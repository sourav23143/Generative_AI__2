from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI

from langchain_community.document_loaders import TextLoader
#by using document loader we can load any documnet

from langchain_core.prompts import ChatPromptTemplate #we are using ChatPromptTemplate as in this we can give roles also.




load_dotenv()

model = ChatMistralAI(model = "mistral-small-2506")



data = TextLoader("4_CourseMate_AI_RAG/document_loaders/notes.txt")
docs = data.load()  #Load data into Document objects.




prompt_template = ChatPromptTemplate.from_messages(
    [("system", "you are a AI that summarizes the text"),
     ("human", "{data}")]

)


# final_prompt = prompt_template.format_messages(data = docs[0].page_content)

#or(we can use both)

final_prompt = prompt_template.invoke(
    {"data" : docs[0].page_content}
)



result = model.invoke(final_prompt)

print(result.content)


#OUTPUT>> 


# **Summary:**

# The document discusses the differences and relationships between covariance and correlation, two fundamental statistical measures used to describe relationships between variables.

# **Covariance:**
# - Measures the direction of the relationship between two variables.
# - Positive covariance: variables move in the same direction.
# - Negative covariance: variables move in opposite directions.
# - Zero covariance: little or no linear relationship.
# - Affected by scale and units, making interpretation of magnitude difficult.

# **Correlation:**
# - Measures both direction and strength of the relationship between two variables.
# - Ranges between -1 and +1.
# - Positive correlation: variables move in the same direction.
# - Negative correlation: variables move in opposite directions.
# - Zero correlation: little or no linear relationship.
# - Standardized, making it unit-free and easier to interpret and compare.

# **Key Differences:**
# - Purpose: Covariance measures direction, correlation measures direction and strength.
# - Range: Covariance has no fixed range, correlation ranges between -1 and +1.
# - Units: Covariance has units, correlation is unit-free.
# - Scale: Covariance is scale-dependent, correlation is not.
# - Interpretation: Correlation is easier to interpret due to standardization.

# **Applications:**
# - Data science: exploratory data analysis, feature selection, multicollinearity detection.
# - Machine learning: feature engineering, model improvement.
# - Finance: portfolio analysis, risk reduction through diversification.

# **Limitations and Considerations:**
# - Correlation does not imply causation.
# - Outliers can significantly affect correlation values.
# - Zero correlation does not necessarily mean variables are independent.
# - Correlation mainly measures linear relationships.

# **Key Takeaways:**
# - Covariance and correlation are fundamental statistical concepts.
# - Covariance identifies the direction of variable movement.
# - Correlation provides information about the strength of the relationship.
# - Both measures have important applications in various fields.
# - Understanding these concepts is crucial for advanced statistical analyses.

# **Conclusion:**
# Understanding covariance and correlation is essential for data scientists and analysts, providing a strong foundation for advanced concepts and analyses.
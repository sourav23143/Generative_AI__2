from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough


model = ChatMistralAI(model = "mistral-small-2506")
parser = StrOutputParser()


code_prompt = ChatPromptTemplate.from_messages({
    ("system", "Ypu are a code generator"),
    ("human", "{topic}")
})


explain_prompt = ChatPromptTemplate.from_messages({
    ("system", "You are a helpful assistant who explains code in simple terms"),
    ("human", "Explain the following code in simple words:\n{code}")
})

#sequence will be something like this >> 

#chain = code_prompt| llm | str_output | explain_prompt | llm | str_output

#then will .invoke() chain 

#_________________________________________________________________________________________________________________________________________________________

# seq = code_prompt| model | parser | explain_prompt | model | parser


# result = seq.invoke({"topic": "write a code of plaindrome in python"})

# print(result)


# _________________________________________________________________________________________________________________________________________________________

#OUTPUT >> 

# This code checks if a given string is a palindrome (a word that reads the same backward as forward). Here's how it works:

# 1. **Function `is_palindrome(s)`**:
#    - Takes a string `s` as input.
#    - **Cleans the string**: Removes all non-alphanumeric characters (like spaces or punctuation) and converts the remaining characters to lowercase. For example, "A man, a plan, a canal: Panama" becomes "amanaplanacanalpanama".
#    - **Checks if the cleaned string is a palindrome**: Compares the cleaned string with its reverse (`cleaned[::-1]`). If they are the same, it returns `True` (meaning it's a palindrome); otherwise, it returns `False`.

# 2. **Example Usage**:
#    - Asks the user to input a string.
#    - Calls `is_palindrome` with the input string.
#    - Prints whether the input is a palindrome or not, along with the original string.

# ### Example:
# - Input: `"racecar"` → Output: `"racecar" is a palindrome.`
# - Input: `"hello"` → Output: `"hello" is not a palindrome.`

# The code handles punctuation and case sensitivity by cleaning the string before comparison.


#WE CAN SEE IN THIS OUTPUT WE NOT GET CODE >> IT  IS ONLY EXPLAINING THE CODE 

# AS WE CAN SEE IN IT >  #seq = code_prompt| model | parser | explain_prompt | model | parser
#WE PASSED  code_prompt to model ,and model to parser and  then parser output will be passed to explain_prompt, 
#BUt we not saved our code output after "parser", so we not get the code 

#SO HERE WE WILL USE PASSTHROUGH WHICH WILL EXTRACT THINGS IN B/W 


#_________________________________________________________________________________________________________________________________________________________


seq = code_prompt| model | parser #THIS Seq will generate code 

#now we have to send this code two way , one we get code first as output, then also forwad it further so that it can review it 

#so for this we will send this generate code to one more Parallel , where in 1st seq. we will use passthrough(), then in second seq we will send it to explain 

seq2 = RunnableParallel(
    {"code": RunnablePassthrough(), #it will return same input it got, exact as output
     "explanation": explain_prompt | model | parser
    }
)


#to invoke both sequence
chain = seq | seq2



# chain.invoke() will take input of "seq", "seq" is taking input of code_prompt (and inside it {topic} is written ), so we will give input i.e {topic}
result = chain.invoke({"topic": "please write a code of palindrome in python" })

 #so it will produce to code 
print(result['code'])
print(result['explanation'])


#_________________________________________________________________________________________________________________________________________________________
#OUTPUT >> 


# Here's a Python function to check if a string is a palindrome (reads the same forwards and backwards):

# ```python
# def is_palindrome(s):
#     # Remove non-alphanumeric characters and convert to lowercase
#     cleaned = ''.join(c for c in s if c.isalnum()).lower()
#     # Compare the cleaned string with its reverse
#     return cleaned == cleaned[::-1]

# # Example usage
# input_string = "A man, a plan, a canal: Panama"
# if is_palindrome(input_string):
#     print(f"'{input_string}' is a palindrome")
# else:
#     print(f"'{input_string}' is not a palindrome")
# ```

# ### Explanation:
# 1. **Cleaning the string**: The function first removes all non-alphanumeric characters (like spaces, punctuation) and converts the string to lowercase to make the comparison case-insensitive.
# 2. **Checking palindrome**: The cleaned string is compared with its reverse (`cleaned[::-1]`). If they match, it's a palindrome.

# ### Example Output:
# For the input `"A man, a plan, a canal: Panama"`, the output will be:
# ```
# 'A man, a plan, a canal: Panama' is a palindrome
# ```

# ### Alternative (Simpler Version):
# If you don't need to handle spaces or punctuation, you can simplify it:
# ```python
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]

# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False
# ```
# ### Simple Explanation of the Palindrome Checker Code:

# #### **What does the code do?**
# This Python function checks if a given string is a palindrome (a word or phrase that reads the same forwards and backwards, like "madam" or "racecar").

# ---

# ### **How does it work?**
# 1. **Cleaning the string:**
#    - The function first removes all non-alphanumeric characters (like spaces, commas, colons) using:
#      ```python
#      cleaned = ''.join(c for c in s if c.isalnum()).lower()
#      ```
#      - `c.isalnum()` checks if a character is a letter or a number.
#      - `.lower()` converts the string to lowercase to make the check case-insensitive.
#    - Example:
#      Input: `"A man, a plan, a canal: Panama"`
#      Cleaned: `"amanaplanacanalpanama"` (all lowercase, no punctuation).

# 2. **Checking if it's a palindrome:**
#    - The cleaned string is compared with its reverse (`cleaned[::-1]`).
#    - `[::-1]` is Python's way of reversing a string.
#    - If they match, it's a palindrome!

# ---

# ### **Example Breakdown:**
# - **Input:** `"A man, a plan, a canal: Panama"`
#   1. Cleaned version: `"amanaplanacanalpanama"`
#   2. Reversed: `"amanaplanacanalpanama"`
#   3. Since they match → **Palindrome!**

# - **Input:** `"hello"`
#   1. Cleaned: `"hello"`
#   2. Reversed: `"olleh"`
#   3. They don’t match → **Not a palindrome.**

# ---

# ### **Simpler Version (No Punctuation Handling):**
# If you don’t need to worry about spaces or punctuation, you can simplify it:
# ```python
# def is_palindrome(s):
#     s = s.lower()  # Convert to lowercase
#     return s == s[::-1]  # Check if it matches its reverse

# print(is_palindrome("RaceCar"))  # True (because it becomes "racecar")
# print(is_palindrome("Python"))   # False
# ```

# ---

# ### **Key Takeaways:**
# 1. The function first cleans the string (removes junk and makes it lowercase).
# 2. Then it checks if the cleaned string reads the same forwards and backwards.
# 3. The `[::-1]` trick is a quick way to reverse a string in Python.

# Would you like any part explained further? 😊
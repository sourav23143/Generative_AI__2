from dotenv import load_dotenv
load_dotenv()



from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# HuggingFaceEndpoint >> through this we retrive the model from HuggingFace Hub and then we can use it in ChatHuggingFace class to
# ChatHuggingFace >>  create a chat model.

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    # temperature=0.7,
    # max_length=1024,
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("who are you ?")
print(response.content)  # to print clean text output without noise and other data



#we can't use it for unlimted time as we are currently using  servers of hugging face and free plan of HuggingFace Hub. So, we can use it for limited time and after that we have to use paid plan of HuggingFace Hub
#    to use it for unlimited time >> we can use it locally.
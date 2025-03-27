from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question bellow.

Here is the conversaion history:{context}

Question: {question}

Answer:

"""

model = OllamaLLM(model="deepseek-r1:7b") # model=your-installed-model
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversaion():
    context = ""
    print("Welcome to the Ai Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context":context, "question":user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"
        
if __name__ == "__main__":
    handle_conversaion()
#this error is because its telliing me to install the following, however since i am running this bot on a VM i dont need to install anything becuase everything that i need is already installed on the VM

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}
Qestion: {question}

Answer:
"""

model = OllamaLLM(model= "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model




def handle_conversation():
    context = ""
    print ("Welcome to the AI Chatbot! Type 'exit' to quit.")

    while True:
        userinput = input("You: ")
        if userinput.lower() == "exit":
            break

        result = chain.invoke({"context":context, "question": userinput})
        print("Bot:", result)

        context += f"\nUser: {userinput}\nAI: {result}"

    

if __name__ == "__main__":
    handle_conversation()






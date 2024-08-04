from langchain_ollama import ChatOllama

model = ChatOllama(model='llama3.1:8b')

file_content = open('./output/whisper.txt', 'r')

prompt = file_content.read()
print('\n',prompt)
output = model.invoke(prompt)

print(output)
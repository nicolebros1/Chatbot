from openai import OpenAI
client = OpenAI(
api_key = "private",
)
#openai.api_key = APIKey

def SendMessage(message, messageList=[]):
    messageList.append(
        {"role":"user","content":message}
    )
    Answer = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messageList,
    )
    return Answer["choices"][0]["message"]
messageList = []
while True:
    text = input("Vamos conversar? escreva sua mensagem ou digite exit para sair ")
    if text == "exit":
        break
    else:
        Answer = SendMessage(text,messageList)
        messageList.append(Answer)
        print ("Bot", Answer["content"])

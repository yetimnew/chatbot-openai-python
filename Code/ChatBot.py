# Importing Bot Definition

from BotDefinition import OpenAIBot

'''Choose whichever model you want to use'''
# engine = "gpt-3.5-turbo"
# engine = "gpt-4o"
engine = "gpt-4o-mini"

'''
Creating the ChatBot
Each Object of "OpenAIBot(engine)" will retain the conversation history and context unless the session is terminated
'''

chatbot = OpenAIBot(engine)

while True:
    # Get Prompt from User
    prompt = input()
    # User can stop the chat by sending 'End Chat' as a Prompt
    if prompt.lower() == 'END CHAT':
        break
    # Generate and Print the Response from ChatBot
    response = chatbot.generate_response(prompt)
    print(response)
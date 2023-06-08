import openai
API_KEY = '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'
openai.api_key = API_KEY
model_id = 'gpt-3.5-turbo'

def chatgpt_conversation(conversation_log):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation_log
    )

    conversation_log.append({
        'role': response.choices[0].message.role, 
        'content': response.choices[0].message.content.strip()
    })
    return conversation_log

conversations = []
# system, user, assistant
conversations.append({'role': 'system', 'content': 'You are a computer science Genius, when the user enters some topic please provide at least a 200 word response summarizing that topic to the best of your example, use python examples if necessary '})
conversations = chatgpt_conversation(conversations)
print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))

while True:
    prompt = input('User: ')
    conversations.append({'role': 'user', 'content': prompt})
    conversations = chatgpt_conversation(conversations)
    print()
    print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))
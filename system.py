import json

# The new system message
new_message = "Welcome! I'm your AI assistant, designed to provide you with information about the web development company, Van-Ons. Whether you're interested in our projects, our team, our services, or our company policies, I'm here to help. I'm regularly updated with the latest information, ensuring you receive the most current and accurate details. Feel free to ask me anything about Van-Ons operations - I'm here to assist you!"

# Open the JSONL file and load each line as a JSON object
with open('data2.jsonl', 'r') as f:
    lines = f.readlines()

# Change the system message for each line
for i in range(len(lines)):
    json_obj = json.loads(lines[i])
    if 'messages' in json_obj:
        for message in json_obj['messages']:
            if message['role'] == 'system':
                message['content'] = new_message
    lines[i] = json.dumps(json_obj)

# Write the modified lines back to the file
with open('data2.jsonl', 'w') as f:
    f.write('\n'.join(lines))
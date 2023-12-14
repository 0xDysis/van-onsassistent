import json

# Load your JSON data
with open('van-onsdataset.json', 'r') as f:
    data = json.load(f)

# Extract the system message
system_message = next(message for message in data['messages'] if message['role'] == 'system')

# Initialize a list to hold the new JSON objects
new_data = []

# Iterate over the messages in pairs (user, assistant)
for i in range(1, len(data['messages']), 2):
    # Check if there is an assistant message for the current user message
    if i+1 < len(data['messages']):
        # Create a new JSON object for each user-assistant pair
        new_object = {
            'messages': [
                system_message,
                data['messages'][i],
                data['messages'][i+1]
            ]
        }
        new_data.append(new_object)

# Write each new JSON object to a new line in a .jsonl file
with open('data.jsonl', 'w') as f:
    for entry in new_data:
        json.dump(entry, f)
        f.write('\n')


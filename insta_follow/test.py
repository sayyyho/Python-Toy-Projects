import json

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_path = './followers_1.json' # 절대 경로로 수정해야 됨
dictionary_data = load_json_file(file_path)

follower = []
for temp in dictionary_data:
    follower.append(temp['string_list_data'][0]['value'])


file_path = './following.json' # 절대 경로로 수정해야 됨
dictionary_data = load_json_file(file_path)

following = []
dictionary_data = dictionary_data['relationships_following']
for temp in dictionary_data:
    following.append(temp['string_list_data'][0]['value'])

# print(follower)
# print(len(follower))
# print()
# print(following)
# print(len(following))
print("-------맞팔X-------")
for temp in following:
    if not temp in follower:
        print(temp)
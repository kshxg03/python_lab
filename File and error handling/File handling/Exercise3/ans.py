

# std_info = {
#     "9843": {"name": "Rabindra", "age": 30, "course": "Python"}, 
#     "9844": {"name": "Hari", "age": 25, "course": "Java"}, 
#     "9845": {"name": "Rex", "age": 26, "course": "Java"}, 
#     "9846": {"name": "Mark", "age": 22, "course": "JavaScript"}, 
#     "9847": {"name": "Anthony", "age": 21, "course": "Python"}
#     }

import json

# with open("info.json", "w") as file_obj:
# 	json.dump(std_info, file_obj, indent=4)
	
# # Rewrite as phone info is missing
# with open("info.json", "r") as file_obj:
# 	data = json.load(file_obj)
# 	data = list(data.values())

# import csv
# with open("info.csv", "w", newline="") as file_obj:
#     fieldnames = ["name", "age", "course"]
#     writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerows(data)
	
with open(r"C:\Users\Kshitiz\OneDrive\Documents\Downloads/election_result.json",  "r", encoding="utf-8") as file_obj:
	data = json.load(file_obj)

# winner = ""
# winner_vote = 0
	
# for candidate_result in data:
# 	vote_received = candidate_result['TotalVoteReceived']
# 	if vote_received > winner_vote:
# 		winner_vote = vote_received
# 		winner = candidate_result["CandidateName"]

# print(winner)


total_vote = 0

for candidate_result in data:
	vote_received = candidate_result['TotalVoteReceived']
	total_vote += vote_received

print(total_vote)
average_vote = total_vote/len(data)
print(average_vote)

import csv
with open('output.csv', 'w', newline='') as f:
    if data:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


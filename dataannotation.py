import csv

# Task 0: Read the data into an appropriate structure
with open('temperature.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader) # skip the first line
    data = []
    for row in reader:
        data.append([row[0].strip(), int(row[1].strip()), int(row[2].strip()), int(row[3].strip()), int(row[4].strip()), int(row[5].strip())])

# Task 1: Show the number of states won by the Republican candidates (Trump / Pence)
republican_states = 0
for row in data:
    if row[3] > row[2]:
        republican_states += 1
print(f"The number of states won by the Republican candidates (Trump / Pence) is **{republican_states}**.")

# Task 2: Show the number of states won by the Democratic candidates (Biden / Harris)
democratic_states = 0
for row in data:
    if row[2] > row[3]:
        democratic_states += 1
print(f"The number of states won by the Democratic candidates (Biden / Harris) is **{democratic_states}**.")

# Task 3: Print the names of the states where split voting was detected
split_voting_states = []
for row in data:
    if row[2] > 0 and row[3] > 0:
        split_voting_states.append(row[0])
if len(split_voting_states) > 0:
    print(f"The names of the states where split voting was detected are: **{', '.join(sorted(split_voting_states))}**.")
else:
    print("No split voting detected.")

# Task 4: List all of the states, one name per line, that were won by the Republican party, sorted in ascending alphabetical order by the state name
republican_winning_states = []
for row in data:
    if row[3] > row[2]:
        republican_winning_states.append(row[0])
if len(republican_winning_states) > 0:
    print(f"The states won by the Republican party, sorted in ascending alphabetical order by the state name are:")
    for state in sorted(republican_winning_states):
        print(f"**{state}**")
else:
    print("No states won by the Republican party.")

# Task 5: List all of the states, one name per line, that were won by the Democratic party, sorted in ascending alphabetical order by the state name
democratic_winning_states = []
for row in data:
    if row[2] > row[3]:
        democratic_winning_states.append(row[0])
if len(democratic_winning_states) > 0:
    print(f"The states won by the Democratic party, sorted in ascending alphabetical order by the state name are:")
    for state in sorted(democratic_winning_states):
        print(f"**{state}**")
else:
    print("No states won by the Democratic party.")

# Task 6: Print the average number of Electoral College votes a state has, to two decimal places
total_votes = 0
for row in data:
    total_votes += row[1]
average_votes = total_votes / len(data)
print(f"The average number of Electoral College votes a state has is **${average_votes:.2f}** to two decimal places.")



# with open("Election2020Results.txt", "r") as file:
#     next(file)
#     data = []
#     for row in file:
#         data.append([row[0].strip(), int(row[1].strip()), int(row[2].strip()), int(row[3].strip()), int(row[4].strip()), int(row[5].strip())])

    
#     republicans = 0
#     for row in data:
#         if row[3]  > row[2] :
#             republicans += 1
#     print(f"NUMBER OF REPUBLICAN STATES: {republicans}" )
    
    
#     democrats = 0
#     for row in data:
#         if row[2] > row[3]:
#             democrats += 1
#     print (f"NUMBER OF DEMOCRATIC STATES: {democrats}" )
    
#     splits = []
#     for row in data:
#         if row[3] > 0 and row[2] > 0:
#             splits.append(row[0])
#     if len(splits) > 0:
#         print(f"STATES WITH SPLIT VOTES: {sorted(splits)}" )
        
#     republican_states = []
#     for row in data:
#         if row[3] > row[2]:
#             republican_states.append(sorted(row[0]))
#     print(f"REPUBLICAN STATE LIST: \n {republican_states}" )
    
#     democartic_states = []
#     for row in data:
#         if row[2] > row[3]:
#             democartic_states.append(sorted(row[0]))
#     print(f"DEMOCRATIC STATE LIST:\n {democartic_states}" )
    
#     total = 0
#     for row in data:
#         total += row[1]
#     average = total / len(data)
#     print(f"AVERAGE ELECTORALVOTES PER STATE: \n {average}" )
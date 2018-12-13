import os
import csv

csvpath = os.path.join("election_data.csv")
def PollData():
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvheader = next(csvreader)
        #declare varibles
        votes = 0
        candidates = []
        county = []
        candidate_list = []
        candidate_votes = {}
        for row in csvreader:
            votes += 1
            candidates.append(row[2])
            county.append(row[1])
        for x in candidates:
            if x not in candidate_list:
                candidate_list.append(x)
            else:
                continue
        print("Election Results")
        print("------------------")
        print(("Total Votes: ") + str(votes))
        print("------------------")
        for x in candidate_list:
            print((x) + ":" + str(round(candidates.count(x) / votes * 100, 2)) + "% "+ ", (" + str(candidates.count(x)) + ")")
        print("------------------")
        print("Winner: " + max(set(candidates), key=candidates.count))
        print("------------------")

with open(output_file, 'w', newline="") as datafile:
    datafile.write(output)
voting_data = [{"county":"Arapahoe" , "registered_voters": 422829} , {"county":"Denver" , "registered_voters": 463353}, {"county":"Jefferson" , "registered_voters": 432438}]

for counties_dict in voting_data:
    for i in counties_dict.values("county") and j in counties_dict.values(registered_voters):
        print(f" {i} county has {j: ,} registered voters.")
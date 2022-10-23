voting_data = [{"county" : "Arapahoe" , "registered_voters" : 422829},
                {"county" : "Denver" , "registered_voters" : 463353}, 
                {"county" : "Jefferson" , "registered_voters" : 432438}]

#prints full dictionary
for county_dict in voting_data:
    print(county_dict)

#uses range to extract county data
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

#nested for loop to extract county and voter count
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


#used to retrieve the number of registed voters for each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#used to retrieve the counties in each dictionary
for county_dict in voting_data:
    print(county_dict['county'])


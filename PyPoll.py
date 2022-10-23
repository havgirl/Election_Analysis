# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total numer of votes each candidate won
# 5. The winner of the elction based on popular vote

#Add our dependencies
import csv

import os

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file. file_variable = open(filename, mode) --> mode is a string specifying the mode for reading or writing the file object
# "r" = read, "w" = open a file to write it, "x" exclusive creation, "a" append data to an existing file, "+" reading/writing
#with open(file_to_load) as election_data:

    # To do: perform analysis/ Print the file object
    #print(election_data)

# Initialize a total vot counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
# Use the open statement to open the file as text file.
#outfile = open(file_to_save, "w")
# Use the with statment to open the file as a text file. (This allows us to save the data without .close() the file)
#with open(file_to_save, "w") as txt_file:
# OR, open the election results and read the file.
with open(file_to_load) as election_data:


    # Write some data to the file.
    #outfile.write("Hello World!")
    # OR
    #txt_file.write("Hello World!")

# Close the file.
#outfile.close()

    # Write three counties to the file.
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")
    # OR
    #txt_file.write(" Arapahoe, Denver, Jefferson")
    # OR
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
    #   print(row)

    # Print the header row.
    #headers = next(file_reader)
    #print(headers)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

    # Print the candidate name for each row.
        candidate_name = row[2]

    # If the candidate does not match any existing candidate....
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

        # Begin tracking that candidates' vote count.
            candidate_votes[candidate_name] = 0 

    # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.

# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calcualate the percentage of votes.
    vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")   

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and Winning_percentage = 
        # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    
    # To do: print out the winning candidate, vote count and %
    #print(f"{candidate_name}, {vote_percentage: .1f}% ({votes:,})\n")
    print(f"{candidate_name}; {vote_percentage:.1f}% ({votes:,})\n")
    
winning_candidate_summary = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n")    
print(winning_candidate_summary)

# Print the candidate list.
#print(candidate_options)

# Print the candidate vote dictionary.
#print(candidate_votes)

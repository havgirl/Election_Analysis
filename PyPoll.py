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
    headers = next(file_reader)
    print(headers)



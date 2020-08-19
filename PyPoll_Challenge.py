import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = '/Users/kathleenphan/Desktop/BOOTCAMP/election-analysis/Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Counties List
counties = []
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the rows
    headers = next(file_reader)
    # Print the candidate name from each row.
    County = row[2]
    Vote = row[3]

# Print the candidate list.
print(counties)

# Counties Dictionary
counties_dict = {}
dict_keys([County])
dict_values([Vote])
counties_dict

most_county = ""
most_county = 0
county_percent = 0



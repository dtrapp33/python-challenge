import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# First column is the animal type and the second column is the name of the animal

# We want to count how many of each type of animal we have at the zoo. We actually don't care 
# what the names of each of the animals are, just how many of each type we have.

# Create an empty dictionary to hold the animals and their counts
candidates = {}
print('Election Results')
print('-----------')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    total_candidates = 0
    for row in csvreader:
        
        total_candidates += 1
        # If the animal type is already in the dictionary, increment the count else 
        # add the animal type to the dictionary
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
            
# Print the contents of the dictionary, the keys are the animals and the values are the counts
# Here's an example of how to loop through a dictionary and print out the contents   
#for key, value in candidates.items():
     
    print(f'Total Votes:  {total_candidates}')
    
print('\n')
Output_path = os.path.join('Output', 'election_results.txt')
with open(Output_path,"w") as output_file:  
# Or maybe we want to print out like this with the percentage of the total

    print('-----------')
    most_candidate = 0
    most_candidate_type = ''
    for key, value in candidates.items():
        print(f'{key}: {round(value/total_candidates*100,2)}% {(value)}')   
        if value > most_candidate:
            most_candidate = value
            most_candidate_type = key
    print('-----------')   
    print(f'\n Winner {most_candidate_type}')

    output_text=(
    f'Election Results\n'
    f'----------------------\n'
    f'Total Votes:   {str(total_candidates)}\n'
    f'----------------------\n'
    f'{key}: {round(value/total_candidates*100,2)}% {(value)}\n'
    f'----------------------\n'
    f'Winner: {most_candidate_type}\n'
    )
    print(output_text)

    Output_path = os.path.join('Output', 'election_results.txt')


    # Method 2: Improved Reading using CSV module

    with open(Output_path,"w") as output_file:
        output_file.write(output_text)
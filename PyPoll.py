#  The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes 
# 3. A percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote. 

# Assign a variable for the file to load and the path.
from isort import file

import csv
import os 

# assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open (file_to_load) as election_data:
    # to do: perform analysis
    print(election_data)
    

    # to do read and analyze the data here

    # read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)



# use the open statement to open the files as a text file.
outfile= open(file_to_save,'w')
# write some data to the file
outfile.write("Hello World")
# close the file 
outfile.close()

# create a filename variable to a direct or indirect path to the file. 
file_to_save=os.path.join("analysis", "election_analysis.txt")

# using the with statement open the file as a text file.
with open (file_to_save,"w") as txt_file:
    # write some data to add to the file
    txt_file.write("Counties in the Election")
    txt_file.write("\n----------------------")
    txt_file.write("\nArapahoe ")
    txt_file.write("\nDenver ")
    txt_file.write("\nJefferson ")
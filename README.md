# Election_Analysis

## **Overview** ##
Tom, a Colorado Board of Elections employee, has asked for assistance with an audit of results of their Congressional election. The audit was performed on all ballot types after their initial count was tabulated. This project called for the following:

Form a complete list of all candidates who were voted for

Calculate the total votes cast

Calculate the total number of votes each candidate received

Calculate the percentage of votes each candidate received

Confirm the winner based on the popular vote 

# **Resources** #
-Data Source: election_analysis.csv
-Software: Python 3.6.1, Visual Staudio Code 1.38.1

# **Summary** #

The **Candidates** were: Charles Casper Stockham, Dianna DeGetter, and Raymon Anthony Doane. This was achieved by using the 
print function which printed every time the candidates name was present in the file. To get it to 1 occurence for each candidate, we then utilized an 'if' statment to iterate through the data and print every name one time only. 

The **Total Votes** were 369,711. This was calulated using an f' string to define and print our variable "election results"

**Charles Casper Stockham** recieved 23.0% of the votes with a total vote count of 85,213

**Diana DeGette** received 73.8% of the votes with a total vote count of 272,892

**Raymon Anthony Doane** received 3.1% of the votes with a total vote count of 11,606

These figutres were obtained by first setting count for each candidate to zero and every occurence of the candidates name was tallied by adding '1' each time. The percentage was then found by using an equation that divided the candidates votes by the total number of votes and multilpying by 100.




# **Challenge Overview** #

# **Challenge Summary** #


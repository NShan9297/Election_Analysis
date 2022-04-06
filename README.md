# Election_Analysis

## **Overview** ##
Tom, a Colorado Board of Elections employee, has asked for assistance with an audit of results of their Congressional election. The audit was performed on all ballot types after their initial count was tabulated. This project called for the following:

- Form a complete list of all candidates who were voted for

- Calculate the total votes cast

- Calculate the total number of votes each candidate received

- Calculate the percentage of votes each candidate received

- Confirm the winner based on the popular vote 

# **Resources** #
-Data Source: election_analysis.csv

-Software: Python 3.6.1, Visual Staudio Code 1.38.1


# **Election-Audit Results** #

- The **Total Votes** cast were 369,711.

- This was calculated using an f' string to define and print our variable "election results"

- The Total Vote count of  369,711 was broken down by the counties in their precinct:


    **County Votes:**

    Jefferson: 10.5% (38,855 total votes)

    Denver: 82.8% (306,055 total votes)

    Arapahoe: 6.7% (24,801 total votes)

    With the largest County Turnout (number of votes) seen in Denver
    
  
- The candidates were obtained by using the print function which printed every time the candidates name was present in the file. To get it to 1 occurrence for each candidate, we then utilized an 'if' statment to iterate through the data and print every name one time only. 


- The breakdown of the number of votes and the percentage of the total votes each candidate received:

     **Charles Casper Stockham** recieved 23.0% of the votes with a total vote count of 85,213

     **Diana DeGette** received 73.8% of the votes with a total vote count of 272,892

     **Raymon Anthony Doane** received 3.1% of the votes with a total vote count of 11,606
     

- These figures were obtained by first setting count for each candidate to zero and every occurrence of the candidates name was tallied by adding '1' each time. The percentage was then found by using an equation that divided the candidates votes by the total number of votes and multiplying by 100.
 

- The winning candidate was Diana DeGette with 73.8% of votes with a total is 272,892



# **Election-Audit Summary** #

The script used for this election audit can be used for any election! We know this because the same general formulas were used to calculate the county and the candidate results. This proves the versatility and reliability of the script. This was achieved by some simple modifications of defined variables, i.e. candidate votes vs. county votes. Another modification that could be made to this script is the number of variables being calculated in one script. Providing more versatility. All percentages, total votes, and winning county/candidates were all performed on the same page. The script allows for all items to be calculated by the computer in one page of script. This will diminish the likelihood of human error as well as provide convenience. 


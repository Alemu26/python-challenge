# Importing pandas library
import pandas as pd

def readcsv():
    print("Reading election csv file")
    # Load the data of csv
    df = pd.read_csv('./Resources/election_data.csv')   
    # Print result to console
    print(df)    
    writeResult(df)
    # writeResultUsingIteration(df)
    
def percentage(num, total):
    percent = 100 * float(num)/float(total)
    return "{0:.3f}%".format(percent)

def writeResult(df): 
    with open('./Resources/analysis/result.txt', 'w') as file:       
        totalVotes = df.shape[0]
        totalVotesStr = "Total Vote: " + str(totalVotes)   
        # group by candidates by name and count ballot                  
        candidates = df.groupby(['Candidate']).size().reset_index(name='Count')
        
        for ind in candidates.index:
            voteCount = candidates['Count'][ind]
            candidateName = candidates['Candidate'][ind]
            result = "%s : %s (%s)\n" % (candidateName, percentage(voteCount, totalVotes), voteCount)
            print(result)
    
        charlesVotes = candidates._get_value(0, 'Count')        
        dianaVotes = candidates._get_value(1, 'Count')
        raymonVotes = candidates._get_value(2, 'Count')
        #Get winner index        
        winnerIndex = candidates['Count'].idxmax()
        
        candidate1 = "Charles Casper Stockham: %s (%s)\n" % (percentage(charlesVotes, totalVotes), charlesVotes)
        candidate2 = "Diana DeGette:%s (%s)\n" % (percentage(dianaVotes, totalVotes), dianaVotes)
        candidate3 = "Raymon Anthony Doane:%s (%s)\n" % (percentage(raymonVotes, totalVotes), raymonVotes)
        winner="Winner: %s" % candidates._get_value(winnerIndex, 'Candidate')
        # Print result to console
        print(totalVotesStr)          
        print(candidate1)
        print(candidate2)
        print(candidate3)
        print(winner)
        
        # Write result to file
        file.write("Election Results\n")
        file.write('------------------------------\n') 
        file.write(totalVotesStr)        
        file.write('\n----------------------------\n')   
        file.write(candidate1)
        file.write(candidate2)
        file.write(candidate3) 
        file.write('\n----------------------------\n')
        file.write(winner)
        file.write('\n-----------------------------')


# result using for loop
def writeResultUsingIteration(df): 
    with open('./Resources/analysis/result.txt', 'w') as file:       
        totalVotes = df.shape[0]
        totalVotesStr = "Total Vote: " + str(totalVotes)   
        # group by candidates by name and count ballot                  
        candidates = df.groupby(['Candidate']).size().reset_index(name='Count')
        # Write result to file
        file.write("Election Results\n")
        file.write('------------------------------\n') 
        file.write(totalVotesStr)        
        file.write('\n----------------------------\n')  
        
        for ind in candidates.index:
            voteCount = candidates['Count'][ind]
            candidateName = candidates['Candidate'][ind]
            result = "%s : %s (%s)\n" % (candidateName, percentage(voteCount, totalVotes), voteCount)
            print(result)
            file.write(result)
            
        #Get winner index        
        winnerIndex = candidates['Count'].idxmax()        
        winner="Winner: %s" % candidates._get_value(winnerIndex, 'Candidate')       
        print(winner)        
        file.write('\n----------------------------\n')
        file.write(winner)
        file.write('\n-----------------------------')
        
def main():
    print("Inside PyPoll main function")
    readcsv()

if __name__ == "__main__":
    main()
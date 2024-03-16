# Importing pandas library
import pandas as pd

def readcsv():
    print("Reading budget csv file")
    # Load the data of csv
    df = pd.read_csv('./Resources/budget_data.csv')
    # display all rows in csv file
    pd.set_option('display.max_rows', None)
    # Print result to console
    print(df)    
    writeResult(df)
   
def writeResult(df): 
    with open('./Resources/analysis/result.txt', 'w') as file:       
        file.write("Financial Analysis\n")
        file.write('------------------------\n')
        rowCount = "Total Months: " + df.shape[0].__str__()                    
        file.write(rowCount) 
        #get Profit/Loses column
        profit=df['Profit/Losses']

        total='\nTotal: $' + profit.sum().__str__()
        average='\nAverage Change: $' + profit.mean().__str__()         
        maxIndex = df['Profit/Losses'].idxmax()
        minIndex = df['Profit/Losses'].idxmin()
        maxProfit='\nGreatest Increase in Profits: ' + df._get_value(maxIndex, 'Date') + ' ($' + profit.max().__str__() + ')'
        minProfit='\nGreatest Decrease in Profits: ' + df._get_value(minIndex, 'Date') + ' ($' + profit.min().__str__() + ')'
        
        file.write(total)
        file.write(average)
        file.write(maxProfit) 
        file.write(minProfit) 
        
        print(total)
        print(average)     
        print(maxProfit)
        print(minProfit)        
        #print('\nGreatest Increase in Profits: ' + df._get_value(minIndex, 'Date') + ' ($' + profit.min().__str__() + ')')
    

def main():
    print("Inside PyBank main function")
    readcsv()

if __name__ == "__main__":
    main()
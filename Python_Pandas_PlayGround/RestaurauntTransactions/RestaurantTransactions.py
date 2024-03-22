import pandas as pd

# YOUR CODE HERE
def getCategory(time):
    """
      Takes time frames and categorizes them.

        Args:
        time(str) = the hour str(ex. "00:00") from the time stamp


        Return:
         a string value with name of the category(ex. Breakfast, Lunch, etc).
    """ 
    
    hour = int(time.split(":")[0])
    if hour <= 10:
        return "breakfast"
    elif 10 < hour < 12:
        return "preLunch"
    elif 12 <= hour < 15:
        return "lunch"
    elif 15 <= hour < 18:
        return "postLunch"
    elif 18 <= hour < 20:
        return "dinner"
    else:
        return "lateDinner"
def restaurant_transactions_by_time_day(filename):
    """
    Creates a column titled "Time_Category" that classifies each transaction based on the hour in the "Time" column.
    
    Args:
    filename(csv file): The path to the csv file containing restauraunt transactions
    
    
    Return:
    A pandas.DataFrame grouped with a new column Time category and the original Item column 
    """
    
     # YOUR CODE HERE
    df = pd.read_csv(filename)
    df['Time_Category'] = df['Time'].apply(getCategory)


# Function to get the mode of 'Item' for each group
    def get_mode(series):
        """
        Gets the most frequent item in the series.

        Args:
        Series(pandas.Series):a series containing items


        Return:
            str: the most frequent item in the series.
        """

        return series.mode().iloc[0]
       
    

# Group by 'Time_Category' and calculate the mode for 'Item'
    result_df = df.groupby('Time_Category')['Item'].agg(get_mode).reset_index(name="item")
    

# Display the result
    return result_df

# example inputs
# fn = "BreadBasket_DMS.csv"
# my_restaurant_df = restaurant_transactions_by_time_day(fn)
# my_restaurant_df
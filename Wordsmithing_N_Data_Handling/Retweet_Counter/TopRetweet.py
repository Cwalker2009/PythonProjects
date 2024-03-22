def topRetweets(tweets_file_name):
    """
    Identifies the Twitter user with the most retweets in given file and returns a dictionary containing the username
    and the corresponding retweet count.
    
    Args:
    tweets_file_name(str): The path to the file containing the tweets.
    
    returns:
        retweet_dict : A dictionary with the username of the most retweeteduser and the corresponding retweet count.
    
    
    """
    retweet_dict = {}
    total_tweets = 0
    Num_retweets = 0
    
    with open(tweets_file_name, 'r') as file:
        for line in file:
            total_tweets += 1
            
            if line.startswith("RT @"):
                Num_retweets += 1
                line_as_list = line.split(" ")
                username = line_as_list[1].rstrip(":")
                new_retweets = retweet_dict.get(username, 0) +1
                retweet_dict[username] = new_retweets
    def RemoveNonTopRetweets(Most_RT, RT_Dict):
        """
        Removes all retweets from given dictionary except for the highest retweeted user.

        Args:
        Most_RT(str): The username of the user with the highest retweet count.
        RT_Dict(dictionary): dictionary containing retweet count for each user.

        returns:
             RT_dictionary
    
        """
        
        temp_dict = dict(RT_Dict)
        for retweet in temp_dict:
            if retweet != Most_RT:
                RT_Dict.pop(retweet)
        return RT_Dict
    if Num_retweets :
        most_retweeted_user = max(retweet_dict, key=retweet_dict.get)
        RemoveNonTopRetweets(most_retweeted_user,retweet_dict)
    
    
    
    print(f'There were {total_tweets} tweets in the file, {Num_retweets} of which were retweets')
    return retweet_dict
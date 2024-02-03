class employees(object):
    """This is a constructior which used to call the attirbutes/variables of the object"""
    def __init__(self, name):
        "This is to initialize the constructor"
        self.name = name
        # self._age = age
    
    def get_name(self):
        return self.name
    


employee_data = employees('John')

print(employee_data.get_name())


class tweet(object):
    tweet_text =""
    """Constructor"""
    def __init__(self, text):
        if len(text) > 280:
            self.tweet_text = text[0: 279]
        else:
            self.tweet_text = text

class Tweet(object):
    _tweet_text= ""
    _likes = 0
    _retweets = 0
    _touches = 0

    def __init__(self, text):
        if len(text)> 280:
            self._tweet_text = text[0: 279]
        else: 
            self._tweet_text = text
    
    # def get_tweet(self):
    #     return self._tweet_text
    
    def set_tweet(self, newText):
        self._tweet_text = newText
    
    def total_impressions(self):
        self.__likes + self._retweets + self._touches

    def set_likes(self, likes):
        if likes >= 0:
            self._likes = likes
    
    def set_retweet(self, retweet):
        if retweet >- 0:
            self._retweets = retweet

    def set_touches(self, touches):
        if touches >= 0:
            self._touches = touches
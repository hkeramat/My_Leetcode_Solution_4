class Tweet:
    def __init__(self, message1, message2) :
        self.message_primary = message1
        self.message_secondary = message2



    def generateMessage(self):
        print("{} is better than {} in Leetcode and Math problems".format(self.message_primary,self.message_secondary))



a = Tweet(' Hadi', " everyone")
a.generateMessage()

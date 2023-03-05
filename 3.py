"""

Question 3
Implement the class MessageBox which makes it possible to send
messages between users. It should have the following methods:
● An __init__ method which initializes the state of the object to
contain no messages.

● A method:

def sendMessage(self, sender, receiver, message): ...
which sends a message from the sender to the receiver. The first
two arguments are the user names of the sender and the receiver.
The last argument is the text of the message itself.
● A method:

def readMessages(self, user): ...
returns a list of unread messages sent to the given user name.
Once the method returns the messages, they are all considered
read. A second call to the method should not return them again.
On the other hand, it may return more messages, if sendMessage
was called in the meantime.


An example use of the class:

#>>> box = MessageBox()
#>>> box.sendMessage("john", "mary", "hi")
#>>> box.sendMessage("john", "mary", "going for lunch?")
#>>> box.sendMessage("john", "greg", "did you finish the
book?")
#>>> box.readMessages("mary")
["hi", "going for lunch?"]
#>>> box.readMessages("mary")
[]
#>>> box.sendMessage("john", "mary", "sorry, I will be
late")
#>>> box.readMessages("mary")
["sorry, I will be late"]
#>>> box.readMessages("greg")
["did you finish the book?"]
#>>> box.readMessages("john")
[]

"""

class MessageBox():
    def __init__(self):
        self.messages={}

    def sendMessage(self, sender, receiver, message):
        try:
            # get receivers messages
            self.currentMessages=self.messages[receiver]
        except KeyError: # if the user is not in the dictionary, there's no messages to get
            self.currentMessages=[]
        # add the message to a list of messages they haven't read
        self.currentMessages+=[[sender,message]]
        # set their unread messages to the list of messages
        self.messages[receiver]=self.currentMessages

    def readMessages(self, user):
        unreadMessages=[]
        try:
            for message in self.messages[user]:
                unreadMessages.append(message[1])
            self.messages[user]=[]
        except KeyError:
            pass
        print(unreadMessages)



box = MessageBox()
box.sendMessage("john", "mary", "hi")
box.sendMessage("john", "mary", "going for lunch?")
box.sendMessage("john", "greg", "did you finish the book?")
box.readMessages("mary")
#["hi", "going for lunch?"]
box.readMessages("mary")
#[]
box.sendMessage("john", "mary", "sorry, I will be late")
box.readMessages("mary")
#["sorry, I will be late"]
box.readMessages("greg")
#["did you finish the book?"]
box.readMessages("john")
#[]
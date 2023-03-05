"""

Question 2
The command grep on Unix/Linux can search for a given word in a file.
Implement the function:
def grep(word,file_name,exact_match):
...
which would do the same (but in a simplified way). Here the argument
word is what we are searching for, and the argument file_name tells us
which file to open. The function should print the line numbers and the
lines themselves that contain the given word. When exact_match is
True, the function should look only for words that exactly match the
search word. Otherwise, it also includes words which start with the given
word.
All words in the file are assumed to be separated by spaces, so you can
safely use split() to separate each line to words.
Examples:
#>>> grep("Python","example.txt",True)
1: Python is an interpreted ...
5: Python is dynamically-typed and ...
7: Python is often described as ...
#>>> grep("Python","example.txt",False)
1: Python is an interpreted ...
2: Python's design philosophy ...
5: Python is dynamically-typed and ...
7: Python is often described as ...
(10 points; 7 points if you choose to ignore argument exact_match)

"""

def grep(word,file_name,exact_match):

    # open and read file
    texten=open(file_name)
    readTexten=texten.read()
    texten.close()

    # split text at linebreak
    splitTexten=readTexten.split('\n')
    #print(splitTexten)

    # if exact_match is true
    if exact_match==True:
        # keep track of the line number
        lineNumber=0
        for line in splitTexten:
            # iterate line number
            lineNumber+=1
            # split the line into words
            ordSplit=line.split()
            # iterate through the words in each line
            for ord in ordSplit:
                # if the word exactly matches the current word in line
                if word == ord:
                    # print line number and line
                    print(str(lineNumber) + ": " + str(line))
    elif exact_match==False:
        lineNumber=0
        for line in splitTexten:
            lineNumber+=1
            ordSplit=line.split()
            for ord in ordSplit:
                # same as if exact match is true but with condition
                # if word in the current word instead
                if word in ord:
                    print(str(lineNumber) + ": " + str(line))


grep('python', 'example.txt', False)
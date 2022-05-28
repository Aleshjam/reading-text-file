# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file(filename):
    # [assignment] Add your code here
    with open("C:/Users/ALESHINLOYE/Desktop/project files/python files/Reading-Text-Files/story.txt","r") as open_file:
        read_file = open_file.read()
    return read_file

   



def count_words():
    text = read_file("C:/Users/ALESHINLOYE/Desktop/project files/python files/Reading-Text-Files/story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    count ={}
    for word in split_text:
        if word in count:
            count[word] += 1
        else:
            count[word] =1
    return count



print(count_words())    

   
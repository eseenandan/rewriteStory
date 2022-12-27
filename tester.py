from markov import *

filename1 = input("Enter the filename 1: ")
filename2 = input("Enter the filename 2: ")

head = trigrams(filename1, filename2)
print("The generated story from the file is: readme.txt\n")
main(head)

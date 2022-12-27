import nltk
import random

#a model nltk to hold all the tokens that are generated from the trigrams
model_ntlk = {}
model_ntlk2 = {}
punctuation = (".", "!", "?", ",")

def write_to_file(story):
    readme_file = open("readme.txt", "a")
    for sentence in story:
        readme_file.write(sentence)

    readme_file.close()

def count_spaces(story):
    count = 0
    for i in story:   
        if i == ' ':
            count+=1
    return count
#a function to convert the source file into the trigrams for story generation
def trigrams(filename1, filename2):

    #reading the cleaning the files
    file1 = open(filename1, "r", errors='ignore')
    text1 = file1.read()
    for sentence in text1:
        if sentence in punctuation:
            text1.replace(sentence, ' ')
    file1.close()
    file2 = open(filename2, "r", errors='ignore')
    text2 = file2.read()
    for sentence in text2:
        if sentence in punctuation:
            text2.replace(sentence, ' ')    
    file2.close()
    text = text1 + ' ' + text2
    #the trigrams are created as a list from the source text
    trigrams = list(nltk.trigrams(text.split()))
    bigrams = list(nltk.bigrams(text.split()))

    #the trigrams are placed into the model for later generating the story
    for trigram in trigrams:
        start = trigram[0] + " " + trigram[1]
        tail = trigram[2]
        model_ntlk.setdefault(start, {})
        model_ntlk[start].setdefault(tail, 0)
        model_ntlk[start][tail] += 1

    for bigram in bigrams:
        start = bigram[0]
        tail = trigram[1]
        model_ntlk2.setdefault(start, {})
        model_ntlk2[start].setdefault(tail, 0)
        model_ntlk2[start][tail] += 1

    #finding the probability of the tokens so that we can show those that have the most prob of being used
    probability = []
    probability2 = []
    for key in model_ntlk.keys():
        if key[0].isupper() and not key.split(" ")[0].endswith(punctuation):
            probability.append(key)

    for key in model_ntlk2.keys():
        if key[0].isupper() and not key.split(" ")[0].endswith(punctuation):
            probability2.append(key)

    return max(probability,probability2) 

def main(probability):
    total = 0
    story = ''
    #implementing a way to only get story somewhat above 2k words
    while total < 1900:
        
        tokens = []
        #getting the starting sentence from the high prob
        start = random.choice(probability)
        tokens.append(start)
        while True:
            #checking all the other tokens that match with the current token
            probability_of_tails = list(model_ntlk[start].keys())
            weights = list(model_ntlk[start].values())
            most_tail = random.choices(probability_of_tails, weights, k=1)[0]

            #if punctuation encounterd append and break
            if most_tail.endswith(punctuation):
                tokens.append(most_tail)
                break
            elif not most_tail.endswith(punctuation):
                #else we append the tail into list of words or tokens and split the sentence to words also adding the tail
                tokens.append(most_tail)
                start = start.split(" ")[1] + " " + most_tail
            elif most_probable_tail.endswith(punctuation):
                tokens = []
                #else just append with the most prob and add that to tokens
                start = random.choice(probability)
                tokens.append(start)

        #adding the new line generated to the story
        story = " ".join(tokens)
        total += count_spaces(story)
        write_to_file(story)
    # print(story)

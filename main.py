from wonderwords import RandomSentence
import random, time, string


paragraph=""
paragraph_words=""
star_time=time.time()
input_paragraph=""
input_words=""
error_value=0
correct_value=0
true_words=""

def created_test():
    global paragraph, paragraph_words
    for i in range(1):
        wonder_sentence=RandomSentence()
        random_sentence=wonder_sentence.sentence()
        paragraph+=random_sentence.lower()+" "
    cleaned_paragraph = ''.join(char for char in paragraph if char not in string.punctuation)
    paragraph_words=cleaned_paragraph.split()
    print(paragraph)
    print(paragraph_words)
def check_input_paragraph(paragraph_words, input_paragraph):
    global input_words, error_value, correct_value, true_words
    input_words=input_paragraph.split()
    if len(paragraph_words)==len(input_words):
        for i in range(len(input_words)):
            input_word=input_words[i]
            paragraph_word=paragraph_words[i]
            if len(input_word)==len(paragraph_word):
                for char in range(len(paragraph_word)):
                    if input_word[char]==paragraph_word[char]:
                        correct_value+=1
                    else:
                        error_value+=1
            else:
                print("You entered extra letters. Your error value increased by 3 points :(\n")
                error_value+=3
            i+=1
    else:
        print("You entered extra words. Your error value increased by 10 points :(\n")
        error_value+=10


            



while time.time()-star_time<20:
    created_test()
    input_paragraph=input("Enter the above paragraph.\n!You don't need to care about punctuation marks!\n")
    check_input_paragraph(paragraph_words, input_paragraph)
    print(error_value)
    print(correct_value)
    print(true_words)

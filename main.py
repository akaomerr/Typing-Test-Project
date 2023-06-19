from wonderwords import RandomSentence
import time, string
import tkinter as tk
from termcolor import colored
paragraph=""
paragraph_words=""
star_time=time.time()
input_paragraph=""
input_words=""
error_value=0
correct_value=0
true_words=0
word_per_second=0
paragraph_length=0
colored_letter=""


def created_test():
    global paragraph, paragraph_words
    wonder_sentence=RandomSentence()
    random_sentence=wonder_sentence.sentence()
    paragraph=random_sentence.lower()+" "
    cleaned_paragraph = ''.join(char for char in paragraph if char not in string.punctuation)
    paragraph_words=cleaned_paragraph.split()
    print(paragraph.upper())




def check_input_paragraph(paragraph_words, input_paragraph):
    global input_words, error_value, correct_value, true_words, colored_letter
    colored_letter=""
    input_words=input_paragraph.split()
    if len(paragraph_words)==len(input_words):
        for i in range(len(input_words)):
            input_word=input_words[i]
            paragraph_word=paragraph_words[i]
            if len(input_word)==len(paragraph_word):
                for char in range(len(paragraph_word)):
                    if input_word[char]==paragraph_word[char]:
                        correct_value+=1
                        colored_letter+=" "+colored(input_word[char],"green")
                    else:
                        colored_letter+=" "+colored(input_word[char],"red")
                        error_value+=1
                if input_word==paragraph_word:
                    true_words+=1
            elif len(input_word)>len(paragraph_word):
                print("You entered extra letters. Your error value increased by 2 points per letter :(\n")
                colored_letter+=" "+colored(input_word,"red")
                error_value+=2*(len(input_word)-len(paragraph_word))
            elif len(input_word)<len(paragraph_word):
                print("You entered missing letters. Your error value increased by 2 points per letter :(\n")
                colored_letter+=" "+colored(input_word,"red")
                error_value+=2*(len(paragraph_word)-len(input_word))
            i+=1
        print(colored_letter)
    elif len(paragraph_words)<len(input_words) :
        print("You entered extra words. Sentence is completely wrong :(\n")
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        error_value+=10*(len(input_words)-len(paragraph_words))
    elif len(paragraph_words)>len(input_words) :
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        print("You entered missing words. Sentence is completely wrong :(\n")
        error_value+=10*(len(paragraph_words)-len(input_words))


root=tk.Tk()
root.geometry("1060x700")



while time.time()-star_time<20:
    created_test()
    input_paragraph=input()
    paragraph_length+=len(paragraph)
    check_input_paragraph(paragraph_words, input_paragraph)
    

error_percent=(error_value/(error_value+correct_value))*100
end_time=time.time()
taken_time=end_time-star_time
print(f"error percent: %{round(error_percent,2)}\n")
print(f"correct value: {correct_value}\n")
word_per_second=true_words/taken_time
print(f"true words:{true_words}\n")
print(f"true word per second: {round(word_per_second,2)}\n")




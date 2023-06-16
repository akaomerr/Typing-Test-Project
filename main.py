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

def gui_app():
    global input_paragraph
    root=tk.Tk()
    root.title("Typing Speed Test App")
    root.geometry("900x660")
    tk.Label(root, text=paragraph, compound=tk.CENTER, font=("Arial",30)).grid(row=0, column=0, rowspan=2, columnspan=10, padx=120, pady=60)
    input_paragraph=tk.Entry(root, font=("Arial", 20), width=50)
    input_paragraph.grid(row=2,column=0,columnspan=10, rowspan=2)
    root.mainloop()



def check_input_paragraph(paragraph_words, input_paragraph):
    global input_words, error_value, correct_value, true_words, colored_letter
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
                colored_letter=colored(paragraph,"red")
                error_value+=2*(len(input_word)-len(paragraph_word))
            elif len(input_word)<len(paragraph_word):
                print("You entered missing letters. Your error value increased by 2 points per letter :(\n")
                colored_letter=colored(paragraph,"red")
                error_value+=2*(len(paragraph_word)-len(input_word))
            i+=1
    elif len(paragraph_words)<len(input_words) :
        print("You entered extra words. Your error value increased by 10 points per word :(\n")
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        error_value+=10*(len(input_words)-len(paragraph_words))
    elif len(paragraph_words)>len(input_words) :
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        print("You entered missing words. Your error value increased by 10 points per word :(\n")
        error_value+=10*(len(paragraph_words)-len(input_words))


            
root=tk.Tk()
root.title("Typing Speed Test App")
root.geometry("900x660")

while time.time()-star_time<5:
    created_test()
    tk.Label(root, text=paragraph, compound=tk.CENTER, font=("Arial",30)).grid(row=0, column=0, rowspan=2, columnspan=10, padx=120, pady=60)
    input_paragraph=str(tk.Entry(root, font=("Arial", 20), width=50))
    input_paragraph.grid(row=2,column=0,columnspan=10, rowspan=2)
    paragraph_length+=len(paragraph)
    check_input_paragraph(paragraph_words, input_paragraph)
    print(colored_letter)
    root.mainloop()
    

error_percent=(error_value/paragraph_length)*100
end_time=time.time()
taken_time=end_time-star_time
print(round(error_percent,2))
print(correct_value)
word_per_second=true_words/taken_time
print(true_words)
print(round(word_per_second,2))




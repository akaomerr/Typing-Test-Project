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
                colored_label.config(text="")
                colored_label.config(text="You entered extra letters. Your error value increased by 2 points per letter :(")
                colored_letter+=" "+colored(input_word,"red")
                error_value+=2*(len(input_word)-len(paragraph_word))
            elif len(input_word)<len(paragraph_word):
                colored_label.config(text="")
                colored_label.config(text="You entered missing letters. Your error value increased by 2 points per letter :(")
                colored_letter+=" "+colored(input_word,"red")
                error_value+=2*(len(paragraph_word)-len(input_word))
            i+=1
        print(colored_letter)
    elif len(paragraph_words)<len(input_words) :
        colored_label.config(text="")
        print("You entered extra words. Sentence is completely wrong :(\n")
        colored_label.config(text="You entered extra words. Sentence is completely wrong :(")
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        error_value+=10*(len(input_words)-len(paragraph_words))
    elif len(paragraph_words)>len(input_words) :
        colored_label.config(text="")
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        colored_label.config(text="You entered missing words. Sentence is completely wrong :(")
        error_value+=10*(len(paragraph_words)-len(input_words))






root=tk.Tk()
root.geometry("1200x700")
root.configure(bg="#F5EFE7")

paragraph_label=tk.Label(root, text=paragraph.upper(), font=("Arial",30), fg="#4F709C", bg="#F5EFE7", pady=30)
paragraph_label.grid(row=0, column=0, rowspan=1, columnspan=10, sticky="nsew")

caution_label=tk.Label(root, text="!Do not pay attention to punctuation marks, write hyphenated words together!", font=("Arial", 20), fg="#E55807", pady=30,  bg="#F5EFE7")
caution_label.grid(row=1, column=0, rowspan=1, columnspan=10)

colored_label=tk.Label(root, font=("Arial",15), bg="#F5EFE7", pady=30)
colored_label.grid(row=3, column=0, rowspan=1, columnspan=10, pady=100)

input_sentence=tk.Entry(root, width=100, font=40, justify="center")
input_sentence.grid(row=2, column=0, rowspan=1, columnspan=10, pady=30)
root.columnconfigure(0, weight=1) 




def enter_to_off():
    root.destroy()



def entry_func(event):
    global paragraph_length
    input_paragraph=input_sentence.get()
    check_input_paragraph(paragraph_words, input_paragraph)
    created_test()
    paragraph_length+=len(paragraph)
    paragraph_label.config(text=paragraph.upper())
    input_sentence.delete(0,tk.END)




created_test()
input_sentence.bind("<Return>", entry_func)
paragraph_length+=len(paragraph)
paragraph_label.config(text=paragraph.upper())
root.mainloop()


error_percent=(error_value/(error_value+correct_value))*100
end_time=time.time()
taken_time=end_time-star_time
print(f"error percent: %{round(error_percent,2)}\n")
print(f"correct value: {correct_value}\n")
word_per_second=true_words/taken_time
print(f"true words:{true_words}\n")
print(f"true word per second: {round(word_per_second,2)}\n")






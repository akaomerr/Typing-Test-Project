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
                colored_label.config(text="You entered extra letters. Your error value increased by 2 points per letter :(", fg="red")
                colored_letter+=" "+colored(input_word,"red")
                error_value+=2*(len(input_word)-len(paragraph_word))
            elif len(input_word)<len(paragraph_word):
                colored_label.config(text="")
                colored_label.config(text="You entered missing letters. Your error value increased by 2 points per letter :(", fg="red")
                colored_letter+=" "+colored(input_word,"red")
                error_value+=2*(len(paragraph_word)-len(input_word))
            i+=1
        print(colored_letter)
    elif len(paragraph_words)<len(input_words) :
        colored_label.config(text="")
        print("You entered extra words. Sentence is completely wrong :(\n")
        colored_label.config(text="You entered extra words. Sentence is completely wrong :(", fg="red")
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        error_value+=10*(len(input_words)-len(paragraph_words))
    elif len(paragraph_words)>len(input_words) :
        colored_label.config(text="")
        colored_letter=colored(paragraph,"red")
        print(colored_letter)
        colored_label.config(text="You entered missing words. Sentence is completely wrong :(", fg="red")
        error_value+=10*(len(paragraph_words)-len(input_words))






root=tk.Tk()
root.title("Typing Speed Test")
root.geometry("1200x700")
root.configure(bg="#F5EFE7")
counter=60

paragraph_label=tk.Label(root, text=paragraph.upper(), font=("Arial",30), fg="#4F709C", bg="#F5EFE7", pady=30)
paragraph_label.grid(row=0, column=0, rowspan=1, columnspan=10, sticky="nsew")

timer_label=tk.Label(root, font=("Arial", 20), width=10, bg="#F5EFE7")
timer_label.grid(row=1, column=0, sticky="nsew")


caution_label=tk.Label(root, text="!Do not pay attention to punctuation marks, write hyphenated words together!", font=("Arial", 20), fg="#E55807", pady=30,  bg="#F5EFE7")
caution_label.grid(row=2, column=0, rowspan=1, columnspan=10)

colored_label=tk.Label(root, font=("Arial",15), bg="#F5EFE7")
colored_label.grid(row=4, column=0, rowspan=1, columnspan=10, pady=20)

input_sentence=tk.Entry(root, width=100, font=40, justify="center")
input_sentence.grid(row=3, column=0, rowspan=1, columnspan=10, pady=30)
root.columnconfigure(0, weight=1) 

look_up_label=tk.Label(root, font=("Arial",20), bg="#F5EFE7", pady=20)
look_up_label.grid(row=5, column=0)








def entry_func(event):
    global paragraph_length
    input_paragraph=input_sentence.get()
    check_input_paragraph(paragraph_words, input_paragraph)
    created_test()
    paragraph_length+=len(paragraph)
    paragraph_label.config(text=paragraph.upper())
    input_sentence.delete(0,tk.END)
    error_percent=(error_value/(error_value+correct_value))*100
    end_time=time.time()
    taken_time=end_time-star_time
    word_per_second=true_words/taken_time

def button_clicked():
    look_up_label.grid_remove()
    timer_label.grid_remove()
    global paragraph_length
    paragraph_length+=len(paragraph)
    paragraph_label.config(text=paragraph.upper())
    input_sentence.delete(0,tk.END)
    error_percent=(error_value/(error_value+correct_value))*100
    end_time=time.time()
    taken_time=end_time-star_time
    word_per_second=true_words/taken_time
    error_label=tk.Label(root, font=("Arial",20), bg="#F5EFE7", pady=20, text=f"Error Percent: %{round(error_percent,2)}", fg="#F45050")
    error_label.grid(row=5, column=0, pady=20)
    correct_label=tk.Label(root, font=("Arial",20), bg="#F5EFE7", pady=20, text=f"Correct Point: {correct_value}", fg="#1F8A70")
    correct_label.grid(row=6, column=0, pady=20)
    true_words_label=tk.Label(root, font=("Arial",20), bg="#F5EFE7", pady=20, text=f"True Words Value: {true_words}", fg="#1F8A70")
    true_words_label.grid(row=7, column=0, pady=20)
    word_per_second_label=tk.Label(root, font=("Arial",20), bg="#F5EFE7", pady=20, text=f"True Word Per Second: {round(word_per_second,2)}", fg="#539165")
    word_per_second_label.grid(row=8, column=0, pady=20)

def update_counter():
    global counter
    timer_label.config(text=f"Timer: {str(counter)}")
    if counter>0:
        counter-=1
        timer_label.after(1000, update_counter)
    else:
        look_up_label.config(text="Press Button To See The Results")
        timer_label.config(text="Time's Up!", fg="red", pady=50)
        paragraph_label.grid_remove()
        caution_label.grid_remove()
        colored_label.grid_remove()
        input_sentence.grid_remove()
        input_sentence.config(state=tk.DISABLED)
        button=tk.Button(root, text=("Show Results"), command=button_clicked)
        button.grid(row=6, column=0)

def entry_focus(event):
    input_sentence.focus()







created_test()
root.bind("<Map>", entry_focus)
input_sentence.bind("<Return>", entry_func)
paragraph_length+=len(paragraph)
paragraph_label.config(text=paragraph.upper())
update_counter()
root.mainloop()







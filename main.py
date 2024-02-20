
from tkinter import *
from tkinter import messagebox 
from quiz import quiz_data
#import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def start_quiz():
    global start
    start=Tk()
    s_label=Label(
      start,
      anchor="center",
      wraplength=500,
    
      borderwidth=3,
      relief="raised",
    
      bg="light blue",
      fg="dark blue",
      font=("Times","24","bold italic")
   
    )
    s_label.pack(pady=10)
    sbtn=Button(start,command=main,anchor="center",borderwidth=3,relief="raised",bg="light blue",fg="dark blue",state="normal")
    sbtn.pack(pady=10)

    s_label.config(text="Lets Start Quiz")
    sbtn.config(text="Start Quiz")
    start.mainloop()


   
def show_question():
    question=quiz_data[current_question]
    qs_label.config(text=question["question"])
    choices=question["options"]
    for i in range(4):
        choice_btns[i].config(text=choices[i],state="normal")
    feedback_label.config(text="")
    next_btn.config(state="disabled")
   

    
def check_answer(choice):
    question=quiz_data[current_question]
    selected_choice=choice_btns[choice].cget("text")
    if selected_choice==question["correct_option"]:
        
        global score
        global rcount
        score+=1
        rcount+=1

        score_label.config(text="Score:{}/{}".format(score,len(quiz_data)))
        feedback_label.config(text="Correct!")
        feedback_label.config(fg="green")
        
    else:
        feedback_label.config(text="Wrong!")
        feedback_label.config(fg="red")
        global wcount
        wcount+=1
    for btn in choice_btns:
        btn.config(state="disabled")
    next_btn.config(state="normal")
        
def next_question():
    global current_question
    current_question+=1
    if current_question<len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("quiz Completed","QUIZ COMPLETED!!")
        root.destroy()
        show_score_window()
      
def show_score_window():    
    msg=Tk()
    msg.title("Quiz Score")
    msg.geometry("600x500")
    msg.config(bg="#856ff8")
    first_label=Label(msg,bg="light blue",fg="dark blue")
    first_label.pack(pady=10)
    second_label=Label(msg,bg="light blue",fg="dark blue")
    second_label.pack(pady=10)
    third_label=Label(msg,bg="light blue",fg="dark blue")
    third_label.pack(pady=10)
    first_label.config(text="Final Score:{}/{}".format(score,len(quiz_data)),font=("times","40","bold italic"))
    second_label.config(text="Right Answers:{}/{}".format(rcount,len(quiz_data)),font=("times","40","bold italic"))
    third_label.config(text="Wrong Answers:{}/{}".format(wcount,len(quiz_data)),font=("times","40","bold italic"))
    open_btn=Button(msg,text="Accuracy Analysis",command=lambda: plot_accuracy(rcount, wcount))   
    open_btn.pack(pady=10)
    msg.mainloop()  

def plot_accuracy(rcount,wcount):
    categories=["correct","incorrect"]
    counts=[rcount,wcount]
    plt.figure(figsize=(8, 6))
    sns.barplot(x=categories, y=counts, palette="viridis")
    plt.show()
    


def main():    
    
    global root, qs_label, choice_btns, feedback_label, score, rcount, wcount, score_label, next_btn, current_question 
    start.destroy()

    root=Tk()
    root.title("Quiz")
    root.geometry("600x500")
    root.config(bg = '#856ff8')
    
  
   
    qs_label=Label(
     root,
     anchor="center",
     wraplength=500,
    
     borderwidth=3,
     relief="raised",
    
     bg="light blue",
     fg="dark blue",
     font=("Times","24","bold italic")
)


    qs_label.pack(pady=10)

    choice_btns=[]
    for i in range(4):
      button=Button(root,
                  anchor="center",
                  borderwidth=3,
                  relief="raised",
    
                  bg="light blue",
                  fg="dark blue",
                  font=("Times","24","bold italic"),
                  command=lambda i=i:check_answer(i)
    )
      button.pack(pady=5)
      choice_btns.append(button)

    feedback_label=Label(root,
                         anchor="center")
    feedback_label.pack(pady=10)
    score=0
    rcount=0
    wcount=0
    score_label=Label(
        root,
        anchor="center",
        borderwidth=3,
        relief="raised",
        bg="light blue",
        fg="dark blue",
        font=("Times","24","bold italic"),
        wraplength=500,
        text="Score:0/{}".format(len(quiz_data)))
    next_btn=Button(root,
                    text="Next",
                    command=next_question,
                    state="disabled")
    next_btn.pack(pady=10)
    current_question=0
    

    show_question()
   
    
                         




    root.mainloop()
start_quiz()
    

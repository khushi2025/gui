from tkinter import *
window=Tk()
window.title("Mile to Km Converter.")
window.minsize(width=400,height=200)
window.config(padx=50,pady=100)
def calculate():
    text = float(entry.get())
    result=round(1.609* text,2)
    answer.config(text=result)

entry=Entry(width=10)
entry.insert(END,"0")
entry.grid(column=1,row=0)

miles=Label(text="Miles",font=("Courier",15,"normal"))
miles.grid(column=2,row=0)

is_equal_to=Label(text="is equal to",font=("Courier",15,"normal"))
is_equal_to.grid(column=0,row=1)

answer=Label(text="0",font=("Courier",15,"normal"))
answer.grid(column=1,row=1)

km=Label(text="Km",font=("Courier",15,"normal"))
km.grid(column=2,row=1)

button=Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)


window.mainloop()
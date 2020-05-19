import tkinter as tk
import time






def setlabel():
    value = entry_gp.get()
    lbl_start['text'] = value + "k GP" 
    entry_gp.delete(0, tk.END)
    btn_start.pack_forget()
    entry_gp.pack_forget()

top = tk.Tk()
top.title('RSFeatherUnpack 1.0')
top.minsize(300,100)


#TOP SECTION
frmleft = tk.Frame(top)
frmright = tk.Frame(top)

lbl_start = tk.Label(
    top, text="Enter GP in thousands"

)

entry_gp = tk.Entry(
    
)

btn_start = tk.Button(
    top,text ="START",
    height=2,
    width = 20,
    command = setlabel
 )

 #MIDDLE SECTIONS
lbl_status_left = tk.Label(
    frmleft,text = " Status:"
)

lbl_status_right = tk.Label(
    frmright,text= "Value "
)

lbl_profit_left = tk.Label(
    frmleft,text = " Total Profit:"
)
lbl_profit_right = tk.Label(
    frmright,text = "XXXX GP "
)


lbl_gphr_left = tk.Label(
    frmleft,text = " GP/hr:"
)
lbl_gphr_right = tk.Label(
    frmright,text = "XXXX GP "
)

lbl_timeleft_left = tk.Label(
    frmleft,text = " Time Left:"
)
lbl_timeleft_right = tk.Label(
    frmright,text = "00:00:00 "
)

#BOTTOM
lbl_perc = tk.Label(
    text='40%s complete' % "%"
)




lbl_start.pack()
entry_gp.pack()
entry_gp.insert(0,"ex. 5000 = 5m")
btn_start.pack()


frmleft.pack(side=tk.LEFT)
lbl_status_left.pack()
lbl_profit_left.pack()
lbl_gphr_left.pack()
lbl_timeleft_left.pack()

frmright.pack(side=tk.RIGHT)
lbl_status_right.pack()
lbl_profit_right.pack()
lbl_gphr_right.pack()
lbl_timeleft_right.pack()
lbl_perc.pack(side=tk.BOTTOM)

top.mainloop()


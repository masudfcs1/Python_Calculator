from tkinter import *
from tkinter import Button

font=('Verdana',22,'bold')


def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='X':
        tf.insert(END,"*")
        return

    if text=='=':
        ex=tf.get()
        ans=eval(ex)
        tf.delete(0,END)
        tf.insert(0,ans)
        return

    tf.insert(END,text)

def all_clear():
    tf.delete(0,END)
def clear():
    ex=tf.get()
    ex=ex[0:len(ex)-1]
    tf.delete(0,END)
    tf.insert(0,ex)

window=Tk()
window.title('Masud Calculator   ". )')
window.geometry('510x550')
pic=PhotoImage(file='img/3.png')


headinglabel=Label(window,image=pic)
headinglabel.pack(side=TOP,pady=15)

#heading label
heading=Label(window,text='Masud calculator',font=font,underline=0)
heading.pack(side=TOP)

tf=Entry(window,font=font,justify=CENTER)
tf.pack(side=TOP,fill=X,padx=8)

bf=Frame(window)
bf.pack(side=TOP)


cnt=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(bf,text=str(cnt),font=font,width=5,relief='ridge',activebackground='yellow',activeforeground='green')
        btn.grid(row=i,column=j,padx=3,pady=2)
        cnt+=1
        btn.bind('<Button-1>',click_btn_function)

zebt=btn=Button(bf,text='0',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green')
zebt.grid(row=3,column=0,padx=3,pady=2)

dotbtn=Button(bf,text='.',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green')
dotbtn.grid(row=3,column=1,padx=3,pady=2)

eqbt=Button(bf,text='=',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green')
eqbt.grid(row=3,column=2,padx=3,pady=2)

plsbtn=Button(bf,text='+',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green')
plsbtn.grid(row=0,column=3,padx=3,pady=2)

substn=Button(bf,text='-',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green')
substn.grid(row=1,column=3,padx=3,pady=2)

mulbtn=Button(bf,text='X',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green')
mulbtn.grid(row=2,column=3,padx=3,pady=2)

divbtn=Button(bf,text='/',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green')
divbtn.grid(row=3,column=3,padx=3,pady=2)

cleabtn=Button(bf,text='<--',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green',command=clear)
cleabtn.grid(row=4,column=0,)

allcleabtn=Button(bf,text='AC',font=font,width=5,relief='ridge',activebackground='white',activeforeground='green',command=all_clear)
allcleabtn.grid(row=4,column=1,)


plsbtn.bind('<Button-1>',click_btn_function)
substn.bind('<Button-1>',click_btn_function)
mulbtn.bind('<Button-1>',click_btn_function)
divbtn.bind('<Button-1>',click_btn_function)
zebt.bind('<Button-1>',click_btn_function)
eqbt.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)





window.mainloop()
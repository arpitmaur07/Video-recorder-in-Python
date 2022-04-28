
from tkinter import *
import cv2 
import datetime

root = Tk()
root.title('Camera App')
# root.geometry('640x520')
root.minsize(470,145)
root.maxsize(470,145)
root.configure(bg='red')


cap= cv2.VideoCapture(0)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
time=str(datetime.datetime.now().today()).replace(':',"_")+'.mp4'


def recordVideo():
    writer= cv2.VideoWriter(time, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
    while True:
        ret,frame= cap.read()
        writer.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    writer.release()
    cv2.destroyAllWindows()
    root.destroy()
    root.quit()  
    
def exitWindow():
    cap.release()
    # writer.release()
    cv2.destroyAllWindows()
    root.destroy()
    root.quit()  
    
f1=LabelFrame(root,bg='#58F',fg='white',text="Click on 'Record Video' button to start recording.\n To stop recoding just press 'q'.",font=('Arial Bold',14))
f1.pack()    
l1=Label(f1,bg='#58F')
l1.pack()
    
b1=Button(l1,bg='green',fg='white',text="Recoder Video",relief=RAISED,font=('Arial Bold',11),activeforeground='green',command=recordVideo)
b1.pack(padx=8,pady=10)
b2=Button(l1,bg='red',fg='white',text="Exit",relief=SUNKEN,font=("Courier", 13, "italic"),activebackground='red',command=exitWindow)
b2.pack(padx=8,pady=2)

root.mainloop()    

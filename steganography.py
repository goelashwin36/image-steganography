from PIL import Image
import tkinter
from tkinter import filedialog
from tkfilebrowser import askopendirname, askopenfilename, asksaveasfilename

def gendat(data):#convert data into binary data

        newd=[]
        for i in data:
            newd.append(format(ord(i),'08b'))
        return newd

def modpix(pix,data):#To return the modified pixels

    datalist=gendat(data)
    lendata=len(datalist)
    imdata=iter(pix)

    for i in range(lendata):
        pix=[value for value in next(imdata)[:3] + next(imdata)[:3] + next(imdata)[:3]]
#the value should be made odd for 1 and even for 0.
        for j in range(0,8):
            if (datalist[i][j]=='0') and (pix[j]%2!=0):
                if (pix[j]%2!=0):
                    pix[j]-=1
            elif (datalist[i][j]=='1') and (pix[j]%2==0):
                pix[j]-=1
#0 means keep reading; 1 means the message is over.
        if i==lendata-1:
            if pix[-1]%2==0:
                pix[-1]-=1
        else:
            if pix[-1]%2!=0:
                pix[-1]-=1

        pix=tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(data):

    s2=tkinter.Tk()
    name=askopenfilename()
    image=Image.open(name,'r')
    global newimg
    newimg=image.copy()

 #   if len(data)==0:
 #       raise ValueError('Data is empty')
 #   elif 3*len(data) > newimg.getdata():
 #       raise ValueError('Data too large')
    w=newimg.size[0]
    (x,y)=(0,0)
    for pixel in modpix(newimg.getdata(),data):
        newimg.putpixel((x,y),pixel)  #To put modified pixels in the newimg
        if x==w-1:
            x=0
            y+=1
        else:
            x+=1
    def call2():
        directory=filedialog.askdirectory()
        newimg.save(directory+'/newimg.png','PNG')
        s2.destroy()
        s3=tkinter.Tk()
        label5=tkinter.Label(s3,text='Data Encoded',padx=10,pady=10)
        label5.grid(row=0,column=1)
        button4=tkinter.Button(s3,text='Quit',pady=10,padx=10,command=s3.destroy)
        button4.grid(row=1,column=1,pady=10,padx=10)
        s3.mainloop()

    button3=tkinter.Button(s2,text='Save as new file',pady=10,command=call2,padx=10)
    button3.grid(row=0,column=1,pady=10,padx=10)
    s2.mainloop()

def encode():#To encode the data
    s.destroy()
    s1=tkinter.Tk()

    label2=tkinter.Label(s1,text='Steganography',padx=10,pady=10)
    label2.grid(row=0,column=0)
    global entry1
    entry1=tkinter.Entry(s1)
    entry1.grid(row=2,column=0,padx=10)

    def call():#To call encode_enc
        data=entry1.get()
        s1.destroy()
        encode_enc(data)
    button1=tkinter.Button(s1,text='Enter data',padx=5,pady=5,command=call)
    button1.grid(row=2,column=1)
    s1.mainloop()

def decode():#To decode the data in the image.
    s.destroy()
    s1=tkinter.Tk()
    imname=str(askopenfilename())
    image=Image.open(imname,'r')
    data=''
    imgdata=iter(image.getdata())
    while True:
        pixels=[value for value in next(imgdata)[:3] + next(imgdata)[:3] + next(imgdata)[:3]]#list of 3 pixels
        binstr=''#string of binary data
        for i in pixels[:8]:
            if i%2==0:
                binstr+='0'
            else:
                binstr+='1'
        data+=chr(int(binstr,2))
        if pixels[-1]%2!=0:
            label2=tkinter.Label(s1,text='Secret code\n'+str(data),padx=20,pady=20)
            label2.grid(row=0,column=1)
            s1.mainloop()

s=tkinter.Tk()

label2=tkinter.Label(s,text='Steganography',pady=25)
label2.grid(row=0,column=0)

button2=tkinter.Button(s,text='Encode',command=encode,padx=5,pady=5)
button2.grid(row=1,column=0,padx=25,pady=10)

button2=tkinter.Button(s,text='Decode',command=decode,padx=5,pady=5)
button2.grid(row=2,column=0,padx=25,pady=10)
s.mainloop()


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from urllib.request import urlopen
import re
pnr = ''
def GUI():
    root = Tk()
    root.geometry("800x500")
    L1 = Label(root, text="Enter the PNR NUMBER ?")
    L1.pack(side=LEFT)
    E1 = Entry(root, bd=10)
    def helloCallBack():
        pnr = E1.get()
        value = calc(pnr)
        msg = messagebox.showinfo("Passenger Info", "\nPNR\t\t"+value["PNR"]+"\nTrain No\t\t"+value["Train No"]+"\nBoarding Date\t"+value["Boarding Date"]+"\nClass\t\t"+value["Class"]+"\nFrom\t\t"+value["From"]+"\nTo\t\t"+value["To"]+"\nBoarding Point\t"+value["Boarding Point"])

    B = Button(root, text="Submit", command=helloCallBack)
    E1.pack(side=RIGHT)
    B.place(x=700, y=300)
    root.mainloop()
def calc(pnr):
    url = "https://www.confirmtkt.com/pnr-status/" + pnr
    htmlfile = urlopen(url)
    htmltext = htmlfile.read()
    regex = '"TrainNo":"*(.+?)"'
    pattern = re.compile(regex)
    st = re.findall(pattern, str(htmltext))
    tno = ''.join(st)
    regex = '"Doj":"(.+?)"'
    pattern = re.compile(regex)
    st = re.findall(pattern, str(htmltext))
    doj = ''.join(st)
    regex = '"Class":"(.+?)"'
    pattern = re.compile(regex)
    st = re.findall(pattern, str(htmltext))
    cla = ''.join(st)
    regex = '"From":"(.+?)"'
    pattern = re.compile(regex)
    st = re.findall(pattern, str(htmltext))
    fr = ''.join(st)
    regex = '"To":"(.+?)"'
    pattern = re.compile(regex)
    st = re.findall(pattern, str(htmltext))
    to = ''.join(st)
    regex = '"BoardingPoint":"(.+?)"'
    pattern = re.compile(regex)
    st = re.findall(pattern, str(htmltext))
    bp = ''.join(st)
    # print(tno.strip("['']"))
    """
    pnr = "4327222000"
    tno = "22501"
    doj = "28- 3-2017"
    cla = "SL"
    fr = "SBC"
    to = "GHY"
    bp = "SBC"
    """
    data = {"PNR": pnr, "Train No": tno, "Boarding Date": doj, "Class": cla, "From": fr, "To": to, "Boarding Point": bp}
    return data
if __name__ == "__main__":
    GUI()

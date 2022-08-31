from tkinter import *
from tkinter.ttk import *
from BellmanFord import bell
from Prims import prims
from FloydWarshal import floydwarshal
from localcluster import localclus
from kruskalmod import kruskal
from Dijkstra import dijkstra
from simplegraph import simpleg
from Boruvka import boruvka
from tkinter import filedialog
##############################################################

filename=''
def browseFiles(self):
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    global  label_file_explorer                                         
    label_file_explorer.configure(text="File Opened: "+filename)
    filename2=filename
    print(filename+"uda")

root = Tk()
root.title("FirstPage")
# Set Geometry(widthxheight)
root.geometry('1500x1500')
T = Text(root, height=5, width=52)
l = Label(root, text="WELCOME TO THE GRAPHING WORLD..!!")
l.config(font=("Courier", 34), foreground="green")
l.pack(padx=5, pady=255)

l1 = Label(root, text="Usama(19k0248)")
l1.config(font=("Courier", 14))
l1.pack(padx=0, pady=0)

l2 = Label(root, text="Abdullah(19k1377)")
l2.config(font=("Courier", 14))
l2.pack(padx=0, pady=0)

l.pack()
# Create style Object
style = Style()

style.configure('TButton', font=
('calibri', 20, 'bold'),
                borderwidth='8',
                fg="red")

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground=[('active', '!disabled', 'green')],background=[('active', 'black')])

# button 1
btn = Button(root, text='exit', command=root.destroy)
proceedbutton = Button(root, text='PROCEED', command=root.destroy).place(x=600,y=400)

# Set the position of button to coordinate (100, 20)
btn.place(x=1600, y=900)
# btn1.grid(row=0, column=3, padx=100)
root.mainloop()

root2 = Tk()
style = Style()

style.configure('TButton', font=
('calibri', 20, 'bold'),
                borderwidth='8',
                fg="red")

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])
root2.title("FirstPage")
root2.geometry('1500x1500')
l1 = Label(root2, text="UPLOAD A FILE")
l1.config(font=("Courier", 24))
l1.pack(padx=0, pady=250)
label_file_explorer = Label(root2,text = "File Explorer using Tkinter")

      
button_explore = Button(root2,text = "Browse Files",command = lambda: [browseFiles(root2), root2.destroy()])
button_explore.place(x=600,y=380)
root2.mainloop()

root3=Tk()
root3.title("third")
root3.geometry('1500x1500')
style = Style()

style.configure('TButton', font=
('calibri', 20, 'bold'),
                borderwidth='8',
                fg="red")
style.map('TButton', foreground=[('active', '!disabled', 'green')],
          background=[('active', 'black')])
proceedbutton = Button(root3, text='KRUSKALS', command=lambda: kruskal(filename)).place(x=500,y=200)
proceedbutton = Button(root3, text='PRIMS', command=lambda: prims(filename)).place(x=500,y=250)
proceedbutton = Button(root3, text='BELLMAN FORD', command=lambda: bell(filename)).place(x=500,y=300)
proceedbutton = Button(root3, text='DIJKSTRA', command=lambda: dijkstra(filename)).place(x=500,y=350)
proceedbutton = Button(root3, text='FLOYD WARSHALL', command=lambda: floydwarshal(filename)).place(x=500,y=400)
proceedbutton = Button(root3, text='LOCAL CLUSTER', command=lambda: localclus(filename)).place(x=500,y=450)
proceedbutton = Button(root3, text='BORUVKA', command=lambda: boruvka(filename)).place(x=500,y=500)
proceedbutton = Button(root3, text='SIMPLE GRAPH', command=lambda: simpleg(filename)).place(x=1150,y=620)
root3.mainloop()
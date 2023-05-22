import tkinter as tk

# boton = tk.Button(root, text="Click")
# boton.pack()

# root.mainloop()

def boton_click():
    print("click echo")
    
root = tk.Tk()

boton = tk.Button(root, text="Click aqui", command=boton_click)
boton.pack()

root.mainloop()
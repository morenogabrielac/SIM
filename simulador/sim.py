import tkinter as tk
from client.gui_app import Frame
def main():
    root = tk.Tk()
    root.title('Simulador 2023')
    root.iconbitmap('img\ingenieria.ico')
    
    
    app = Frame(root= root)

    app.mainloop()
    
    
if __name__=='__main__':
        main()
import tkinter as tk


class Flashcard:
    
    def __init__(self, root):
        
        self.root = root
        self.root.title("Flashcard")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        


        
    
        
if __name__ == "__main__":
    root = tk.Tk()
    Flashcard(root)
    root.mainloop()
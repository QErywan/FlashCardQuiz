import tkinter as tk


class Flashcard:
    
    def __init__(self, root):
        
        self.questions = {}
        
        self.root = root
        self.root.title("Flashcard")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        self.main_menu()
        
    def main_menu(self):
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame.pack(fill="both", expand=True)
        
        self.main_menu_label = tk.Label(self.main_menu_frame, text="Flashcard", font=("Arial", 20))
        self.main_menu_label.pack(pady=20)
        
        self.create_flashcard_button = tk.Button(self.main_menu_frame, text="Create Flashcard", command=self.create_flashcard)
        self.create_flashcard_button.pack(pady=10)
        
        self.quiz_button = tk.Button(self.main_menu_frame, text="Quiz", command=self.quiz)
        self.quiz_button.pack(pady=10)
        
    ''' create section '''
    def create_flashcard(self):
        self.main_menu_frame.destroy()
        
        self.create_flashcard_frame = tk.Frame(self.root)
        self.create_flashcard_frame.pack(fill="both", expand=True)
        
        self.create_flashcard_label = tk.Label(self.create_flashcard_frame, text="Create Flashcard", font=("Arial", 20))
        self.create_flashcard_label.pack(pady=20)
        
        self.flashcard_question_label = tk.Label(self.create_flashcard_frame, text="Question")
        self.flashcard_question_label.pack(pady=10)
        self.flashcard_question_entry = tk.Entry(self.create_flashcard_frame)
        self.flashcard_question_entry.pack(pady=10)
        
        self.flashcard_answer_label = tk.Label(self.create_flashcard_frame, text="Answer")
        self.flashcard_answer_label.pack(pady=10)
        self.flashcard_answer_entry = tk.Entry(self.create_flashcard_frame)
        self.flashcard_answer_entry.pack(pady=10)
        
        self.create_flashcard_button = tk.Button(self.create_flashcard_frame, text="Create", command=self.add_question)
        self.create_flashcard_button.pack(pady=10)
        
        self.create_flashcard_back_button = tk.Button(self.create_flashcard_frame, text="Back", command=self.create_flashcard_back)
        self.create_flashcard_back_button.pack(pady=10)
        
    
    def add_question(self):
        question = self.flashcard_question_entry.get()
        answer = self.flashcard_answer_entry.get()
        
        self.questions[question] = answer
        
        print(self.questions)
        
        
    def create_flashcard_back(self):
        self.create_flashcard_frame.destroy()
        self.main_menu()
        
        
    ''' quiz section  '''  
    def quiz(self):
        self.main_menu_frame.destroy()
        '''
        quiz state
        0 = stop
        1 = start
        '''
        quiz_state = 1
        
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack(fill="both", expand=True)
        
        self.quiz_label = tk.Label(self.quiz_frame, text="Quiz", font=("Arial", 20))
        self.quiz_label.pack(pady=20)
        
        while quiz_state == 1:
            if self.questions:
                for question, answer in self.questions.items():
                    self.quiz_question_label = tk.Label(self.quiz_frame, text=question)
                    self.quiz_question_label.pack(pady=10)
                    
                    self.quiz_answer_entry = tk.Entry(self.quiz_frame)
                    self.quiz_answer_entry.pack(pady=10)
                    
                    self.quiz_answer_button = tk.Button(self.quiz_frame, text="Answer", command=self.quiz_answer)
                    self.quiz_answer_button.pack(pady=10)
                    
                    self.quiz_next_button = tk.Button(self.quiz_frame, text="Next", command=self.quiz_next)
                    self.quiz_next_button.pack(pady=10)
                    
                    self.quiz_stop_button = tk.Button(self.quiz_frame, text="Stop", command=self.quiz_stop)
                    self.quiz_stop_button.pack(pady=10)
                    
                    self.quiz_back_button = tk.Button(self.quiz_frame, text="Back", command=self.quiz_back)
                    self.quiz_back_button.pack(pady=10)
                    
                    
            else:
                self.quiz_label = tk.Label(self.quiz_frame, text="No questions found")
                self.quiz_label.pack(pady=10)
                
                
                quiz_state = 0
                
        
        
        self.quiz_back_button = tk.Button(self.quiz_frame, text="Back", command=self.quiz_back)
        self.quiz_back_button.pack(pady=10)
        
    def quiz_back(self):
        self.quiz_frame.destroy()
        self.main_menu()
        
        
        
        
        
        
        


        
    
        
if __name__ == "__main__":
    root = tk.Tk()
    Flashcard(root)
    root.mainloop()
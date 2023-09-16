import tkinter as tk
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Earth", "Jupiter"], "answer": "Mars"},
            {"question": "Who wrote the play 'Romeo and Juliet'?", "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"], "answer": "William Shakespeare"}
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 14), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.option_buttons.append(button)
        
        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            random.shuffle(self.questions[self.current_question]["options"])
            self.question_label.config(text=self.questions[self.current_question]["question"])
            for i in range(4):
                self.option_buttons[i].config(text=self.questions[self.current_question]["options"][i])
            self.current_question += 1
        else:
            self.show_score()
    
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question - 1]["answer"]
        selected_answer = self.questions[self.current_question - 1]["options"][selected_option]
        
        if selected_answer == correct_answer:
            self.score += 1
        
        self.next_question()
    
    def show_score(self):
        self.question_label.config(text=f"Quiz Completed! Your Score: {self.score}/{len(self.questions)}")
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

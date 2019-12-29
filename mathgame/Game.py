from Question import Question
from Group import Group
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.relativelayout import RelativeLayout

question_list = [
        Question(50, "What is two times the sum of a number and five?",
                 "2(x+5)", ["2(x+5)", "4x", "2x+5", "x+5"]),
        Question(100, """What is the solution to?
                 
                 x^2 + 2x + 1
        
                 """,
                 "-1", ["1", "-1", "1, -1", "None"]),
        Question(150, """What is the solution to?
                 
                 2x + 3y = 5
                 x + 2y = 3
        
                 """,
                 "(1,1)", ["(-1,-1)", "(1,1)", "Infinite", "None"]),
        Question(200, """What is the solution to?
                 
                 3x + 6y = 9
                 5x + 10y = 10
        
                 """,
                 "None", ["11", "13", "Infinite", "None"]),
        Question(250, """What is the solution to?
                 
                 x^3 + 3x^2 + 6x + 1
        
                 """,
                 "-0.182", ["0.3", "0.182", "-0.182", "None"]),
                 
        Question(300, "what is not correct?",
                 "cos(60) = 1/2", ["Cos(30 degrees) = sqrt(3)/2", "cos(60) = 1/2", "cos(pi/2) = 0", "sin(180 degrees) = sin(0)"]),
        Question(350, "What is NOT a valid trig identity?",
                 "Sin(x) = Cos(x)",["Sin(x) = Cos(x)", "Sin(2x) = 2sin(x)cos(x)", "sin(x) = cos(pi/2 - x)", "sin^2(x) + cos^2(x) = 1"]),
        Question(400, """What is the derivative of

                 x^2 + 2x + 1
                (calculus question)
                 """,
             "2x + 2", ["x^3/3 + x^2 + x", "DNE", "x+1", "2x + 2"]),
        Question(450, "What is the indefinite integral of x^2 + 2x + 1?", "x^3/3 + x^2 + x + C",
                 ["x^3 + 2x^2 + x", "x^3/3 + x^2 + x", "x^3/3 + x^2 + x + C", "x^3/3 + 2x^2 + x + C"]),
        Question(500, "What is the integral of 4*sec^2(x)*tan^4(x)?", "4/5 * tan^5(x) + C",
                 ["tan(x) + C", "4*tan^5(x) + C", "4/5 * tan^5(x) + C", "4/5 * sec^5(x) + C"])
                 ]

group_list = []
question_screens = []
sm = ScreenManager()
end_screen = []


class OpenScreen(Screen):
    def __init__(self, **kwargs):
        super(OpenScreen, self).__init__(**kwargs)
        self.welcome = Label(text="welcome! Choose how many groups there are on the textbox and play the game!")
        self.add_widget(self.welcome)
        self.group_counter = TextInput(input_type="number",input_filter="int", text="")
        self.add_widget(self.group_counter)
        self.button = Button(text="Go!")
        self.button.bind(on_release=self.get_questions)
        
    def create_groups(self):
        for i in range(int(self.group_counter.text)):
            group_list.append(Group("A" + str(i), 0))
            
    def get_questions(self):
        self.create_groups()
        question_screens = [QuestionScreen(question) for question in question_list]
        sm.switch_to(question_screens[0])

class QuestionScreen(Screen):
    def __init__(self, question, **kwargs):
        super(QuestionScreen, self).__init__(**kwargs)
        self.question = question
        print(question)
        self.question_text = Label(text=question.text)
        self.add_widget(self.question_text)
        self.group_spinner = Spinner(
                text = group_list[0].name,
                values = tuple([group.name for group in group_list]))
        self.add_widget(self.group_spinner)
        sm.add_widget(self)
        self.answer_buttons = [Button(text=answer_choice, on_press=self.verify_answer(answer_choice)) for answer_choice in question.answer_choices]
    
    def verify_answer(self, answer):
        group = self.get_group_by_name(self.group_spinner.text)
        if answer == self.question.answer:
            group.add_points(self.question.get_point_value())
        else:
            group.add_points(self.question.get_point_value()*-1)
        if question_screens.index_of(self)+1 < len(question_list):
            sm.switch_to(question_screens[question_screens.index_of(self)+1])
        else:
            end_screen = EndScreen()
            sm.switch_to(end_screen)
        
    
    def get_group_by_name(self, group_name):
        for group in group_list:
            if group.name == group_name:
                return group
            
            

class EndScreen(Screen):
    def __init__(self, **kwargs):
        super(EndScreen, self).__init__(**kwargs)
        self.label = Label(text="Thank you for playing, here are the scores")
        self.add_widget(self.label)
        for group in group_list:
            self.add_widget(Label(text=group.to_string()))
        
class MathGame(App):
    def build(self):
        return OpenScreen()         
            
        
        
        
            
    
    
    

        







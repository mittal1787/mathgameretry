from Question import Question
from Group import Group
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class MathGame(App):
    
    #Main initiative
    def __init__(self):
        self.question_list = [
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
        self.group_list = []


    # Create the manager
        self.sm = ScreenManager()

        self.screen_open = Screen()
        self.screen_open.add_widget(Label(text="Please put how many teams are there"))
        text_int = TextInput(text="1",input_type="number", input_filter="int")
        self.screen_open.add_widget(text_int)
        self.btn1 = Button(text="proceed")

        self.question_labels = []
        self.screens_q = []

        for i in range(10):
            screen_q = Screen()
            question = self.question_list[i]
            question_label = Label(text=question.get_text())
            self.question_labels.append(question_label)
            screen_q.add_widget(question_label)
            screen_q.add_widget(Label(text=str(question.get_point_value())))
            self.screens_q.append(screen_q)

        end_screen = Screen()
        self.screens_q.append(end_screen)
        
        self.sm.switch_to(self.screen_open)
        self.btn1.bind(on_press=self.instantiate_buttons())
        self.screen_open.add_widget(self.btn1)

    
    #find group by name
    def find_group_by_name(self, group_name):
        for group in self.group_list:
            if group_name == group.name:
                return group

    def click_answer(self, screen_1, text, group_name, screen_2):
        if text == self.question_list[self.screens_q.index_of(screen_1)].answer:
            group = self.find_group_by_name(group_name)
            group.add_points(self.question_list[self.screens_q.index_of(screen_1)].point_value)
        else:
            group = self.find_group_by_name(group_name)
            group.add_points(self.question_list[self.screens_q.index_of(screen_1)].point_value*-1)
        for group in self.group_list:
            screen_2.add_widget(Label(text=group.to_string()))
        self.sm.switch_to(screen_2)




    def instantiate_buttons(self):
        for i in range(int(self.text_int.text)):
            self.group_list.append(Group("A" + str(i), 0))
    
        spinner = Spinner(
            text = self.group_list[0].name,
            values = tuple([group.name for group in self.group_list]),
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5})
    
        for i in range(len(self.screens_q)-1):
            self.screens_q[i].add_widget(spinner)
        
    
        for i in range(len(self.screens_q)-1):
            for x in range(len(self.question_list[i].answer_choices)):
                btn = Button(text=(self.question_list[i]).answer_choices[x],
                          on_press=self.click_answer(self.screens_q[i], (self.question_list[i]).answer_choices[x], spinner.text, self.screens_q[i+1]))
                self.screens_q[i].add_widget(btn)
        self.sm.switch_to(self.screens_q[0])


        







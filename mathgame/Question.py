class Question():
    def __init__(self, point_value, text, answer, answer_choices):
        self.point_value = point_value
        self.text = text
        self.answer = answer
        self.answer_choices = answer_choices
    
    def get_point_value(self):
        return self.point_value
    
    def get_text(self):
        return self.text
    
    def get_answer(self):
        return self.answer
    
    def get_answer_choices(self):
        return self.answer_choices
        
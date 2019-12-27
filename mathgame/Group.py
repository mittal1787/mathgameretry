class Group():
    def __init__(self, name, points):
        self.name = name
        self.points = points
        
    def add_points(self, points):
        self.points += points

    def to_string(self):
        return "Name: " + self.name + ", Points: " + str(self.points)
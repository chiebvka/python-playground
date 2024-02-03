
import datetime


x= 5
y = 'string'

print(type(x))
print(type(y)) 




def func(x):
    return x + 1

print(func(6))


class dog(object):
    def  __init__(self) -> None:
        print("nice you made a dog")

    def speak(self):
        pass


class KSProject(object):
    """Represents a kickstarter project"""



new_project = KSProject()
new_project.name = "Super Mario Bros"
new_project.category = "Metal"
new_project.launched = "2024-01-04"
new_project.dealine = "2024-02-04"
new_project.state = False
new_project.backers = 0
new_project.pledged = 0.0
new_project.goal = 5000.0 

print(new_project.name)

print(f"({new_project.name}, is a big piece of, {new_project.category} )")

print(f"Distance to goal can be calculated by subtracting the distance to goal of {new_project.pledged} fro the distance to goal of {new_project.goal} ")

def print_project(p):
    print(f"hello {p.name} nice to meet you and welcome to {p.category}")

print_project(new_project)

class KSProjects(object):
    """Represents a kickstarted project class"""
    def __init__(self, name, goal, launch, close):
        self.name =  ""
        self.category = ""
        self.launched = launch
        self.deadline = close
        self.backers = 0
        self.pledged = 0.0
        self.goal = 0.0



newer_project = KSProjects("john wick", 5400.0, datetime.date(2023,12, 16), datetime.date(2024, 1, 16))

print(newer_project)


class KSProjector(object):
    """This is a constructor which is used to """ 
    def __init__(self, name, goal): 
        self._name = name
        self._goal = goal

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


news_project = KSProjector('John Wick', 45000)


print(news_project.get_name())
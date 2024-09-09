class Student():
    def __init__(self, name, school, colour):
        self.name = name
        self.school = school
        self.fav_colour = colour

    def speak(self, pozdrav):
        print(f"{pozdrav}. Moje oblíbená barva je {self.fav_colour}")


hvezdon = Student("Hvězdoň", "Třebešín", "yellow")

print(hvezdon.fav_colour)
hvezdon.speak("Ahoj")


rehor = Student("Řehoř", "Úžlabina", "blue")
rehor.speak("Čau")
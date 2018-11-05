class Duck:
    def quack(self):
        print("duck")

    def feathers(self):
        print("white and grey")

class Person:
    def quack(self):
        print("Simulate a duck")

    def feathers(self):
        print("show feather to other")

def in_the_forest(duck):
    duck.quack ()
    duck.feathers ()

def game():
    donald = Duck ()
    john = Person ()
    in_the_forest (donald)
    in_the_forest (john)


game ()
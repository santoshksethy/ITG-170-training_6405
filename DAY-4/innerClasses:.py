class Outer:
    def __init__(self, name):
        self.name = name
    class Inner:
        def __init__(self):
            self.name="inner"
        def display(self):
            print("Inner")
o=Outer("balajiS")
i=o.Inner()
i.display()
class Hello:
    def __init__(self,name):
        self._name=name

    def sayHello(self):
        print("hello {0}".format(self._name))



h = Hello("little sheep")
h.sayHello()
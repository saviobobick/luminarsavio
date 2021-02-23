class swift:
    def start(self):
        print("Swift starts")
    def stop(self):
        print("Swift stops")
class seltos:
    def start(self):
        print("Seltos starts")
    def stop(self):
        print("Seltos stops")
class person:
    def drive(self,car):
        car.start()
        car.stop()
p=person()
c=seltos()
p.drive(c)
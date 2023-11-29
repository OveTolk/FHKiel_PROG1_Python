class StepCounter:
    def __init__(self):
        self.steps = 0
    def addStep(self):
        self.steps = self.steps + 1
        print(self.steps)
    

ove = StepCounter()
ove.addStep()


            
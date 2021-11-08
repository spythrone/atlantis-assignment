import sys


class LiftManager(object):

    def __init__(self, value):

        self.direct_lifts = []
        self.upward_lifts = []
        self.downward_lifts = []
        self.minval = sys.maxsize
        self.value = value
        self.lifts = ['0', '1D', '12', '4U', '19D']
        self.floors = 20
        self.calval = None
        self.sol = None

    def aggregate_lifts(self):

        for lift in self.lifts:
            if lift and lift[-1] == "D":
                self.downward_lifts.append(-1*int(lift[0:-1]))
            elif lift and lift[-1] == "U":
                self.upward_lifts.append(int(lift[0:-1]))
            else:
                self.direct_lifts.append(int(lift))

    def adjust_value(self):

        if self.value and self.value[-1] == "D":
            self.calval = -1*int(self.value[0:-1])
        elif self.value and self.value[-1] == "U":
            self.calval = int(self.value[0:-1])
        else:
            self.calval = int(self.value)


class LiftLogicImplementor(object):

    def __init__(self, manager):
        self.manager = manager

    def calculate_min_distance(self):

        for elem in self.manager.direct_lifts:
            tmp = abs(abs(elem) - abs(self.manager.calval))
            if tmp <= self.manager.minval:
                self.manager.minval = tmp
                self.manager.sol = str(elem)

        for elem in self.manager.upward_lifts:
            tmp = self.manager.calval - elem
            if tmp >= 0:
                if tmp <= self.manager.minval:
                    self.manager.minval = tmp
                    self.manager.sol = str(elem) + 'U'
            else:
                if tmp+(self.manager.floors*2) <= self.manager.minval:
                    self.manager.minval = tmp+(self.manager.floors*2)
                    self.manager.sol = str(elem) + 'U'

        for elem in self.manager.downward_lifts:
            tmp = self.manager.calval - elem
            if tmp >= 0:
                if tmp <= self.manager.minval:
                    self.manager.minval = tmp
                    self.manager.sol = str(-1*elem) + 'D'
            else:
                if tmp+(self.manager.floors*2) <= self.manager.minval:
                    self.manager.minval = tmp+(self.manager.floors*2)
                    self.manager.sol = str(-1*elem) + 'D'


class LiftRequestSolution(object):

    def __init__(self, manager, implementor):
        self.manager = manager
        self.implementor = implementor

    def get_solution(self):
        self.manager.aggregate_lifts()
        self.manager.adjust_value()
        self.implementor.calculate_min_distance()
        indx = self.manager.lifts.index(self.manager.sol) + 1
        return "Lift #{} will be coming up to receive you.".format(indx)


if __name__ == "__main__":

    while(True):
        inp = input("Enter a request? ")
        manager = LiftManager(inp)
        implementor = LiftLogicImplementor(manager)
        solution = LiftRequestSolution(manager, implementor)
        print(solution.get_solution())

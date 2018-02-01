import Problem as problem


class Vehicles:

    def __init__(self, nPackages, garage, distance, nVisited):
        self.nPackages = nPackages
        self.nVisited = nVisited
        self.nVisited = []
        self.garage = garage
        self.distance = distance

    def getVariables(self):
        print("Number of packages: " + self.nPackages)
        print("Number of Visited Places" + self.nVisited)
        print("Garage origin" + self.garage)
        print("Total distance travelled" + self.distance)

if __name__ == '__main__':
    # vehicles = (5, problem.garage, )
    print("THis isright ")

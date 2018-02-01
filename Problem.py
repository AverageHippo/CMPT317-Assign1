class Problem:
    #declaring and initializing our 4 variables for the MNKY problem

    def __init__(self, M, N, K, Y, garage = []):
        self.M = M
        self.K = K
        self.N = N
        self.Y = Y
        self.garage = []  #Garage is always at the origin of the problem


    def printVariables(self):
        print("Number of Vehicles", self.M)
        print("Number of Packages", self.N)
        print("Number of Packages per vehicle", self.K)
        print("City Dimensions", self.Y)



    def setGarage(self):
        if (self.Y == 1):
            garage = [0]
        elif(self.Y == 2):
            garage = [0,0]
        print("The garage destnation : ", garage)


    #Our goal state is: all packages delivered from source to destination, and all vehicles have been returned to the garage
    def isGoal(self, state):

        print("The goal is reached... ")


    def successors(self , state):
        print(" The next state the problem will go to")



if __name__ == '__main__':
    problem = Problem(1, 1, 1, 2)

    problem.setGarage()
    problem.printVariables()

    # problem.isGoal()
    # problem.successors()





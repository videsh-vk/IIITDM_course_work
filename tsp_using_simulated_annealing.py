#tsp using simulated annealing
import numpy
import matplotlib.pyplot as plt

class Space:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    def get_dist(a,b):
        return numpy.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
    
    @staticmethod
    def get_total_dist(coords):
        dist = 0
        for i,j in zip(coords[:-1], coords[1:]):
            dist+=Space.get_dist(i,j)
        dist+=Space.get_dist(coords[0], coords[-1])
        return dist
    
if __name__ == '__main__':
    coords=[]
    #space = Space()
    for i in range(20):
        coords.append(Space(numpy.random.uniform(), numpy.random.uniform()))

    cost = Space.get_total_dist(coords)

    T=30
    factor=0.99
    T_init = T
    for i in range(1000):
        print(i, "cost=", cost)
        T = T*factor
        for j in range(500):
            #exchange coordinates to get new neighbours
            r_1, r_2 = numpy.random.randint(0, len(coords), size=2)
            temp = coords[r_1]
            coords[r_1] = coords[r_2]
            coords[r_2] = temp

            new_cost = Space.get_total_dist(coords)

            if new_cost < cost:
                cost = new_cost
            else:
                x = numpy.random.uniform()
                if x < numpy.exp((cost - new_cost)/T):
                    cost = new_cost

    print("Final cost :", cost)


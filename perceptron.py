import numpy as np
import matplotlib.pyplot as plt


class perceptron:

    def __init__(self, num_dimensions):
        self.num_dims = num_dimensions
        self.num_steps = 0
        self.generate_data()
        self.theta = [np.zeros(num_dimensions)]
        self.updates = [0]
    
        
        
    def generate_data(self):
        num_points = 40
        cov = [[0.25, 0], [0, 0.25]]
        ### Old method of picking points
        # pick a random point on the unit circle (or sphere), and also the opposite point
#        mean1 = np.random.random(self.num_dims)
#        mean1 = mean1/np.linalg.norm(mean1) # normalize
#
#        mean2 = -mean1
#
    
        # pick num_points points normally distributed from the random means
#        self.data_set1 = np.random.multivariate_normal(mean1, cov, num_points).T
#        self.data_set2 = np.random.multivariate_normal(mean2, cov, num_points).T
#        self.data = [self.data_set1, self.data_set2]
        
        ### New Method
        # pick a random slope
        self.slope = np.tan(2*np.pi*np.random.rand())
        theta = np.array([-self.slope, 1])
        
        # pick a bunch of random points and classify them
        
        data = np.random.multivariate_normal(np.zeros(self.num_dims), cov, num_points)
        classified_data = [[[],[]],[[],[]]]
        for pt in data:
            if np.dot(pt, theta) >= 0:
                classified_data[0][0].append(pt[0])
                classified_data[0][1].append(pt[1])
            else:
                classified_data[1][0].append(pt[0])
                classified_data[1][1].append(pt[1])
                
        self.data = [np.array(classified_data[0]), np.array(classified_data[1])]
        
    def plot_data(self, ax):
        if self.num_dims == 2:
            ax.plot(self.data[0][0], self.data[0][1], 'go')
            ax.plot(self.data[1][0], self.data[1][1], 'ro')
        
        if self.num_dims == 3:
            ax.plot(self.data[0][0], self.data[0][1], self.data[0][2], 'go')
            ax.plot(self.data[1][0], self.data[1][1], self.data[1][2], 'ro')
        
    
    def classify(self):
        while self.perceptron_update() == False:
            self.num_steps += 1
            
    
    def perceptron_update(self):
        for set in range(2):
            label = 1 if set == 0 else -1
            for i in range(len(self.data[set][0])):
                dot = np.dot(self.theta[-1], self.data[set].T[i])
                prediction = 1 if dot > 0 else -1
                
                if (prediction * label) <= 0:
                    self.theta.append(self.theta[-1] + label*self.data[set].T[i])
                    self.updates.append(label*self.data[set].T[i])
                    return False
                    
        return True

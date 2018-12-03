import numpy as np

import matplotlib.animation as animation
import matplotlib


import matplotlib.pyplot as plt


class gradintDescentVisualization():
     def __init__(self):
        """

            The graidient descent Algorithm is using for estimate parameter

            this script show how Gradient Decent work by matplotlib Live graph

        """

        self.fig = plt.figure()
        self.axis = self.fig.add_subplot(111)

        self.x = np.array([1,2,2.5,3,4,5,6,7,8,9,10])
        self.y =np.array([4,4,6,7,8,7,10,9,12,11,14])
        self.theta_0 = 8
        self.theta_1 = 0.5
        self.alpha = 0.01
        self.axis.scatter(self.x,self.y)




     def gradientdesent(self, i):


           if self.axis.lines != []: self.axis.lines.pop()
           n = len(self.x)

           model = self.theta_0 + self.theta_1 * self.x

           cb = (1 / n) * self.alpha * np.sum(model - self.y)  # derivitive of cost fumction for thetha_0
           cm = (1 / n) * self.alpha * np.sum((model - self.y) * self.x)  # derivitive of cost fumction for thetha_1

           self.theta_0 = self.theta_0 -  cb
           self.theta_1 = self.theta_1 - cm
           self.axis.plot(self.x,model)
           self.axis.set_title(r'\TeX y = {} + {} * x'.format(self.theta_0,self.theta_1))




     def  animate(self):
         anime = animation.FuncAnimation(self.fig,self.gradientdesent,interval = 1)

         plt.show()



grd = gradintDescentVisualization()
grd.animate()



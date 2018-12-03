import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class gradientDesent():
    def __init__(self):
        """
            The graidient descent Algorithm is using for estimate parameter

            in this code it estimates a simple Linear Regression Parameters( y = b_0 + b1*X)


            =====================
            ::parameter
                x : regressor Variable of trainig Data
                y : predictor Variable of trainig Data

            ::return
                theata_0 : estimated theta 0 ,

                theta_1  : estimated theta 1

            ===============





        """
        pass



    def gradientDisent(self):

        x = self.x #  x as regressor
        y =self.y  #  y as pridictor

        theata_1 = 2
        theata_0 = 4
        alpha = 0.01
        itrator = 10000
        n = len(x)
        for i in range(itrator):
            model = theata_0 + theata_1 * x

            cb = (1 / n) * alpha * np.sum(model - y)  # derivitive of cost fumction for thetha_0
            cm = (1 / n) * alpha * np.sum((model - y) * x)  # derivitive of cost fumction for thetha_1

            theata_0 = theata_0 - cb
            theata_1 = theata_1 - cm

        print(theata_0,theata_1)


grd = gradientDesent()

grd.gradientDisent()



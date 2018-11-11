class gradientDesent():
    def __init__(self):
       
        pass


    def gradientDisent(self):

        x = np.array([1 ,2,3,4]) #  x as regressor
        y = np.array([2,4,6,8])  #  y as pridictor
       
        theata_1 = 2                 
        theta_0 = 4
        alpha = 0.01
        itrator = 10000   
       
        for i in range(itrator):
            model = t0 + t1*x

            cb = (1/4)*alpha* np.sum(model - y)  # derivitive of cost fumction for thetha_0
            cm = (1/4)* alpha * np.sum((model -y)*x)# derivitive of cost fumction for thetha_1
           
            theata_0 = theata_0 - cb
            theata_1 = theata_1 - cm
            
        print(t0,t1)
       

grd = gradientDesent()
grd.gradientDisent()
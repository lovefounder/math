import pulp as pl
import numpy as np
import matplotlib.pyplot as plt

x_name = [i for i in np.arange(0, 0.271, 0.001)]
y_name = []
for k in np.arange(0,0.271,0.001):
    model = pl.LpProblem(name = 'My_model' , sense = pl.LpMinimize)

    # define the decision variables
    R = pl.LpVariable(name = "R")
    x = {i:pl.LpVariable(name = f"x{i}",lowBound = 0 ,) for i in range(5)}

    # add constraints
    model += (R-0.025*x[1] >= 0)
    model += (R-0.015*x[2] >= 0)
    model += (R-0.055*x[3] >= 0)
    model += (R-0.026*x[1] >= 0)
    model += (x[0]+1.01*x[1]+1.02*x[2]+1.045*x[3]+1.065*x[4] == 1)
    model += (0.05*x[0]+0.27*x[1]+0.19*x[2]+0.185*x[3]+0.185*x[4] >= k)

    # Set the Objective
    model += R

    status = model.solve()
    y_name.append(model.objective.value())
    # Get the results
    # with open("optput.txt",'a') as f:
    #     f.write(f"k = {k}\n")
    #     f.write(f"status: {model.status}, {pl.LpStatus[model.status]}\n")
    #     f.write(f"objective: {model.objective.value()}\n")
        
    #     for var in model.variables():
    #         f.write(f"{var.name}: {var.value()}\n")
plt.scatter(x_name,y_name,color='blue',marker='x',label='item 1')
plt.grid(True)
plt.legend()
plt.show()
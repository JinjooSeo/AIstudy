import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.], [3., 6., 9., 12., 15., 18]], float)

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.001
num_range = 1000

for i in range(num_range):
    y_tmp = (x_train * beta_gd) + bias
    
    error = y_tmp - y_train
    grad = x_train * error * 2
    
    beta_gd -= learning_rate * grad.mean()
    bias -= error.mean()

    if i % 100 == 0 :
        print("Epoch ({:10d}/{}) \t error : {:10f}, \t beta_gd : {:10f}, \t bias : {:10f})".format(i, num_range, (error**2).mean(), beta_gd.item(), bias.item()))
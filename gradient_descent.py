# imports
import numpy as np
import matplotlib.pyplot as plt
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
import seaborn as sns

# 3d figures
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# creating animations
import matplotlib.animation
from IPython.display import HTML

# styling additions
from IPython.display import HTML
style = '''
    <style>
        div.info{
            padding: 15px;
            border: 1px solid transparent;
            border-left: 5px solid #dfb5b4;
            border-color: transparent;
            margin-bottom: 10px;
            border-radius: 4px;
            background-color: #fcf8e3;
            border-color: #faebcc;
        }
        hr{
            border: 1px solid;
            border-radius: 5px;
        }
    </style>'''
HTML(style)

"""# Gradient Descent"""

x = np.linspace(-1,2.5)

def f(x):
    return x**3 - 2*x**2 +2

plt.plot(x,f(x));
plt.xlim([-1,2.5]);
plt.ylim([0,3]);

def f_prime(x):
    return 3*x**2-4*x
plt.plot(x,f_prime(x))

initialGuess = -0.1

# step-size/learning-rate
eta = 0.1

# delta value (difference of new weight and old)
# that I want to stop at:
delta_stop = 0.001

# setup path holding variables
wPath = [initialGuess]
fPath = [f(initialGuess)]

# setup initial weights
w_t = 0
w_t_new = initialGuess

# give a a formula for Δw in terms of the variables
# we defined above!
# HINT: Its the same as in class!
delta_w = 1

max_iter = 10
iters = 1
while abs(delta_w) > delta_stop and  iters <= max_iter:
    iters += 1

    # set last iterations "new" weights as our current weights
    w_t = w_t_new

    # update weights using the gradient
    w_t_new = w_t - eta*f_prime(w_t)

    # store the weights for plotting
    wPath.append(w_t_new)
    fPath.append(f(w_t_new))

    # recalculate delta_w
    delta_w = w_t_new - w_t

# convert back from list to array for plotting
wPath = np.asarray(wPath)
fPath = np.asarray(fPath)

# print start and end points
endPoint = np.round((wPath[-1],wPath[-1]),2)
print("Staring at:{}, GD ended at:{} with {} steps".format(initialGuess, endPoint,fPath.shape[0]))

"""## Visualization"""

plt.xlim([-1,2.5]);
plt.ylim([0,3]);
plt.axis('off')
plt.title(r"{} steps of GD with learning rate: {} starting at: {}".format(fPath.shape[0],eta,initialGuess), fontsize=20)

plt.plot(x,f(x));
plt.plot(wPath,fPath,color='orange');
plt.scatter(wPath,fPath,color='orange');

fig, ax = plt.subplots()

# setup a frame
plt.xlim([-1,2.5]);
plt.ylim([0,3]);
plt.axis('off')
plt.title(r"{} steps of GD with learning rate: {} starting at: {}".format(fPath.shape[0],eta,initialGuess))

ax.plot(x,f(x));

l, = ax.plot([],[],color="orange");
scat = ax.scatter([],[],color="orange");

# animate frames
def animate(i):
    l.set_data(wPath[:i], fPath[:i]);
    data = np.hstack((wPath[:i,np.newaxis], fPath[:i, np.newaxis]))
    scat.set_offsets(data)

# create gif
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(fPath), interval=500);
plt.close()
HTML(ani.to_html5_video())

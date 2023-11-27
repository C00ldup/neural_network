import numpy as np
import matplotlib.pyplot as plt
import step_function

'''
dense layer = input_neuron->hidden_layer/s->output(next_input_neuron)->input_neuron->output

output = weight * input + bias
(y = mx + q)
'''
weight = 1 # m
Input = np.arange(-5, 5+1) # x
bias = 0 # q

output = weight * Input + bias

m = weight
x = Input
q = bias
y = m * x + q
print(step_function.activation(y))

plt.plot(x, y)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xticks(np.arange(-10, 10+1, 0.5))
plt.yticks(np.arange(-10, 10+1, 0.5))

# Define x and y values for cartesian plane
x_cartesian = [-10, 10]
y_cartesian = [0, 0]
# Plot a horizontal line
plt.plot(x_cartesian, y_cartesian, 'black', linewidth=1)
plt.plot(y_cartesian, x_cartesian, 'black', linewidth=1)
plt.get_current_fig_manager().full_screen_toggle()

plt.show()
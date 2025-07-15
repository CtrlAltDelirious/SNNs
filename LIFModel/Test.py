import sys
sys.path.append("C:/Users/zafir/OneDrive/PC_STUFF/Desktop/Queen_Mary/Research/Code")
import brian2 as b2
from brian2 import uamp
from SNNs.LIFModel import Main
from SNNs.tools import input_factory
from SNNs.tools import plot_tools
import matplotlib.pyplot as plt

print("resting potential: {}".format(Main.V_REST))

# create a step current with amplitude = I_min
step_current = input_factory.get_step_current(
    t_start=0, t_end=100, unit_time=b2.ms,
    amplitude=0.0021*uamp)  # set I_min to your value

# run the LIF model.
# Note: As we do not specify any model parameters, the simulation runs with the default values
(state_monitor,spike_monitor) = Main.simulate_LIF_neuron(input_current=step_current, simulation_time = 100 * b2.ms)

# plot I and vm
plot_tools.plot_voltage_and_current_traces(
state_monitor, step_current, title="min input", firing_threshold=Main.FIRING_THRESHOLD)
plt.show()
print("nr of spikes: {}".format(spike_monitor.count[0]))  # should be 0

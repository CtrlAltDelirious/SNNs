import sys
sys.path.append("C:/Users/zafir/OneDrive/PC_STUFF/Desktop/Queen_Mary/Research/Code")
import brian2 as b2
import numpy as np
from brian2 import uamp
from SNNs.LIFModel import Main
from SNNs.tools import input_factory
from SNNs.tools import plot_tools
import matplotlib.pyplot as plt

new_param = Main.get_random_param_set(423)

Main.print_obfuscated_parameters(new_param)

step_current = input_factory.get_step_current(
    t_start=0, t_end=100, unit_time=b2.ms,
    amplitude=0.003*uamp)

(state_monitor,spike_monitor) = Main.simulate_random_neuron(input_current=step_current, obfuscated_param_set=new_param)

# plot I and vm
new_param = Main._deobfuscate_params(new_param)
plot_tools.plot_voltage_and_current_traces(
state_monitor, step_current, title="experiment", firing_threshold=new_param[2])
plt.show()

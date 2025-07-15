import sys
sys.path.append("C:/Users/zafir/OneDrive/PC_STUFF/Desktop/Queen_Mary/Research/Code")
import brian2 as b2
import numpy as np
from brian2 import uamp
from SNNs.LIFModel import Main
from SNNs.tools import input_factory
from SNNs.tools import plot_tools
import matplotlib.pyplot as plt

print("resting potential: {}".format(Main.V_REST))

spikes = []
I = []

for x in range(0, 100):
    I_current = x * 0.0005
    step_current = input_factory.get_step_current(
        t_start=0, t_end=500, unit_time=b2.ms,
        amplitude=I_current * uamp)
    I.append(I_current)
    state_monitor, spike_monitor = Main.simulate_LIF_neuron(
        input_current=step_current, simulation_time=500 * b2.ms)
    spikes.append(spike_monitor.count[0])  # Store as integer

#convert to firing rate (Hz)
firing_rates = [count / 0.5 for count in spikes]
I_namp = [current*1000 for current in I]

plt.plot(I_namp, firing_rates)
plt.xlabel("Input current (nA)")
plt.ylabel("Firing rate (Hz)")
plt.title("f-I curve")
plt.show()
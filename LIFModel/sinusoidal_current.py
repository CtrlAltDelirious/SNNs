import sys
sys.path.append("C:/Users/zafir/OneDrive/PC_STUFF/Desktop/Queen_Mary/Research/Code")
import brian2 as b2
from brian2 import uamp
from SNNs.LIFModel import Main
from SNNs.tools import input_factory
from SNNs.tools import plot_tools
import matplotlib.pyplot as plt

amplitudes = []
frequencies = []

for x in range(10, 1000):
    sinusoidal_current = input_factory.get_sinusoidal_current(
        200, 1000, unit_time=0.1 * b2.ms, amplitude= 0.0025 * b2.uamp,
        frequency=x*b2.Hz, direct_current=0. * b2.uamp)

    frequencies.append(x)

    (state_monitor, spike_monitor) = Main.simulate_LIF_neuron(
        input_current=sinusoidal_current, simulation_time = 120 * b2.ms,
        firing_threshold=0*b2.mV)
    
    amplitudes.append(plot_tools.get_amplitude(state_monitor, sinusoidal_current, title="Sinusoidal input current"))

amplitudes_adjusted = [volts*1000 for volts in amplitudes]

plt.plot(frequencies, amplitudes_adjusted)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (mV)")
plt.title("Amplitude of Subthreshold Oscillations")
plt.show()

#########################################################################
# This example is an advanced PicoScope example with minimal abstraction.
# This will return the raw ctypes ADC data as samples. 
#
#########################################################################

import pypicosdk as psdk
from matplotlib import pyplot as plt

# Pico examples use inline argument values for clarity

# Capture configuration
SAMPLES = 100000

# Initialise PicoScope
scope = psdk.ps6000a()
scope.open_unit()
print(scope.get_unit_serial())

# Setup channels and trigger (inline arguments)
scope.set_channel(channel=psdk.CHANNEL.A, range=psdk.RANGE.V1)
scope.set_simple_trigger(channel=psdk.CHANNEL.A, threshold_mv=0)

# Preferred: convert sample rate to timebase
TIMEBASE = scope.sample_rate_to_timebase(50, psdk.SAMPLE_RATE.MSPS)
# TIMEBASE = 2  # direct driver timebase
# TIMEBASE = scope.interval_to_timebase(20E-9)

# Run block capture and retrieve values
channels_buffer = scope.set_data_buffer_for_enabled_channels(samples=SAMPLES)
scope.run_block_capture(timebase=TIMEBASE, samples=SAMPLES)
scope.get_values(SAMPLES)

# No ADC to mV conversion, add it here

# Finish with PicoScope
scope.close_unit()

# Build a Histogram of data
plt.figure(0)
plt.hist(channels_buffer[psdk.CHANNEL.A])
plt.savefig('histogram_6000a.png')

# Plot a graph of data
plt.figure(1)
plt.plot(channels_buffer[psdk.CHANNEL.A])
plt.savefig('graph_6000a.png')

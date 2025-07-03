import pypicosdk as psdk
from matplotlib import pyplot as plt

# Pico examples use inline argument values for clarity

# Capture configuration
SAMPLES = 50_000

# SigGen variables
frequency = 100_000
pk2pk = 0.8
wave_type = psdk.WAVEFORM.SINE

# Initialise PicoScope 6000
scope = psdk.ps6000a()
scope.open_unit()

# Setup siggen
scope.set_siggen(frequency, pk2pk, wave_type)

# Setup channels and trigger (inline arguments)
scope.set_channel(channel=psdk.CHANNEL.A, range=psdk.RANGE.V1)
scope.set_simple_trigger(channel=psdk.CHANNEL.A, threshold_mv=0)

# Preferred: convert sample rate to timebase
TIMEBASE = scope.sample_rate_to_timebase(50, psdk.SAMPLE_RATE.MSPS)
# TIMEBASE = 2  # direct driver timebase
# TIMEBASE = scope.interval_to_timebase(20E-9)

# Run the block capture
channel_buffer, time_axis = scope.run_simple_block_capture(TIMEBASE, SAMPLES)

# Finish with PicoScope
scope.close_unit()

# Plot data to pyplot
plt.plot(time_axis, channel_buffer[psdk.CHANNEL.A])

# Add labels to pyplot
plt.xlabel("Time (ns)")     
plt.ylabel("Amplitude (mV)")
plt.ylim(-500, 500)
plt.grid(True)
plt.show()

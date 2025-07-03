import pypicosdk as psdk
from matplotlib import pyplot as plt

# Pico examples use inline argument values for clarity

# Streaming configuration
sample_interval = 1
sample_units = psdk.PICO_TIME_UNIT.US
samples = 5000

# SigGen variables
siggen_frequency = 1000  # Hz
siggen_pk2pk = 2  # Volts peak-to-peak

# Initialise PicoScope
scope = psdk.ps6000a()
scope.open_unit()

# Output a sine wave to help visualise captured data
scope.set_siggen(frequency=1000, pk2pk=2, wave_type=psdk.WAVEFORM.SINE)

# Setup channels and trigger
scope.set_channel(channel=psdk.CHANNEL.A, range=psdk.RANGE.V1)
scope.set_simple_trigger(channel=psdk.CHANNEL.A, threshold_mv=0)

# Run streaming capture
channels, time_axis = scope.run_simple_streaming_capture(
    sample_interval=sample_interval,
    sample_interval_time_units=sample_units,
    samples=samples,
    auto_stop=True,
    datatype=psdk.DATA_TYPE.INT16_T,
    ratio_mode=psdk.RATIO_MODE.RAW,
)

# Finish with PicoScope
scope.close_unit()

# Plot data to pyplot
plt.plot(time_axis, channels[psdk.CHANNEL.A])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (mV)")
plt.grid(True)
plt.show()


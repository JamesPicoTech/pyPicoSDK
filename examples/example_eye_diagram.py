import pypicosdk as psdk
from matplotlib import pyplot as plt
import numpy as np

# Pico examples use inline argument values for clarity

# Configuration
# Capture a CAN H signal using a 10:1 probe. The bus typically swings between
# roughly 1.5–3.5 V, so with the probe attenuation the scope sees about
# 0.15–0.35 V. A ±1 V range with a slight negative offset keeps the high
# level centred on the display.
SAMPLE_RATE_MSPS = 40  # ADC sample rate in mega-samples per second
BIT_RATE_MBPS = 0.4   # CAN bit rate (400 kbps)

# Derived value: number of ADC samples representing one bit/symbol. With the
# default values above this is 100 samples per CAN bit.
SAMPLES_PER_SYMBOL = int(SAMPLE_RATE_MSPS / BIT_RATE_MBPS)

# Capture two symbols per block so the triggered bit is centred with
# half a bit of context either side
SAMPLES = SAMPLES_PER_SYMBOL * 2
CAPTURES = 20  # Blocks overlaid in the eye diagram

# Initialise device
scope = psdk.ps6000a()
scope.open_unit()

# Configure channels before calculating the timebase. The SDK requires at least
# one channel to be enabled for ``sample_rate_to_timebase`` to succeed.
scope.set_channel(channel=psdk.CHANNEL.A, range=psdk.RANGE.V1, probe_scale=10, offset=-0.3)
scope.set_channel(channel=psdk.CHANNEL.B, enabled=0, range=psdk.RANGE.V1)
scope.set_channel(channel=psdk.CHANNEL.C, enabled=0, range=psdk.RANGE.V1)
scope.set_channel(channel=psdk.CHANNEL.D, enabled=0, range=psdk.RANGE.V1)

# Convert the desired sample rate into a driver-specific timebase value.
TIMEBASE = scope.sample_rate_to_timebase(SAMPLE_RATE_MSPS, psdk.SAMPLE_RATE.MSPS)

# Setup an advanced trigger.
# 250 mV at the scope corresponds to a mid-level threshold on a CAN H signal when using a 10:1 probe.
threshold_adc = scope.mv_to_adc(250, psdk.RANGE.V1)
scope.set_trigger_channel_properties(
    threshold_adc, 0, threshold_adc, 0, psdk.CHANNEL.A
)
scope.set_trigger_channel_conditions(
    psdk.CHANNEL.A, psdk.PICO_TRIGGER_STATE.TRUE
)
scope.set_trigger_channel_directions(
    psdk.CHANNEL.A,
    psdk.PICO_THRESHOLD_DIRECTION.PICO_RISING_OR_FALLING,
    psdk.PICO_THRESHOLD_MODE.PICO_LEVEL,
)

# Collect multiple captures
# Pre-trigger percentage aligns half a bit before the threshold crossing so the
# triggered bit appears centred in the capture
pre_trig_percent = int(round((SAMPLES_PER_SYMBOL / 2) / SAMPLES * 100))
buffers, time_axis = scope.run_simple_rapid_block_capture(
    timebase=TIMEBASE,
    samples=SAMPLES,
    n_captures=CAPTURES,
    pre_trig_percent=pre_trig_percent,
)
captures = buffers[psdk.CHANNEL.A]

scope.close_unit()

# //todo: explore splitting captures into multiple segments again later
segments_np = np.array(captures)

# Time axis corresponding to the captured samples
segment_time = np.array(time_axis)

# Flatten arrays for 2D histogram
times = np.tile(segment_time, len(segments_np))
values = segments_np.flatten()

hist, x_edges, y_edges = np.histogram2d(
    times,
    values,
    bins=[SAMPLES, 200],
)

extent = [x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]]

hist_log = np.log1p(hist)

plt.imshow(
    hist_log.T,
    extent=extent,
    origin="lower",
    aspect="auto",
    cmap="inferno",
)
plt.xlabel("Time (ns)")
plt.ylabel("Amplitude (mV)")
plt.title("Eye Diagram")
plt.colorbar(label="Count")
plt.show()

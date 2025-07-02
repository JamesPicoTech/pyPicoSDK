import pypicosdk as psdk

# Pico examples use inline argument values for clarity

# Capture configuration
SAMPLES = 1000
CAPTURES = 4

# Initialize and configure the scope
scope = psdk.ps6000a()
scope.open_unit()
scope.set_channel(psdk.CHANNEL.A, psdk.RANGE.V1)
scope.set_simple_trigger(psdk.CHANNEL.A, threshold_mv=0)

# Preferred: convert sample rate to timebase
TIMEBASE = scope.sample_rate_to_timebase(50, psdk.SAMPLE_RATE.MSPS)
# TIMEBASE = 2  # direct driver timebase
# TIMEBASE = scope.interval_to_timebase(20E-9)

# Acquire multiple waveforms in rapid block mode
buffers, time_axis = scope.run_simple_rapid_block_capture(
    timebase=TIMEBASE,
    samples=SAMPLES,
    n_captures=CAPTURES,
    ratio=1,
    ratio_mode=psdk.RATIO_MODE.TRIGGER,
)

# Retrieve the trigger time offset for each capture
# Values below roughly one-tenth of the sample period may not be reliable
# because the driver interpolates between samples.
offsets = scope.get_values_trigger_time_offset_bulk(0, CAPTURES - 1)
for i, (offset, unit) in enumerate(offsets):
    print(f"Segment {i}: offset = {offset} {unit.name}")

scope.close_unit()

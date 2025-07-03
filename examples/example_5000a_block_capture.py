import pypicosdk as psdk
from matplotlib import pyplot as plt

# Pico examples use inline argument values for clarity

scope = psdk.ps5000a()

SAMPLES = 10000

scope.open_unit()

scope.open_unit(resolution=psdk.RESOLUTION._16BIT)
scope.change_power_source(psdk.POWER_SOURCE.SUPPLY_NOT_CONNECTED)

print(scope.get_unit_serial())
scope.set_channel(channel=psdk.CHANNEL.A, range=psdk.RANGE.V1, coupling=psdk.DC_COUPLING)
scope.set_channel(channel=psdk.CHANNEL.B, range=psdk.RANGE.V1, coupling=psdk.AC_COUPLING)
scope.set_simple_trigger(
    channel=psdk.CHANNEL.B,
    threshold_mv=0,
    auto_trigger_ms=5000,
)

# Preferred: convert sample rate to timebase
TIMEBASE = scope.sample_rate_to_timebase(125, psdk.SAMPLE_RATE.MSPS)
# TIMEBASE = 2  # direct driver timebase
# TIMEBASE = scope.interval_to_timebase(20E-9)

# Easy Block Capture
buffer = scope.run_simple_block_capture(TIMEBASE, SAMPLES)

scope.close_unit()


# print(buffer)
plt.plot(buffer[psdk.CHANNEL.A])
plt.plot(buffer[psdk.CHANNEL.B])
plt.savefig('graph.png')
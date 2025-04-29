import argparse

# Setup argparser
parser = argparse.ArgumentParser(description="Control PicoScope via socket commands.")
subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

# run command
run_parser = subparsers.add_parser('run', help='Run block capture with specified settings')
run_parser.add_argument('-s', '--samples', type=int, help='Number of samples to capture')
run_parser.add_argument('-t', '--timebase', type=int, help='Timebase setting for capture (e.g., 1 for 1µs/div)')
run_parser.add_argument('-f', '--filename', type=str, help='Filename to save captured data')

# siggen command
siggen_parser = subparsers.add_parser('siggen', help='Configure and start the signal generator')
siggen_parser.add_argument('-f', '--frequency', type=float, help='Frequency of waveform in Hz')
siggen_parser.add_argument('-a', '--amplitude', type=float, help='Amplitude of waveform in volts')
siggen_parser.add_argument('-w', '--waveform', type=str, help='Waveform type (sine, square, triangle)')

# channel command
channel_parser = subparsers.add_parser('channel', help='Enable and set voltage range for a specific channel')
channel_parser.add_argument('-ch', '--channel', type=int, help='Channel number to configure (e.g., 1 or 2)')
channel_parser.add_argument('-r', '--range', type=str, help='Voltage range for the channel (e.g., 2V, 5V)')

# trigger command
trigger_parser = subparsers.add_parser('trigger', help='Configure the trigger settings')
trigger_parser.add_argument('-ch', '--channel', type=int, help='Channel number for trigger')
trigger_parser.add_argument('-th', '--threshold', type=float, help='Trigger threshold in millivolts')

# close command (no args)
subparsers.add_parser('close', help='Close the application')


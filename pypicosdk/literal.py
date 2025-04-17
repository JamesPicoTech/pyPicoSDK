from typing import Literal

_channel = Literal["channel_a", "channel_b", "channel_c", "channel_d", "channel_e", "channel_f", "channel_g", "channel_h"]
_channel_map = {
    "channel_a": 0,
    "channel_b": 1,
    "channel_c": 2,
    "channel_d": 3,
    "channel_e": 4,
    "channel_f": 5,
    "channel_g": 6,
    "channel_h": 7,
}

_resolution = Literal["8bit", "10bit", "12bit", "14bit", "15bit", "16bit"]
_resolution_map = {
    "8bit": 0,
    "10bit": 10, 
    "12bit": 1, 
    "14bit": 2, 
    "15bit": 3, 
    "16bit": 4
}

_unit_info = Literal[
    "driver_version",
    "usb_version",
    "hardware_version",
    "variant_info",
    "batch_and_serial",
    "cal_date",
    "kernel_version",
    "digital_hardware_version",
    "analogue_hardware_version",
    "firmware_version_1",
    "firmware_version_2",
]
_unit_info_map = {
    "driver_version": 0,
    "usb_version": 1,
    "hardware_version": 2,
    "variant_info": 3,
    "batch_and_serial": 4,
    "cal_date": 5,
    "kernel_version": 6,
    "digital_hardware_version": 7,
    "analogue_hardware_version": 8,
    "firmware_version_1": 9,
    "firmware_version_2": 10,
}

_sample_rate = Literal["S/s", "kS/s", "MS/s", "GS/s"]
_sample_rate_map = {
    "S/s": 1,
    "kS/s": 1_000,
    "MS/s": 1_000_000,
    "GS/s": 1_000_000_000,
}

_time_unit = Literal["ps", "ns", "us", "ms", "s"]
_time_unit_map = {
    "ps": 1_000_000_000_000,
    "ns": 1_000_000_000,
    "us": 1_000_000,
    "ms": 1_000,
    "s": 1,
}

_power_source = Literal["supply_connected", "supply_not_connected", "usb3.0_device_non_usb3.0_port"]
_power_source_map = {
    "supply_connected": 0x00000119,
    "supply_not_connected": 0x0000011A,
    "usb3.0_device_non_usb3.0_port": 0x0000011E
}

_coupling = Literal["AC", "DC", "DC_50_Ohm"]
_coupling_map = {
    "AC": 0,
    "DC": 1,
    "DC_50_Ohm": 50,
}

_bandwidth = Literal["full", "20mhz", "200mhz"]
_bandwidth_map = {
    "full": 0,
    "20mhz": 1,
    "200mhz": 2,
}

_trigger_dir = Literal["above", "below", "rising", "falling", "rising_or_falling"]
_trigger_dir_map = {
    "above": 0,
    "below": 1,
    "rising": 2,
    "falling": 3,
    "rising_or_falling": 4,
}

_data_type = Literal["int8", "int16", "int32", "uint32", "int64"]
_data_type_map = {
    "int8": 0,
    "int16": 1,
    "int32": 2,
    "uint32": 3,
    "int64": 4,
}

_ratio_mode = Literal[
    "aggregate", "decimate", "average", "distribution", "sum",
    "trigger_data_for_time_calculation", "segment_header",
    "trigger", "raw"
]
_ratio_mode_map = {
    "aggregate": 1,
    "decimate": 2,
    "average": 4,
    "distribution": 8,
    "sum": 16,
    "trigger_data_for_time_calculation": 0x10000000,
    "segment_header": 0x20000000,
    "trigger": 0x40000000,
    "raw": 0x80000000,
}

_action = Literal[
    "clear_all",
    "add",
    "clear_all_add"
    "clear_this_data_buffer",
    "clear_waveform_data_buffers",
    "clear_waveform_read_data_buffers"
]

_action_map = {
    "clear_all": 0x00000001,
    "add": 0x00000002,
    "clear_all_add": 0x00000003,
    "clear_this_data_buffer": 0x00001000,
    "clear_waveform_data_buffers": 0x00002000,
    "clear_waveform_read_data_buffers": 0x00004000,
}

_waveform = Literal[
    "sine", "square", "triangle", "ramp_up", "ramp_down",
    "sinc", "gaussian", "half_sine", "dc_voltage",
    "pwm", "whitenoise", "prbs", "arbitrary"
]
_waveform_map = {
    "sine": 0x00000011,
    "square": 0x00000012,
    "triangle": 0x00000013,
    "ramp_up": 0x00000014,
    "ramp_down": 0x00000015,
    "sinc": 0x00000016,
    "gaussian": 0x00000017,
    "half_sine": 0x00000018,
    "dc_voltage": 0x00000400,
    "pwm": 0x00001000,
    "whitenoise": 0x00002001,
    "prbs": 0x00002002,
    "arbitrary": 0x10000000,
}

_range = Literal[
    "10mv", "20mv", "50mv", "100mv", "200mv", "500mv",
    "1v", "2v", "5v", "10v", "20v", "50v"
]
_range_map = {
    "10mv": 0,
    "20mv": 1,
    "50mv": 2,
    "100mv": 3,
    "200mv": 4,
    "500mv": 5,
    "1v": 6,
    "2v": 7,
    "5v": 8,
    "10v": 9,
    "20v": 10,
    "50v": 11,
}
from vcdvcd import VCDVCD

# Do the parsing.
vcd = VCDVCD("negator_tb.vcd")

# List all human readable signal names.
print("signal_list: ", vcd.references_to_ids.keys())

# View all signal data.
# print(vcd.data)

# Get a signal by human readable name.
signal = vcd['negator_tb.clock']

# tv is a list of Time/Value delta pairs for this signal.
tv = signal.tv
print("clock: ", tv)

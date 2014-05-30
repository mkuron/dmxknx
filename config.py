# Set this channel to 0-127 to dim KNX values or 128-255 to switch them
channel_switch = 400
suffix_value = '_Wert'
suffix_switch = '_EA'

min_pause = 1.0
loop_pause = 0.05

# Mappings of DMX channels to FHEM objects. DMX channels are 1-512
channels = ['']*513
channels[401] = 'K13_Empore'
channels[402] = 'K14'
channels[403] = 'K17_Treppe'
channels[404] = 'K57_Mensa'
channels[405] = 'K58_Mensa'
channels[406] = 'K59_Mensa'
channels[407] = 'K60_vorBuehne'
channels[408] = 'K62_Buehne'
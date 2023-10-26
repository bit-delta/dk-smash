from pyboy import PyBoy, WindowEvent

gb_path = './DK.gb'

pyboy = PyBoy(gb_path)
assert pyboy.cartridge_title() == "DONKEY KONG"
pyboy.set_emulation_speed(1)

state = open('DK-1-1.gb.state', 'rb')
pyboy.load_state(state)
while not pyboy.tick():
    pass

# save_file = open('DK-1-1.gb.state', 'wb')
# pyboy.save_state(save_file)
pyboy.stop(save=False)

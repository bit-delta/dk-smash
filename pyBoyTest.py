from pyboy import PyBoy, WindowEvent

gb_path = './DK.gb'

pyboy = PyBoy(gb_path)
assert pyboy.cartridge_title() == "DONKEY KONG"

# state = open('DK.gb.state', 'rb')
# pyboy.load_state(state)
while True:
    pyboy.tick()

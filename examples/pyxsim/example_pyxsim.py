from pathlib import Path

import Pyxsim


class ExampleSimThread(Pyxsim.SimThread):
    def __init__(self, port0: str, port1: str):
        self._port0 = port0
        self._port1 = port1

    def run(self):
        self._wait_for_port_pins_change([self._port0])
        val = self.xsi.sample_port_pins(self._port0)
        breakpoint()


xe = Path(__file__).parent / "bin" / "example_pyxsim.xe"

simthreads = [
    ExampleSimThread("tile[0]:XS1_PORT_1G", "tile[0]:XS1_PORT_1H"),
]

tester = Pyxsim.testers.ComparisonTester("Hello World!")

simargs = ["--max-cycles", "15000000"]

result = Pyxsim.run_on_simulator_(
    xe,
    do_xe_prebuild=False,
    #cmake=True,
    tester=tester,
    simargs=simargs,
)

#breakpoint()
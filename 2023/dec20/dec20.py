from collections import deque
from math import gcd, lcm

circuit = {} # map with keys as module labels, and values as the module objects
pulse_counts = [0, 0]
class FlipFlop:
    def __init__(self, name, outputs):
        self.name = name
        self.on = False # on and off state
        self.outputs = outputs # list of output labels
        self.inputs = {}

    def add_input(self, input):
        self.inputs[input] = None
    
    def update_state(self, pulse, input):
        if pulse:
            return None
        else:
            self.on = not self.on
            return self.on
    
    def __str__(self):
        return f'FlipFlop: on: {self.on}, inputs: {self.inputs}, outputs: {self.outputs}'
    
class Conjunction:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        self.inputs = {}

    def add_input(self, input):
        self.inputs[input] = None

    def update_state(self, pulse, input):
        self.inputs[input] = pulse
        return not all([mem == 1 for mem in self.inputs.values()])

    
    def __str__(self):
        return f'Conjunction: inputs: {self.inputs} outputs: {self.outputs}'

class Broadcaster:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs
        
    
    def update_state(self, pulse, input):
        return pulse
    
    def __str__(self):
        return f'Broadcaster: outputs: {self.outputs}'

def print_circuit(circuit):
    print('\n')
    for name, module in circuit.items():
        print(name, module)

for connection in open('input.txt').read().split('\n'):
    outputs = connection.split('-> ')[1].split(', ')        
    if connection.startswith('broadcaster'):
        circuit['broadcaster'] = Broadcaster('broadcaster', outputs)
    else:
        name = connection[1:].split(' ->')[0]
        if connection.startswith('%'):
            circuit[name] = FlipFlop(name, outputs)
        else:
            circuit[name] = Conjunction(name, outputs)

for name, module in circuit.items():
    for output in module.outputs:
        # if some module outputs to a Conjunction, we need to add it to the conjunction's input
        if output in circuit:
            output_module = circuit[output]
            if type(output_module) is not Broadcaster:
                output_module.add_input(name)

#print_circuit(circuit)


def solve(circuit):
    nr_input_buttons_to_low = {}
    nr_module = circuit['nr'] 
    for input in nr_module.inputs:
        nr_input_buttons_to_low[input] = 0

    button_pulse = 0
    while True:
        button_pulse += 1
        pulse_counts[0] += 1
        #print('\nbutton -low-> broadcaster')
        broadcaster = circuit['broadcaster']
        pulse_q = deque([(broadcaster, broadcaster.update_state(0, 'button'))])
        while pulse_q:
            #print_circuit(circuit)
            module, pulse = pulse_q.popleft()
            
            for output in module.outputs:
                pulse_counts[pulse] += 1
                if output in circuit:
                    if pulse and circuit[output].name == 'nr':
                        if nr_input_buttons_to_low[module.name] == 0:
                            nr_input_buttons_to_low[module.name] = button_pulse
                        if all([button_pulse > 0 for button_pulse in nr_input_buttons_to_low.values()]):
                            print(nr_input_buttons_to_low)
                            p2 = lcm(*nr_input_buttons_to_low.values())
                            return p1, p2
                    if (new_signal := circuit[output].update_state(pulse, module.name)) is not None:
                        pulse_q.append((circuit[output], new_signal))
        if button_pulse == 1000:
            p1 = pulse_counts[1] * pulse_counts[0] 

p1, p2 = solve(circuit)
print("part 1: {}\npart 2: {}".format(p1, p2))




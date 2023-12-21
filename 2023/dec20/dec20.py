from collections import deque
from math import gcd

circuit = {} # map with keys as module labels, and values as the module objects
pulse_counts = [0, 0]
class FlipFlop:
    def __init__(self, label, outputs):
        self.label = label
        self.on = False # on and off state
        self.outputs = outputs # list of output labels
        self.pulse_to_send = 1
        self.received_pulses = deque()

    def receive_pulse(self, pulse, input):
        self.received_pulses.append(pulse)
        if pulse == 0: # received low pulse
            if self.on: # if it was on, turn it off and should send a low pulse to outputs
                self.on = False
                self.pulse_to_send = 0
            else: # it was off, so turn it on and should send a high pulse to outputs
                self.on = True
                self.pulse_to_send = 1
            self.should_send = True

    def send_pulse(self): 
        if self.received_pulses.popleft() == 0:
            for output in self.outputs:
                pulse_counts[self.pulse_to_send] += 1
                #print(self.label + ' -' + self.pulse_to_send + '-> ' + output)
                if output in circuit:
                    circuit[output].receive_pulse(self.pulse_to_send, self.label)
            return True
        return False
    
    def __str__(self):
        return f'FlipFlop: {self.label}, on: {self.on}, outputs: {self.outputs}, pulse_to_send: {self.pulse_to_send}, received_pulses: {self.received_pulses}'
    
class Conjunction:
    def __init__(self, label, outputs):
        self.label = label
        self.outputs = outputs
        self.input_memory = {}
        self.pulse_to_send = 1

    def add_input(self, input):
        self.input_memory[input] = 0

    def receive_pulse(self, pulse, input):
        self.input_memory[input] = pulse
        if all([pulse == 1 for pulse in self.input_memory.values()]):
            self.pulse_to_send = 0
        else:
            self.pulse_to_send = 1
    
    def send_pulse(self):
        return_val = True
        for output in self.outputs:
            pulse_counts[self.pulse_to_send] += 1
            if output in circuit:
                #print(self.label + ' -' + self.pulse_to_send + '-> ' + output)
                circuit[output].receive_pulse(self.pulse_to_send, self.label)
        return return_val
    
    def __str__(self):
        return f'Conjunction: {self.label}, outputs: {self.outputs}, pulse_to_send: {self.pulse_to_send}, input_memory: {self.input_memory}'

class Broadcaster:
    def __init__(self, outputs):
        self.label = 'broadcaster'
        self.outputs = outputs
        self.pulse_to_send = 0
    
    def send_pulse(self):
        return_val = True
        for output in self.outputs:
            pulse_counts[self.pulse_to_send] += 1            
            if output in circuit:
                #print(self.label + ' -' + self.pulse_to_send + '-> ' + output)
                circuit[output].receive_pulse(self.pulse_to_send, self.label)
        return return_val
    
    def __str__(self):
        return f'Broadcaster: outputs: {self.outputs}, pulse_to_send: {self.pulse_to_send}'

def print_circuit(circuit):
    print('\n')
    for module in circuit.values():
        print(module)

for connection in open('input.txt').read().split('\n'):
    outputs = connection.split('-> ')[1].split(', ')        
    if connection.startswith('broadcaster'):
        circuit['broadcaster'] = Broadcaster(outputs)
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
            if type(output_module) is Conjunction:
                output_module.add_input(name)

p2 = 0

nr_input_buttons_to_low = {}
nr_module = circuit['nr'] 
for input in nr_module.input_memory:
    nr_input_buttons_to_low[input] = 0

print(nr_input_buttons_to_low)
button_pulse = 0
while True:
    button_pulse += 1
    pulse_counts[0] += 1
    #print('\nbutton -low-> broadcaster')

    pulse_q = deque(['broadcaster'])
    while pulse_q:
        #print_circuit(circuit)
        name = pulse_q.popleft()
        if name in circuit:
            module = circuit[name]
            if send_val:=module.send_pulse():
                pulse_q.extend(module.outputs)
    
    if button_pulse == 1000:
        p1 = pulse_counts[1] * pulse_counts[0] 
        print(p1)

    nr_module = circuit['nr'] 
    if any([memory == 1 for memory in nr_module.input_memory.values()]):
        print(nr_module)
    for input, memory in nr_module.input_memory.items():
        if memory == 1:
            nr_input_buttons_to_low[input] = button_pulse + 1
            print(nr_input_buttons_to_low)
    if all([button_counts > 0 for button_counts in nr_input_buttons_to_low.values()]):
        p2 = 1
        for button_counts in nr_input_buttons_to_low.values():
            p2 = p2 * button_counts // gcd(p2, button_counts)
        break

print("part 1: {}\npart 2: {}".format(p1, p2))




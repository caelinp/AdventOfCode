from abc import ABC, abstractclassmethod
from collections import deque
import math

class Module(ABC):
    def __init__(self, id: str, connections: list[str], enabled: bool) -> None:
        self.id = id
        self.connections = connections
        self.enabled = enabled
        self.inputs: dict[str, bool] = {}

    @abstractclassmethod
    def updateState(self, input: bool, inputId: str): 
        pass

class BroadCaster(Module):
    def __init__(self, connections: list[str]) -> None:
        super().__init__('broadcaster', connections, True)
    
    def updateState(self, input: bool, inputId: str):
        return input
    

class FlipFlop(Module):
    def __init__(self, id: str, connections: list[str]) -> None:
        super().__init__(id, connections, False)

    def updateState(self, input: bool, inputId: str) -> bool:
        if input == True:
            return None
        self.enabled = not self.enabled
        return self.enabled
            

class Conjunction(Module):
    def __init__(self, id: str, connections: list[str]) -> None:
        super().__init__(id, connections, True)

    def updateState(self, input: bool, inputId: str) -> bool:
        self.inputs[inputId] = input
        return not all(value == True for key, value in self.inputs.items())

        
def solve(modules: dict[str, Module]):
    high = low = 0
    moduleRx = {}

    for i in range(5000):
        if i == 1000:
            part1 = high*low
        low += 1
        currentModule = modules['broadcaster']
        signal = currentModule.updateState(0, None)
        q = deque([(currentModule, signal)])

        while q:
            currentModule, signal = q.popleft()
            for con in currentModule.connections:
                if signal:
                    high += 1
                else:
                    low += 1

                if modules.get(con):
                    if signal and modules[con].id == 'nr':
                        if not moduleRx.get(currentModule.id):
                            moduleRx[currentModule.id] = i + 1
                        if set(moduleRx) == set(modules[con].inputs):
                            return part1, math.lcm(*moduleRx.values())

                    newSignal = modules[con].updateState(signal, currentModule.id)

                    if newSignal is not None:
                        q.append((modules[con], newSignal))

    return high * low

def parseInput(inputFile, modules, callback):
    for line in open(inputFile, 'r').read().splitlines():
        module, connections = line.strip().split(' -> ')
        connections = connections.split(', ')
        id = module.strip('&%')
        callback(modules, module, id, connections)

def initModules(modules, module, id, connections):
    if '%' in module:
        current = FlipFlop(id, connections)
    elif '&' in module:
        current = Conjunction(id, connections)
    else:
        current = BroadCaster(connections)

    modules[id] = current

def initInputs(modules: dict[str, Module], module: Module, id, connections):
    for con in connections:
        if modules.get(con):
            modules[con].inputs[id] = False
        

def day20():
    inputFile = 'input.txt'
    modules: dict[str, Module] = {}
    parseInput(inputFile, modules, initModules)
    parseInput(inputFile, modules, initInputs)

    return solve(modules)

print(day20())
class HardwareAbstractionLayer:
    def __init__(self):
        self.cpu = "Intel CPU"
        self.gpu = "Intel GPU"
        self.npu = "Intel NPU"
    
    def initialize(self):
        print(f"Initializing hardware: {self.cpu}, {self.gpu}, {self.npu}")

class Scheduler:
    def __init__(self, config, hardware_layer):
        self.hardware_layer = hardware_layer
        self.max_cpu_usage = config["max_cpu_usage"]
        self.max_gpu_usage = config["max_gpu_usage"]
        self.max_npu_usage = config["max_npu_usage"]

    def process_tiles(self, tiles, model):
        results = []
        for tile in tiles:
            # Example: Assign tile to CPU
            result = model(tile)
            results.append(result)
        return torch.cat(results, dim=1)

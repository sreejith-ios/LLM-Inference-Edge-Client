class TilingModule:
    def __init__(self, config):
        self.tile_size = config["tile_size"]

    def partition_input(self, tokens):
        return [tokens[i:i + self.tile_size] for i in range(0, len(tokens), self.tile_size)]

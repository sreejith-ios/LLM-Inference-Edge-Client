import logging
from utility.configuration_module import ConfigurationModule
from utility.logging_module import setup_logging
from application.inference_engine import InferenceEngine
from data_access.hardware_abstraction_layer import HardwareAbstractionLayer
from service.tiling import TilingModule
from service.scheduler import Scheduler

def main():
    # Setup logging
    setup_logging()
    logging.info("Initializing the LLM Inference Optimization Module...")
    
    # Load configurations
    config = ConfigurationModule.load_config("config.json")
    logging.info("Configuration loaded successfully.")
    
    # Initialize hardware
    hardware_layer = HardwareAbstractionLayer()
    hardware_layer.initialize()
    
    # Setup Tiling and Scheduler
    tiling_module = TilingModule(config["tiling"])
    scheduler = Scheduler(config["scheduler"], hardware_layer)
    
    # Initialize and run inference engine
    model_name_or_path = config["model"]["path"]
    inference_engine = InferenceEngine(model_name_or_path, tiling_module, scheduler)
    output = inference_engine.run_inference("Example input text")
    logging.info(f"Inference output: {output}")

if __name__ == "__main__":
    main()

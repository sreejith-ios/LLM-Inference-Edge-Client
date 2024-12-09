# LLM Edge Inference Client

**LLM Edge Inference Client** is a modular system designed to enable efficient, scalable, and maintainable large language model (LLM) inference on edge devices. By leveraging a dynamic orchestration architecture, this client optimizes workloads across CPUs, GPUs, and NPUs through a unified Hardware Abstraction Layer (HAL), ensuring both flexibility and performance.

---

## Table of Contents

1. [Overview](#overview)  
2. [High-Level Architecture](#high-level-architecture)  
   - [Layers and Their Responsibilities](#layers-and-their-responsibilities)  
   - [Data Flow](#data-flow)  
3. [Key Components](#key-components)  
   - [CLI Layer](#cli-layer)  
   - [Application Layer](#application-layer)  
   - [Service Layer](#service-layer)  
   - [Data Access Layer](#data-access-layer)  
   - [Hardware Layer](#hardware-layer)  
   - [Utility Modules](#utility-modules)  
4. [Codebase Organization](#codebase-organization)  
   - [Directory Structure](#directory-structure)  
   - [Module Descriptions](#module-descriptions)  
5. [Getting Started](#getting-started)  
6. [Configuration](#configuration)  
7. [Logging & Monitoring](#logging--monitoring)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## Overview

As the capabilities of edge devices advance, the demand for on-device LLM inference grows. The **LLM Edge Inference Client** addresses this challenge by providing a layered and modular architecture. It abstracts away hardware complexity, enabling seamless integration of various accelerators and simplifying the process of scaling and maintaining LLM-driven applications at the edge.

Key benefits of this architecture include:

- **Modularity:** Clearly separated concerns simplify updates and maintenance.
- **Scalability:** Easily integrate new hardware accelerators or additional devices.
- **Adaptability:** The Hardware Abstraction Layer shields upper layers from vendor-specific APIs, ensuring compatibility as hardware evolves.
- **Performance:** Dynamic scheduling and tiling efficiently utilize all available compute resources.

---

## High-Level Architecture

The system’s architecture is structured into distinct layers. Each layer focuses on a specific aspect of the inference pipeline, improving maintainability and extensibility.

### Layers and Their Responsibilities

1. **CLI Layer**  
   - **User Input Parser:** Interprets and validates user commands or queries.  
   - **Output Display:** Presents results to the user.

2. **Application Layer**  
   - **LLM Inference Engine:** Manages the inference logic, including prompt processing and model execution.

3. **Service Layer**  
   - **Tiling Module:** Breaks down large inference tasks into manageable tiles.  
   - **Dynamic Scheduler Module:** Allocates and balances tiles across available compute resources.

4. **Data Access Layer**  
   - **Hardware Abstraction Layer (HAL):** Provides a uniform interface to interact with CPUs, GPUs, and NPUs, hiding hardware-specific complexities.

5. **Hardware Layer**  
   - **CPU, GPU, NPU:** The actual compute resources that execute inference tasks.

6. **Utility Modules**  
   - **Logging Module:** Captures system events and application logs.  
   - **Performance Monitor:** Tracks system metrics (e.g., latency, throughput).  
   - **Configuration Module:** Manages runtime parameters and system settings.

### Data Flow

1. **Input Parsing (CLI Layer):**  
   User inputs are parsed, validated, and normalized.

2. **Inference Request (Application Layer):**  
   The LLM Inference Engine processes the request, prepares tokens, and sets inference parameters.

3. **Task Management (Service Layer):**  
   - **Tiling Module** divides the inference request into smaller units (tiles) for parallelization.  
   - **Dynamic Scheduler** assigns these tiles to the available hardware units based on load and performance metrics.

4. **Hardware Interaction (Data Access Layer):**  
   The HAL translates these tasks into low-level instructions, interacting with CPUs, GPUs, and NPUs without exposing hardware-specific details.

5. **Execution (Hardware Layer):**  
   The hardware resources run the inference tasks and return the computed results.

6. **Results & Logging (Utility Modules):**  
   Final results are collected, logged, and monitored. The system metrics are updated and configuration checks ensure correct operation. Outputs are then displayed to the user.

---

## Key Components

### CLI Layer

- **User Input Parser:** Validates and interprets user commands.  
- **Output Display:** Renders the inference results and any status messages.

### Application Layer

- **LLM Inference Engine:**  
  - Tokenizes input prompts.  
  - Runs inference on the underlying model.  
  - Returns generated responses.

### Service Layer

- **Tiling Module:**  
  - Splits large inference requests for efficient parallel processing.  
  - Improves utilization of hardware resources.

- **Dynamic Scheduler Module:**  
  - Allocates tiles to available compute units.  
  - Adapts scheduling decisions based on real-time performance metrics.

### Data Access Layer

- **Hardware Abstraction Layer (HAL):**  
  - Provides a stable API that upper layers use to submit work.  
  - Translates high-level commands into hardware-specific execution calls.

### Hardware Layer

- **CPU, GPU, NPU:**  
  - Executes low-level instructions provided by the HAL.  
  - Delivers computation results back to the higher layers.

### Utility Modules

- **Logging Module:**  
  - Records system and application-level logs for debugging and auditing.

- **Performance Monitor:**  
  - Collects runtime metrics such as latency, resource utilization, and throughput.

- **Configuration Module:**  
  - Loads and applies settings from configuration files or environment variables.  
  - Adjusts parameters like model selection, batch size, and hardware allocation strategies.

---

## Codebase Organization

### Directory Structure

```bash
llm-edge-inference-client/
├─ cli/
│  ├─ input_parser.py
│  ├─ output_display.py
│  └─ __init__.py
├─ application/
│  ├─ llm_inference_engine.py
│  ├─ model/
│  │  ├─ tokenizer.py
│  │  ├─ model_wrapper.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ service/
│  ├─ tiling_module.py
│  ├─ dynamic_scheduler.py
│  └─ __init__.py
├─ data_access/
│  ├─ hardware_abstraction_layer.py
│  ├─ device_drivers/
│  │  ├─ cpu_driver.py
│  │  ├─ gpu_driver.py
│  │  ├─ npu_driver.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ hardware/
│  ├─ cpu/
│  ├─ gpu/
│  ├─ npu/
│  └─ __init__.py
├─ utility/
│  ├─ logging_module.py
│  ├─ performance_monitor.py
│  ├─ configuration_module.py
│  └─ __init__.py
└─ tests/
   ├─ unit/
   ├─ integration/
   └─ __init__.py


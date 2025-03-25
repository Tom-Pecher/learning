
### GPU Introduction

CPUs (Central Processing Units):
 - General purpose
 - High clock speed
 - Few cores
 - High cache
 - Low latency
 - Low throughput

GPUs (Graphics Processing Units):
 - Specialised
 - Low clock speed
 - Many cores
 - Low cache
 - High latency
 - High throughput

TPUs (Tensor Processing Units):
 - Specialised GPUs for deep learning algorithms (matrix multiplication)
 - Higher cost, industry level, less accessible to consumers (hence why we work with GPUs)

FPGAs (Field Programmable Gate Arrays):
 - Specialised hardware that can be custom-made for specific tasks
 - Very high cost
 - Very low latency
 - Very high throughput
 - Very high power consumption

Key terms:
    Host (CPU):
 - Goal: minimise time for single task
 - Metric: latency (seconds)

    Device (GPU):
 - Goal: maximise tasks per second
 - Metric: throughtput (e.g. pixels per millisecond)

    Kernel (GPU kernel)
    

Typical CUDA program:
 - CPU allocates CPU memory
 - CPU copies data to GPU
 - CPU launches kernel on GPU (processing is done in GPU)
 - CPU copies result from GPU back to CPU and does something with it



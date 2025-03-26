
#include <stdio.h>

// A kernel is a special function that runs on your GPU (Graphics Card) instead of your CPU. 
// Think of it like giving instructions to a large team of workers (GPU threads) who can all work at the same time. 
// You mark a kernel with __global__ keyword, and it can only return void. Example:
__global__ void whoami(void) {
    // The grid represents the entire set of threads launched for a single kernel invocation. 
    // Think of it as the overall execution space. It's a collection of thread blocks.

    // A block is a group of threads that can cooperate and share data quickly through shared memory.
    // Threads within a block can share memory, synchronize with each other and cooperate on tasks:
    int block_id =
        blockIdx.x +
        blockIdx.y * gridDim.x +
        blockIdx.z * gridDim.x * gridDim.y;

    int block_offset =
        block_id *
        blockDim.x * blockDim.y * blockDim.z;

    // Warps are a group of threads that are executed together within a block.
    // Each warp is inside of a block and parallelizes 32 threads.
    // Threads in a warp share memory in an L1 cache so they can communicate quickly.
    // Instructions are issued to warps that then tell the threads what to do (not directly sent to threads).

    // The thread is the smallest unit of execution in CUDA. Each thread executes the kernel code independently. 
    // Within a block, threads are identified by a unique thread ID. 
    // This ID allows you to access specific data or perform different operations based on the thread's position within the block:
    int thread_offset =
        threadIdx.x +  
        threadIdx.y * blockDim.x +
        threadIdx.z * blockDim.x * blockDim.y;

    int id = block_offset + thread_offset; // the global id

    printf("%04d | Block(%d %d %d) = %3d | Thread(%d %d %d) = %3d\n",
        id,
        blockIdx.x, blockIdx.y, blockIdx.z, block_id,
        threadIdx.x, threadIdx.y, threadIdx.z, thread_offset);
}

int main(int argc, char **argv) {
    const int b_x = 2, b_y = 3, b_z = 4;
    const int t_x = 4, t_y = 4, t_z = 4; // the max warp size is 32, so 
    // we will get 2 warp of 32 threads per block

    int blocks_per_grid = b_x * b_y * b_z;
    int threads_per_block = t_x * t_y * t_z;

    printf("%d blocks/grid\n", blocks_per_grid);
    printf("%d threads/block\n", threads_per_block);
    printf("%d total threads\n", blocks_per_grid * threads_per_block);

    dim3 blocksPerGrid(b_x, b_y, b_z); // 3d cube of shape 2*3*4 = 24
    dim3 threadsPerBlock(t_x, t_y, t_z); // 3d cube of shape 4*4*4 = 64

    whoami<<<blocksPerGrid, threadsPerBlock>>>();
    cudaDeviceSynchronize();
}

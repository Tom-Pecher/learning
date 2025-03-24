
#include <iostream>

__global__ void hello_kernel() {
    printf("Hello, World! from GPU thread %d\n", threadIdx.x);
}

int main() {
    hello_kernel<<<1, 10>>>();
    cudaDeviceSynchronize();
    
    return 0;
}

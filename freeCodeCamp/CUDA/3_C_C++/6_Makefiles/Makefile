
# If clean exists in directory, it will be used instead of the default clean target (hence we use .PHONY to specify to instead run the clean target).
.PHONY clean

# Define Variables:
GCC = gcc
NVCC = nvcc
CUDA_FLAGS = -arch=sm_86

# Define Targets:
01:	# Running "make 01" will run "gcc 01.c -o 01"
	@$(GCC) -o 01 01.c 	 # The @ symbol is used to execute the command in a separate shell (prevents command appearing in the terminal).

02:
	@$(NVCC) $(CUDA_FLAGS) -o 02 02.cu
	@./02 	# Also run the executable.

03: 01 02  # Run other targets.

clean:
	rm -f 01 02 	# Remove the executables.
	
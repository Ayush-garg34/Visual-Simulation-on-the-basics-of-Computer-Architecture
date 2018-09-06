## How to visualize the code
In the folder there is a file named input.txt.

Write the code there in the specified syntax. There is also an example code given in the file. Please be carefull of the spaces and syntax as mentioned in the report.

Then we first compile the code, for that open the compiler.py file in any python compiler and run the code. On running the code, the python terminal will list the sequence of asseembly instructions compiled from the code given in input.txt by the user.The same instructions will also be stored along with the memory location of the defined variables in a separate file in the same folder named compiler_output.txt.

Next, we open the assembler.py in python compiler and run the code. It will take compiler_output.txt as the input.Hence, the compiler.py must be executed before assembler.py. On running the code, the python terminal will list all the instructions in the file along with their equivalent binary representation.

In the end, to visualize the memory organisation, we need to run mem_display.py code. On running the code, a seperate window will open up with different components of the memory organisation . Let the window load completely and all things settle. Once the screen is loaded completely one can scroll up and down to see various components like PC, registers, also the division in the memory - instructions at the bottom, gloabal variables in middle and stack space at the top. Now on each click by the user, instructions are execute one by one. Each instruction requires time to execute. After clicking once, wait for the instruction to execute completely. Also, there are comments displayed in the lower right corner in case one needs to understand the working of the instruction.

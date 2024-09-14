# This is a Bash Script that creates a C dynamic or shared library.
# Simply compile to create a dynamic library.

#!/bin/bash
echo -e "\e[1;32m Compiling .c files into object files ... \e[0m"
gcc -fPIC -c *.c
echo -e "\e[1;32m\nDone.\n\nCreating shared library liball.so ...\e[0m"
gcc -shared *.o -o liball.so
echo -e "\e[1;32m\nDone.\n\nInspecting and displaying list of symbols in liball.so ...\e[0m"
nm -D liball.so
echo -e "\e[1;32m\nDone.\n\nExporting your shared library to your system's shared library search path...\e[0m"
export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
echo -e "\e[1;32m\nDone.\n\n\n\e[0m"
echo -e "\e[1;32mCongratulations $USER!\nYou have successfully created a C dynamic library.\n\e[0m"

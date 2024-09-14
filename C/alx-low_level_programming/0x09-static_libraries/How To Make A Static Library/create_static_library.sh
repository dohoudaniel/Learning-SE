# This is a Bash Script that creates a C static library.
# Simply compile to create a static library.

#!/bin/bash
echo -e "\e[1;32m Compiling .c files into object files... \e[0m"
gcc -Wall -pedantic -Werror -Wextra -std=gnu89 -c *.c
echo -e "\e[1;32m\nDone.\n\nCreating static library libname.a...\e[0m"
ar -rc libname.a *.o
echo -e "\e[1;32m\nDone.\n\nListing object files in libname.a...\e[0m"
ar -t libmane.a
echo -e "\e[1;32m\nDone.\n\nInspecting and displaying list of symbols in libmane.a...\e[0m"
nm libname.a
echo -e "\e[1;32m\nDone.\n\nIndexing libname.a for the advantage of faster symbol-lookup by the compiler...\e[0m"
ranlib libname.a
echo -e "\e[1;32m\nDone.\n\n\n\e[0m"
echo -e "\e[1;32mCongratulations $USER!\nYou have successfully created a C static library.\n\e[0m"
echo

#!/usr/bin/env bash
# A Bash script that installs everything I need to prepare for the malloc and free challenge
sudo apt update
sudo apt upgrade
sudo apt install build-essential
sudo apt install gcc
gcc --version
sudo apt install git
sudo apt install make
sudo apt install valgrind
sudo apt install libcunit1 libcunit1-dev
pkg-config --modversion cunit
echo "Creating a C file..."
echo "#include <CUnit/CUnit.h>
#include <CUnit/Basic.h>

void test_example(void) {
    CU_ASSERT(1 == 1);
}

int main() {
    CU_initialize_registry();
    CU_pSuite suite = CU_add_suite("Example Suite", NULL, NULL);
    CU_add_test(suite, "Example Test", test_example);
    CU_basic_set_mode(CU_BRM_VERBOSE);
    CU_basic_run_tests();
    CU_cleanup_registry();
    return CU_get_error();
}" > test.c
gcc -o test test.c -lcunit
./test
sudo apt install check                    # For Check
sudo apt install gdb
pip3 install alx-utils
sudo apt install gcc+

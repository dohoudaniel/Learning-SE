#!/usr/bin/python3

if __name__ == "__main__":
    """Prints trhe addition of all the entered arguments"""
    import sys
    
    total = 0
    
    for i in range(len(sys.argv) - 1):
        total = total + int(sys.argv[i + 1])
        # Typecasting to an int
        
    print("{}".format(total))


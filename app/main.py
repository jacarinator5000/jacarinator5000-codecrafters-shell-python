import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()
    
    # read command from stdin
    command = input()
     
    # print error message for invalid command
    sys.stdout.write(f"{command}: command not found\n")
    main()

if __name__ == "__main__":
    main()

import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # read command from stdin
        line = input().strip()
        if not line:
            continue
        
        parts = line.split()
        command = parts[0].lower()
        args = parts[1:]

        # command for exiting shell
        if command == "exit":
            sys.exit()

        # print arguments to stdout
        elif command == "echo":
            sys.stdout.write("".join(args) + "\n")

        # print error message for invalid command
        else:
            sys.stdout.write(f"{command}: command not found\n")    
    

if __name__ == "__main__":
    main()

from assistant import handle_command
from logger import log_operation

def main():
    print("Welcome to your Virtual Assistant!")
    while True:
        command = input("How can I assist you? (type 'exit' to quit): ").strip()
        if command.lower() == 'exit':
            break
        response = handle_command(command)
        print(response)
        log_operation(command, response)

if __name__ == "__main__":
    main()
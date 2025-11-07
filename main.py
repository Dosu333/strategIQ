from agents.orchestrator import get_response


def main():
    print("Welcome to StrategIQ")
    print("Type 'exit' to end the conversation")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for visiting! Goodbye!")
            break

        response = get_response(user_input)
        print(f"StrategIQ: {response}\n")


if __name__ == "__main__":
    main()

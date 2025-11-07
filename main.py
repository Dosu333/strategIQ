from agent import get_response


def main():
    print("Welcome to StrategIQ")
    print("Enter a prompt to get started")

    while True:
        prompt = input("Enter a prompt: ")
        response = get_response(prompt)
        print(response)


if __name__ == "__main__":
    main()

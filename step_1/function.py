def read_input():
    return "some input"


def do_calculation(data):
    return data + " " + data


def send_email(body, to):
    # some magic that sends the email
    return True


def main():
    inputValue = read_input()
    result = do_calculation(inputValue)
    send_emailResult(result, "asdfgh@gmail.com")
    if send_emailResult == True:
        print("send email successful")
    else:
        print("Send email UNSUCCESSFUL")


main()

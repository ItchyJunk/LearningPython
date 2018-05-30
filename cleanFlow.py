def bool_response(msg):
    """Get a boolean response from user input.

    Arguments
    ---------
    msg : str
        Display message.

    Returns
    -------
    A boolean value.
    """
    while True:
        response = input(msg).lower()

        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("{} is not a valid choice".format(response))


while True:
    if bool_response("Is it raining? (yes/no)? "):
        if bool_response("Do you have an umbrella (yes/no)? "):
            break
        else:
            print("Wait a while.")
    else:
        break

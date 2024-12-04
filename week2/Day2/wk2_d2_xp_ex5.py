#Exercise 5 : Let’s create some personalized shirts !

def make_shirt(size="Large", text="I love Python"):
    """Prints a summary of the shirt size and message.
    :param size: The size of the shirt (default is 'large').
    :param text: The text to be printed on the shirt (default is 'I love Python').
    """
    print(f"The size of the shirt is {size} and text is '{text}'.")

    make_shirt()

    make_shirt(size="Medium")

    make_shirt(size="Small", text="life")

    make_shirt(text="Custom Message", size="Extrsa large")
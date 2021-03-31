def format_position(lat, long):  # defined function
    formatedPosition = "Lat: {} - Long: {}".format(
        lat, long
    )  # assigned variable inside function. format looks for curly braces and replaces with lat long
    return formatedPosition


# call function to use
print(format_position(-52.33, 120.00))

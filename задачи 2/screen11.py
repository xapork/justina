def nezvannye (list):
    for guests in list:
        print("Hello, {}! We don't want to see y'all!".format(guests))
guests = ["Alice", "Bob", "Charlie"]
nezvannye(guests)

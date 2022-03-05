from src.build_segments import *

def pal(*args, tail=False):
    final_outcome = []
    """
    Checks if user is passing multiple lists to process,
    if not it will pass the arguments of args on their own in the else
    statement.
    """
    if isinstance(args[0], tuple):
        for arg in args:
            if isinstance(args, tuple):
                if len(args) < 2:
                    return("Must pass required arguments")
                else:
                    """
                    Checks to make sure the percent is real,
                    right now, it doesn't handle partitioning above 50% properly.
                    """
                    if arg[1] not in range(0, 101):
                        print("Division of group must be a valid percent from 0 to 100")
                    elif 100 / arg[1] > len(arg[0]):
                        print(f"Cannot divide {arg[0]} into that many slices")
                    else:
                        final_outcome.append(segment_builder(arg, tail))
            else:
                return("{arg} passed is not a tuple, skipping this argument")
    else:
        return(segment_builder(args, tail))

    return final_outcome
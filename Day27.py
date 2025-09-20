# Timer: Start a timer, stop it with a keypress, and show elapsed time. Use "time" module.

# import time module
import time

# function to calculate elapsed time between two key presses
def start_timer():
    '''
    Calculate elapsed time between two key presses.
    returns elapsed time in seconds.
    '''
    input("⏱️ Press Enter to start the timer...")
    start = time.time()
    input("⌛ Press Enter again to stop the timer...")
    end = time.time()

    elapsed = end - start
    print(f"⏲️ Elapsed time: {elapsed:.2f} seconds.")

# Run the timer
start_timer()


# End of code

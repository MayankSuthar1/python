import time

def stopwatch():
    start_time = time.time()
    print("Stopwatch started. Press Ctrl+C to stop.")

    try:
        while True:
            elapsed_time = time.time() - start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

            timer = "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, milliseconds)
            print(timer, end="\r")
            time.sleep(0.001)  # Sleep for 1 millisecond

    except KeyboardInterrupt:
        print("\nStopwatch stopped.")

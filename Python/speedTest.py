import speedtest
from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread
import socket

done = False


def animate():
    for c in cycle(['|', '/', '-', '\\']):
        if done:
            break
        terminal.write('\rTesting ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\rDone!')
    terminal.flush()


# Check for a connection
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def network_check():
    if not is_connected():
        print("No internet connection.")
        return False, None

    try:
        s = speedtest.Speedtest()
        s.get_best_server()
        return True, s
    except speedtest.ConfigRetrievalError:
        print("Failed to retrieve configuration. Please check your network settings.")
        return False, None


# Function to turn the bytes result into megabytes
def bytes_to_mb(bytes):
    kb = 1024
    mb = kb * 1024
    return int(bytes / mb)


# Tests
def setup(speedtest_instance):
    test_arr = ["download", "upload", "ping", "run_all"]
    selection = input("Tests Available:\n For download speed test, press 1.\n For Upload speed test, press 2.\n "
                      "For Ping, press 3.\n To run all tests, press 4\n")
    test = test_arr[int(selection) - 1]
    best_server = speedtest_instance.get_best_server()

    return test, test_arr, best_server


# Takes the test selected by the user and runs that test
def run_selected_test(test, test_arr, best_server, s):
    # Loading animation
    print(f"\nTesting {test} speed on server: {best_server}\n")
    global done
    done = False
    t = Thread(target=animate)
    t.start()

    if test == "download":
        download_speed = bytes_to_mb(s.download())
        print("\nYour Download speed is:", download_speed, "Mbits/s\n")

    elif test == "upload":
        upload_speed = bytes_to_mb(s.upload())
        print("Your Upload speed is:", upload_speed, "Mbits/s\n")

    elif test == "ping":
        s.get_servers([])
        ping = s.results.ping
        print("Your current ping is:", ping, "ms\n")

    elif test == "run_all":
        download_speed = bytes_to_mb(s.download())
        upload_speed = bytes_to_mb(s.upload())
        s.get_servers([])
        ping = s.results.ping
        print("\nYour Download speed is:", download_speed, "Mbits/s\n")
        print("Your Upload speed is:", upload_speed, "Mbits/s\n")
        print("Your current ping is:", ping, "ms\n")

    done = True
    t.join()

    print("\nPress 1 to return to the main menu or 2 to exit.\nConfirm your choice by pressing Enter.")
    choice = input()
    while choice != "1" and choice != "2":
        print("Invalid selection. Please try again.")
        choice = input()
    if choice == "1":
        main()
    else:
        exit("Program will now exit.")


def main():
    connected, speedtest_instance = network_check()
    if connected:
        test, test_arr, best_server = setup(speedtest_instance)
        run_selected_test(test, test_arr, best_server, speedtest_instance)
    else:
        exit("Program will now exit.")


if __name__ == "__main__":
    main()

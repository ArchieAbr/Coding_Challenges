import speedtest
from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread


# TODO: Write a statement that deals with null connections

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


s = speedtest.Speedtest()


# Function to turn the bytes result into megabytes
def bytes_to_mb(bytes):
    kb = 1024
    mb = kb * 1024
    return int(bytes / mb)


# Tests
def setup():
    test_arr = ["download", "upload", "ping", "run_all"]
    selection = input("Tests Available:\n For download speed test, press 1.\n For Upload speed test, press 2.\n "
                      "For Ping, press 3.\n To run all tests, press 4\n")
    test = test_arr[int(selection) - 1]
    best_server = s.get_best_server()

    return test, test_arr, best_server


# Takes the test selected by the user and runs that test
def run_selected_test(test, test_arr, best_server):
    i = 0
    for i in test_arr:
        if test == "download":
            print("\nTesting Download speed... on server:", best_server, "\n")
            global done
            done = False
            t = Thread(target=animate)
            t.start()
            download_speed = bytes_to_mb(s.download())
            print("\nYour Download speed is:", download_speed, "MB/s\n")
            done = True
            break
        elif test == "upload":
            print("\nTesting Upload speed... on server:", best_server, "\n")
            done = False
            t = Thread(target=animate)
            t.start()
            upload_speed = bytes_to_mb(s.upload())
            print("Your Upload speed is:", upload_speed, "MB/s\n")
            done = True
            break
        elif test == "ping":
            done = False
            t = Thread(target=animate)
            t.start()
            s.get_servers([])
            ping = s.results.ping
            print("Your current ping is:", ping, "ms\n")
            done = True
            break
        elif test == "run_all":
            print("\nTesting on sever", best_server, "\n")
            done = False
            t = Thread(target=animate)
            t.start()
            download_speed = bytes_to_mb(s.download())
            upload_speed = bytes_to_mb(s.upload())
            s.get_servers([])
            ping = s.results.ping

            print("\nYour Download speed is:", download_speed, "MB/s\n")
            print("Your Upload speed is:", upload_speed, "MB/s\n")
            print("Your current ping is:", ping, "ms\n")
            print("Program will now exit\n")
            done = True
            break
        else:
            print("Invalid selection. Please try again.")
            break


def main():
    # Handle the case where the user has no internet connection
    try:
        s.get_best_server()
    except speedtest.NoMatchedServers:
        print("No servers available. Please check your internet connection.")
        exit()
    test, test_arr, closest_server = setup()
    run_selected_test(test, test_arr, closest_server)


if __name__ == "__main__":
    main()

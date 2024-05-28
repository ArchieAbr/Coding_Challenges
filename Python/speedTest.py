import speedtest

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

    return test, test_arr


# Takes the test selected by the user and runs that test
def run_selected_test(test, test_arr):
    i = 0
    for i in test_arr:
        if test == "download":
            download_speed = bytes_to_mb(s.download())
            print("Your Download speed is:", download_speed, "MB/s\n")
            break
        elif test == "upload":
            upload_speed = bytes_to_mb(s.upload())
            print("Your Upload speed is:", upload_speed, "MB/s\n")
            break
        elif test == "ping":
            s.get_servers([])
            ping = s.results.ping
            print("Your current ping is:", ping)
            break
        elif test == "run_all":
            download_speed = bytes_to_mb(s.download())
            upload_speed = bytes_to_mb(s.upload())
            s.get_servers([])
            ping = s.results.ping
            print("Your Download speed is:", download_speed, "MB/s\n")
            print("Your Upload speed is:", upload_speed, "MB/s\n")
            print("Your current ping is:", ping)
            print("Program will now exit")
            break
        else:
            print("Invalid selection. Please try again.")
            break


test, test_arr = setup()
run_selected_test(test, test_arr)

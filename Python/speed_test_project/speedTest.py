import speedtest
from time import sleep
from itertools import cycle
from threading import Thread
import socket
from sys import stdout as terminal
from sys import exit
import csv
import os
from datetime import datetime

done = False

# TODO: Create a routine that deals with exceptionally low network speeds
# At the moment the app is running the network_check() routine which will fail for super slow networks


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
        # Tests for internet connection by pinging google.com
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


# Store results in CSV and HTML files
def store_result(data):
    # Write to CSV
    file_exists = os.path.isfile('speedtest_results.csv')
    with open('speedtest_results.csv', 'a', newline='') as csvfile:
        fieldnames = ['date', 'time', 'download', 'upload', 'ping']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

    # Write to HTML
    html_content = f"""
<html>
<head>
    <title>Speed Test Results</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
        .table thead th {{
            background-color: #4CAF50; /* Green */
            color: white;
        }}
        .table tbody tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>Speed Test Results</h1>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">Date</th>
                <th scope="col">Time</th>
                <th scope="col">Download Speed</th>
                <th scope="col">Upload Speed</th>
                <th scope="col">Ping</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{data['date']}</td>
                <td>{data['time']}</td>
                <td>{data.get('download', 'N/A')} Mbits/s</td>
                <td>{data.get('upload', 'N/A')} Mbits/s</td>
                <td>{data.get('ping', 'N/A')} ms</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

    with open('speedtest_results.html', 'a') as f:
        f.write(html_content)

    # Print link to the HTML file
    html_file_path = os.path.abspath('speedtest_results.html')
    print(f"Results have been saved. You can view them at: file://{html_file_path}")


# Tests
def setup(speedtest_instance):
    test_arr = ["run_all", "download", "upload", "ping"]
    selection = input("Tests Available:\n to run all tests, press 1.\n For Upload speed test, press 2.\n " # Archie: Edited test orders (for Matt)
                      "For Ping, press 3.\n To test ping, press 4\n")
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

    # Get the current date and time
    timestamp = datetime.now()
    date = timestamp.strftime("%Y-%m-%d")
    time = timestamp.strftime("%H:%M:%S")

    if test == "download":
        download_speed = bytes_to_mb(s.download())
        print("\nYour Download speed is:", download_speed, "Mbits/s\n")
        store_result({'date': date, 'time': time, 'download': download_speed, 'upload': 'N/A', 'ping': 'N/A'})

    elif test == "upload":
        upload_speed = bytes_to_mb(s.upload())
        print("Your Upload speed is:", upload_speed, "Mbits/s\n")
        store_result({'date': date, 'time': time, 'download': 'N/A', 'upload': upload_speed, 'ping': 'N/A'})

    elif test == "ping":
        s.get_servers([])
        ping = s.results.ping
        print("Your current ping is:", ping, "ms\n")
        store_result({'date': date, 'time': time, 'download': 'N/A', 'upload': 'N/A', 'ping': ping})

    elif test == "run_all":
        download_speed = bytes_to_mb(s.download())
        upload_speed = bytes_to_mb(s.upload())
        s.get_servers([])
        ping = s.results.ping
        print("\nYour Download speed is:", download_speed, "Mbits/s\n")
        print("Your Upload speed is:", upload_speed, "Mbits/s\n")
        print("Your current ping is:", ping, "ms\n")
        store_result({'date': date, 'time': time, 'download': download_speed, 'upload': upload_speed, 'ping': ping})

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


# Main function
def main():
    connected, speedtest_instance = network_check()
    if connected:
        test, test_arr, best_server = setup(speedtest_instance)
        run_selected_test(test, test_arr, best_server, speedtest_instance)
    else:
        exit("Program will now exit.")


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
import threading
import speedtest
import socket


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def network_check():
    if not is_connected():
        print("No internet connection.")
        return False, None

    try:
        s = speedtest.Speedtest()
        best_server = s.get_best_server()
        server_info.set(f"Testing on server: {best_server['host']} in {best_server['name']}, {best_server['country']}")
        return True, s
    except speedtest.ConfigRetrievalError:
        print("Failed to retrieve configuration.")
        return False, None


def bytes_to_mb(bytes):
    kb = 1024
    mb = kb * 1024
    return int(bytes / mb)


def update_results(test_type, result):
    labels[test_type].config(
        text=f"{test_type} Speed: {result} Mbps" if test_type != 'Latency' else f"Latency: {result} ms")
    status_label.config(text=f"Completed {test_type} Test")
    progress.step(33.3)


def animate_dots(test_type):
    labels[test_type].config(text=f"{test_type} Speed: ..." if test_type != 'Latency' else "Latency: ...")


def threaded_test(speed_tester):
    root.after(0, progress.configure, {'value': 5})  # Pre-fill the bar slightly
    if speed_tester:
        root.after(0, animate_dots, 'Latency')
        speed_tester.get_servers([])
        latency = speed_tester.results.ping
        root.after(0, update_results, 'Latency', latency)
        root.after(0, animate_dots, 'Download')
        download_speed = bytes_to_mb(speed_tester.download())
        root.after(0, update_results, 'Download', download_speed)
        root.after(0, animate_dots, 'Upload')
        upload_speed = bytes_to_mb(speed_tester.upload())
        root.after(0, update_results, 'Upload', upload_speed)


def run_speed_test():
    status_label.config(text="Running Tests...")
    progress['value'] = 0  # Reset progress bar
    network_ok, speed_tester = network_check()
    if network_ok:
        threading.Thread(target=threaded_test, args=(speed_tester,)).start()


root = tk.Tk()
root.title("Speed Test 2.0")

style = ttk.Style(root)
style.theme_use('clam')
style.configure("TProgressbar", thickness=20, troughcolor='grey', background='blue', bordercolor='black',
                lightcolor='lightblue', darkcolor='darkblue')

main_frame = ttk.Frame(root, padding=(200, 200))
main_frame.grid()

title_label = ttk.Label(main_frame, text="Speed Test 2.0", font=("Helvetica", 72))
title_label.grid(row=0, column=0, columnspan=2)

server_info = tk.StringVar()
server_label = ttk.Label(main_frame, textvariable=server_info, font=("Helvetica", 25))
server_label.grid(row=1, column=0, columnspan=2)

status_label = ttk.Label(main_frame, text="Click start to run tests...", font=("Helvetica", 20))
status_label.grid(row=2, column=0, columnspan=2)

progress = ttk.Progressbar(main_frame, orient="horizontal", length=300, mode='determinate', maximum=100)
progress.grid(row=3, column=0, columnspan=2, pady=(10, 20))

start_button = ttk.Button(main_frame, text="Start Speed Test", command=run_speed_test)
start_button.grid(row=4, column=0, columnspan=2)

labels = {
    'Download': ttk.Label(main_frame, text="Download Speed: ", font=("Helvetica", 15)),
    'Upload': ttk.Label(main_frame, text="Upload Speed: ", font=("Helvetica", 15)),
    'Latency': ttk.Label(main_frame, text="Latency: ", font=("Helvetica", 15))
}

labels['Download'].grid(row=6, column=0, pady=(10, 0))
labels['Upload'].grid(row=7, column=0, pady=(10, 0))
labels['Latency'].grid(row=5, column=0, pady=(10, 0))

root.mainloop()

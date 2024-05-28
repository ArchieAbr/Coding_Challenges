import speedtest

s = speedtest.Speedtest()


# Function to turn the bytes result into megabytes
def bytes_to_mb(bytes):
    kb = 1024
    mb = kb * 1024
    return int(bytes / mb)


# Ping
s.get_servers([])
ping = s.results.ping

# Download speed test
download_speed = bytes_to_mb(s.download())

# Upload speed test
upload_speed = bytes_to_mb(s.upload())

print("Your download speed is:", download_speed, "MB/s\n")
print("Your upload speed is:", upload_speed, "MB/s\n")
print("Your current ping is:", ping)

import speedtest

s = speedtest.Speedtest()

# Ping
s.get_servers([])
ping = s.results.ping

# Download speed test
download_speed = s.download()

# Upload speed test
upload_speed = s.upload()

print("Your download speed is:", download_speed)
print("Your upload speed is:", upload_speed)
print("Your current ping is:", ping)


from ppadb.client import Client as AdbClient

client = AdbClient(host='127.0.0.1', port=5037)
devices = client.devices()

if len(devices) == 0:
    print('no devices')
    quit()

devices = devices[0]
print(f'Connected to {devices}')

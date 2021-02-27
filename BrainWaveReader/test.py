import bluetooth

try:
    address = "C4-64-E3-EA-60-FE" # Bluetooth address of EEG
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((address,1))
    # print(socket.getsockname())
    socket.setblocking(False)
    print("foo")
    # print(socket.last_event_code)
except:
    print("Failed")
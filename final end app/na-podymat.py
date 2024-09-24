from pysnmp.hlapi import *

def get_snmp_data(ip, oid):
    iterator = getCmd(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget((ip, 161)),
                      ContextData(),
                      ObjectType(ObjectIdentity(oid)))

    error_indication, error_status, error_index, var_binds = next(iterator)

    if error_indication:
        print(error_indication)
    elif error_status:
        print(f'{error_status.prettyPrint()} at {error_index and var_binds[int(error_index) - 1] or "?"}')
    else:
        for var_bind in var_binds:
            return var_bind.prettyPrint().split('=')[1].strip()

ip_address = '192.168.1.100'  # IP вашего принтера
serial_oid = '1.3.6.1.2.1.43.5.1.1.17.1'  # OID для серийного номера
serial_number = get_snmp_data(ip_address, serial_oid)
print(f'Serial number: {serial_number}')



import bluetooth

def get_bluetooth_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in nearby_devices:
        print(f"Address: {addr}, Name: {name}")

get_bluetooth_devices()

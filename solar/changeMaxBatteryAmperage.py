""" Scan Modbus registers to find valid registers"""
from pysolarmanv5 import PySolarmanV5
import requests

def main():
    modbus = PySolarmanV5(
        "192.168.0.123", 1234567890, port=8899, mb_slave_id=1, verbose=0
    )

    """Max charge current"""
    print(modbus.read_holding_registers(register_addr=108, quantity=1))

    """Change Max charge current"""
    modbus.write_multiple_holding_registers(register_addr=108, values=[4])

    """Max charge current new result"""
    print(modbus.read_holding_registers(register_addr=108, quantity=1))

if __name__ == "__main__":
    main()
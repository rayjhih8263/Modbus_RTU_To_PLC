import time
import serial
import time
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu

#cst.READ_COILS = 0x01
#cst.READ_DISCRETE_INPUTS = 0x02
#cst.READ_HOLDING_REGISTERS = 0x03
#cst.READ_INPUT_REGISTERS = 0x04
#cst.WRITE_SINGLE_COIL = 0x05
#cst.WRITE_SINGLE_REGISTER = 0x06
#WRITE_MULTIPLE_COILS = 0x15
#WRITE_MULTIPLE_REGISTERS = 0x16

class data:

    timeout = 100
    onoff = ['on','off']

    def __init__(self, comport, baudrate, databit, parity, stopbit):
        self.modbus_port = serial.Serial(port=comport, baudrate=baudrate, bytesize=databit, parity=parity, stopbits=stopbit)
        self.master = modbus_rtu.RtuMaster(self.modbus_port)
        self.master.set_timeout(self.timeout/1000.0)
        self.master._do_close()

    def parameter(self, id_address, function_code, data_address, data_quantity, data_value):
        self.id_address = id_address
        self.function_code = function_code
        self.data_address = data_address
        self.data_quantity = data_quantity
        self.data_value = data_value
        self.getdata()

    def getdata(self):
        self.master._do_open()
        try:
            a = 0
            rr = self.master.execute(self.id_address, self.function_code, self.data_address, self.data_quantity, self.data_value)
            for i in range(self.data_quantity):
                print(hex(self.data_address+a), rr[i])
                time.sleep(0.1)
                a = a+1
            print('===================================================')
        except Exception as e:
            print("modbus test Error: " + str(e))
        self.master._do_close()

    def status(self):
        return self.mb_port
        
        
if __name__=='__main__':
    a = data('COM15', 19200, 8, 'N', 1)
    a.parameter(15,cst.READ_HOLDING_REGISTERS,0x1000,0x8,0x00)
        




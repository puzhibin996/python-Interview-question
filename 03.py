import time

# 初始化菊水程控电源

import pyvisa

# 初始化资源管理器
rm = pyvisa.ResourceManager()

# 列出所有可用的设备
devices = rm.list_resources()
print("Available devices:", devices)

# 连接到菊水电源
# 这里假设电源的资源名称为 'USB0::0x0B3E::0x1003::XXXXXXXX::INSTR'
# 请根据实际情况修改
power_supply = rm.open_resource('USB0::0x0B3E::0x1049::DR001401::0::INSTR')

# 检查电源标识
print(power_supply.query('*IDN?'))

# 上电函数
def power_on():
    power_supply.write('OUTP ON')
    print("Power is ON")

# 下电函数
def power_off():
    power_supply.write('OUTP OFF')
    print("Power is OFF")

# 设置输出电压和电流
def set_voltage_current(voltage, current):
    power_supply.write(f'VOLT {voltage}')
    power_supply.write(f'CURR {current}')
    print(f"Voltage set to {voltage}V and Current set to {current}A")

# 关闭资源
def close_connection():
    power_supply.close()
    print("Connection closed")

# 示例使用
try:
    # set_voltage_current(13.5, 15.0)  # 设置输出电压为5V，电流为2A
    for i in range(100):
        time.sleep(0.4)
        power_on()  # 上电
    # 可以在此处添加其他控制逻辑，例如等待一段时间等
        time.sleep(0.4)
        power_off()  # 下电
finally:
    close_connection()

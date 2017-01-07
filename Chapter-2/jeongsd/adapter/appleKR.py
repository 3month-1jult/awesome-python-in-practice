#!/usr/bin/env python3

SUPPORT_VOLTAGE = 220

class Mac:
    def __init__(self, socket):
        self.socket = socket;

    def pushPowerButton(self):
        voltage = self.socket.getVoltage()
        if voltage > SUPPORT_VOLTAGE:
            print('폭발')
        elif voltage == SUPPORT_VOLTAGE:
            print('부팅중..')
        else:
            print('반응없음')

        if self.socket.hasEarth():
            print('접지 연결')

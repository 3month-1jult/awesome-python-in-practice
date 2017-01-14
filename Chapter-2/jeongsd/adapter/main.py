#!/usr/bin/env python3

import appleKR
import appleUS
import socket


def main():
    # 이 방에서는 TypeB(110v)를 사용한다
    wallSocket = socket.SocketTypeB();

    macUS = appleUS.Mac(wallSocket)
    print('us 맥 전원버튼 누르기')
    macUS.pushPowerButton()

    print('------------------------')

    macKR = appleKR.Mac(socket.TypeBtoTypeCAdapter(wallSocket))
    print('kr 맥 전원버튼 누르기')
    macKR.pushPowerButton()

if __name__ == "__main__":
    main()

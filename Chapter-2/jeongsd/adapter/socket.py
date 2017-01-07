#!/usr/bin/env python3

# https://namu.wiki/w/%EB%8B%A8%EC%9E%90/%EC%A0%84%EC%9B%90?from=%EC%BD%98%EC%84%BC%ED%8A%B8

# 미국 110v
class SocketTypeB:
    def __init__(self):
        self.voltage = 110

    def getVoltage(self):
        return self.voltage

    def hasEarth(self):
        return True

# 한국 220v
class SocketTypeC:
    def __init__(self):
        self.voltage = 220

    def getVoltage(self):
        return self.voltage

    def hasEarth(self):
        return False

# 돼지코 100v -> 220v
class TypeBtoTypeCAdapter:
    def __init__(self, socket):
        if not isinstance(socket, SocketTypeB):
            raise TypeError("올바르지 않은 소켓 타입입니다.")
        self.socket = socket

    def getVoltage(self):
        return 220

    def hasEarth(self):
        return self.socket.hasEarth();

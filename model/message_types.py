__author__ = 'susperius'

MESSAGE_TYPES = {0x01: "BEACON", 0x02: "SET_CONFIG", 0x03: "GET_CONFIG", 0x04: "OK", 0x05: "RESET", 0x06: "", 0xFF: "CRASH"}


def create_beacon(node_name, node_listener_port):
    return [0x01, [node_name, node_listener_port]]

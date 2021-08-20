import struct


TCP_HEAD = b'\xaa\xdd\xdd\xaa'
TCP_END = b'\xee\xdd'

LEN_HEAD = 4
LEN_LEN = 2
LEN_END = 2
LEN_TOTAL = 8


def cut_message_by_head(buffer):
    buffer_len = len(buffer)
    msg_with_head = bytes()
    idx = 0
    while idx <= buffer_len - LEN_HEAD:
        if buffer[idx:idx+LEN_HEAD] == TCP_HEAD:
            msg_with_head = buffer[idx:]
            break
        idx += 1
    return msg_with_head


def get_data_len(msg_with_head):
    data_len = 0
    msg_len = len(msg_with_head)
    miss_len = LEN_TOTAL - msg_len
    if miss_len <= 0:
        data_len = struct.unpack('!H', msg_with_head[LEN_HEAD:LEN_HEAD + LEN_LEN])[0]
        miss_len += data_len
    return data_len, miss_len


def decode_message(msg_with_head, data_len):
    data = bytes()
    error = ''
    msg_after = msg_with_head
    msg_len = len(msg_with_head)
    # DECODE
    if msg_len - LEN_HEAD - LEN_LEN - LEN_END - data_len >= 0:
        end = msg_with_head[LEN_HEAD + LEN_LEN + data_len:LEN_HEAD + LEN_LEN + data_len + LEN_END]
        if end == TCP_END:
            data = msg_with_head[LEN_HEAD + LEN_LEN:LEN_HEAD + LEN_LEN + data_len]
            msg_after = msg_with_head[LEN_HEAD + LEN_LEN + data_len + LEN_END:]
        else:
            error = 'DATA_BAD'
            msg_after = msg_with_head[LEN_HEAD:]
    return data, msg_after, error


def build_tx_message(data):
    msg = TCP_HEAD + struct.pack('!H', len(data)) + data + TCP_END
    return msg, len(msg)

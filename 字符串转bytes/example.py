bin_str_a = '3020231293123123'

bin_str_a_to_bytes = bin_str_a.encode('utf-8')
print(bin_str_a_to_bytes)


bin_str_a_to_hex = bytes.fromhex(bin_str_a)
print(bin_str_a_to_hex)

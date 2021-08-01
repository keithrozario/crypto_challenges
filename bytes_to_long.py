long_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
value = int.from_bytes(long_int, byteorder='big')
new_bytevalues = value.to_bytes(length=len(long_int), byteorder='big')
print(long_int.to_bytes(2, 'big'))
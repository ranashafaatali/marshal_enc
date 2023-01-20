import os


banner = '''
.____  __    _   ___        __   __
 /      |\   |  .'   \       |    | 
 |__.   | \  |  |      .---' |\  /| 
 |      |  \ |  |            | \/ | 
 /----/ |   \|   `.__,       /    /\n
  << Coded By Rana Shafaat Ali >>
    << The Multi Encryption >>
          << Marshal >>'''

try:
    import marshal
    os.system('clear')
    print(banner)
    __F = input('\n [•] Input script path: ')
    O__ = input('\n [•] Out putt path: ')
    try:
        __R = open(__F,'r').read()
    except:
        exit('\n script not found ')
    os.system(f'cp {__F} {O__}')
    for _ in range(20):
        cc = open(O__,'r').read()
        data = marshal.dumps(cc)
        _nop_ = open(O__,'w')
        _nop_.write('#Enc > Rana Shafaat Ali\n')
        _nop_.write('import marshal\n')
        _nop_.write(f'exec(marshal.loads({repr(data)}))')
        _nop_.close()
    print(f'\n [•] file saved in: {O__}')
    exit()
except Exception as e:
    exit(e)
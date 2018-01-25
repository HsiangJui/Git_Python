'''
Created on 2018-01-23

@author: gary.wang
'''
from ctypes.wintypes import DOUBLE
from Chap2 import DigiStrVar


if __name__ == '__main__':
    pass


def main():
    a = 123.456
    
    print(a)
    print(int(a))
    print DOUBLE(a)

    a = int(a)
    c = 3 + float(a)

    
main()

print ' ----------Chapter 2-----------'
StrFunc = DigiStrVar(1)
StrFunc.DigiNumberFunc()
StrFunc.StringFunc()
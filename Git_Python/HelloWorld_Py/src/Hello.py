'''
Created on 2018-01-23

@author: gary.wang
'''
from Chap2 import DigiStrVar
from Chap3 import ListTupleDictSet
#from ctypes import c_double


if __name__ == '__main__':
    pass


def main():
    a = 123.456
    
    print a
    print int(a)
    #a = DOUBLE(a)
    print a
    
    a = int(a)
    c = 3 + float(a)
    print c

    
main()

print ' ----------Chapter 2-----------'
StrFunc = DigiStrVar(1)
StrFunc.DigiNumberFunc()
StrFunc.StringFunc()

print ' ----------Chapter 3-----------'
Chap3Func = ListTupleDictSet(1)
Chap3Func.ListFunc()

'''
Created on 2018-01-23

@author: gary.wang
'''

class DigiStrVar(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    
    def DigiNumberFunc(self):
        ab =0.0
        float(ab) 
        ab = (9/5)
        print (ab)
        
        b = 95
        b = b- int(ab)
        print (b)
        
        c = 9//5
        print '9//5 =', c  #Python 3 need ()
        
        print 'divmod(9,5) = ', divmod(9,5)
        
        print '9 % 5 =', 9 % 5
        
        print 0b10
        
        print 'float(a) =', float(ab)
        
        
        
            
    def StringFunc(self):
        b = 'abcdefghijklmnopqrstuvwxyz'
        print(b)
        print(b[3:-3])
        print(b[3:-3:2])
        print(len(b[3:-3])) 
        print "abc"
        print " 'abc' "
        
        poem = ''' 
"Since it's not an integration for a specific IDE like Visual Studio, 
    Eclipse or others, you can use it with whatever development tools you like, 
    and with any type of file. 
Main interaction with TortoiseGit will be using the context menu of the Windows explorer."
'''
        print poem
        
        c = str(1.88)
        print c, "is string"
        
        print "Since it's not an integration \nfor a specific IDE like Visual \nStudio,"
        
        c = c+' '+b
        print c

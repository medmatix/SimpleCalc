'''
ButtonActionspy
Created on Aug 20, 2018

@author: David York
'''

import tkinter as tk

class ButtonActions():
    '''
    Button Function, actions carried out in response to button presses
    
    '''

    '''
    Constructor for Button Action selt tests

    '''
    def __init__(self):
        self.TKGUI = TKGUI
        print("initialized ButtonActions")

    # module variables and constants 

    ''' Register and variable cleanup functions '''
    def clrCurRegr(self):
        # clear the entry in the current input register
        self.currentRegisterStr = ''
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        print('cleared current register')

    def do_clrAllRegr(self):
        # clear all the registers and variables for a  new calculation stream
        self.currentRegisterStr = ''
        self.inReg.delete(0, tk.END)
        self.currentVariable = 0.0
        self.operandTwo = 0.0
        self.operandThree = 0.0
        self.resultVariable = 0.0
        # log action to history 
        self.history.insert(tk.END, 'CLEAR ALL  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        print('cleared all registers and variables')
        print('current Register: ' + self.currentRegisterStr)
        print('current Variable: ' + str(self.currentVariable))
        print('Operand 2 Variable: ' + str(self.operandTwo))
    
    def do_clrHistory(self):
        # clear the calculation history
        self.history.delete(1.0,tk.END)
        self.log.writeToLog(msg='cleared the calculation history', loglevel=1)
        print('cleared the calculation history')
        
    def do_prtHistory(self):
        print("\n Calculation history:\n")
        print(self.history.get(1.0, tk.END) + '\n')  # to Console
        #self.historyToDialog()  # and show in a dialog
        
    # appending digits to input    
    
    def append_digit0(self):        
        self.currentRegisterStr = self.currentRegisterStr +'0'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr)  
        print(0)            # check on value
        
    def append_digit1(self):        
        self.currentRegisterStr = self.currentRegisterStr + '1' 
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)  
        self.entFlag = False  
        print(self.currentRegisterStr)              # check on value
        print(1)    
        
    def append_digit2(self):
        self.currentRegisterStr = self.currentRegisterStr + '2'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(2)
        
    def append_digit3(self):
        self.currentRegisterStr = self.currentRegisterStr + '3'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(3)
        
    def append_digit4(self):
        self.currentRegisterStr = self.currentRegisterStr + '4'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(4)    
        
    def append_digit5(self):
        self.currentRegisterStr = self.currentRegisterStr + '5'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(5)
        
    def append_digit6(self):
        self.currentRegisterStr = self.currentRegisterStr + '6'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(6)
        
    def append_digit7(self):
        self.currentRegisterStr = self.currentRegisterStr + '7'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(7)    
        
    def append_digit8(self):
        self.currentRegisterStr = self.currentRegisterStr + '8'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(8)
        
    def append_digit9(self):
        self.currentRegisterStr = self.currentRegisterStr + '9'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print(9)
    def append_minsgn(self):
        self.currentRegisterStr = self.currentRegisterStr + '-'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)    
        self.entFlag = False
        print(self.currentRegisterStr) 
        print('-')
        
    def append_dec(self):
        self.currentRegisterStr = self.currentRegisterStr + '.'        
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, self.currentRegisterStr)
        self.entFlag = False
        print(self.currentRegisterStr) 
        print('.')


    # doing operations       
    def do_add(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # add variables entered together
        self.resultVariable = self.operandTwo + self.currentVariable
        # log action to history 
        self.history.insert(self.tk.END, "SUM" + '  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk.INSERT, str(self.resultVariable))
        # set up for chain operation
        self.do_enterReg()

        print("adding")
        print("sum is {}".format(self.resultVariable))
        
    def do_subt(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # subtract variables entered 
        self.resultVariable = self.operandTwo - self.currentVariable
        # log action to history 
        self.history.insert(self.tk.END, "DIFF" + '  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk.INSERT, str(self.resultVariable))
        # set up for chain operation
        self.do_enterReg()

        print("subtracting")
        print("difference is {}".format(self.resultVariable))
        
    def do_mult(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # multiply variables entered 
        self.resultVariable = self.operandTwo * self.currentVariable
        # log action to history 
        self.history.insert(self.tk.END, "PROD" + '  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk.INSERT, str(self.resultVariable))
        # set up for chain operation
        self.do_enterReg()
        self.log.writeToLog(self, msg="PROD" + '  ' + str(self.resultVariable) + '\n', loglevel=1)
        print("multiplying")
        print("product is {}".format(self.resultVariable))
        
    def do_div(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # divide variables entered, second from first 
        self.resultVariable = self.operandTwo / self.currentVariable
        # log action to history 
        self.history.insert(self.tk.END, "DIVD" + '  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk.INSERT, str(self.resultVariable))
        # set up for chain operation
        self.do_enterReg()

        print("dividing")
        print("dividend is {}".format(self.resultVariable))
        
    def do_enterReg(self):
        self.operandTwo = self.currentVariable
        try:
            self.currentVariable=float(self.inReg.get())
        except:
            self.castError()
            print("the input can't be blank, a '0' is atleast needed")
        self.clrCurRegr()
        # log action to history 
        self.history.insert(self.tk.END, 'ENTERED  ' + str(self.currentVariable) + '\n')
        self.entFlag = True
        print('current Register: ' + self.currentRegisterStr)
        print('current Variable: ' + str(self.currentVariable))
        print("Entered current register into current variable and clear current register")
        print('Operand 2 Variable: ' + str(self.operandTwo))
        
    def do_sqrt(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # calculate sqrt(x)
        self.resultVariable = self.math.sqrt(self.currentVariable)
                # log action to history 
        self.history.insert(self.tk.END, 'XSQRT  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk.INSERT, str(self.resultVariable))
        # set up for chain operation
        self.do_enterReg()

        print("square of x is {}".format(self.resultVariable))
        print('sqrt')
        
    def do_invert(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # calculate square of (x)
        self.resultVariable = 1/self.currentVariable
        # log action to history 
        self.history.insert(self.tk.END, 'INVERSE  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk)
        # set up for chain operation
        self.do_enterReg()

        print("inverse of x is {}".format(self.resultVariable))
        print('inverse')
        print('inverse of x')
        # calculate inverse (x)
        print('inverted x')
    
    def do_power2(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # calculate square of (x)
        self.resultVariable = self.currentVariable**2
                # log action to history 
        self.history.insert(self.tk.END, 'XSQD  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk.INSERT, str(self.resultVariable))
        # set up for chain operation
        self.do_enterReg()

        print("square of x is {}".format(self.resultVariable))
        print('sqrt')
        print('squared x')
    
    def do_sgn(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # do change of sign too (x)
        self.resultVariable = self.currentVariable * -1
        # log action to history 
        self.history.insert(self.tk.END, "SGN" + '  ' + str(self.resultVariable) + '\n')
        self.history.see(self.tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,self.tk.END)
        self.inReg.insert(self.tk.INSERT, str(self.resultVariable))
        print("sign changed, x is now {}".format(self.resultVariable))
        print('change of sign')
        
    def do_blank(self):
        # check for entered button
        if not self.entFlag:
            self.do_enterReg()
        # do something else to (x)
        print('unused key')
        
    
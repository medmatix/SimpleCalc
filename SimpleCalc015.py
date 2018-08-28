# -*- coding: utf-8 -*-
'''

SimpleCalc, Main Program Module

Created on Aug 28, 2018
@version: 0.1
@author: David A York
@ copyright: 2018
@note: Single file program and classes

@license: LGPL, https://www.gnu.org/licenses/lgpl.html 

'''

#======================================================
# imports
#======================================================
# standard library imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
# from tkinter import Canvas
from tkinter import messagebox as mBox
import math
# module imports


# ~~~ End import section ~~~ =================


# ===================================
# GlobalVariables and Constants
# ===================================

# module level  GLOBALS
currentRegisterStr = ''
currentVariable = 0.0
operandTwo = 0.0
operandThree = 0.0
resultVariable = 0.0
entFlag = False
logHistoryName = "historyLog"

## ~~~ END of Glogal Declarations ~~ =================


#=====================================================
# Class definitions
#=====================================================

'''
ButtonActionspy
Created on Aug 20, 2018

@author: David York
'''



    
        
class TKGUI():
    ''' 
    GUI building functions and variables
    
    '''
    
    
    # Class Constructor ------------------------------
    def __init__(self):
        self.currentRegisterStr = ''
        self.currentVariable = 0.0
        self.operandTwo = 0.0
        self.operandThree = 0.0
        self.resultVariable = 0.0
        self.entFlag = False
        self.logHistoryName = "historyLog"
       
        
        
        # Create instance
        self.win = tk.Tk()

        # Add a title
        self.win.title("Simple Calculator")
        
        # Initialize widgets
        self.createWidgets()
        
    # ~~~ End class contruction / initializer ~~-----
    
    
    # == GUI widget Functions and Definitions =================================
    # -- Exit GUI cleanly -------------
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        print('run is done, exited normally!')
        exit()
    
    # -- make an messages and messageBoxes for GUI help and errors
    def info(self):
        mBox.showinfo('About Template', 'A Simple Arithmetic Calculator\n (c) David A York, 2018\n \nlicense: MIT/X-Windows')

    # catch trying to cast a blank to a number
    def castError(self):
        mBox.showwarning(title= "Ooops!!!", message="the input field can't be blank, \nat least one number should be entered first\nREVERSE POLISH notation means: enter all numbers, THEN choose an operation.The result is always brought forward as follow-up input in case needed\nOperations can be chained by just entering next input.")
    
    def arithmeticError(self):
        mBox.showwarning(title= "Ooops!!!", message="you need to enter value before selecting an operation")
        
    def underConstruction(self):
        mBox.showwarning(title= "Men at Work!!", message="This function has note been implemented yet, \nsorrrrrrry - see next version :)")
        
    # -- make history display dialog and print 
    def historyToDialog(self):
        mBox._show(title="History", message=self.history.get(1.0, tk.END), _icon="", _type="")
         
        
    # == GUI widget constructiom ==============================================
    def createWidgets(self):
        
        
        # Tab Controls introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control

        tab1 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab1, text='Calculator')      # Add the tab

        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Notes')      # Make second tab visible
        
        tab3 = ttk.Frame(tabControl)            # Add a third tab
        tabControl.add(tab3, text='Documentation')      # Make third tab visible

        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ end ~ Tab Controls introduced here -----------------------------------------

        #  We are creating a container frame to tab1 widgets ============================
        self.display = ttk.LabelFrame(tab1, text=' Display Registers ')
        self.display.grid(column=0, row=0, padx=8, pady=4)
        
        self.clears = ttk.LabelFrame(tab1)
        self.clears.grid(column=0, row=5, padx=8, pady=4)
        
        # We are creating a frame to hold the a data block of text
        self.inKeys = ttk.LabelFrame(tab1, text=' Number Keys ')
        self.inKeys.grid(column=0, row=10, padx=8, pady=4)
        
        self.operKeys = ttk.LabelFrame(tab1, text=' Operator Keys ')
        self.operKeys.grid(column=0, row=16, padx=8, pady=4)
        
        self.functKeys = ttk.LabelFrame(tab1, text=' Function Keys ')
        self.functKeys.grid(column=0, row=18, padx=8, pady=8)
        # Input field = current register
        # Creating a Label
        ttk.Label(self.display, text="Current Operand:").grid(column=0, row=0, sticky='W')
 
        # Adding a Textbox Entry widget
        self.inReg = ttk.Entry(self.display, width=68, text='Enter a number')
        self.inReg.grid(column=0, row=1, sticky='W')
          
        # Scrolling history field:
        # Creating a Label
        ttk.Label(self.display, text="Calculation History:").grid(column=0, row=3, sticky='W')
        
        # Using a scrolled Text control for review of action history
        scrolW1  = 50; scrolH1  =  4
        self.history = scrolledtext.ScrolledText(self.display, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.history.grid(column=0, row=4, padx=4, pady=4, sticky='WE', columnspan=3)
        
        # House keeping function buttons
        
        self.clrCurReg = ttk.Button(self.clears, text=" CE ", command=lambda: ButtonActions.do_clrCurRegr(self))
        self.clrCurReg.grid(column=0, row=0, padx=4, pady=4)

        self.clrAllReg = ttk.Button(self.clears, text=" CLR ", command=lambda: ButtonActions.do_clrAllRegr(self))
        self.clrAllReg.grid(column=1, row=0, padx=4, pady=4)
        
        self.prtHx = ttk.Button(self.clears, text=" PrtHx ", command=lambda: ButtonActions.do_prtHistory(self))
        self.prtHx.grid(column=2, row=0, padx=4, pady=4)
        
        self.clrHx = ttk.Button(self.clears, text=" CLHx ", command=lambda: ButtonActions.do_clrHistory(self))
        self.clrHx.grid(column=3, row=0, padx=4, pady=4)

        # Populate inKeys frame with the digit input keys (buttons)
        # Adding digit entry buttons 1 to 3
        
        self.action1 = ttk.Button(self.inKeys, text=" 1 ", command=lambda: ButtonActions.append_digit1(self))
        self.action1.grid(column=0, row=0, padx=4, pady=2)

        self.action2 = ttk.Button(self.inKeys, text=" 2 ", command=lambda: ButtonActions.append_digit2(self))
        self.action2.grid(column=1, row=0, padx=4, pady=2)
        
        self.action3 = ttk.Button(self.inKeys, text=" 3 ", command=lambda: ButtonActions.append_digit3(self))
        self.action3.grid(column=2, row=0, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action4 = ttk.Button(self.inKeys, text=" 4 ", command=lambda: ButtonActions.append_digit4(self))
        self.action4.grid(column=0, row=2, padx=4, pady=2)

        self.action5 = ttk.Button(self.inKeys, text=" 5 ", command=lambda: ButtonActions.append_digit5(self))
        self.action5.grid(column=1, row=2, padx=4, pady=2)
        
        self.action6 = ttk.Button(self.inKeys, text=" 6 ", command=lambda: ButtonActions.append_digit6(self))
        self.action6.grid(column=2, row=2, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action7 = ttk.Button(self.inKeys, text=" 7 ", command=lambda: ButtonActions.append_digit7(self))
        self.action7.grid(column=0, row=4, padx=4, pady=2)

        self.action8 = ttk.Button(self.inKeys, text=" 8 ", command=lambda: ButtonActions.append_digit8(self))
        self.action8.grid(column=1, row=4, padx=4, pady=2)
        
        self.action9 = ttk.Button(self.inKeys, text=" 9 ", command=lambda: ButtonActions.append_digit9(self))
        self.action9.grid(column=2, row=4, padx=4, pady=2)
        
        self.actionmin = ttk.Button(self.inKeys, text=" - ", command=lambda: ButtonActions.append_minsgn(self))
        self.actionmin.grid(column=0, row=6, padx=4, pady=2)     
        
        self.action0 = ttk.Button(self.inKeys, text=" 0 ", command=lambda: ButtonActions.append_digit0(self))
        self.action0.grid(column=1, row=6, padx=4, pady=2)  
        
        self.actiondec = ttk.Button(self.inKeys, text=" . ", command=lambda: ButtonActions.append_dec(self))
        self.actiondec.grid(column=2, row=6, padx=4, pady=2)  
        
        #Populate operator keys frame
        # Adding
        self.action_add = ttk.Button(self.operKeys, text=" + ", command=lambda: ButtonActions.do_add(self))
        self.action_add.grid(column=0, row=0, padx=4, pady=6)

        self.action_subt = ttk.Button(self.operKeys, text=" - ", command=lambda: ButtonActions.do_subt(self))
        self.action_subt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_mult = ttk.Button(self.operKeys, text=" * ", command=lambda: ButtonActions.do_mult(self))
        self.action_mult.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_div = ttk.Button(self.operKeys, text=" / ", command=lambda: ButtonActions.do_div(self))
        self.action_div.grid(column=4, row=0, padx=4, pady=6)
        
        self.action_equal = ttk.Button(self.operKeys, text="ENTER", command=lambda: ButtonActions.do_enterReg(self))
        self.action_equal.grid(column=5, row=0, padx=4, pady=6)
        
        #Populate function keys frame
        # Adding
        self.action_xpowy = ttk.Button(self.functKeys, text=" x**y ", command=lambda: ButtonActions.do_blank(self))
        self.action_xpowy.grid(column=0, row=0, padx=4, pady=6)

        self.action_sqrt = ttk.Button(self.functKeys, text=" sqrt ", command=lambda: ButtonActions.do_sqrt(self))
        self.action_sqrt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_inverse = ttk.Button(self.functKeys, text=" 1/x ", command=lambda: ButtonActions.do_invert(self))
        self.action_inverse.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_power2 = ttk.Button(self.functKeys, text=" **2 ", command=lambda: ButtonActions.do_power2(self))
        self.action_power2.grid(column=3, row=0, padx=4, pady=6)
        
        self.action_sgn = ttk.Button(self.functKeys, text="+/-", command=lambda: ButtonActions.do_sgn(self))
        self.action_sgn.grid(column=4, row=0, padx=4, pady=6)
        
        self.action_cos = ttk.Button(self.functKeys, text="cos", command=lambda: ButtonActions.do_blank(self))
        self.action_cos.grid(column=0, row=1, padx=4, pady=6)
        
        self.action_sin = ttk.Button(self.functKeys, text="sin", command=lambda: ButtonActions.do_blank(self))
        self.action_sin.grid(column=1, row=1, padx=4, pady=6)
        
        self.action_tan = ttk.Button(self.functKeys, text="tan", command=lambda: ButtonActions.do_blank(self))
        self.action_tan.grid(column=2, row=1, padx=4, pady=6)
        
        self.action_log10 = ttk.Button(self.functKeys, text="log10", command=lambda: ButtonActions.do_blank(self))
        self.action_log10.grid(column=3, row=1, padx=4, pady=6)
        
        self.action_ln = ttk.Button(self.functKeys, text="ln", command=lambda: ButtonActions.do_blank(self))
        self.action_ln.grid(column=4, row=1, padx=4, pady=6)
        
        # Creating a container frame to hold tab2 graphing widgets ============================
#===============================================================================
#         self.graphical = ttk.LabelFrame(tab2, text=' Graphical Output ')
#         self.graphical.grid(column=0, row=0, padx=8, pady=4)
# 
#         # Adding a graphic window (canvas widget
#         w = Canvas(self.graphical, width=400, height=300)
#         w.grid(column=0, row=1, padx=8, pady=4, sticky='W')
#===============================================================================


        
        # We are creating a container frame to hold tab2 widgets ============================
        self.notes = ttk.LabelFrame(tab2, text=' Notes ')
        self.notes.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        
        self.notesctl = ttk.LabelFrame(self.notes)
        self.notesctl.grid(column=0, row=0, padx=8, pady=4, sticky='W')
        self.action_clrnotes = ttk.Button(self.notesctl, text="CLEAR", command=lambda: ButtonActions.do_note(self))
        self.action_clrnotes.grid(column=0, row=0, padx=4, pady=6)
        self.action_prtnotes = ttk.Button(self.notesctl, text="PRINT", command=lambda: ButtonActions.do_note(self))
        self.action_prtnotes.grid(column=1, row=0, padx=4, pady=6)
        self.action_lognotes = ttk.Button(self.notesctl, text="LOG IT", command=lambda: ButtonActions.do_note(self))
        self.action_lognotes.grid(column=2, row=0, padx=4, pady=6)
        self.action_savenotes = ttk.Button(self.notesctl, text="SAVE", command=lambda: ButtonActions.do_note(self))
        self.action_savenotes.grid(column=3, row=0, padx=4, pady=6)
        self.action_menunotes = ttk.Button(self.notesctl, text="MENU", command=lambda: ButtonActions.do_note(self))
        self.action_menunotes.grid(column=4, row=0, padx=4, pady=6)
        
        scrolW1  = 50; scrolH1  =  20
        self.notes = scrolledtext.ScrolledText(self.notes, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.notes.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)
        
        
        
        # We are creating a container frame to hold tab3 widgets ============================
        self.documentation = ttk.LabelFrame(tab3, text=' The Manual ')
        self.documentation.grid(column=0, row=3, padx=8, pady=4, sticky='W')
        

        
        # the index of the manual
        ttk.Label(self.documentation, text="Manual Index:").grid(column=0, row=0)
        choice = tk.StringVar()
        indexChosen = ttk.Combobox(self.documentation, width=65, textvariable=choice)
        indexChosen['values'] = ('Introduction', 'Overview', 'Functions', 'References', 'Further Explorations')
        indexChosen.grid(column=0, row=1)
        indexChosen.current(0)
        
        # The Manual text                
        # Scrolling Documentation field:
        # Creating a Label
        ttk.Label(self.documentation, text="Documentation:").grid(column=0, row=5, sticky='W')
        
        # Using a scrolled Text control for review of action history
        scrolW1  = 50; scrolH1  =  20
        self.manual = scrolledtext.ScrolledText(self.documentation, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.manual.grid(column=0, row=6, padx=4, pady=4, sticky='WE', columnspan=3)
        
        
        # Creating a Menu Bar ---------------------------------------------------------------------
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)

        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        # Add an Edit Menu
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        editMenu.add_separator()
        editMenu.add_command(label="Options")
        menuBar.add_cascade(label="Edit", menu=editMenu)

        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="Context Help")
        helpMenu.add_command(label="Documentation")
        helpMenu.add_command(label="About", command=self.info)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # ~ end of menu bar ~ ------------------------------------------------- 
        # Change the main windows icon
        #self.win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')

        # Place cursor into name Entry
        #nameEntered.focus()
        
        # Set Focus to Tab2
        tabControl.select(0)


        # Add a Tooltip to the Spinbox
# ~~ End of TKGUI CLass =======================================================        
        
        
class ButtonActions():
    '''
    Button Function, actions carried out in response to button presses
    
    '''

    '''
    Constructor for Button Action selt tests

    '''
    def __init__(self):
        print("initialized ButtonActions")

    # module variables and constants 

    ''' Register and variable cleanup functions '''
    def do_clrCurRegr(self):
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
        #self.history.insert(tk.END, 'CLEAR HISTORY\n')
        self.history.see(tk.END)
        print('cleared the calculation history')
        
    def do_prtHistory(self):
        print("\n Calculation history:\n")
        print(self.history.get(1.0, tk.END) + '\n')  # to Console
        self.history.insert(tk.END, 'PRINT HISTORY\n')
        self.history.see(tk.END)
        self.historyToDialog()  # and show in a dialog
        
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


    # doing operations and functions ------------------------------------------
    def do_add(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # add variables entered together
        self.resultVariable = self.operandTwo + self.currentVariable
        # log action to history 
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'SUM  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ButtonActions.do_enterReg(self)
        print("adding")
        print("sum is {}".format(self.resultVariable))
        
    def do_subt(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # subtract variables entered 
        self.resultVariable = self.operandTwo - self.currentVariable
        # log action to history 
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'DIFF  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ButtonActions.do_enterReg(self)

        print("subtracting")
        print("difference is {}".format(self.resultVariable))
        
    def do_mult(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # multiply variables entered 
        self.resultVariable = self.operandTwo * self.currentVariable
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transfering result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'PROD  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ButtonActions.do_enterReg(self)
        print("multiplying")
        print("product is {}".format(self.resultVariable))
        
    def do_div(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # divide variables entered, second from first 
        self.resultVariable = self.operandTwo / self.currentVariable
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'DIVD  ' + str(self.resultVariable) + '\n')
        # set up for chain operation
        ButtonActions.do_enterReg(self)

        print("dividing")
        print("dividend is {}".format(self.resultVariable))
        
    def do_enterReg(self):
        self.operandTwo = self.currentVariable
        try:
            self.currentVariable=float(self.inReg.get())
        except:
            self.castError()
            print("the input can't be blank, a '0' is atleast needed")
        ButtonActions.do_clrCurRegr(self)
        # log action to history 
        self.history.insert(tk.END, 'ENTERED  ' + str(self.currentVariable) + '\n')
        self.history.see(tk.END)
        self.entFlag = True
        print('current Register: ' + self.currentRegisterStr)
        print('current Variable: ' + str(self.currentVariable))
        print("Entered current register into current variable and clear current register")
        print('Operand 2 Variable: ' + str(self.operandTwo))
        
    def do_sqrt(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate sqrt(x)
        self.resultVariable = math.sqrt(self.currentVariable)
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'SQRT  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ButtonActions.do_enterReg(self)

        print("square of x is {}".format(self.resultVariable))
        print('sqrt')
        
    def do_invert(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate square of (x)
        self.resultVariable = 1/self.currentVariable
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'INVERSE  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ButtonActions.do_enterReg(self)

        print("inverse of x is {}".format(self.resultVariable))
        print('inverse')
        print('inverse of x')
        # calculate inverse (x)
        print('inverted x')
    
    def do_power2(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        # calculate square of (x)
        self.resultVariable = self.currentVariable**2
                # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.resultVariable))
        self.history.insert(tk.END, 'POWER2  ' + str(self.resultVariable) + '\n')
        self.history.see(tk.END)
        # set up for chain operation
        ButtonActions.do_enterReg(self)

        print("square of x is {}".format(self.resultVariable))
        print('sqrt')
        print('squared x')
    
    def do_sgn(self):
        # check for entered button
        if not self.entFlag:
            ButtonActions.do_enterReg(self)
        # do change of sign too (x)
        self.currentVariable = self.currentVariable * -1
        # log action to history 
        
        self.history.see(tk.END)
        # clear register before transferring result there
        self.inReg.delete(0,tk.END)
        self.inReg.insert(tk.INSERT, str(self.currentVariable))
        self.history.insert(tk.END, ' +/- ' + str(self.currentVariable) + '\n')
        self.history.see(tk.END)
        print("sign changed, x is now {}".format(self.currentVariable))
        print('change of sign')
        
    def do_blank(self):
        # check for entered button
        if not self.entFlag:
            self.arithmeticError()
            return
        self.history.insert(tk.END, 'NOP  \n')
        self.history.see(tk.END)
        # do something else to (x)
        print('unused key')
        
    def do_note(self):
        # check for entered button
        # do something else to (x)
        self.underConstruction()
        print('note function')
        

#======================
# Start GUI
#======================
# tkgui = TKGUI()

#running methods in threads
#runT=Thread(target=oop.methodInAThread)

# tkgui.win.mainloop()

# ===============================================
# Unit Testing Code
# ===============================================
if __name__ == '__main__':
    print("tkGUI is running as main; \n    ie. a module self test")
    tkgui = TKGUI()
    tkgui.win.mainloop()
#~~~ END test code ==============================
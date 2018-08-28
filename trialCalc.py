# -*- coding: utf-8 -*-
'''

tkGUI Main Program Module

Created on Aug 16, 2018
@version: 1.0
@author: David A York
@ copyright: 2018
@note: after B Mayer, Python GUI Programming Solutions

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
from os import path
# import math
# from threading import Thread
# from time import sleep
# from TCP_Server import startServer
# import URL as url

# module imports
from ButtonActions import ButtonActions as ba
from Logging import Logger

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

        # create Logger instance
        fullPath = path.realpath(__file__)
        logName = fullPath + logHistoryName
        self.log = Logger(logName, 1)
        self.loggingLevel = 1
        print(self.log)

        # Add a title
        # self.win.title(self.i18n.title)
        self.win.title("Simple Calculator")
        
        #create queue
        # self.guiQueue=Queue()
        
        # Initialize GUI and it's CONSTANTS and variables
        self.createWidgets()
        


        
        # svrT = Thread(target=startServer, daemon = True)
        # svrT.start()
    # ~~~ End class contruction / initializer ~~-----
    
    
    # == GUI widget Functions and Definitions =================================
    # -- Exit GUI cleanly -------------
    def _quit(self):
        self.log.writeToLog(msg='run is done, exiting normally', loglevel=1)
        self.win.quit()
        self.win.destroy()
        print('run is done, exited normally!')
        exit()
    
    # -- make an messages and messageBoxes for GUI help and errors
    def info(self):
        mBox.showinfo('About Template', 'A Simple Arithmetic Calculator (c) David A York, 2018\n \nlicense: LGPL, https://www.gnu.org/licenses/lgpl.html This is a Help item under construction.')

    # catch trying to cast a blank to a number
    def castError(self):
        mBox.showwarning(title= "Ooops!!!", message="the input field can't be blank, \nat least a '0' is needed")
        self.log.writeToLog(msg="Cast Error, 'the input field can't be blank, \nat least a '0' is needed'", loglevel=1)
        
    #===========================================================================
    # # -- make history display dialog and print 
    # def historyToDialog(self):
    #     mBox._show(title="History", message=self.history.get(1.0, tk.END), _icon="", _type="")
    #     
    #===========================================================================
        
    # == GUI widget constructiom ==============================================
    def createWidgets(self):
        
        
        # Tab Controls introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control

        tab1 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab1, text='Calculator')      # Add the tab

        #=======================================================================
        # tab2 = ttk.Frame(tabControl)            # Add a second tab
        # tabControl.add(tab2, text='Graphical')      # Make second tab visible
        #=======================================================================
        
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
        scrolW1  = 50; scrolH1  =  2
        self.history = scrolledtext.ScrolledText(self.display, width=scrolW1, height=scrolH1, wrap=tk.WORD)
        self.history.grid(column=0, row=4, padx=4, pady=4, sticky='WE', columnspan=3)
        
        # House keeping function buttons
        
        self.clrCurReg = ttk.Button(self.clears, text=" CE ", command=ba.clrCurRegr(self))
        self.clrCurReg.grid(column=0, row=0, padx=4, pady=4)

        self.clrAllReg = ttk.Button(self.clears, text=" CLR ", command=ba.do_clrAllRegr(self))
        self.clrAllReg.grid(column=1, row=0, padx=4, pady=4)
        
        self.prtHx = ttk.Button(self.clears, text=" PrtHx ", command=ba.do_prtHistory(self))
        self.prtHx.grid(column=2, row=0, padx=4, pady=4)
        
        self.clrHx = ttk.Button(self.clears, text=" CLHx ", command=ba.do_clrHistory(self))
        self.clrHx.grid(column=3, row=0, padx=4, pady=4)

        # Populate inKeys frame with the digit input keys (buttons)
        # Adding digit entry buttons 1 to 3
        
        self.action1 = ttk.Button(self.inKeys, text=" 1 ", command=ba.append_digit1(self))
        self.action1.grid(column=0, row=0, padx=4, pady=2)

        self.action2 = ttk.Button(self.inKeys, text=" 2 ", command=ba.append_digit2(self))
        self.action2.grid(column=1, row=0, padx=4, pady=2)
        
        self.action3 = ttk.Button(self.inKeys, text=" 3 ", command=ba.append_digit3(self))
        self.action3.grid(column=2, row=0, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action4 = ttk.Button(self.inKeys, text=" 4 ", command=ba.append_digit4(self))
        self.action4.grid(column=0, row=2, padx=4, pady=2)

        self.action5 = ttk.Button(self.inKeys, text=" 5 ", command=ba.append_digit5(self))
        self.action5.grid(column=1, row=2, padx=4, pady=2)
        
        self.action6 = ttk.Button(self.inKeys, text=" 6 ", command=ba.append_digit6(self))
        self.action6.grid(column=2, row=2, padx=4, pady=2)
        # Adding digit entry buttons 1 to 3
        self.action7 = ttk.Button(self.inKeys, text=" 7 ", command=ba.append_digit7(self))
        self.action7.grid(column=0, row=4, padx=4, pady=2)

        self.action8 = ttk.Button(self.inKeys, text=" 8 ", command=ba.append_digit8(self))
        self.action8.grid(column=1, row=4, padx=4, pady=2)
        
        self.action9 = ttk.Button(self.inKeys, text=" 9 ", command=ba.append_digit9(self))
        self.action9.grid(column=2, row=4, padx=4, pady=2)
        
        self.actionmin = ttk.Button(self.inKeys, text=" - ", command=ba.append_minsgn(self))
        self.actionmin.grid(column=0, row=6, padx=4, pady=2)     
        
        self.action0 = ttk.Button(self.inKeys, text=" 0 ", command=ba.append_digit0(self))
        self.action0.grid(column=1, row=6, padx=4, pady=2)  
        
        self.actiondec = ttk.Button(self.inKeys, text=" . ", command=ba.append_dec(self))
        self.actiondec.grid(column=2, row=6, padx=4, pady=2)  
        
        #Populate operator keys frame
        # Adding
        self.action_add = ttk.Button(self.operKeys, text=" + ", command=ba.do_add)
        self.action_add.grid(column=0, row=0, padx=4, pady=6)

        self.action_subt = ttk.Button(self.operKeys, text=" - ", command=ba.do_subt)
        self.action_subt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_mult = ttk.Button(self.operKeys, text=" * ", command=ba.do_mult)
        self.action_mult.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_div = ttk.Button(self.operKeys, text=" / ", command=ba.do_div)
        self.action_div.grid(column=4, row=0, padx=4, pady=6)
        
        self.action_equal = ttk.Button(self.operKeys, text="Ret", command=ba.do_enterReg)
        self.action_equal.grid(column=5, row=0, padx=4, pady=6)
        
        #Populate function keys frame
        # Adding
        self.action_prtHistory = ttk.Button(self.functKeys, text=" prnt ", command=ba.do_prtHistory)
        self.action_prtHistory.grid(column=0, row=0, padx=4, pady=6)

        self.action_sqrt = ttk.Button(self.functKeys, text=" sqrt ", command=ba.do_sqrt)
        self.action_sqrt.grid(column=1, row=0, padx=4, pady=6)
        
        self.action_inverse = ttk.Button(self.functKeys, text=" 1/x ", command=ba.do_invert)
        self.action_inverse.grid(column=2, row=0, padx=4, pady=6)
        
        self.action_power2 = ttk.Button(self.functKeys, text=" **2 ", command=ba.do_power2)
        self.action_power2.grid(column=3, row=0, padx=4, pady=6)
        
        self.action_sgn = ttk.Button(self.functKeys, text="+/-", command=ba.do_sgn)
        self.action_sgn.grid(column=4, row=0, padx=4, pady=6)
        
        self.action_blank1 = ttk.Button(self.functKeys, text="unused", command=ba.do_blank)
        self.action_blank1.grid(column=0, row=1, padx=4, pady=6)
        
        self.action_blank2 = ttk.Button(self.functKeys, text="unused", command=ba.do_blank)
        self.action_blank2.grid(column=1, row=1, padx=4, pady=6)
        
        self.action_blank3 = ttk.Button(self.functKeys, text="unused", command=ba.do_blank)
        self.action_blank3.grid(column=2, row=1, padx=4, pady=6)
        
        self.action_blank4 = ttk.Button(self.functKeys, text="unused", command=ba.do_blank)
        self.action_blank4.grid(column=3, row=1, padx=4, pady=6)
        
        self.action_blank5 = ttk.Button(self.functKeys, text="unused", command=ba.do_blank)
        self.action_blank5.grid(column=4, row=1, padx=4, pady=6)
        
        # Creating a container frame to hold tab2 graphing widgets ============================
#===============================================================================
#         self.graphical = ttk.LabelFrame(tab2, text=' Graphical Output ')
#         self.graphical.grid(column=0, row=0, padx=8, pady=4)
# 
#         # Adding a graphic window (canvas widget
#         w = Canvas(self.graphical, width=400, height=300)
#         w.grid(column=0, row=1, padx=8, pady=4, sticky='W')
#===============================================================================


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

        # ~ end of menu bar ~ ------------------------------------------------------------------
        
        # Change the main windows icon
        #self.win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')

        # Place cursor into name Entry
        #nameEntered.focus()
        
        # Set Focus to Tab2
        tabControl.select(0)


        # Add a Tooltip to the Spinbox


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
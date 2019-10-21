

from tkinter import *
import math

class TipCalculator:
    def __init__(self):
        window = Tk()
        window.title("Tippity Split")

        Label(window, text = "Tippity Split - Tip Calculator", fg = "Red").grid(row = 1, column = 1,
                                                                                columnspan = 2, )
                                                                                
                                                                                
                                                                                
        # Labels on left side of GUI and left of Entry boxes                                                                                                                                                
        Label(window, text = "Check Amount $").grid(row = 2, column = 1, sticky = "W")
        Label(window, text = "Tip %").grid(row = 3, column = 1, sticky = "W")
        Label(window, text = "Split (x Ways):").grid(row = 4, column = 1, sticky = "W")


        # Entry Boxes
        self.checkAmount = StringVar()
        Entry(window, textvariable = self.checkAmount).grid(row = 2, column = 2)
        self.checkAmount.set("0.00")
        self.tipPercent = StringVar()
        Entry(window, textvariable = self.tipPercent).grid(row = 3, column = 2)
        self.tipPercent.set("15")
        self.split = StringVar()
        Entry(window, textvariable = self.split).grid(row = 4, column = 2)
        self.split.set("1")

        # Radio Buttons for rounding up
        self.roundRadioButtons = IntVar()
        roundButton = Radiobutton(window, text = "Round Up", variable = self.roundRadioButtons,
                                  value = 0).grid(row = 5, column = 1)
        dontRound = Radiobutton(window, text = "Don't Round", variable = self.roundRadioButtons,
                                value = 1).grid(row = 5, column = 2)

        # Buttons to perform calculation and clear data
        calcButton = Button(window, text = "Calculate", command = self.calculate).grid(row = 6,
                                                                    column = 1)
        
        clearButton = Button(window, text = "Clear", command = self.clear).grid(row = 6,
                                                                    column = 2)
        # Results Labels at bottom of GUI
        self.tipLabel = StringVar()
        tipLabel = Label(window, textvariable = self.tipLabel).grid(row = 7, columnspan = 2,
                                                                    sticky = "W")                            
        self.tipLabel.set("The tip is $0.00")

        self.totalLabel = StringVar()
        totalLabel = Label(window, textvariable = self.totalLabel).grid(row = 8, columnspan = 2,
                                                                        sticky = "W")
        self.totalLabel.set("The total after tip is $0.00")
        self.splitLabel = StringVar()
        self.splitLabel.set("Each gues should pay $0.00")
        splitLabel = Label(window, textvariable = self.splitLabel).grid(row = 9, columnspan = 2,
                                                                        sticky = "W")


        window.mainloop()
        
    def calculate(self):
        ''' Calculates tip, total check and split
            input: none
            returns: values to result labels
        '''
        rad = self.roundRadioButtons.get()
        if rad == 0:
            tip = math.ceil(float(self.checkAmount.get()) * float(self.tipPercent.get()) / 100)
            total = math.ceil(tip + float(self.checkAmount.get()))
            splitPay = math.ceil(total / int(self.split.get()))

        else:
            tip = float(self.checkAmount.get()) * float(self.tipPercent.get()) / 100
            total = tip + float(self.checkAmount.get())
            splitPay = total / int(self.split.get())
            

        self.tipLabel.set(str("The tip is $" + str(tip)))
        self.totalLabel.set(str("The total after tip is $" + str(total)))
        self.splitLabel.set(str("Each guest should pay $" + str(splitPay)))

    def clear(self):
        ''' clears all data from labels and entry boxes
            input: none
            returns: default amounts
        '''
        self.tipLabel.set("The tip is $")
        self.totalLabel.set("The total after tip is $0.00")
        self.splitLabel.set("Each guest should pay $0.00")
        self.checkAmount.set("0.00")
        self.tipPercent.set("15")
        self.tipLabel.set("The total after tip is $0.00")
        self.splitLabel.set("Each gues should pay $0.00")
        
        


        












        




TipCalculator()
        
    

from PyQt5 import QtWidgets, uic , QtGui,QtCore 
from PyQt5.QtWidgets import QMessageBox , QCompleter , QPushButton
from PyQt5.QtGui import QClipboard
import sys , os , time
def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False
def print_sudoku(input):
    counti = 0
    for i in (input):
        
        if (counti % 3 == 0):
            if(counti == 0) :
                print("_________________________")
            else:    
                print("|_______|_______|_______|")

            print("|       |       |       |")    
        counti += 1        
        count = 0
        strin = "| "
        for x in i :
            strin += str(x)+" "
            count += 1
            if (count % 3 == 0):
                strin += "| "
        print(strin)
    print("|_______|_______|_______|")    
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(resource_path('untitled1.ui'), self)
        self.setWindowIcon(QtGui.QIcon(resource_path('sudo.ico'))) 
        self.setWindowTitle("SODUKO")
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.findChild(QtWidgets.QPushButton, 'button').clicked.connect(self.printButtonPressed) # Find the button
        self.findChild(QtWidgets.QPushButton, 'clear').clicked.connect(self.clearbox) # Find the button
        
        # Remember to pass the definition/method, not the return value!
        
        self.show()
    def clearbox(self):
        for i in range(1,82):
            self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).setText("")
            self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).setStyleSheet(""".QLineEdit {
                                                                                background-color: black;
                                                                                color: white;
                                                                                border-radius: 12px;
                                                                                border: 3px solid red;
                                                                                font-size: 30px;
                                                                                text-align: right;
                                                                                        }""")    
    def printButtonPressed(self):
         
        baste = []
        for i in range(1,82):
            check = self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).text()
            #if (check == "") : print(check)
            #print(check)
            
            if not (check.isnumeric()) and not(check == ""):
                QMessageBox.critical(self, "مشکل !", "يا عدد بگذاريد يا خالي باشد ورودي "+check+" اشتباه است.")
                return False    
        array = []
        array10 = []
        array20 = []
        array30 = []
        array40 = []
        array50 = []
        array60 = []
        array70 = []
        array80 = []
        array90 = []
        nums = []
        for i in range(1,82):
            check = self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).text()
            if (check == "") :
                check = 0
            else :
                nums.append(int(i))
            if i < 10 : array10.append(int(check)) 
            if i > 9 and i < 19 : array20.append(int(check))
            if i > 18 and i < 28 : array30.append(int(check))
            if i > 27 and i < 37 : array40.append(int(check))
            if i > 36 and i < 46 : array50.append(int(check))
            if i > 45 and i < 55 : array60.append(int(check))
            if i > 54 and i < 64 : array70.append(int(check))
            if i > 63 and i < 73 : array80.append(int(check))
            if i > 72 and i < 82 : array90.append(int(check))
        array.append(array10)
        array.append(array20)
        array.append(array30)
        array.append(array40)
        array.append(array50)
        array.append(array60)
        array.append(array70)
        array.append(array80)
        array.append(array90)
        first = [
            [1,2,3, 10,11,12, 19,20,21],
            [4,5,6, 13,14,15, 22,23,24],
            [7,8,9, 16,17,18, 25,26,27],
            
            [28,29,30, 37,38,39, 46,47,48],
            [31,32,33, 40,41,43, 49,50,51],
            [34,35,36, 43,44,45, 50,53,54],
            
            [55,56,57, 64,65,66, 73,74,75],
            [58,59,60, 67,68,69, 76,77,78],
            [61,62,63, 70,71,72, 79,80,81]
            ]
        for i in nums:
                for x in nums:
                        avl = self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).text()
                        dov = self.findChild(QtWidgets.QLineEdit, 'input'+str(x)).text()
                        if not x == i and avl == dov :
                                if int(i%9) == int(x%9) :
                                        QMessageBox.critical(self, "مشکل !", "دو عدد "+avl+" در يک ستون تکراري است")
                                        return False
                                elif (x < 10 and i < 10) or (9 < x < 19 and  9 < i < 19 )  or (18 < x < 28 and  18 < i < 28 ) or (27 < x < 37 and  27 < i < 37 ) or (36 < x < 46 and  36 < i < 46 )  or (45 < x < 55 and  45 < i < 55 ) or (54 < x < 64 and  54 < i < 64 ) or (63 < x < 73 and  63 < i < 73 ) or (72 < x < 82 and  72< i < 82 ):                       
                                        QMessageBox.critical(self, "مشکل !", "دو عدد "+avl+" در يک رديف تکراري است")
                                        return False
                                #else :
                                 #       for z in range(9):
                                  #              if x in first[z]  and i in first[z]:
                                   #                     QMessageBox.critical(self, "مشکل !", "دو عدد "+avl+" در يک مربع تکراري است")
                                    #                    return False
                                                        
                     
        solveSudoku(array)
        #print_sudoku(array)

        for i in range(1,82):
            if not i in nums:
                baghi = i%9
                if baghi == 0 :
                    self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).setText(str(array[int(i/9)-1][8]))
                else:
                    self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).setText(str(array[int((i - baghi )/ 9)][baghi-1]))
            else:
                self.findChild(QtWidgets.QLineEdit, 'input'+str(i)).setStyleSheet(""".QLineEdit {
                                                                                background-color: black;
                                                                                color: rgb( 249, 255, 47 );
                                                                                border-radius: 12px;
                                                                                border: 3px solid red;
                                                                                font-size: 30px;
                                                                                text-align: right;
                                                                                        }""")

                
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

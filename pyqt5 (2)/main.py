import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import ui_newtask, ui_cal,ui_status,ui_popup
#select_text = []
callback = None
check = False

class NewTask(QMainWindow):
    def __init__(self):
        super().__init__()
        # global callback
        # callback = self.uiCallBack()
        self.ui = ui_newtask.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame_2.hide()
        self.ui.graph1.hide()
        self.ui.frame_5.show()
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)
        self.timer3 = QTimer(self)
        self.timer4 = QTimer(self)

        self.counter = 1
        #self.check = False
        self.recognitionflag = False

        self.statusui = Status(self, self.uiCallBack)
        self.calculatorui = Calculator(self)
        # self.statusui.backendCallbk = self.uiCallBack
        self.popupui = PopUp(self)
        self.installEventFilter(self)
        icon = QIcon('icon/recipe.png')
        self.ui.selection.setIcon(icon)
        icon = QIcon('icon/recipe.png')
        self.ui.selection2.setIcon(icon)
        icon = QIcon('icon/recipe.png')
        self.ui.selection3.setIcon(icon)
        icon = QIcon('icon/recipe.png')
        self.ui.selection4.setIcon(icon)
        icon = QIcon('icon/complete.png')
        self.ui.complete.setIcon(icon)
        icon = QIcon('icon/complete.png')
        self.ui.complete2.setIcon(icon)
        icon = QIcon('icon/complete.png')
        self.ui.complete3.setIcon(icon)
        icon = QIcon('icon/complete.png')
        self.ui.complete4.setIcon(icon)
        icon = QIcon('icon/ipad.png')
        self.ui.ipad.setIcon(icon)
        icon = QIcon('icon/ipad.png')
        self.ui.ipad2.setIcon(icon)
        icon = QIcon('icon/ipad.png')
        self.ui.ipad3.setIcon(icon)
        icon = QIcon('icon/ipad.png')
        self.ui.ipad4.setIcon(icon)
        icon = QIcon('icon/ipad.png')
        self.ui.ipad4.setIcon(icon)
        icon = QIcon('icon/ipad.png')
        self.ui.ipad4.setIcon(icon)
        icon = QIcon('icon/usb.png')
        self.ui.usb.setIcon(icon)
        icon = QIcon('icon/worker.png')
        self.ui.person.setIcon(icon)
        icon = QIcon('icon/back.png')
        self.ui.push.setIcon(icon)
        icon = QIcon('icon/back.png')
        self.ui.graph.setIcon(icon)

        self.ui.graph.clicked.connect(self.graphclick)
        self.ui.manual.clicked.connect(self.manualclick)
        self.ui.push.clicked.connect(self.pushclick)
        #self.ui.lineEdit.mousePressEvent = self.opencalculator

        self.ui.off1.clicked.connect(self.off1click)
        self.ui.off2.clicked.connect(self.off2click)
        self.ui.off3.clicked.connect(self.off3click)
        self.ui.off4.clicked.connect(self.off4click)
        for cal in [self.ui.lineEdit, self.ui.lineEdit_67, self.ui.lineEdit_69,
                    self.ui.lineEdit_71, self.ui.lineEdit_72, self.ui.lineEdit_4,
                    self.ui.lineEdit_66, self.ui.lineEdit_68, self.ui.lineEdit_70,
                    self.ui.lineEdit_73]: cal.mousePressEvent = self.opencalculator
        for bowl in [self.ui.bowl1, self.ui.bowl2, self.ui.bowl3,
                     self.ui.bowl4]: bowl.clicked.connect(self.toggle_bowl)

        for offon in [self.ui.off,self.ui.offr1, self.ui.offr2, self.ui.offr3, self.ui.offr4,
                      self.ui.offr5, self.ui.offr6, self.ui.offr7, self.ui.offr8, self.ui.offr9,
                      self.ui.offr10, self.ui.off11, self.ui.off12, self.ui.off13, self.ui.off14,
                      self.ui.offr15, self.ui.offr16, self.ui.offr17, self.ui.offr18, self.ui.offr19,
                      self.ui.offr20, self.ui.offr21, self.ui.offr22, self.ui.offr23, self.ui.offr24,
                      self.ui.offr25, self.ui.offr26, self.ui.offr27,
                      self.ui.offr28]: offon.clicked.connect(self.toggle_text)

        for stop in [self.ui.stop1, self.ui.stop2, self.ui.stop3, self.ui.stop4,
                     self.ui.stop5, self.ui.stop6,self.ui.stop7, self.ui.stop8,
                     self.ui.stop9, self.ui.stop10]: stop.clicked.connect(self.toggle_stop)

        for forwd in [self.ui.fwd1, self.ui.fwd2, self.ui.fwd3, self.ui.fwd4,
                     self.ui.fwd5, self.ui.fwd6,self.ui.fwd7, self.ui.fwd8,
                     self.ui.fwd9, self.ui.fwd10]: forwd.clicked.connect(self.toggle_fwd)

        for disc in [self.ui.disc1, self.ui.disc2, self.ui.disc3, self.ui.disc4,
                     self.ui.disc5, self.ui.disc6]: disc.clicked.connect(self.disc_click)


        for select in [self.ui.selection, self.ui.selection2, self.ui.selection3,
                       self.ui.selection4]: select.clicked.connect(self.selectionclick)

       # for comple in [self.ui.complete, self.ui.complete2, self.ui.complete3,
                      # self.ui.complete4]: comple.clicked.connect(self.completeclick)
        self.ui.complete.clicked.connect(self.completeclick1)
        self.ui.complete2.clicked.connect(self.completeclick2)
        self.ui.complete3.clicked.connect(self.completeclick3)
        self.ui.complete4.clicked.connect(self.completeclick4)

       # for pad in [self.ui.ipad, self.ui.ipad2, self.ui.ipad3,
                      # self.ui.ipad4]: pad.clicked.connect(self.ipadclick)
        self.ui.ipad.clicked.connect(self.ipadclick1)
        self.ui.ipad2.clicked.connect(self.ipadclick2)
        self.ui.ipad3.clicked.connect(self.ipadclick3)
        self.ui.ipad4.clicked.connect(self.ipadclick4)
        self.currently_selected_widget = 0

    def manualclick(self):
       self.ui.frame_5.hide()
       self.ui.frame_2.show()


    def pushclick(self):
        self.ui.frame_2.hide()
        self.ui.frame_5.show()



    def ipadclick1(self):

        self.ui.frame_5.hide()
        self.ui.graph1.show()
    def ipadclick2(self):
        self.ui.frame_5.hide()
        self.ui.graph1.show()
    def ipadclick3(self):
        self.ui.frame_5.hide()
        self.ui.graph1.show()
    def ipadclick4(self):
        self.ui.frame_5.hide()
        self.ui.graph1.show()

    def graphclick(self):
        self.ui.graph1.hide()
        self.ui.frame_5.show()

    def onclicked(self):

        self.ui.frame_5.show()

    def opencalculator(self, mouseEvent):
         sender = self.sender
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=1)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=2)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=3)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=4)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=5)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=6)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=7)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=8)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=9)
         if sender is self.ui.lineEdit:
             self.calculatorui.setsender(num=10)
         self.calculatorui.show()


    def toggle_bowl(self):
        sender_button = self.sender()
        current_text = sender_button.text()

        if current_text == "OFF":
            self.sender().setText("ON")
            self.sender().setStyleSheet("background-color: red;"
                                        "border-radius: 10px;"
                                        "border: 2px solid  #000000;"
                                        "font: 12pt")
        else:
            self.sender().setText("OFF")
            self.sender().setStyleSheet("background-color: #c8c8c8;"
                                        "border-radius: 10px;"
                                        "border: 2px solid  #000000;"
                                        "font: 12pt")

    def toggle_text(self):

         sender_button = self.sender()
         current_text = sender_button.text()

         if current_text == "OFF":
             self.sender().setText("ON")
             self.sender().setStyleSheet("background-color: lightgreen;")
         else:
             self.sender().setText("OFF")
             self.sender().setStyleSheet("background-color: #0392ff;")

    def toggle_stop(self):


          sender_button = self.sender()
          current_text = sender_button.text()

          if current_text == "STOP":
              self.sender().setText("START")
              self.sender().setStyleSheet("background-color: lightgreen;")
          else:
              self.sender().setText("STOP")
              self.sender().setStyleSheet("background-color: #0392ff;")


    def toggle_fwd(self):
        sender_button = self.sender()
        current_text = sender_button.text()
        if current_text == "FWD":
            self.sender().setText("REV")
            self.sender().setStyleSheet("background-color: lightgreen;")
        else:
            self.sender().setText("FWD")
            self.sender().setStyleSheet("background-color: #0392ff;")

    def selectionclick(self):

        self.statusui.reset_fields()

        if self.recognitionflag == False:
            sender = self.sender()
            if sender is self.ui.selection:
                self.statusui.set_sender(id=1)
            elif sender is self.ui.selection2:
                self.statusui.set_sender(id=2)
            elif sender is self.ui.selection3:
                self.statusui.set_sender(id=3)
            elif sender is self.ui.selection4:
                self.statusui.set_sender(id=4)

            self.statusui.ui.successfull.hide()
            self.statusui.ui.food.show()
            self.statusui.showMaximized()




    def completeclick1(self):

      if self.timer.start:
        self.statusui.ui.food.hide()

        self.statusui.ui.successfull.show()
        self.statusui.showMaximized()
      else:
        pass
    def completeclick2(self):

        self.statusui.ui.food.hide()

        self.statusui.ui.successfull.show()
        self.statusui.showMaximized()

    def completeclick3(self):

        self.statusui.ui.food.hide()

        self.statusui.ui.successfull.show()
        self.statusui.showMaximized()

    def completeclick4(self):

        self.statusui.ui.food.hide()

        self.statusui.ui.successfull.show()
        self.statusui.showMaximized()
    def disc_click(self):

            sender = self.sender()


            if self.currently_selected_widget:

                self.currently_selected_widget.setStyleSheet("""QPushButton:hover{\n   
                      background-color:rgb(255, 85, 0);\n          border-radius: 5px;\n}\nQPushButton{\n    
                            border: 2px solidrgb(255, 255, 255);\n	     font: 75 11pt "MS Shell Dlg 2";\n}""")



            sender.setStyleSheet("background-color: red")


            self.currently_selected_widget = sender

    def off1click(self):

       if self.ui.lineEdit_21.text():
         if self.ui.off1.text() == "1 OFF":
            self.ui.off1.setText("1 ON")
            self.popupui.ui.loading.hide()
            self.popupui.ui.send.show()
            self.popupui.show()
            self.timer1.timeout.connect(self.close_dialog1)
            self.timer1.start(1000)
         else:
             self.ui.off1.setText("1 OFF")
             self.ui.red1.setStyleSheet("background-color: red;"
                                        "border-radius: 5px;")
             self.timer1.stop()
             self.ui.te.clear()
             self.counter = 0
             self.ui.lineEdit_21.clear()
             self.ui.lineEdit_22.clear()
             self.ui.lineEdit_23.clear()
             self.ui.lineEdit_13.clear()
             self.ui.lineEdit_28.clear()
             self.recognitionflag = False
       else:
           pass

    def off2click(self):

       if self.ui.lineEdit_15.text():
         if self.ui.off2.text() == "2 OFF":
            self.ui.off2.setText("2 ON")
            self.popupui.ui.loading.hide()
            self.popupui.ui.send.show()
            self.popupui.show()
            self.timer2.timeout.connect(self.close_dialog2)
            self.timer2.start(1000)
         else:
             self.ui.off2.setText("2 OFF")
             self.ui.red2.setStyleSheet("background-color: red;"
                                        "border-radius: 5px;")
             self.timer2.stop()
             self.ui.te2.clear()
             self.counter = 0
             self.ui.lineEdit_15.clear()
             self.ui.lineEdit_16.clear()
             self.ui.lineEdit_17.clear()
             self.ui.lineEdit_27.clear()
             self.ui.lineEdit_30.clear()
             self.recognitionflag = False
       else:
           pass

    def off3click(self):

       if self.ui.lineEdit_29.text():
         if self.ui.off3.text() == "3  OFF":
            self.ui.off3.setText("3  ON")
            self.popupui.ui.loading.hide()
            self.popupui.ui.send.show()
            self.popupui.show()
            self.timer3.timeout.connect(self.close_dialog3)
            self.timer3.start(1000)
         else:
             self.ui.off3.setText("3  OFF")
             self.ui.red3.setStyleSheet("background-color: red;"
                                        "border-radius: 5px;")
             self.timer3.stop()
             self.ui.te3.clear()
             self.counter = 0
             self.ui.lineEdit_29.clear()
             self.ui.lineEdit_12.clear()
             self.ui.lineEdit_24.clear()
             self.ui.lineEdit_25.clear()
             self.ui.lineEdit_26.clear()
             self.recognitionflag = False
       else:
           pass

    def off4click(self):

       if self.ui.lineEdit_18.text():
         if self.ui.off4.text() == "4 OFF":
            self.ui.off4.setText("4 ON")


            self.popupui.ui.loading.hide()
            self.popupui.ui.send.show()
            self.popupui.show()
            self.timer4.timeout.connect(self.close_dialog4)
            self.timer4.start(1000)
         else:
             self.ui.off4.setText("4 OFF")
             self.ui.red4.setStyleSheet("background-color: red;"
                                        "border-radius: 5px;")
             self.timer4.stop()
             self.ui.te4.setText("0")
             self.counter = 0
             self.ui.lineEdit_18.clear()
             self.ui.lineEdit_19.clear()
             self.ui.lineEdit_20.clear()
             self.ui.lineEdit_14.clear()
             self.ui.lineEdit_31.clear()
             self.recognitionflag = False
       else:
           pass

    def close_dialog1(self):
        self.timer1.stop()
        self.popupui.close()
        self.ui.red1.setStyleSheet("background-color: green;"
                                 "border-radius: 5px;")
        self.timer1.start(1000)
        self.ui.te.setText(str(self.counter))
        self.counter += 1

    def close_dialog2(self):
        self.timer2.stop()
        self.popupui.close()
        self.ui.red2.setStyleSheet("background-color: green;"
                                   "border-radius: 5px;")
        self.timer2.start(1000)
        self.ui.te2.setText(str(self.counter))
        self.counter += 1

    def close_dialog3(self):
        self.timer3.stop()
        self.popupui.close()
        self.ui.red3.setStyleSheet("background-color: green;"
                                   "border-radius: 5px;")
        self.timer3.start(1000)
        self.ui.te3.setText(str(self.counter))
        self.counter += 1

    def close_dialog4(self):
        self.timer4.stop()
        self.popupui.close()
        self.ui.red4.setStyleSheet("background-color: green;"
                                   "border-radius: 5px;")
        self.timer4.start(1000)
        self.ui.te4.setText(str(self.counter))
        self.counter += 1




    def uiCallBack(self,action,data,list_id = None):
        global select_text
        print("action" , action)
        print("data = ", data)
        if action == "loadtext":
            print("List id ",list_id)
            if list_id == 1:
                line_edit_fields = [self.ui.lineEdit_21, self.ui.lineEdit_22, self.ui.lineEdit_23,
                                    self.ui.lineEdit_13, self.ui.lineEdit_28]
            elif list_id == 2:
                line_edit_fields = [self.ui.lineEdit_15, self.ui.lineEdit_16, self.ui.lineEdit_17,
                                    self.ui.lineEdit_27, self.ui.lineEdit_30]
            elif list_id == 3:
                line_edit_fields = [self.ui.lineEdit_29, self.ui.lineEdit_12, self.ui.lineEdit_24,
                                    self.ui.lineEdit_25, self.ui.lineEdit_26]
            elif list_id == 4:
                line_edit_fields = [self.ui.lineEdit_18, self.ui.lineEdit_19, self.ui.lineEdit_20,
                                    self.ui.lineEdit_14, self.ui.lineEdit_31]

            for i, line_edit in enumerate(line_edit_fields):
                if i < len(data):
                    line_edit.setText(data[i])

            self.recognitionflag = True
  #  def  uiCallBack1(self,action,data,number = None):
       # if action == "load":
          #  print("data = ", data)
           # if number == 1:
              #  self.ui.lineEdit.setText(data)





class Calculator(QMainWindow):
    def __init__(self,parent,callback = None):
        super().__init__(parent)
        self.ui = ui_cal.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(250,350)
        self.setGeometry(1000,240,300,400)
        self.setWindowFlag(Qt.FramelessWindowHint)
       # self.backendcallbak = callback
       # self.num = None
        self.ui.one.clicked.connect(self.button_click)
        self.ui.two.clicked.connect(self.button_click)
        self.ui.three.clicked.connect(self.button_click)
        self.ui.four_2.clicked.connect(self.button_click)
        self.ui.five.clicked.connect(self.button_click)
        self.ui.six.clicked.connect(self.button_click)
        self.ui.seven.clicked.connect(self.button_click)
        self.ui.eight.clicked.connect(self.button_click)
        self.ui.nine.clicked.connect(self.button_click)
        self.ui.zero.clicked.connect(self.button_click)
        self.ui.dot.clicked.connect(self.button_click)
        self.ui.zero.clicked.connect(self.button_click)
        self.ui.minus.clicked.connect(self.button_click)
        self.ui.clear.clicked.connect(self.clear_function)
        self.ui.back.clicked.connect(self.backclick)
        self.ui.enter.clicked.connect(self.enterclick)





        self.current_expression = ""
        self.ui.output.setText("")  # Assuming you have a QLineEdit widget for displaying the input and result

    def button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == '=':
            try:
                result = str(eval(self.current_expression))
                self.ui.output.setText(result)
                self.current_expression = result
            except Exception as e:
                self.ui.output.setText("Error")
                self.current_expression = ""
        else:
            self.current_expression += text
            self.ui.output.setText(self.current_expression)

    def clear_function(self):

        self.ui.output.clear()
        self.current_expression = ""


    def backclick(self):

        current_text = self.ui.output.text()
        if current_text:
            new_text = current_text[:-1]  # Remove the last character
            self.ui.output.setText(new_text)
            self.current_expression = new_text

    def enterclick(self):
       # current_text = self.ui.output.text()
        #print(current_text)
       # if current_text:
       # self.backendCallbak(action="load", data=current_text, number=self.num)
       # self.num = None
        self.hide()
   # def setsender(self, num):
       # self.num = num



#backendCallbk =None
class Status(QMainWindow):
    def __init__(self,parent, callback=None):
        super().__init__(parent)
        self.ui = ui_status.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.food.hide()
        self.ui.successfull.hide()

        self.id = None

        self.popupui = PopUp(self)

        self.backendCallbk = callback
        self.timer = QTimer(self)
        icon = QIcon('icon/back.png')
        self.ui.push.setIcon(icon)
        icon = QIcon('icon/back.png')
        self.ui.foodback.setIcon(icon)
        self.ui.load.clicked.connect(self.loadclick)
        self.ui.push.clicked.connect(self.pushclick)
        self.ui.foodback.clicked.connect(self.foodclicked)
        for pb in [self.ui.pbNum1,self.ui.pbNum2,self.ui.pbNum3,self.ui.pbNum4,
                   self.ui.pbNum5,self.ui.pbNum6,self.ui.pbNum7,self.ui.pbNum8,
                   self.ui.pbNum9,self.ui.pbNum10,self.ui.pbNum11,self.ui.pbNum12,
                   self.ui.pbNum13,self.ui.pbNum14,self.ui.pbNum15,self.ui.pbNum16,
                   self.ui.pbNum17,self.ui.pbNum18,self.ui.pbNum19,self.ui.pbNum20,
                   self.ui.pbNum21,self.ui.pbNum22,self.ui.pbNum23,self.ui.pbNum24,
                   self.ui.pbNum25,self.ui.pbNum26,self.ui.pbNum27,self.ui.pbNum28,
                   self.ui.pbNum29]: pb.clicked.connect(self.selection)
        #pb.setStyleSheet("QPushButton{ background-color: red; }")

        self.newtaskui = parent
        self.select_text = []
        self.counter = 0
    def foodclicked(self):
        self.close()

    def set_sender(self, id):
        self.id = id


    def reset_fields(self):
        for pb in [self.ui.pbNum1, self.ui.pbNum2, self.ui.pbNum3, self.ui.pbNum4,
                   self.ui.pbNum5, self.ui.pbNum6, self.ui.pbNum7, self.ui.pbNum8,
                   self.ui.pbNum9, self.ui.pbNum10, self.ui.pbNum11, self.ui.pbNum12,
                   self.ui.pbNum13, self.ui.pbNum14, self.ui.pbNum15, self.ui.pbNum16,
                   self.ui.pbNum17, self.ui.pbNum18, self.ui.pbNum19, self.ui.pbNum20,
                   self.ui.pbNum21, self.ui.pbNum22, self.ui.pbNum23, self.ui.pbNum24,
                   self.ui.pbNum25, self.ui.pbNum26, self.ui.pbNum27, self.ui.pbNum28,
                   self.ui.pbNum29]:
            pb.setStyleSheet("""QPushButton{\n	        font: 75 14pt "MS Shell Dlg 2";\n            background-color: rgb(232, 232, 232);\n            border: 2px solid  rgb(86, 86, 86);\n}\nQPushButton:hover{\n            background-color:rgb(255, 85, 0);\n}""")
        self.select_text.clear()
        self.ui.countrecipe.setText("0")
        self.counter = 0
    def selection(self):
      # global select_text
      # select_text = self.select_text
      if self.counter < 5:
        sender = self.sender()
        text = sender.text()
        self.sender().setStyleSheet("background-color: red;")
        self.select_text.append(text)

        self.counter += 1
        self.ui.countrecipe.setText(str(self.counter))



    def loadclick(self):
        # global select_text
      if self.select_text:
        self.backendCallbk(action = "loadtext" , data = self.select_text, list_id = self.id)
        self.select_text = []
        self.id = None
        self.popupui.ui.send.hide()
        self.popupui.ui.loading.show()
        self.popupui.show()
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer_close)
      else:
          pass
    def timer_close(self):
        self.timer.stop()
        self.popupui.close()
        self.close()

    def pushclick(self):
        self.close()
class PopUp(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = ui_popup.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loading.hide()
        self.ui.send.hide()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(250, 350)
        self.setWindowModality(Qt.ApplicationModal)






if __name__ =="__main__":
   app = QApplication(sys.argv)
   window = NewTask()
   window.showMaximized()
   sys.exit(app.exec())
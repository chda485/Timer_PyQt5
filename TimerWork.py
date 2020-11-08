from PyQt5 import QtCore, QtWidgets, QtGui
import sys, TimerForm, playsound

seconds = 0
minutes = 0
       
def on_timeout():
    global minutes
    global seconds
    if minutes == 0 and seconds == 0:
        ui.timer.setText("00:00")
        ui.start.setEnabled(True)
        ui.stop.setEnabled(False)
        ui.minute.setEnabled(True)
        ui.second.setEnabled(True)
        tim.stop()
        playsound.playsound('sound.mp3')
    elif seconds == 0:
        seconds = 59
        minutes -=1
        ui.timer.setText("{:02}".format(minutes) + ":" + (str)(seconds))
    else:
        seconds -=1
        ui.timer.setText("{:02}".format(minutes) + ":" + "{:02}".format(seconds))
        
tim = QtCore.QTimer()
tim.timeout.connect(on_timeout)

def startTimer():
    global minutes
    global seconds
    if ui.second.text() and ui.minute.text():
        seconds = (int)(ui.second.text())
        minutes = (int)(ui.minute.text())
        tim.start(1000)
        ui.start.setEnabled(False)
        ui.stop.setEnabled(True)
        ui.minute.setEnabled(False)
        ui.second.setEnabled(False)

def stopTimer():
    ui.timer.setText("00:00")
    ui.start.setEnabled(True)
    ui.stop.setEnabled(False)
    ui.minute.setEnabled(True)
    ui.second.setEnabled(True)
    tim.stop()

#def proba():

    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = TimerForm.Ui_MainWindow()
ui.setupUi(window)
ui.start.clicked.connect(startTimer)
ui.stop.clicked.connect(stopTimer)
ui.start.setEnabled(True)
ui.stop.setEnabled(False)
window.show()
sys.exit(app.exec_())

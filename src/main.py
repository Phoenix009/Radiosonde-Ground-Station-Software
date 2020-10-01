# standard library imports
import sys 

# third party library imports 
from PySide2.QtWidgets import *

# local imports 
from app.views.StartMenuWindow import StartMenuWindow
if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    
    MainWindow = QMainWindow()
    # QMainWindow using QWidget as central widget
    window = StartMenuWindow()
    window.setupUi(MainWindow)
    MainWindow.show()

    # Execute application
    sys.exit(app.exec_())

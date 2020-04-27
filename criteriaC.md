Criteria C: Developement
==
## Creating a mainApp file:
### a) Starting Imports: 
In order to collect all of my windows into one application, I created a mainApp.py folder. After changing all of the dialog windows into QDialog by importing QDialog and changing from object to QDialog`

from PyQt5.QtWidgets import QDialog 
class Ui_Dialog(QDialog):`

I began with also importing the necessary imports from PyQt5 to the main App. These are: 

`from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QTableWidgetItem
import sys`

As you can see I also imported sys which is the system. After that, to collect all of the different py files to the main app I imported them to the main app and changed their names so that it is easier to work on.

`from untitled2 import Ui_MainWindow as mainW
from login import Ui_Dialog as loginD
from register import Ui_Dialog as regD
from Draftsketch1 import Ui_list as listD`

I added addtional imports but I will get to them when I work on it. 

### b) Creating classes:
I found that the easiest way to work on the different windows of the program in the same file will be through creating classes. I started by creating my mainWindow app by 

`class mainWindowApp(QMainWindow, mainW):
    def __init__(self, parent=None):
        super(mainWindowApp, self).__init__(parent)
        self.setupUi(self)`
        
I modified all of the classes to be their parent so any work I do on a class only affects that window. I did these for the other windows as well. for instance the login window:

`class logInApp(loginD):
    def __init__(self, parent=None):
        super(logInApp, self).__init__(parent)
        self.setupUi(self)`
### c) Final touches before I started the functioning process:

I wanted my login app to appear as the first window so first, I chaned my login app to a stable window so it is attached in front of the mainwindow (from QTDesigner). To make the login app appear first, in the MainWindow class I put 

`logVar = logInApp(self)
 logVar.show()`
 Right under the `self.setupUi` so that the mainwindow app is inaccesable with the login, which looks like this:
 
 ![main window is behind](appic.png)

Finally, since the program is abitrary (personal whim) amount of objects, I had to define QApplications as a container and the main as myMain window. Here is how I did it:

`container = QApplication(sys.argv)
main = mainWindowApp()
main.show()
container.exec_()`

Now that everything is done on the set-up part, I continued on with the functioning buttons

## Functioning Buttons:
### a) Functioning betton for directing to other windows.
To start with the program, I begined with placing the "Login" window in front of the MainWindow which is the menu. Firstly, I 
## Reading a database:

## Login:

## Register:

## Editing

## Adding

## Deleting

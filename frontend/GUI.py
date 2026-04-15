#GUI for the coderisk analyzer 
#Developed a PyQt6 interface with the file selection, tool selection, and the results displays
import sys
from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout, QPushButton, QFileDialog, QLabel, QComboBox, QTextEdit
class CodeRiskAnalyzerGUI(QWidget):
    def __init__(self):
        
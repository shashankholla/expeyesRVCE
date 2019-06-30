import sys, time, utils, math, os.path

from QtVersion import *

import sys, time, utils, math
import pyqtgraph as pg
import numpy as np
import eyes17.eyemath17 as em

class Expt(QWidget):
	TIMER = 50
	def __init__(self, device=None):
		QWidget.__init__(self)
		self.p = device		
		layout = QVBoxLayout()
		H = QHBoxLayout()
		l = QLabel(text=self.tr('Enter Text'))
		l.setMaximumWidth(100)
		H.addWidget(l)
		self.inpText = utils.lineEdit(150, "", 6, None)
		self.inpText.textChanged.connect(self.updateBin)
		H.addWidget(self.inpText)	
		layout.addLayout(H)
		H = QHBoxLayout()
		l = QLabel(text=self.tr('Enter Delay'))
		l.setMaximumWidth(100)
		H.addWidget(l)
		self.delay = utils.lineEdit(50, "", 6, None)
		
		H.addWidget(self.delay)	
		layout.addLayout(H)

		H = QHBoxLayout()
		l = QLabel(text="The binary representation is")
		H.addWidget(l)
		self.binRep = QLabel("")
		

		H = QHBoxLayout()
		self.startInputButton = QPushButton(self.tr("Start"))
		self.startInputButton.clicked.connect(self.send)
		H.addWidget(self.startInputButton)
		layout.addLayout(H)
		full = QVBoxLayout()
		full.addLayout(layout)
		self.setLayout(full)
		self.timer = QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(self.TIMER)

	def updateBin():
		pass

	def send(self):
		ip = self.p.set_pv1(3)

		text = self.inpText.text()
		
		print("Input text" + text)
		outputText = ""
		textList = list(text)
		
		for i in textList:
			l = list(bin(ord(i)))[2:] #get rid of 0b
			recCharBin = ""
			print(l)
			for j in l:
				k = int(j)
				self.p.set_pv1(5*k)
				#read
				time.sleep(0.25)
				read = self.p.get_voltage('A1')
				#print(read)
				if(read >= 1):
					recCharBin = recCharBin + "1"
				else:
					recCharBin = recCharBin + "0"
			recChar = chr(int(recCharBin,2))
			outputText += recChar
			#print(recChar)
			#outputText = outputText + chr(int(recChar,2))
		print(outputText)
		

		
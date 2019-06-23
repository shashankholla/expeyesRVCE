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
		


		full = QVBoxLayout()
		full.addLayout(layout)
		self.setLayout(full)

	def updateBin():
		pass
		
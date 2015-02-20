# -*- coding: utf-8 -*-
# -----------------------#
# License: GPL           #
# Author: NeuronalMotion #
# -----------------------#

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsLinearLayout
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

import subprocess

class NMAmixer(plasmascript.Applet):
    buttonSpeaker = None
    buttonHeadphones = None

    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)
 
        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)

        self.buttonSpeaker = Plasma.PushButton(self.applet)
        self.buttonSpeaker.setText("Rear")
        self.buttonSpeaker.clicked.connect(self.onClickButtonSpeaker)
        self.layout.addItem(self.buttonSpeaker)

        self.buttonHeadphones = Plasma.PushButton(self.applet)
        self.buttonHeadphones.setText("Front")
        self.buttonHeadphones.clicked.connect(self.onClickButtonFront)
        self.layout.addItem(self.buttonHeadphones)

        self.applet.setLayout(self.layout)
        self.resize(75,150)

    def onClickButtonSpeaker(self):
	print "SPEAKER MODE"
	subprocess.Popen(["amixer sset \"Analog Output\" \"Stereo Headphones\""], shell = True)

    def onClickButtonFront(self):
	print "HEADPHONES MODE"
	subprocess.Popen(["amixer sset \"Analog Output\" \"Stereo Headphones FP\""], shell = True)

def CreateApplet(parent):
    return NMAmixer(parent)


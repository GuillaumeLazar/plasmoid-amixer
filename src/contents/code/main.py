# -*- coding: utf-8 -*-
# -----------------------#
# License: GPL           #
# Author: NeuronalMotion #
# -----------------------#

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsLinearLayout
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4 import kdecore

import subprocess
import re
import time
import os

class NMAmixer(plasmascript.Applet):
    cardName = "DGX" #from cat /proc/asound/cards
    mixerControlName = "Analog Output"
    frontAmixerValue = "Stereo Headphones FP"
    rearAmixerValue = "Stereo Headphones"

    frontLabel = "HP"
    rearLabel = "Rear"

    frontPicture = "/images/headphones.png"
    rearPicture = "/images/speaker.png"

    cardIndex = 0
    buttonSwitchOutput = None
    rootPath = None

    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.rootPath = kdecore.KGlobal.dirs().locate("data", "plasma/plasmoids/nm-plasmoid-amixer/contents/")
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)

        self.searchCardIndex()

        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        self.buttonSwitchOutput = Plasma.PushButton(self.applet)
        #self.buttonSwitchOutput.setText(self.getCurrentOutputLabel())
        self.buttonSwitchOutput.setImage(self.getCurrentOutputPicture())
        self.buttonSwitchOutput.clicked.connect(self.onClickButtonSwitchOutput)
        self.layout.addItem(self.buttonSwitchOutput)

        self.applet.setLayout(self.layout)
        self.resize(75,150)

    def searchCardIndex(self):
        proc = subprocess.Popen(["cat /proc/asound/cards | grep %s" % self.cardName], shell = True, stdout = subprocess.PIPE)
        for line in proc.stdout:
            m = re.search("(\\d).*\\[", line)
            self.cardIndex = m.group(1)
            print "card index is %s" % self.cardIndex

    def getCurrentOutputName(self):
        output = ""

        cli = "amixer -c %s sget \"%s\"" % (self.cardIndex, self.mixerControlName)
        print cli
        proc = subprocess.Popen([cli], shell = True, stdout = subprocess.PIPE)

        for line in proc.stdout:
            if "Item0" in line:
                m = re.search("'(.*)'", line)
                output = m.group(1)

        print output
        return output

    def getCurrentOutputLabel(self):
        label = "?"
        outputName = self.getCurrentOutputName()

        if outputName == self.frontAmixerValue:
            label = self.frontLabel
        elif outputName == self.rearAmixerValue:
            label = self.rearLabel

        return label

    def getCurrentOutputPicture(self):
        picture = ""
        outputName = self.getCurrentOutputName()

        if outputName == self.frontAmixerValue:
            picture = self.frontPicture
        elif outputName == self.rearAmixerValue:
            picture = self.rearPicture

        return self.rootPath + picture


    def onClickButtonSwitchOutput(self):
        outputName = self.getCurrentOutputName()
        outputNameTarget = None

        if outputName == self.frontAmixerValue:
            outputNameTarget = self.rearAmixerValue
        elif outputName == self.rearAmixerValue:
            outputNameTarget = self.frontAmixerValue

        cli = "amixer -c %s sset \"Analog Output\" \"%s\"" % (self.cardIndex, outputNameTarget)
        print cli
        subprocess.Popen([cli], shell = True, stdout = subprocess.PIPE)

        # Avoid IOError: [Errno 4] Interrupted system call
        time.sleep(1)

        #self.buttonSwitchOutput.setText(self.getCurrentOutputLabel())
        self.buttonSwitchOutput.setImage(self.getCurrentOutputPicture())

def CreateApplet(parent):
    return NMAmixer(parent)


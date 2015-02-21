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
import re
import time

class NMAmixer(plasmascript.Applet):
    mixerControlName = "Analog Output"
    frontAmixerValue = "Stereo Headphones FP"
    rearAmixerValue = "Stereo Headphones"

    frontLabel = "HP"
    rearLabel = "Rear"

    buttonSwitchOutput = None

    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)

        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)

        self.buttonSwitchOutput = Plasma.PushButton(self.applet)
        self.buttonSwitchOutput.setText(self.getCurrentOutputLabel())
        self.buttonSwitchOutput.clicked.connect(self.onClickButtonSwitchOutput)
        self.layout.addItem(self.buttonSwitchOutput)

        self.applet.setLayout(self.layout)
        self.resize(75,150)

    def getCurrentOutputName(self):
        output = ""

        proc = subprocess.Popen(["amixer sget \"%s\"" % self.mixerControlName], shell = True, stdout = subprocess.PIPE)
        for line in proc.stdout:
            if "Item0" in line:
                m = re.search("'(.*)'", line)
                output = m.group(1)

        return output

    def getCurrentOutputLabel(self):
        label = "?"
        outputName = self.getCurrentOutputName()

        if outputName == self.frontAmixerValue:
            label = self.frontLabel
        elif outputName == self.rearAmixerValue:
            label = self.rearLabel

        return label

    def onClickButtonSwitchOutput(self):
        outputName = self.getCurrentOutputName()
        outputNameTarget = None

        if outputName == self.frontAmixerValue:
            outputNameTarget = self.rearAmixerValue
        elif outputName == self.rearAmixerValue:
            outputNameTarget = self.frontAmixerValue

        subprocess.Popen(["amixer sset \"Analog Output\" \"%s\"" % outputNameTarget], shell = True, stdout = subprocess.PIPE)

        # Avoid IOError: [Errno 4] Interrupted system call
        time.sleep(1)

        self.buttonSwitchOutput.setText(self.getCurrentOutputLabel())

def CreateApplet(parent):
    return NMAmixer(parent)


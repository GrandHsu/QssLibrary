#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年9月2日
@author: Irony."[讽刺]
@email: 892768447@qq.com
@description: 
'''
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from qsslib.Application import Application


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Window(QWidget):

    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        # 加载ui文件
        self.ui = uic.loadUi("ui/buttons.ui", self)

        # 设置按钮属性(不同的属性对应不同的样式)
        self.ui.primaryBtn.setProperty("primary", True)
        self.ui.warningBtn.setProperty("warning", True)
        self.ui.defaultBtn.setProperty("default", True)
        self.ui.dangerBtn.setProperty("danger", True)
        self.ui.successBtn.setProperty("success", True)
        self.ui.inverseBtn.setProperty("inverse", True)
        self.ui.infoBtn.setProperty("info", True)

        # 由于设置属性后需要重新设置样式
        Application.instance().initSkin()

if __name__ == "__main__":
    import sys
    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

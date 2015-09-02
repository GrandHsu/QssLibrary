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
        self.ui = uic.loadUi("ui/QLineEdit.ui", self)

        # 设置按钮属性(不同的属性对应不同的样式)
        self.ui.errorEdit.setProperty("error", True)
        self.ui.successEdit.setProperty("success", True)

        self.ui.searchEdit.setProperty("search", True)

        # 同时带有两种属性
        self.ui.search2Edit.setProperty("search", True)
        self.ui.search2Edit.setProperty("error", True)

        # 由于设置属性后需要重新设置样式
        Application.instance().initSkin()

if __name__ == "__main__":
    import sys
    app = Application(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

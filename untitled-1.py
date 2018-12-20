import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton 
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit, QCheckBox
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QPixmap
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap



class Example(QWidget, QPixmap):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 200, 700, 700)
        self.setWindowTitle('Выбор меню')   

        pix1 = QPixmap("C:\\Users\\RAYKS\\Desktop\\download.jpg")
        pix1 = pix1.scaled(100,100)
        self.label1 = QLabel(self)
        self.label1.setPixmap(pix1)

        pix2 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\download.jpg")
        pix2 = pix2.scaled(100,100)
        self.label2 = QLabel(self)
        self.label2.setPixmap(pix2)               

        pix3 = QPixmap("C:\\Users\\RAYKS\\Desktop\\MpStXtYMIwJ49N9dV00XA.jpg")
        pix3 = pix3.scaled(100,100)
        self.label3 = QLabel(self)
        self.label3.setPixmap(pix3)        

        pix4 = QPixmap("C:\\Users\RAYKS\\Desktop\\Питон D18\\Бургеры\\gurman_dostavka_edi_noviy_urengoy_sezar_roll.png")
        pix4 = pix4.scaled(100,100)
        self.label4 = QLabel(self)
        self.label4.setPixmap(pix4)   

        pix5 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\large_картофель.jpg")
        pix5 = pix5.scaled(100,100)
        self.label5 = QLabel(self)
        self.label5.setPixmap(pix5)  

        pix6 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\large_srimp_800x800_1_.jpg")
        pix6 = pix6.scaled(100,100)
        self.label6 = QLabel(self)
        self.label6.setPixmap(pix6)  

        pix7 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\large_стартер.jpg")
        pix7 = pix7.scaled(100,100)
        self.label7 = QLabel(self)
        self.label7.setPixmap(pix7)  

        pix8 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\large_chicken_wings_big_1_.jpg")
        pix8 = pix8.scaled(100,100)
        self.label8 = QLabel(self)
        self.label8.setPixmap(pix8) 

        pix9 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\large_кока_кола.jpg")
        pix9 = pix9.scaled(100,100)
        self.label9 = QLabel(self)
        self.label9.setPixmap(pix9) 

        pix10 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\large_спрайт_1_.jpg")
        pix10 = pix10.scaled(100,100)
        self.label10 = QLabel(self)
        self.label10.setPixmap(pix10) 

        pix11 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\large_fanta_1_.jpg")
        pix11 = pix11.scaled(100,100)
        self.label11 = QLabel(self)
        self.label11.setPixmap(pix11)

        pix13 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\large_Salsa-big.jpg")
        pix13 = pix13.scaled(100,100)
        self.label13 = QLabel(self)
        self.label13.setPixmap(pix13) 

        pix14 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\Соус-горчица-1-300x300.jpg")
        pix14 = pix14.scaled(100,100)
        self.label14 = QLabel(self)
        self.label14.setPixmap(pix14) 

        pix15 = QPixmap("C:\\Users\\RAYKS\\Desktop\\Питон D18\\Бургеры\\p_O.jpg")
        pix15 = pix15.scaled(100,100)
        self.label15 = QLabel(self)
        self.label15.setPixmap(pix15) 

        self.btn = QPushButton('ЗАКАЗАТЬ', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.hello)

        self.btn1 = QPushButton('ПОСЧИТАТЬ КАЛОРИЙНОСТЬ ЗАКАЗА', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.clicked.connect(self.helloo)

        self.btn2 = QPushButton('РАСПЕЧАТАТЬ ЧЕК', self)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.clicked.connect(self.hellooo)

        self.box1 = QCheckBox(self)
        self.box1.setText("БИГ МАК\t130р")
        self.box1.clicked.connect(self.run1)

        self.box2 = QCheckBox(self)
        self.box2.setText("ФИЛЕ-О-ФИШ\t127р")
        self.box2.clicked.connect(self.run2)

        self.box3 = QCheckBox(self)
        self.box3.setText("БИГ ТЕЙСТИ\t240р")
        self.box3.clicked.connect(self.run3)

        self.box4 = QCheckBox(self)
        self.box4.setText("ЦЕЗАРЬ РОЛЛ\t164р")
        self.box4.clicked.connect(self.run4)

        self.box5 = QCheckBox(self)
        self.box5.setText("ЧИКЕН МАКНАГГЕТС\t105р")
        self.box5.clicked.connect(self.run5)

        self.box6 = QCheckBox(self)
        self.box6.setText("КРЕВЕТКИ\t160р")
        self.box6.clicked.connect(self.run6)

        self.box7 = QCheckBox(self)
        self.box7.setText("КОКА-КОЛА\t90р")
        self.box7.clicked.connect(self.run7)

        self.box9 = QCheckBox(self)
        self.box9.setText("КАРТОФЕЛЬ ФРИ\t44р")
        self.box9.clicked.connect(self.run9)

        self.box10 = QCheckBox(self)
        self.box10.setText("КУРИНЫЕ КРЫЛЫШКИ\t131р")
        self.box10.clicked.connect(self.run10)

        self.box11 = QCheckBox(self)
        self.box11.setText("СПРАЙТ\t90р")
        self.box11.clicked.connect(self.run11)

        self.box12 = QCheckBox(self)
        self.box12.setText("ФАНТА\t90р")
        self.box12.clicked.connect(self.run12)

        self.box13 = QCheckBox(self)
        self.box13.setText("КЕТЧУП\t20р")
        self.box13.clicked.connect(self.run13)

        self.box14 = QCheckBox(self)
        self.box14.setText("ГОРЧИЦА\t20р")
        self.box14.clicked.connect(self.run14)

        self.box15 = QCheckBox(self)
        self.box15.setText("КИСЛО-СЛАДКИЙ\t20р")
        self.box15.clicked.connect(self.run15)

        self.hec = QPlainTextEdit(self)
        self.hec.move(75, 260)

        self.label = QLabel(self)
        self.label.setText("ВАШ ЗАКАЗ:")
        self.label.move(75, 240)

        tab_1 = QFrame() 
        layout_tab_1 = QVBoxLayout()
        layout_tab_1.addWidget(self.label5)
        layout_tab_1.addWidget(self.box9)
        layout_tab_1.addWidget(self.label6)
        layout_tab_1.addWidget(self.box6)
        layout_tab_1.addWidget(self.label7)
        layout_tab_1.addWidget(self.box5) 
        layout_tab_1.addWidget(self.label8)
        layout_tab_1.addWidget(self.box10) 
        tab_1.setLayout(layout_tab_1)

        tab_2 = QFrame()
        layout_tab_2 = QVBoxLayout()
        layout_tab_2.addWidget(self.label1)
        layout_tab_2.addWidget(self.box1)
        layout_tab_2.addWidget(self.label2)
        layout_tab_2.addWidget(self.box2)
        layout_tab_2.addWidget(self.label3)
        layout_tab_2.addWidget(self.box3)
        layout_tab_2.addWidget(self.label4)
        layout_tab_2.addWidget(self.box4)         
        tab_2.setLayout(layout_tab_2) 

        tab_3 = QFrame()
        layout_tab_3 = QVBoxLayout()
        layout_tab_3.addWidget(self.label9)
        layout_tab_3.addWidget(self.box7) 
        layout_tab_3.addWidget(self.label10)
        layout_tab_3.addWidget(self.box11)
        layout_tab_3.addWidget(self.label11)
        layout_tab_3.addWidget(self.box12) 
        tab_3.setLayout(layout_tab_3) 

        tab_4 = QFrame()
        layout_tab_4 = QVBoxLayout()
        layout_tab_4.addWidget(self.label13)
        layout_tab_4.addWidget(self.box13)
        layout_tab_4.addWidget(self.label14)
        layout_tab_4.addWidget(self.box14)
        layout_tab_4.addWidget(self.label15)
        layout_tab_4.addWidget(self.box15)
        tab_4.setLayout(layout_tab_4)

        tab_5 = QFrame()
        layout_tab_5 = QVBoxLayout()
        layout_tab_5.addWidget(self.label)
        layout_tab_5.addWidget(self.hec)
        layout_tab_5.addWidget(self.btn)
        layout_tab_5.addWidget(self.btn1)
        layout_tab_5.addWidget(self.btn2)
        tab_5.setLayout(layout_tab_5)

        self.tab = QTabWidget()
        self.tab.addTab(tab_1, "СТАРТЕРЫ")
        self.tab.addTab(tab_2, "БУРГЕРЫ")
        self.tab.addTab(tab_3, "НАПИТКИ")
        self.tab.addTab(tab_4, "СОУСЫ")
        self.tab.addTab(tab_5, "ВАШ ЗАКАЗ")

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout) 

    def run1(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box101 = i 

    def run2(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box102 = i    

    def run3(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box103 = i    

    def run4(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box104 = i  

    def run5(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box105 = i    

    def run6(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box106 = i    

    def run7(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box107 = i    

    def run9(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box109 = i    

    def run10(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box1010 = i    

    def run11(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box1011 = i    

    def run12(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box1012 = i    

    def run13(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box1013 = i 

    def run14(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box1014 = i 

    def run15(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "", "ВВЕДИТЕ КОЛ-ВО:"
        )
        if okBtnPressed:
            self.box1015 = i    


    def hello(self):
        a = []
        b = 0
        c = 0
        if self.box1.isChecked() is True:
            c = 130*self.box101
            a.append("БИГ МАК\t130р x " + str(self.box101))
            b += c
        if self.box2.isChecked() is True:
            c = 127*self.box102
            a.append("ФИЛЕ-О-ФИШ\t127р x " + str(self.box102))
            b += c
        if self.box3.isChecked() is True: 
            c = 240*self.box103
            a.append("БИГ ТЕЙСТИ\t240р x " + str(self.box103))
            b += c
        if self.box4.isChecked() is True:
            c = 164*self.box104
            a.append("ЦЕЗАРЬ РОЛЛ\t164р x " + str(self.box104))
            b += c
        if self.box5.isChecked() is True:
            c = 105*self.box105
            a.append("ЧИКЕН МАКНАГГЕТС\t105р x " + str(self.box105))
            b += c
        if self.box6.isChecked() is True:
            c = 160*self.box106
            a.append("КРЕВЕТКИ\t160р x " + str(self.box106))
            b += c
        if self.box7.isChecked() is True:
            c = 90*self.box107
            a.append("КОКА-КОЛА\t90р x " + str(self.box107))
            b += c
        if self.box9.isChecked() is True:
            c = 44*self.box109
            a.append("КАРТОФЕЛЬ ФРИ\t44р x " + str(self.box109))
            b += c
        if self.box10.isChecked() is True:
            c = 131*self.box1010
            a.append("КУРИНЫЕ КРЫЛЫШКИ\t131р x " + str(self.box1010))
            b += c
        if self.box11.isChecked() is True:
            c = 90*self.box1011
            a.append("СПРАЙТ\t90р x " + str(self.box1011))
            b += c
        if self.box12.isChecked() is True:
            c = 90*self.box1012
            a.append("ФАНТА\t90р x " + str(self.box1012))
            b += c
        if self.box13.isChecked() is True:
            c = 20*self.box1013
            a.append("КЕТЧУП\t20р x " + str(self.box1013))
            b += c
        if self.box14.isChecked() is True:
            c = 20*self.box1014
            a.append("ГОРЧИЦА\t20р x " + str(self.box1014))
            b += c
        if self.box15.isChecked() is True:
            c = 20*self.box1015
            a.append("КИСЛО-СЛАДКИЙ\t20р x " + str(self.box1015))
            b += c
        a.append("---------------------")
        a.append("ИТОГО: " + str(b) + "р")
        a.append("---------------------")
        a.append('')
        a.append('')
        a.append('')
        self.c = a
        self.hec.setPlainText('\n'.join(a))

    def helloo(self):
        a = []
        b = 0
        c = 0
        if self.box1.isChecked() is True:
            c = 257*self.box101
            a.append("БИГ МАК\t257kkal x " + str(self.box101))
            b += c
        if self.box2.isChecked() is True:
            c = 320*self.box102
            a.append("ФИЛЕ-О-ФИШ\t320kkal x " + str(self.box102))
            b += c
        if self.box3.isChecked() is True: 
            c = 226*self.box103
            a.append("БИГ ТЕЙСТИ\t226kkal x " + str(self.box103))
            b += c
        if self.box4.isChecked() is True:
            c = 510*self.box104
            a.append("ЦЕЗАРЬ РОЛЛ\t510kkal x " + str(self.box104))
            b += c
        if self.box5.isChecked() is True:
            c = 302*self.box105
            a.append("ЧИКЕН МАКНАГГЕТС\t302kkal x " + str(self.box105))
            b += c
        if self.box6.isChecked() is True:
            c = 95*self.box106
            a.append("КРЕВЕТКИ\t95kkal x " + str(self.box106))
            b += c
        if self.box7.isChecked() is True:
            c = 380*self.box107
            a.append("КОКА-КОЛА\t380kkal x " + str(self.box107))
            b += c
        if self.box9.isChecked() is True:
            c = 312*self.box109
            a.append("КАРТОФЕЛЬ ФРИ\t312kkal x " + str(self.box109))
            b += c
        if self.box10.isChecked() is True:
            c = 237*self.box1010
            a.append("КУРИНЫЕ КРЫЛЫШКИ\t237kkal x " + str(self.box1010))
            b += c
        if self.box11.isChecked() is True:
            c = 390*self.box1011
            a.append("СПРАЙТ\t390kkal x " + str(self.box1011))
            b += c
        if self.box12.isChecked() is True:
            c = 480*self.box1012
            a.append("ФАНТА\t480kkal x " + str(self.box1012))
            b += c
        if self.box13.isChecked() is True:
            c = 112*self.box1013
            a.append("КЕТЧУП\t112kkal x " + str(self.box1013))
            b += c
        if self.box14.isChecked() is True:
            c = 112*self.box1014
            a.append("ГОРЧИЦА\t112kkal x " + str(self.box1014))
            b += c
        if self.box15.isChecked() is True:
            c = 112*self.box1015
            a.append("КИСЛО-СЛАДКИЙ\t112kkal x " + str(self.box1015))
            b += c
        a.append("---------------------")
        a.append("ИТОГО: " + str(b) + "kkal")
        a.append("---------------------")       
        self.hec.setPlainText('\n'.join(a))

    def hellooo(self):
        print('\n'.join(self.c))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
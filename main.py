from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout,
                           QSlider, QProgressBar, QTabWidget, QCalendarWidget, QCheckBox)

app = QApplication([])
window = QWidget()

#c1
tab1 = QWidget()
slider = QSlider()
progress = QProgressBar()
progress.setValue(0)

v1 = QVBoxLayout()
v1.addWidget(slider)
v1.addWidget(progress)
tab1.setLayout(v1)

slider.valueChanged.connect(lambda value:progress.setValue(value))
#

#2
tab2 = QWidget()
calendar = QCalendarWidget()
v2 = QVBoxLayout()
v2.addWidget(calendar)
tab2.setLayout(v2)

tab3 = QWidget()
chek = QCheckBox()
v3 = QVBoxLayout()
v3.addWidget(chek)
tab3.setLayout(v3)

#

tabs = QTabWidget()
tabs.addTab(tab1, 'Вкладка №1')
tabs.addTab(tab2, 'Вкладка №2')
tabs.addTab(tab3, 'Вкладка №3')
v2 = QVBoxLayout()
v2.addWidget(tabs)
window.setLayout(v2)




window.show()
app.exec_()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(540, 369)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        SettingsDialog.setToolTip("")
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 330, 521, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.pagesTabWidget = QtWidgets.QTabWidget(SettingsDialog)
        self.pagesTabWidget.setGeometry(QtCore.QRect(10, 10, 521, 311))
        self.pagesTabWidget.setObjectName("pagesTabWidget")
        self.pagesTabWidgetPage1 = QtWidgets.QWidget()
        self.pagesTabWidgetPage1.setObjectName("pagesTabWidgetPage1")
        self.layoutWidget_2 = QtWidgets.QWidget(self.pagesTabWidgetPage1)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 501, 229))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setSpacing(20)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_55.addWidget(self.label_14)
        self.resolutionSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.resolutionSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.resolutionSpinBox.setMinimum(0.1)
        self.resolutionSpinBox.setMaximum(500.0)
        self.resolutionSpinBox.setProperty("value", 20.0)
        self.resolutionSpinBox.setObjectName("resolutionSpinBox")
        self.horizontalLayout_55.addWidget(self.resolutionSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_55)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setSpacing(20)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_54.addWidget(self.label_13)
        self.rowsSeparationSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.rowsSeparationSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.rowsSeparationSpinBox.setMinimum(0.1)
        self.rowsSeparationSpinBox.setMaximum(5.0)
        self.rowsSeparationSpinBox.setProperty("value", 0.7)
        self.rowsSeparationSpinBox.setObjectName("rowsSeparationSpinBox")
        self.horizontalLayout_54.addWidget(self.rowsSeparationSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_54)
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setSpacing(20)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_56.addWidget(self.label_15)
        self.segmentVegThrSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.segmentVegThrSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.segmentVegThrSpinBox.setSuffix("")
        self.segmentVegThrSpinBox.setMinimum(-100.0)
        self.segmentVegThrSpinBox.setMaximum(100.0)
        self.segmentVegThrSpinBox.setProperty("value", 1.0)
        self.segmentVegThrSpinBox.setObjectName("segmentVegThrSpinBox")
        self.horizontalLayout_56.addWidget(self.segmentVegThrSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_56)
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setSpacing(20)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_50.addWidget(self.label)
        self.mapsColormapComboBox = QtWidgets.QComboBox(self.layoutWidget_2)
        self.mapsColormapComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.mapsColormapComboBox.setMinimumContentsLength(0)
        self.mapsColormapComboBox.setObjectName("mapsColormapComboBox")
        self.horizontalLayout_50.addWidget(self.mapsColormapComboBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_50)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setSpacing(20)
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_83.addWidget(self.label_2)
        self.mapsCellWidthSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.mapsCellWidthSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.mapsCellWidthSpinBox.setMinimum(0.1)
        self.mapsCellWidthSpinBox.setProperty("value", 2.0)
        self.mapsCellWidthSpinBox.setObjectName("mapsCellWidthSpinBox")
        self.horizontalLayout_83.addWidget(self.mapsCellWidthSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_83)
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setSpacing(20)
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_86.addWidget(self.label_4)
        self.mapsCellHeightSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.mapsCellHeightSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.mapsCellHeightSpinBox.setMinimum(0.1)
        self.mapsCellHeightSpinBox.setProperty("value", 2.0)
        self.mapsCellHeightSpinBox.setObjectName("mapsCellHeightSpinBox")
        self.horizontalLayout_86.addWidget(self.mapsCellHeightSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_86)
        self.pagesTabWidget.addTab(self.pagesTabWidgetPage1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 20, 501, 191))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.roiAutoDetectCheckBox = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.roiAutoDetectCheckBox.setChecked(True)
        self.roiAutoDetectCheckBox.setObjectName("roiAutoDetectCheckBox")
        self.verticalLayout.addWidget(self.roiAutoDetectCheckBox)
        self.dirAutoDetectCheckBox = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.dirAutoDetectCheckBox.setChecked(True)
        self.dirAutoDetectCheckBox.setObjectName("dirAutoDetectCheckBox")
        self.verticalLayout.addWidget(self.dirAutoDetectCheckBox)
        self.line = QtWidgets.QFrame(self.layoutWidget_3)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.runSegmentVegCheckBox = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.runSegmentVegCheckBox.setChecked(True)
        self.runSegmentVegCheckBox.setObjectName("runSegmentVegCheckBox")
        self.verticalLayout.addWidget(self.runSegmentVegCheckBox)
        self.runDetectRowsCheckBox = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.runDetectRowsCheckBox.setChecked(True)
        self.runDetectRowsCheckBox.setObjectName("runDetectRowsCheckBox")
        self.verticalLayout.addWidget(self.runDetectRowsCheckBox)
        self.runMapVegCheckBox = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.runMapVegCheckBox.setChecked(True)
        self.runMapVegCheckBox.setObjectName("runMapVegCheckBox")
        self.verticalLayout.addWidget(self.runMapVegCheckBox)
        self.runMapWeedsCheckBox = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.runMapWeedsCheckBox.setChecked(True)
        self.runMapWeedsCheckBox.setObjectName("runMapWeedsCheckBox")
        self.verticalLayout.addWidget(self.runMapWeedsCheckBox)
        self.pagesTabWidget.addTab(self.tab, "")
        self.pagesTabWidgetPage2 = QtWidgets.QWidget()
        self.pagesTabWidgetPage2.setObjectName("pagesTabWidgetPage2")
        self.layoutWidget = QtWidgets.QWidget(self.pagesTabWidgetPage2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 19, 501, 229))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setSpacing(20)
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.label_70 = QtWidgets.QLabel(self.layoutWidget)
        self.label_70.setObjectName("label_70")
        self.horizontalLayout_89.addWidget(self.label_70)
        self.rowsDirWindowWidthSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.rowsDirWindowWidthSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.rowsDirWindowWidthSpinBox.setMinimum(0.01)
        self.rowsDirWindowWidthSpinBox.setMaximum(500.0)
        self.rowsDirWindowWidthSpinBox.setProperty("value", 30.0)
        self.rowsDirWindowWidthSpinBox.setObjectName("rowsDirWindowWidthSpinBox")
        self.horizontalLayout_89.addWidget(self.rowsDirWindowWidthSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_89)
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setSpacing(20)
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.label_71 = QtWidgets.QLabel(self.layoutWidget)
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_90.addWidget(self.label_71)
        self.rowsDirWindowHeightSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.rowsDirWindowHeightSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.rowsDirWindowHeightSpinBox.setMinimum(0.01)
        self.rowsDirWindowHeightSpinBox.setMaximum(500.0)
        self.rowsDirWindowHeightSpinBox.setProperty("value", 20.0)
        self.rowsDirWindowHeightSpinBox.setObjectName("rowsDirWindowHeightSpinBox")
        self.horizontalLayout_90.addWidget(self.rowsDirWindowHeightSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_90)
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setSpacing(20)
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.label_68 = QtWidgets.QLabel(self.layoutWidget)
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_84.addWidget(self.label_68)
        self.rowsDetectMaxExtentSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.rowsDetectMaxExtentSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.rowsDetectMaxExtentSpinBox.setMinimum(1.0)
        self.rowsDetectMaxExtentSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.rowsDetectMaxExtentSpinBox.setProperty("value", 5.0)
        self.rowsDetectMaxExtentSpinBox.setObjectName("rowsDetectMaxExtentSpinBox")
        self.horizontalLayout_84.addWidget(self.rowsDetectMaxExtentSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_84)
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setSpacing(20)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.label_69 = QtWidgets.QLabel(self.layoutWidget)
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_85.addWidget(self.label_69)
        self.rowsDetectExtentThrSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.rowsDetectExtentThrSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.rowsDetectExtentThrSpinBox.setMinimum(0.01)
        self.rowsDetectExtentThrSpinBox.setProperty("value", 0.1)
        self.rowsDetectExtentThrSpinBox.setObjectName("rowsDetectExtentThrSpinBox")
        self.horizontalLayout_85.addWidget(self.rowsDetectExtentThrSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_85)
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setSpacing(20)
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.label_74 = QtWidgets.QLabel(self.layoutWidget)
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_88.addWidget(self.label_74)
        self.rowsDetectFusionThrSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.rowsDetectFusionThrSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.rowsDetectFusionThrSpinBox.setMinimum(0.01)
        self.rowsDetectFusionThrSpinBox.setMaximum(5.0)
        self.rowsDetectFusionThrSpinBox.setProperty("value", 0.4)
        self.rowsDetectFusionThrSpinBox.setObjectName("rowsDetectFusionThrSpinBox")
        self.horizontalLayout_88.addWidget(self.rowsDetectFusionThrSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_88)
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setSpacing(20)
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.label_72 = QtWidgets.QLabel(self.layoutWidget)
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_87.addWidget(self.label_72)
        self.rowsDetectLinkThrSpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rowsDetectLinkThrSpinBox.sizePolicy().hasHeightForWidth())
        self.rowsDetectLinkThrSpinBox.setSizePolicy(sizePolicy)
        self.rowsDetectLinkThrSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.rowsDetectLinkThrSpinBox.setSuffix("")
        self.rowsDetectLinkThrSpinBox.setPrefix("")
        self.rowsDetectLinkThrSpinBox.setMinimum(1)
        self.rowsDetectLinkThrSpinBox.setProperty("value", 3)
        self.rowsDetectLinkThrSpinBox.setObjectName("rowsDetectLinkThrSpinBox")
        self.horizontalLayout_87.addWidget(self.rowsDetectLinkThrSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_87)
        self.pagesTabWidget.addTab(self.pagesTabWidgetPage2, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 20, 501, 211))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.roiLineColorLayout = QtWidgets.QHBoxLayout()
        self.roiLineColorLayout.setSpacing(20)
        self.roiLineColorLayout.setObjectName("roiLineColorLayout")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.roiLineColorLayout.addWidget(self.label_17)
        self.verticalLayout_17.addLayout(self.roiLineColorLayout)
        self.rowsDirLineColorLayout = QtWidgets.QHBoxLayout()
        self.rowsDirLineColorLayout.setSpacing(20)
        self.rowsDirLineColorLayout.setObjectName("rowsDirLineColorLayout")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.rowsDirLineColorLayout.addWidget(self.label_18)
        self.verticalLayout_17.addLayout(self.rowsDirLineColorLayout)
        self.rowsRidgesColorLayout = QtWidgets.QHBoxLayout()
        self.rowsRidgesColorLayout.setSpacing(20)
        self.rowsRidgesColorLayout.setObjectName("rowsRidgesColorLayout")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.rowsRidgesColorLayout.addWidget(self.label_19)
        self.verticalLayout_17.addLayout(self.rowsRidgesColorLayout)
        self.rowsFurrowsColorLayout = QtWidgets.QHBoxLayout()
        self.rowsFurrowsColorLayout.setSpacing(20)
        self.rowsFurrowsColorLayout.setObjectName("rowsFurrowsColorLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.rowsFurrowsColorLayout.addWidget(self.label_3)
        self.verticalLayout_17.addLayout(self.rowsFurrowsColorLayout)
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setSpacing(20)
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_91.addWidget(self.label_5)
        self.drawLineWidthSpinBox = QtWidgets.QSpinBox(self.layoutWidget_4)
        self.drawLineWidthSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.drawLineWidthSpinBox.setMinimum(1)
        self.drawLineWidthSpinBox.setMaximum(10)
        self.drawLineWidthSpinBox.setObjectName("drawLineWidthSpinBox")
        self.horizontalLayout_91.addWidget(self.drawLineWidthSpinBox)
        self.verticalLayout_17.addLayout(self.horizontalLayout_91)
        self.pagesTabWidget.addTab(self.tab_2, "")

        self.retranslateUi(SettingsDialog)
        self.pagesTabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Dialog"))
        self.label_14.setText(_translate("SettingsDialog", "Input image resolution:"))
        self.resolutionSpinBox.setSuffix(_translate("SettingsDialog", " px/m"))
        self.label_13.setText(_translate("SettingsDialog", "Mean crop row separation:"))
        self.rowsSeparationSpinBox.setSuffix(_translate("SettingsDialog", " m"))
        self.label_15.setText(_translate("SettingsDialog", "Vegetation threshold:"))
        self.label.setText(_translate("SettingsDialog", "Colormap:"))
        self.label_2.setText(_translate("SettingsDialog", "Map grid cell width:"))
        self.mapsCellWidthSpinBox.setSuffix(_translate("SettingsDialog", " m"))
        self.label_4.setText(_translate("SettingsDialog", "Map grid cell height:"))
        self.mapsCellHeightSpinBox.setSuffix(_translate("SettingsDialog", " m"))
        self.pagesTabWidget.setTabText(self.pagesTabWidget.indexOf(self.pagesTabWidgetPage1), _translate("SettingsDialog", "General"))
        self.roiAutoDetectCheckBox.setText(_translate("SettingsDialog", "Detect main crop area"))
        self.dirAutoDetectCheckBox.setText(_translate("SettingsDialog", "Detect crop rows direction"))
        self.runSegmentVegCheckBox.setText(_translate("SettingsDialog", "Segment vegetation"))
        self.runDetectRowsCheckBox.setText(_translate("SettingsDialog", "Detect crop rows"))
        self.runMapVegCheckBox.setText(_translate("SettingsDialog", "Map vegetation density"))
        self.runMapWeedsCheckBox.setText(_translate("SettingsDialog", "Map weed density"))
        self.pagesTabWidget.setTabText(self.pagesTabWidget.indexOf(self.tab), _translate("SettingsDialog", "Processing steps"))
        self.label_70.setText(_translate("SettingsDialog", "Direction window width:"))
        self.rowsDirWindowWidthSpinBox.setSuffix(_translate("SettingsDialog", " m"))
        self.label_71.setText(_translate("SettingsDialog", "Direction window height:"))
        self.rowsDirWindowHeightSpinBox.setSuffix(_translate("SettingsDialog", " m"))
        self.label_68.setText(_translate("SettingsDialog", "Maximum profile extent:"))
        self.rowsDetectMaxExtentSpinBox.setSuffix(_translate("SettingsDialog", " m"))
        self.label_69.setText(_translate("SettingsDialog", "Profile extent threshold:"))
        self.rowsDetectExtentThrSpinBox.setSuffix(_translate("SettingsDialog", " m"))
        self.label_74.setText(_translate("SettingsDialog", "Fusion threshold:"))
        self.label_72.setText(_translate("SettingsDialog", "Linking threshold:"))
        self.rowsDetectLinkThrSpinBox.setToolTip(_translate("SettingsDialog", "Resizes images by the largest side.\n"
" Set to zero to skip resize"))
        self.pagesTabWidget.setTabText(self.pagesTabWidget.indexOf(self.pagesTabWidgetPage2), _translate("SettingsDialog", "Rows detection"))
        self.label_17.setText(_translate("SettingsDialog", "ROI polygon line color:"))
        self.label_18.setText(_translate("SettingsDialog", "Rows direction line color:"))
        self.label_19.setText(_translate("SettingsDialog", "Crow rows ridges color:"))
        self.label_3.setText(_translate("SettingsDialog", "Crop rows furrows color:"))
        self.label_5.setText(_translate("SettingsDialog", "Line width:"))
        self.pagesTabWidget.setTabText(self.pagesTabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "Drawing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsDialog = QtWidgets.QDialog()
    ui = Ui_SettingsDialog()
    ui.setupUi(SettingsDialog)
    SettingsDialog.show()
    sys.exit(app.exec_())

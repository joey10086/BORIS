# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boris.ui'
#
# Created: Thu Oct  6 15:15:00 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbLogoBoris = QtWidgets.QLabel(self.centralwidget)
        self.lbLogoBoris.setText("")
        self.lbLogoBoris.setScaledContents(False)
        self.lbLogoBoris.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLogoBoris.setObjectName("lbLogoBoris")
        self.verticalLayout_3.addWidget(self.lbLogoBoris)
        self.lbLogoUnito = QtWidgets.QLabel(self.centralwidget)
        self.lbLogoUnito.setText("")
        self.lbLogoUnito.setTextFormat(QtCore.Qt.AutoText)
        self.lbLogoUnito.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLogoUnito.setWordWrap(True)
        self.lbLogoUnito.setObjectName("lbLogoUnito")
        self.verticalLayout_3.addWidget(self.lbLogoUnito)
        self.lbFocalSubject = QtWidgets.QLabel(self.centralwidget)
        self.lbFocalSubject.setObjectName("lbFocalSubject")
        self.verticalLayout_3.addWidget(self.lbFocalSubject)
        self.lbCurrentStates = QtWidgets.QLabel(self.centralwidget)
        self.lbCurrentStates.setObjectName("lbCurrentStates")
        self.verticalLayout_3.addWidget(self.lbCurrentStates)
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setEnabled(True)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 522, 402))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuObservations = QtWidgets.QMenu(self.menubar)
        self.menuObservations.setObjectName("menuObservations")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        self.menuPlayback = QtWidgets.QMenu(self.menubar)
        self.menuPlayback.setObjectName("menuPlayback")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuTransitions_flow_diagram = QtWidgets.QMenu(self.menuTools)
        self.menuTransitions_flow_diagram.setObjectName("menuTransitions_flow_diagram")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setToolTip("")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dwEthogram = QtWidgets.QDockWidget(MainWindow)
        self.dwEthogram.setFloating(False)
        self.dwEthogram.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dwEthogram.setObjectName("dwEthogram")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.twEthogram = QtWidgets.QTableWidget(self.dockWidgetContents_3)
        self.twEthogram.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twEthogram.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twEthogram.setAlternatingRowColors(True)
        self.twEthogram.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twEthogram.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twEthogram.setObjectName("twEthogram")
        self.twEthogram.setColumnCount(6)
        self.twEthogram.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twEthogram.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twEthogram.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twEthogram.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twEthogram.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twEthogram.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twEthogram.setHorizontalHeaderItem(5, item)
        self.verticalLayout_4.addWidget(self.twEthogram)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.dwEthogram.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwEthogram)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dwObservations = QtWidgets.QDockWidget(MainWindow)
        self.dwObservations.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dwObservations.setFloating(False)
        self.dwObservations.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dwObservations.setObjectName("dwObservations")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.twEvents = QtWidgets.QTableWidget(self.dockWidgetContents_2)
        self.twEvents.setEnabled(True)
        self.twEvents.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twEvents.setAutoScroll(False)
        self.twEvents.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twEvents.setTabKeyNavigation(False)
        self.twEvents.setProperty("showDropIndicator", False)
        self.twEvents.setDragDropOverwriteMode(False)
        self.twEvents.setAlternatingRowColors(True)
        self.twEvents.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.twEvents.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twEvents.setObjectName("twEvents")
        self.twEvents.setColumnCount(0)
        self.twEvents.setRowCount(0)
        self.verticalLayout.addWidget(self.twEvents)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.dwObservations.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dwObservations)
        self.dwSubjects = QtWidgets.QDockWidget(MainWindow)
        self.dwSubjects.setFloating(False)
        self.dwSubjects.setObjectName("dwSubjects")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.twSubjects = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.twSubjects.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twSubjects.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twSubjects.setAlternatingRowColors(True)
        self.twSubjects.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twSubjects.setObjectName("twSubjects")
        self.twSubjects.setColumnCount(4)
        self.twSubjects.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.twSubjects)
        self.dwSubjects.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwSubjects)
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPause = QtWidgets.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setObjectName("actionPlay")
        self.actionOpen_video_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_video_file.setObjectName("actionOpen_video_file")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionFaster = QtWidgets.QAction(MainWindow)
        self.actionFaster.setEnabled(True)
        self.actionFaster.setObjectName("actionFaster")
        self.actionSlower = QtWidgets.QAction(MainWindow)
        self.actionSlower.setEnabled(True)
        self.actionSlower.setObjectName("actionSlower")
        self.actionJumpForward = QtWidgets.QAction(MainWindow)
        self.actionJumpForward.setObjectName("actionJumpForward")
        self.actionLoad_configuration = QtWidgets.QAction(MainWindow)
        self.actionLoad_configuration.setObjectName("actionLoad_configuration")
        self.actionDelete_selected_observations = QtWidgets.QAction(MainWindow)
        self.actionDelete_selected_observations.setObjectName("actionDelete_selected_observations")
        self.actionDelete_all_observations = QtWidgets.QAction(MainWindow)
        self.actionDelete_all_observations.setObjectName("actionDelete_all_observations")
        self.actionSort_observations = QtWidgets.QAction(MainWindow)
        self.actionSort_observations.setObjectName("actionSort_observations")
        self.actionLoad_observations_file = QtWidgets.QAction(MainWindow)
        self.actionLoad_observations_file.setObjectName("actionLoad_observations_file")
        self.actionSelect_observations = QtWidgets.QAction(MainWindow)
        self.actionSelect_observations.setObjectName("actionSelect_observations")
        self.actionConfigure_states_and_events = QtWidgets.QAction(MainWindow)
        self.actionConfigure_states_and_events.setEnabled(False)
        self.actionConfigure_states_and_events.setObjectName("actionConfigure_states_and_events")
        self.actionEdit_event = QtWidgets.QAction(MainWindow)
        self.actionEdit_event.setObjectName("actionEdit_event")
        self.actionLoad_configuration_file = QtWidgets.QAction(MainWindow)
        self.actionLoad_configuration_file.setObjectName("actionLoad_configuration_file")
        self.actionMedia_file_information = QtWidgets.QAction(MainWindow)
        self.actionMedia_file_information.setObjectName("actionMedia_file_information")
        self.actionStart_live_observation = QtWidgets.QAction(MainWindow)
        self.actionStart_live_observation.setObjectName("actionStart_live_observation")
        self.actionNew_project = QtWidgets.QAction(MainWindow)
        self.actionNew_project.setObjectName("actionNew_project")
        self.actionTime_budget = QtWidgets.QAction(MainWindow)
        self.actionTime_budget.setObjectName("actionTime_budget")
        self.actionSave_project = QtWidgets.QAction(MainWindow)
        self.actionSave_project.setObjectName("actionSave_project")
        self.actionOpen_project = QtWidgets.QAction(MainWindow)
        self.actionOpen_project.setObjectName("actionOpen_project")
        self.actionSet_offset = QtWidgets.QAction(MainWindow)
        self.actionSet_offset.setObjectName("actionSet_offset")
        self.actionEdit_project = QtWidgets.QAction(MainWindow)
        self.actionEdit_project.setObjectName("actionEdit_project")
        self.actionSave_project_as = QtWidgets.QAction(MainWindow)
        self.actionSave_project_as.setObjectName("actionSave_project_as")
        self.actionVisualize_data = QtWidgets.QAction(MainWindow)
        self.actionVisualize_data.setObjectName("actionVisualize_data")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionNew_observation = QtWidgets.QAction(MainWindow)
        self.actionNew_observation.setObjectName("actionNew_observation")
        self.actionSave_observation = QtWidgets.QAction(MainWindow)
        self.actionSave_observation.setObjectName("actionSave_observation")
        self.actionClose_observation = QtWidgets.QAction(MainWindow)
        self.actionClose_observation.setObjectName("actionClose_observation")
        self.actionEdit_current_observation = QtWidgets.QAction(MainWindow)
        self.actionEdit_current_observation.setEnabled(False)
        self.actionEdit_current_observation.setObjectName("actionEdit_current_observation")
        self.actionOpen_observation_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_observation_2.setEnabled(False)
        self.actionOpen_observation_2.setVisible(False)
        self.actionOpen_observation_2.setObjectName("actionOpen_observation_2")
        self.actionAdd_event = QtWidgets.QAction(MainWindow)
        self.actionAdd_event.setObjectName("actionAdd_event")
        self.actionDeselectCurrentSubject = QtWidgets.QAction(MainWindow)
        self.actionDeselectCurrentSubject.setObjectName("actionDeselectCurrentSubject")
        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setIconVisibleInMenu(False)
        self.actionNext.setObjectName("actionNext")
        self.actionPrevious = QtWidgets.QAction(MainWindow)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionJumpTo = QtWidgets.QAction(MainWindow)
        self.actionJumpTo.setEnabled(True)
        self.actionJumpTo.setObjectName("actionJumpTo")
        self.actionJumpBackward = QtWidgets.QAction(MainWindow)
        self.actionJumpBackward.setObjectName("actionJumpBackward")
        self.actionEdit_observation = QtWidgets.QAction(MainWindow)
        self.actionEdit_observation.setEnabled(False)
        self.actionEdit_observation.setVisible(False)
        self.actionEdit_observation.setObjectName("actionEdit_observation")
        self.actionCheckUpdate = QtWidgets.QAction(MainWindow)
        self.actionCheckUpdate.setObjectName("actionCheckUpdate")
        self.actionExportEvents = QtWidgets.QAction(MainWindow)
        self.actionExportEvents.setObjectName("actionExportEvents")
        self.actionExportEventString = QtWidgets.QAction(MainWindow)
        self.actionExportEventString.setObjectName("actionExportEventString")
        self.actionClose_project = QtWidgets.QAction(MainWindow)
        self.actionClose_project.setObjectName("actionClose_project")
        self.actionObservationsList = QtWidgets.QAction(MainWindow)
        self.actionObservationsList.setObjectName("actionObservationsList")
        self.actionMapCreator = QtWidgets.QAction(MainWindow)
        self.actionMapCreator.setObjectName("actionMapCreator")
        self.actionNormalSpeed = QtWidgets.QAction(MainWindow)
        self.actionNormalSpeed.setObjectName("actionNormalSpeed")
        self.actionSnapshot = QtWidgets.QAction(MainWindow)
        self.actionSnapshot.setObjectName("actionSnapshot")
        self.actionFrame_by_frame = QtWidgets.QAction(MainWindow)
        self.actionFrame_by_frame.setCheckable(True)
        self.actionFrame_by_frame.setObjectName("actionFrame_by_frame")
        self.actionExportEventsSQL = QtWidgets.QAction(MainWindow)
        self.actionExportEventsSQL.setObjectName("actionExportEventsSQL")
        self.actionAggregatedEventsTabularFormat = QtWidgets.QAction(MainWindow)
        self.actionAggregatedEventsTabularFormat.setObjectName("actionAggregatedEventsTabularFormat")
        self.actionOpen_observation = QtWidgets.QAction(MainWindow)
        self.actionOpen_observation.setObjectName("actionOpen_observation")
        self.actionExportEventTabular_ODS = QtWidgets.QAction(MainWindow)
        self.actionExportEventTabular_ODS.setObjectName("actionExportEventTabular_ODS")
        self.actionAaaa = QtWidgets.QAction(MainWindow)
        self.actionAaaa.setObjectName("actionAaaa")
        self.menuCreate_subtitles_2 = QtWidgets.QAction(MainWindow)
        self.menuCreate_subtitles_2.setObjectName("menuCreate_subtitles_2")
        self.actionExportEventTabular_XLS = QtWidgets.QAction(MainWindow)
        self.actionExportEventTabular_XLS.setObjectName("actionExportEventTabular_XLS")
        self.actionUser_guide = QtWidgets.QAction(MainWindow)
        self.actionUser_guide.setObjectName("actionUser_guide")
        self.actionEdit_observation_2 = QtWidgets.QAction(MainWindow)
        self.actionEdit_observation_2.setObjectName("actionEdit_observation_2")
        self.actionCheckStateEvents = QtWidgets.QAction(MainWindow)
        self.actionCheckStateEvents.setObjectName("actionCheckStateEvents")
        self.actionEdit_selected_events = QtWidgets.QAction(MainWindow)
        self.actionEdit_selected_events.setObjectName("actionEdit_selected_events")
        self.actionShow_spectrogram = QtWidgets.QAction(MainWindow)
        self.actionShow_spectrogram.setObjectName("actionShow_spectrogram")
        self.actionExport_events_as_Praat_TextGrid = QtWidgets.QAction(MainWindow)
        self.actionExport_events_as_Praat_TextGrid.setObjectName("actionExport_events_as_Praat_TextGrid")
        self.actionExtract_events_from_media_files = QtWidgets.QAction(MainWindow)
        self.actionExtract_events_from_media_files.setObjectName("actionExtract_events_from_media_files")
        self.actionDistance = QtWidgets.QAction(MainWindow)
        self.actionDistance.setObjectName("actionDistance")
        self.actionFrame_forward = QtWidgets.QAction(MainWindow)
        self.actionFrame_forward.setObjectName("actionFrame_forward")
        self.actionFrame_backward = QtWidgets.QAction(MainWindow)
        self.actionFrame_backward.setObjectName("actionFrame_backward")
        self.actionFilterBehaviors = QtWidgets.QAction(MainWindow)
        self.actionFilterBehaviors.setObjectName("actionFilterBehaviors")
        self.actionShowAllBehaviors = QtWidgets.QAction(MainWindow)
        self.actionShowAllBehaviors.setObjectName("actionShowAllBehaviors")
        self.actionExport_aggregated_events = QtWidgets.QAction(MainWindow)
        self.actionExport_aggregated_events.setObjectName("actionExport_aggregated_events")
        self.actionBehaviors_map = QtWidgets.QAction(MainWindow)
        self.actionBehaviors_map.setObjectName("actionBehaviors_map")
        self.actionTime_budget_by_behaviors_category = QtWidgets.QAction(MainWindow)
        self.actionTime_budget_by_behaviors_category.setObjectName("actionTime_budget_by_behaviors_category")
        self.actionExport_events_as_SDIS_file = QtWidgets.QAction(MainWindow)
        self.actionExport_events_as_SDIS_file.setObjectName("actionExport_events_as_SDIS_file")
        self.actionRecode_resize_video = QtWidgets.QAction(MainWindow)
        self.actionRecode_resize_video.setObjectName("actionRecode_resize_video")
        self.actionMedia_file_information_2 = QtWidgets.QAction(MainWindow)
        self.actionMedia_file_information_2.setObjectName("actionMedia_file_information_2")
        self.actionCreate_transitions_matrix = QtWidgets.QAction(MainWindow)
        self.actionCreate_transitions_matrix.setObjectName("actionCreate_transitions_matrix")
        self.actionCreate_transitions_flow_diagram = QtWidgets.QAction(MainWindow)
        self.actionCreate_transitions_flow_diagram.setObjectName("actionCreate_transitions_flow_diagram")
        self.menuHelp.addAction(self.actionUser_guide)
        self.menuHelp.addAction(self.actionCheckUpdate)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionNew_project)
        self.menuFile.addAction(self.actionOpen_project)
        self.menuFile.addAction(self.actionEdit_project)
        self.menuFile.addAction(self.actionSave_project)
        self.menuFile.addAction(self.actionSave_project_as)
        self.menuFile.addAction(self.actionClose_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuObservations.addAction(self.actionNew_observation)
        self.menuObservations.addAction(self.actionOpen_observation)
        self.menuObservations.addAction(self.actionEdit_observation_2)
        self.menuObservations.addAction(self.actionObservationsList)
        self.menuObservations.addAction(self.actionOpen_observation_2)
        self.menuObservations.addAction(self.actionEdit_observation)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionClose_observation)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionAdd_event)
        self.menuObservations.addAction(self.actionEdit_selected_events)
        self.menuObservations.addAction(self.actionCheckStateEvents)
        self.menuObservations.addAction(self.actionSelect_observations)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionDelete_selected_observations)
        self.menuObservations.addAction(self.actionDelete_all_observations)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionLoad_observations_file)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionExportEvents)
        self.menuObservations.addAction(self.actionExport_aggregated_events)
        self.menuObservations.addAction(self.actionExportEventString)
        self.menuObservations.addAction(self.actionExport_events_as_Praat_TextGrid)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.menuCreate_subtitles_2)
        self.menuObservations.addAction(self.actionMedia_file_information)
        self.menuObservations.addAction(self.actionExtract_events_from_media_files)
        self.menuObservations.addAction(self.actionCreate_transitions_matrix)
        self.menuAnalyze.addAction(self.actionTime_budget)
        self.menuAnalyze.addAction(self.actionTime_budget_by_behaviors_category)
        self.menuAnalyze.addAction(self.actionVisualize_data)
        self.menuPlayback.addAction(self.actionJumpForward)
        self.menuPlayback.addAction(self.actionJumpBackward)
        self.menuPlayback.addAction(self.actionJumpTo)
        self.menuPlayback.addSeparator()
        self.menuPlayback.addAction(self.actionPlay)
        self.menuPlayback.addAction(self.actionPause)
        self.menuPlayback.addAction(self.actionPrevious)
        self.menuPlayback.addAction(self.actionNext)
        self.menuTransitions_flow_diagram.addAction(self.actionCreate_transitions_flow_diagram)
        self.menuTools.addAction(self.actionShow_spectrogram)
        self.menuTools.addAction(self.actionDistance)
        self.menuTools.addAction(self.actionBehaviors_map)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionMapCreator)
        self.menuTools.addAction(self.actionRecode_resize_video)
        self.menuTools.addAction(self.actionMedia_file_information_2)
        self.menuTools.addAction(self.menuTransitions_flow_diagram.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuObservations.menuAction())
        self.menubar.addAction(self.menuPlayback.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addAction(self.actionJumpBackward)
        self.toolBar.addAction(self.actionJumpForward)
        self.toolBar.addAction(self.actionNormalSpeed)
        self.toolBar.addAction(self.actionFaster)
        self.toolBar.addAction(self.actionSlower)
        self.toolBar.addAction(self.actionPrevious)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addAction(self.actionSnapshot)
        self.toolBar.addAction(self.actionFrame_by_frame)
        self.toolBar.addAction(self.actionFrame_backward)
        self.toolBar.addAction(self.actionFrame_forward)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BORIS"))
        self.lbFocalSubject.setText(_translate("MainWindow", "lbFocalSubject"))
        self.lbCurrentStates.setText(_translate("MainWindow", "lbCurrentStates"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuObservations.setTitle(_translate("MainWindow", "Observations"))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analysis"))
        self.menuPlayback.setTitle(_translate("MainWindow", "Playback"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuTransitions_flow_diagram.setTitle(_translate("MainWindow", "Transitions flow diagram"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dwEthogram.setWindowTitle(_translate("MainWindow", "Ethogram"))
        item = self.twEthogram.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key"))
        item = self.twEthogram.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Code"))
        item = self.twEthogram.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.twEthogram.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description"))
        item = self.twEthogram.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Modifiers"))
        item = self.twEthogram.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Excluded"))
        self.dwObservations.setWindowTitle(_translate("MainWindow", "Events"))
        self.dwSubjects.setWindowTitle(_translate("MainWindow", "Subjects"))
        item = self.twSubjects.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key"))
        item = self.twSubjects.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.twSubjects.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.twSubjects.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Current state(s)"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setToolTip(_translate("MainWindow", "Pause"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionOpen_video_file.setText(_translate("MainWindow", "Open media file"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionFaster.setText(_translate("MainWindow", "Faster"))
        self.actionSlower.setText(_translate("MainWindow", "Slower"))
        self.actionJumpForward.setText(_translate("MainWindow", "Jump forward"))
        self.actionLoad_configuration.setText(_translate("MainWindow", "Load configuration"))
        self.actionDelete_selected_observations.setText(_translate("MainWindow", "Delete selected events"))
        self.actionDelete_all_observations.setText(_translate("MainWindow", "Delete all events"))
        self.actionSort_observations.setText(_translate("MainWindow", "Sort events"))
        self.actionLoad_observations_file.setText(_translate("MainWindow", "Import events"))
        self.actionSelect_observations.setText(_translate("MainWindow", "Select events from interval"))
        self.actionConfigure_states_and_events.setText(_translate("MainWindow", "Configure states and events"))
        self.actionEdit_event.setText(_translate("MainWindow", "Edit event"))
        self.actionLoad_configuration_file.setText(_translate("MainWindow", "Load state and events configuration file"))
        self.actionMedia_file_information.setText(_translate("MainWindow", "Media file information"))
        self.actionStart_live_observation.setText(_translate("MainWindow", "Start observation without media file"))
        self.actionNew_project.setText(_translate("MainWindow", "New project"))
        self.actionNew_project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionTime_budget.setText(_translate("MainWindow", "Time budget"))
        self.actionSave_project.setText(_translate("MainWindow", "Save project"))
        self.actionSave_project.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen_project.setText(_translate("MainWindow", "Open project"))
        self.actionOpen_project.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSet_offset.setText(_translate("MainWindow", "Set time offset"))
        self.actionEdit_project.setText(_translate("MainWindow", "Edit project"))
        self.actionSave_project_as.setText(_translate("MainWindow", "Save project as ..."))
        self.actionVisualize_data.setText(_translate("MainWindow", "Plot events"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionNew_observation.setText(_translate("MainWindow", "New observation"))
        self.actionSave_observation.setText(_translate("MainWindow", "Save current observation"))
        self.actionClose_observation.setText(_translate("MainWindow", "Close observation"))
        self.actionEdit_current_observation.setText(_translate("MainWindow", "Edit current observation"))
        self.actionOpen_observation_2.setText(_translate("MainWindow", "Open observation"))
        self.actionAdd_event.setText(_translate("MainWindow", "Add event"))
        self.actionDeselectCurrentSubject.setText(_translate("MainWindow", "Deselect current subject"))
        self.actionNext.setText(_translate("MainWindow", "Next"))
        self.actionNext.setToolTip(_translate("MainWindow", "Next media file"))
        self.actionPrevious.setText(_translate("MainWindow", "Previous"))
        self.actionPrevious.setToolTip(_translate("MainWindow", "Previous media file"))
        self.actionJumpTo.setText(_translate("MainWindow", "Jump to specific time"))
        self.actionJumpBackward.setText(_translate("MainWindow", "Jump backward"))
        self.actionJumpBackward.setToolTip(_translate("MainWindow", "Jump backward"))
        self.actionEdit_observation.setText(_translate("MainWindow", "Edit observation"))
        self.actionCheckUpdate.setText(_translate("MainWindow", "Check for updates"))
        self.actionExportEvents.setText(_translate("MainWindow", "Export events"))
        self.actionExportEventString.setText(_translate("MainWindow", "Export events as behavioural strings"))
        self.actionClose_project.setText(_translate("MainWindow", "Close project"))
        self.actionObservationsList.setText(_translate("MainWindow", "Observations list"))
        self.actionMapCreator.setText(_translate("MainWindow", "Map creator"))
        self.actionNormalSpeed.setText(_translate("MainWindow", "Normal speed"))
        self.actionSnapshot.setText(_translate("MainWindow", "Snapshot"))
        self.actionFrame_by_frame.setText(_translate("MainWindow", "Frame by frame"))
        self.actionExportEventsSQL.setText(_translate("MainWindow", "Structured Query Language (SQL)"))
        self.actionAggregatedEventsTabularFormat.setText(_translate("MainWindow", "Tab Separated Values (tsv)"))
        self.actionOpen_observation.setText(_translate("MainWindow", "Open observation"))
        self.actionExportEventTabular_ODS.setText(_translate("MainWindow", "Open Document Spreadsheet (ods)"))
        self.actionAaaa.setText(_translate("MainWindow", "aaaa"))
        self.menuCreate_subtitles_2.setText(_translate("MainWindow", "Create subtitles"))
        self.actionExportEventTabular_XLS.setText(_translate("MainWindow", "Microsoft Excel format (xls)"))
        self.actionUser_guide.setText(_translate("MainWindow", "User guide"))
        self.actionEdit_observation_2.setText(_translate("MainWindow", "Edit observation"))
        self.actionCheckStateEvents.setText(_translate("MainWindow", "Check state events"))
        self.actionEdit_selected_events.setText(_translate("MainWindow", "Edit selected event(s)"))
        self.actionShow_spectrogram.setText(_translate("MainWindow", "Show spectrogram"))
        self.actionExport_events_as_Praat_TextGrid.setText(_translate("MainWindow", "Export events as Praat TextGrid"))
        self.actionExtract_events_from_media_files.setText(_translate("MainWindow", "Extract sequences from media files"))
        self.actionDistance.setText(_translate("MainWindow", "Geometric measurement"))
        self.actionFrame_forward.setText(_translate("MainWindow", "Frame forward"))
        self.actionFrame_backward.setText(_translate("MainWindow", "frame backward"))
        self.actionFilterBehaviors.setText(_translate("MainWindow", "Filter behaviors"))
        self.actionShowAllBehaviors.setText(_translate("MainWindow", "Show all behaviors"))
        self.actionShowAllBehaviors.setToolTip(_translate("MainWindow", "Show all behaviors"))
        self.actionExport_aggregated_events.setText(_translate("MainWindow", "Export aggregated events"))
        self.actionBehaviors_map.setText(_translate("MainWindow", "Coding pad"))
        self.actionTime_budget_by_behaviors_category.setText(_translate("MainWindow", "Time budget by behaviors category"))
        self.actionExport_events_as_SDIS_file.setText(_translate("MainWindow", "Export events as SDIS file"))
        self.actionRecode_resize_video.setText(_translate("MainWindow", "Re-encode/resize video"))
        self.actionMedia_file_information_2.setText(_translate("MainWindow", "Media file information"))
        self.actionCreate_transitions_matrix.setText(_translate("MainWindow", "Create transitions matrix"))
        self.actionCreate_transitions_flow_diagram.setText(_translate("MainWindow", "Create transitions DOT script"))


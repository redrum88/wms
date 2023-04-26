# Autor: Eimantas aka REDRUM
# Date: 2023-04-23
# Version: 1.0.0 Initial version
# Description: This is a snippet for creating a main window with tabs and menu bar.
# Path: wms\ui\MainWindow.py

import sys
import os

# Add path to ui directory
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import PySide6
from PySide6 import QtGui, QtWidgets, QtCore, QtMultimedia, QtMultimediaWidgets, QtNetwork, QtPrintSupport, QtSvg, QtUiTools, QtWebEngineWidgets, QtWebSockets, QtXml, QtSql
from PySide6.QtGui import QBrush, QColor, QFont, QIcon, QImage, QPainter, QPalette, QPen, QPixmap, QPolygon, QPolygonF, QRegion, QTransform, QWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel, QSqlRelationalTableModel, QSqlRelationalDelegate, QSqlRelation
from PySide6.QtCore import Qt, QUrl, QEvent, QThread, QThreadPool, QRunnable, QObject, Signal, Slot, QCoreApplication, QSettings, QTranslator, QLibraryInfo, QLocale, QLibrary, QMimeData, QBuffer, QByteArray, QIODevice, QDataStream, QTemporaryFile, QProcess


from Categories import Categories
from Tab2 import Tab2

class MainWindow(QtWidgets.QMainWindow):
    pass

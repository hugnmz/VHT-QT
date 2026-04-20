/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QProgressBar *barRam;
    QLabel *lblCpu;
    QProgressBar *barCpu;
    QTextBrowser *textBrowser_receivedMessages;
    QGridLayout *gridLayout_2;
    QPushButton *btnMess;
    QPushButton *btnAttach;
    QHBoxLayout *horizontalLayout;
    QComboBox *receiver;
    QLineEdit *inputMess;
    QLabel *lblRam;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(582, 482);
        MainWindow->setStyleSheet(QString::fromUtf8(""));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        barRam = new QProgressBar(centralWidget);
        barRam->setObjectName(QString::fromUtf8("barRam"));
        barRam->setValue(24);

        gridLayout->addWidget(barRam, 5, 0, 1, 1);

        lblCpu = new QLabel(centralWidget);
        lblCpu->setObjectName(QString::fromUtf8("lblCpu"));

        gridLayout->addWidget(lblCpu, 2, 0, 1, 1);

        barCpu = new QProgressBar(centralWidget);
        barCpu->setObjectName(QString::fromUtf8("barCpu"));
        barCpu->setValue(24);

        gridLayout->addWidget(barCpu, 3, 0, 1, 1);

        textBrowser_receivedMessages = new QTextBrowser(centralWidget);
        textBrowser_receivedMessages->setObjectName(QString::fromUtf8("textBrowser_receivedMessages"));
        textBrowser_receivedMessages->setStyleSheet(QString::fromUtf8(""));

        gridLayout->addWidget(textBrowser_receivedMessages, 0, 0, 1, 1);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        btnMess = new QPushButton(centralWidget);
        btnMess->setObjectName(QString::fromUtf8("btnMess"));
        btnMess->setMinimumSize(QSize(0, 0));
        btnMess->setStyleSheet(QString::fromUtf8(""));

        gridLayout_2->addWidget(btnMess, 1, 0, 1, 1);

        btnAttach = new QPushButton(centralWidget);
        btnAttach->setObjectName(QString::fromUtf8("btnAttach"));
        btnAttach->setStyleSheet(QString::fromUtf8(""));
        btnAttach->setFlat(false);

        gridLayout_2->addWidget(btnAttach, 1, 1, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        receiver = new QComboBox(centralWidget);
        receiver->addItem(QString());
        receiver->setObjectName(QString::fromUtf8("receiver"));
        receiver->setMinimumSize(QSize(110, 0));

        horizontalLayout->addWidget(receiver);

        inputMess = new QLineEdit(centralWidget);
        inputMess->setObjectName(QString::fromUtf8("inputMess"));
        inputMess->setMinimumSize(QSize(150, 0));
        inputMess->setStyleSheet(QString::fromUtf8(""));

        horizontalLayout->addWidget(inputMess);


        gridLayout_2->addLayout(horizontalLayout, 0, 0, 1, 2);


        gridLayout->addLayout(gridLayout_2, 1, 0, 1, 1);

        lblRam = new QLabel(centralWidget);
        lblRam->setObjectName(QString::fromUtf8("lblRam"));

        gridLayout->addWidget(lblRam, 4, 0, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 582, 26));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "QTCPServer", nullptr));
        lblCpu->setText(QCoreApplication::translate("MainWindow", "M\341\273\251c ti\303\252u th\341\273\245 c\341\273\247a CPU: ", nullptr));
        btnMess->setText(QCoreApplication::translate("MainWindow", "Send Message", nullptr));
        btnAttach->setText(QCoreApplication::translate("MainWindow", "Send Attachment", nullptr));
        receiver->setItemText(0, QCoreApplication::translate("MainWindow", "Broadcast", nullptr));

        lblRam->setText(QCoreApplication::translate("MainWindow", "M\341\273\251c ti\303\252u th\341\273\245 c\341\273\247a RAM: ", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H

/********************************************************************************
** Form generated from reading UI file 'sig.ui'
**
** Created by: Qt User Interface Compiler version 5.14.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SIG_H
#define UI_SIG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_sig
{
public:
    QPushButton *btnExit;

    void setupUi(QWidget *sig)
    {
        if (sig->objectName().isEmpty())
            sig->setObjectName(QString::fromUtf8("sig"));
        sig->resize(400, 300);
        btnExit = new QPushButton(sig);
        btnExit->setObjectName(QString::fromUtf8("btnExit"));
        btnExit->setGeometry(QRect(50, 150, 75, 24));

        retranslateUi(sig);

        QMetaObject::connectSlotsByName(sig);
    } // setupUi

    void retranslateUi(QWidget *sig)
    {
        sig->setWindowTitle(QCoreApplication::translate("sig", "Form", nullptr));
        btnExit->setText(QCoreApplication::translate("sig", "Exit", nullptr));
    } // retranslateUi

};

namespace Ui {
    class sig: public Ui_sig {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SIG_H

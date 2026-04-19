
#include "mainwindow.h"

#include <QApplication>
#include <QSslSocket>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    MainWindow w;
    qDebug() << "Hỗ trợ SSL:" << QSslSocket::supportsSsl();
    qDebug() << "Phiên bản OpenSSL thực tế tại máy:" << QSslSocket::sslLibraryVersionString();
    w.show();
    return a.exec();
}

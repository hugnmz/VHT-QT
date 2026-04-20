#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTcpSocket>
#include <QSslSocket>
#include <windows.h>
#include <QUdpSocket>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();


signals:
    void newMessage(QString);

public slots:
    void readSocket();
    void discardSocket();
    void on_btnMess_clicked();
    void sendData(QTcpSocket *socket, QString type, QString fileName, QByteArray content);
    void on_btnAttach_clicked();
    void displayMessage(const QString& str);
    void processIncommingFile(QString fileName, QByteArray content);
    double getCpuUsage();
    double getRamUsage();
    void sendCpuAndRam();
private:
    QUdpSocket *m_udpSocket;
    QTcpSocket *socket;
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H

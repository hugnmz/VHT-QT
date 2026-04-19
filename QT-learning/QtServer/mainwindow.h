#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "networkworker.h"
#include <QMainWindow>
#include <QTcpSocket>
#include <QTcpServer>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_btnMess_clicked();
    void on_btnAttach_clicked();
    void newConnection();

    void displayMessage(const QString &mess);
    void refresH();

private:
    QMap<qintptr, NetworkWorker*> m_workers;
    QTcpServer *server;
    QSet<QTcpSocket*> m_socket;
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H

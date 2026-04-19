#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QTcpServer>
#include <QTcpSocket>
#include <QDataStream>
#include <QFile>
#include <QStandardPaths>
#include <QFileDialog>
#include <QThread>
#include <QMetaObject>
#include <QSslSocket>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    server = new QTcpServer(this);

    if(server->listen(QHostAddress::AnyIPv4, 8085)){
        connect(server, &QTcpServer::newConnection, this, &MainWindow::newConnection);

    }
}

MainWindow::~MainWindow()
{
    foreach(QTcpSocket *s, m_socket){
        s->close();
        s->deleteLater();
    }
    server->close();
    server->deleteLater();
    delete ui;
}


void MainWindow::newConnection(){
    while (server->hasPendingConnections()) {
        QSslSocket *sslSocket = qobject_cast<QSslSocket*>(server->nextPendingConnection());
        sslSocket->setLocalCertificate("server.crt");
        sslSocket->setPrivateKey("server.key");
        sslSocket->startServerEncryption(); // Bắt đầu mã hóa
        qintptr descriptor = sslSocket->socketDescriptor();

        QThread *thread = new QThread();
        NetworkWorker *w = new NetworkWorker(descriptor);

        w->moveToThread(thread);

        m_workers.insert(descriptor, w);
        ui->receiver->addItem(QString::number(descriptor));

        connect(thread, &QThread::started, w, &NetworkWorker::process);
        connect(w, &NetworkWorker::messageReceived, this, &MainWindow::displayMessage);

        connect(w, &NetworkWorker::finished, thread, &QThread::quit);
        connect(w, &NetworkWorker::finished, w, &QObject::deleteLater);
        connect(thread, &QThread::finished, thread, &QObject::deleteLater);
        connect(w, &NetworkWorker::finished, [this,descriptor](){
            this->m_workers.remove(descriptor);
            refresH();
        });

        thread->start();

    }
}




void MainWindow::displayMessage(const QString &mess){
    ui->textBrowser_receivedMessages->append(mess);
}


void MainWindow::on_btnMess_clicked() {
    QString message = ui->inputMess->text();
    QString targetId = ui->receiver->currentText();

    if("Broadcast" == targetId){
        foreach(NetworkWorker *worker, m_workers.values()){
                // Gọi slot qua hệ thống Signal/Slot (đảm bảo an toàn luồng)
                QMetaObject::invokeMethod(worker, "sendData",
                                         Qt::QueuedConnection,
                                         Q_ARG(QString, "TEXT"),
                                         Q_ARG(QString, "mess"),
                                         Q_ARG(QByteArray, message.toUtf8()));

        }
    }else{
        if (m_workers.contains(targetId.toLongLong())) {

            // Gọi slot qua hệ thống Signal/Slot (đảm bảo an toàn luồng)
            QMetaObject::invokeMethod(m_workers[targetId.toLongLong()], "sendData",
                                     Qt::QueuedConnection,
                                     Q_ARG(QString, "TEXT"),
                                     Q_ARG(QString, "mess"),
                                     Q_ARG(QByteArray, message.toUtf8()));
        }
    }
}

void MainWindow::on_btnAttach_clicked()
{
    QString receiver = ui->receiver->currentText();
    QString filePath = QFileDialog::getOpenFileName(this, ("Select an attachment"), QStandardPaths::writableLocation(QStandardPaths::DocumentsLocation), ("File (*.json *.txt *.png *.jpg *.jpeg)"));


    // xử lí việc đọc file
    QFile file(filePath);

    // lấy ra thông tin của file
    if(file.open(QIODevice::ReadOnly)){

        QFileInfo fileInfo(file.fileName());

        QString fileName(fileInfo.fileName());
        if("Broadcast" == receiver){
            foreach(NetworkWorker *worker, m_workers.values()){
                QMetaObject::invokeMethod(worker, "sendData",
                                         Qt::QueuedConnection,
                                         Q_ARG(QString, "FILE"),
                                         Q_ARG(QString, fileName),
                                         Q_ARG(QByteArray, file.readAll()));
            }
        }else{
           if(m_workers.contains(receiver.toLongLong())){
               QMetaObject::invokeMethod(m_workers[receiver.toLongLong()], "sendData",
                                        Qt::QueuedConnection,
                                        Q_ARG(QString, "FILE"),
                                        Q_ARG(QString, fileName),
                                        Q_ARG(QByteArray, file.readAll()));
           }
        }
    }
}


void MainWindow::refresH(){
    ui->receiver->clear();
    ui->receiver->addItem("Broadcast");

    foreach(qintptr id, m_workers.keys()){
            ui->receiver->addItem(QString::number(id));
        }
}

#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QTcpSocket>
#include <QFile>
#include <QFileDialog>
#include <QStandardPaths>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{

    ui->setupUi(this);
    socket = new QTcpSocket(this);

    // kết nối tín hiệu trước khi gọi connect vs host
        connect(socket, &QTcpSocket::connected, [this](){
            ui->statusBar->showMessage("Kết nối bảo mật thành công!");
        });
    connect(this, &MainWindow::newMessage, this, &MainWindow::displayMessage);
    connect(socket, &QTcpSocket::readyRead, this, &MainWindow::readSocket);
    connect(socket, &QTcpSocket::disconnected, this, &MainWindow::discardSocket);

    socket->connectToHost("127.0.0.1", 8085);
}

MainWindow::~MainWindow()
{
    if(socket->isOpen()) socket->close();
    socket->deleteLater();
    delete ui;
}

void MainWindow::on_btnMess_clicked()
{
    QString message = ui->inputMess->text();

    sendData(socket, "TEXT", "mess", message.toUtf8());

}

void MainWindow::on_btnAttach_clicked()
{
    QString filePath = QFileDialog::getOpenFileName(this, ("Select an attachment"), QStandardPaths::writableLocation(QStandardPaths::DocumentsLocation), ("File (*.json *.txt *.png *.jpg *.jpeg)"));


    // xử lí việc đọc file
    QFile file(filePath);

    // lấy ra thông tin của file
    if(file.open(QIODevice::ReadOnly)){

        QFileInfo fileInfo(file.fileName());

        QString fileName(fileInfo.fileName());
        sendData(socket, "FILE", fileName, file.readAll());
    }
}

void MainWindow::displayMessage(const QString &str){
    ui->textBrowser_receivedMessages->append(str);
}

void MainWindow::readSocket(){

    QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender());

    QByteArray buffer;
    QDataStream in(socket);
    in.setVersion(QDataStream::Qt_5_14);

    while(true){
        quint32 blockSize = socket->property("blockSize").toUInt();

        if(blockSize == 0){
            if (socket->bytesAvailable() < (qint64)sizeof(quint32)) break;
            in >> blockSize;
            socket->setProperty("blockSize", blockSize);
        }

        // nếu đã đủ payload
        if(socket->bytesAvailable() < blockSize) break;

        QString type, fileName;
        QByteArray content;

        in >> type >> fileName >> content;

        if("TEXT" == type){
            QString message = QString::fromUtf8(content);
            displayMessage(message);
        }
        if("FILE" == type){


            processIncommingFile(fileName,content);
        }


        socket->setProperty("blockSize", 0);

    }
}

void MainWindow::processIncommingFile(QString fileName, QByteArray content){
    QMetaObject::invokeMethod(this, [this, fileName, content](){
        auto res = QMessageBox::question(this, "Nhận file", "Bạn có muốn nhận file: " + fileName);
        if(res == QMessageBox::Yes){
            QFile file("download_" + fileName);
                        if(file.open(QIODevice::WriteOnly)) {
                            file.write(content);
                            file.close();
                            displayMessage("Lưu file thành công: " + fileName);
                        }
        }
    }, Qt::QueuedConnection);
}

void MainWindow::sendData(QTcpSocket *s, QString type, QString fileName, QByteArray content){


    QByteArray package;
    QDataStream ou(&package, QIODevice::WriteOnly);


    ou.setVersion(QDataStream::Qt_5_14);
    ou << (quint32)0;

    ou<<type << fileName << content;
    ou.device()->seek(0);
    ou << (quint32)(package.size() - sizeof(quint32));

    s->write(package);
    s->flush();

}

void MainWindow::discardSocket(){
    socket->deleteLater();
    socket = nullptr;

    ui->statusBar->showMessage("Disconnnected");
}


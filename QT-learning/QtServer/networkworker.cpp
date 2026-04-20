#include "NetworkWorker.h"
#include <QThread>
#include <QFile>

NetworkWorker::NetworkWorker(qintptr socketDescriptor, QObject *parent)
    : QObject(parent), m_socketDescriptor(socketDescriptor), m_socket(nullptr) {

}

// khởi tạo socket
void NetworkWorker::process(){

    m_socket = new QTcpSocket();

    if(!m_socket->setSocketDescriptor(m_socketDescriptor)){
        emit finished();
        return;
    }

    connect(m_socket, &QTcpSocket::readyRead, this, &NetworkWorker::readData);
    connect(m_socket, &QTcpSocket::disconnected, this, &NetworkWorker::onDisconnected);


}


void NetworkWorker::readData(){
    // xác định đến từ socket nào
    QTcpSocket* socket = qobject_cast<QTcpSocket*>(sender());


    QByteArray buffer;

    // gắn data stream vào socket
    QDataStream in(socket);
    in.setVersion(QDataStream::Qt_5_14);

    // xử lí trường hợp có nhều gói tin đến cùng lúc
    while (true) {
        quint32 m_blockSize = socket->property("m_blockSize").toUInt();

        // đọc header
        if(m_blockSize == 0){
            if (socket->bytesAvailable() < (qint64)sizeof(quint32)) break;
            in >> m_blockSize;
            socket->setProperty("m_blockSize", m_blockSize);
        }

        // kiểm tra xem đã có đủ payload chưa
        if(socket->bytesAvailable() < m_blockSize) break;

        // nếu đủ data roi

        QString type;
        QString fileName;
        QByteArray content;

        in >> type;
        in >> fileName;
        in >>content;

        if("TEXT" == type){
            QString message = QString::fromUtf8(content);
            emit messageReceived(message);
        }
        if("FILE" == type){
            QFile file("QT_download" + fileName);
            if(file.open(QIODevice::WriteOnly)){
                file.write(content);
                file.close();
                emit messageReceived("Tải về thành công");
            }
        }


        socket->setProperty("m_blockSize", 0);
    }
}

// Giữ nguyên logic sendData của bạn nhưng áp dụng cho m_socket nội bộ
void NetworkWorker::sendData(QString type, QString fileName, QByteArray content) {
    if (!m_socket || m_socket->state() != QTcpSocket::ConnectedState) return;

    QByteArray block;
    QDataStream out(&block, QIODevice::WriteOnly);
    out.setVersion(QDataStream::Qt_5_14);
    out << (quint32)0 << type << fileName << content;
    out.device()->seek(0);
    out << (quint32)(block.size() - sizeof(quint32));
    m_socket->write(block);
}

void NetworkWorker::onDisconnected() {
    emit finished();
}

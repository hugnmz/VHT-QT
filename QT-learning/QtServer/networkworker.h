#ifndef NETWORKWORKER_H
#define NETWORKWORKER_H

//đảm nhận việc nói chuyện với client
#include <QObject>
#include <QTcpSocket>
#include <QDataStream>

class NetworkWorker : public QObject{
    Q_OBJECT

    //ctor truyền vào socketDescriptor thay vì cả socket
public:
    explicit NetworkWorker(qintptr socketDescriptor, QObject *parent = nullptr);

public slots:
    void process();  // Hàm khởi tạo socket trong luồng mới
    void readData();
    void sendData(QString type, QString fileName, QByteArray content);
    void onDisconnected();

signals:
    void messageReceived(QString msg); // Gửi tin nhắn về UI để hiển thị
    void fileReceived(QString fileName);
    void finished(); // Báo hiệu để xóa luồng
    void encrypted();
private:
    qintptr m_socketDescriptor;
    QTcpSocket *m_socket;
};

#endif // NETWORKWORKER_H

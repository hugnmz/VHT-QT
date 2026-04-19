#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->btnExit, &QPushButton::clicked, this, &MainWindow::close);
    connect(ui->btnSayHello, &QPushButton::clicked, this, &MainWindow::displayText); // displayText là hàm phải thuojc this

    setWindowFlags(Qt::FramelessWindowHint); // ẩn thanh tiêu đề mặc định

    // tùy chọn làm nền cửa sổ trong suốt để bo góc QSS có tác dụng
    setAttribute(Qt::WA_TranslucentBackground);
}


void MainWindow::displayText(){
    ui->lblHello->setText("Xin chao Hung");
}


MainWindow::~MainWindow()
{
    delete ui;
}




from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap 

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setFixedSize(300, 400)
        
        layout = QVBoxLayout()
        
        self.image_label = QLabel()
        pixmap = QPixmap("moon.jpg.jpeg")
        scaled_pixmap = pixmap.scaled(180, 180)
        self.image_label.setPixmap(scaled_pixmap)
        layout.addWidget(self.image_label)
        
        name_label = QLabel("Name: Yuval Ben Natan")
        layout.addWidget(name_label)
        
        email_label = QLabel("Email: yuval.bennatan@gmail.com")
        layout.addWidget(email_label)
        
        link_label = QLabel('<a href="https://www.facebook.com/yuval.bennatan">My Facebook Profile</a>')
        link_label.setOpenExternalLinks(True)
        layout.addWidget(link_label)

        github_label = QLabel('<a href="https://github.com/Yuval-BN/exe_4_icecream">GitHub Repository</a>')
        github_label.setOpenExternalLinks(True)
        layout.addWidget(github_label)
        
        self.setLayout(layout)
if __name__ == '__main__':
    app = QApplication([])
    window = AboutWindow()
    window.show()
    app.exec()
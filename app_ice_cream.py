import sys

from About import AboutWindow
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget


class IceCreamApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.temperatures = []
        self.revenues = []
        self.selected_file = ""

        self.setWindowTitle("Ice Cream Sales")
        self.resize(900, 600)

        with open("style.qss", "r") as style_file:
            self.setStyleSheet(style_file.read())

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        button_layout = QHBoxLayout()

        load_button = QPushButton("Load Data")
        load_button.clicked.connect(self.load_data)
        button_layout.addWidget(load_button)

        about_button = QPushButton("About")
        about_button.clicked.connect(self.show_about)
        button_layout.addWidget(about_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)

        self.axes = self.figure.add_subplot(111)
        self.plot_data()

    def load_data(self):
        self.selected_file, _ = QFileDialog.getOpenFileName(
            self, "Load Data", "", "CSV Files (*.csv)"
        )

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def plot_data(self):
        self.axes.clear()
        self.axes.plot([1, 2, 3, 4], [3, 5, 4, 7], color="#e97c5b", marker="o")
        self.axes.set_title("Ice Cream Sales")
        self.axes.set_xlabel("Day")
        self.axes.set_ylabel("Sales")
        self.axes.grid(True, alpha=0.25)
        self.figure.tight_layout()
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IceCreamApp()
    window.show()
    sys.exit(app.exec())

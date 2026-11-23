import sys
import numpy as np
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
        filename, _ = QFileDialog.getOpenFileName(self, "Select a file")
        if filename:
            self.temperatures = []
            self.revenues = []
            with open(filename, "r") as f:
                next(f)
                for line in f:
                    parts = line.strip().split(",")
                    self.temperatures.append(float(parts[0]))
                    self.revenues.append(float(parts[1]))
            self.plot_data()
        

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def plot_data(self):
        self.axes.clear()
        self.axes.scatter(self.temperatures, self.revenues, s=1)
        if self.temperatures:
            slope, intercept = np.polyfit(self.temperatures, self.revenues, 1)
            trendline_x = np.linspace(min(self.temperatures), max(self.temperatures), 100)
            trendline_y = slope * trendline_x + intercept
            self.axes.plot(trendline_x, trendline_y, color="red")
            self.axes.text(
                0.05,
                0.95,
                f"y = {slope:.2f}x + {intercept:.2f}",
                transform=self.axes.transAxes,
                verticalalignment="top",
            )
        self.axes.set_title("Ice Cream Revenue vs Temperature")
        self.axes.set_xlabel("Temperature (°C)")
        self.axes.set_ylabel("Revenue ($)")
        self.axes.spines["top"].set_visible(False)
        self.axes.spines["right"].set_visible(False)
        self.figure.tight_layout()
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IceCreamApp()
    window.show()
    sys.exit(app.exec())

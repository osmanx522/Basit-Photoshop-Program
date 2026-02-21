import gui
import sys

if __name__ == "__main__":
    app = gui.QApplication(sys.argv)
    pencere = gui.AnaPencere()
    pencere.show()
    sys.exit(app.exec_())
import sys
import pyautogui
import keyboard
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QCheckBox, QLabel, QFrame, QSpacerItem
from PyQt5.QtGui import QPixmap, QIcon
import time

ajanlar = ["astra", "breach", "brimstone", "chamber",
           "clove", "cypher", "deadlock", "fade",
           "gekko", "harbor", "iso", "jett",
           "kay/o", "killjoy", "neon", "omen",
           "phoenix", "raze", "reyna", "sage",
           "skye", "sova", "tejo", "viper",
           "vyse", "waylay", "yoru"]

konumlar = ((100, 350), (200, 350), (300, 350), (400, 350),
            (100, 450), (200, 450), (300, 450), (400, 450),
            (100, 550), (200, 550), (300, 550), (400, 550),
            (100, 650), (200, 650), (300, 650), (400, 650),
            (100, 750), (200, 750), (300, 750), (400, 750),
            (100, 850), (200, 850), (300, 850), (400, 850),
            (100, 850), (200, 850), (300, 850), (400, 850),
            (100, 850), (200, 850), (300, 850), (400, 850))


class ValorantPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Sol taraf
        left_layout = QVBoxLayout()
        label = QLabel("Açık Ajanlar", self)
        label.setStyleSheet("font-size: 18px;")

        # Ajanlar için grid layout
        grid_layout = QGridLayout()
        self.checkboxes = {}

        for index, ajan in enumerate(ajanlar):
            checkbox = QCheckBox(ajan, self)
            self.checkboxes[ajan] = checkbox
            grid_layout.addWidget(checkbox, index // 4, index % 4)

        # Tüm ajanları seç ve kutuları kilitle checkbox'ları
        self.selectAllCheckbox = QCheckBox("Tüm Ajanları Seç", self)
        self.selectAllCheckbox.stateChanged.connect(self.toggleAllCheckboxes)

        self.lockChechbox = QCheckBox("Kutuları kilitle", self)
        self.lockChechbox.stateChanged.connect(self.lockChechboxes)

        # Layout Tanımlama ve Yerleştirmeleri
        main_layout = QHBoxLayout()
        left_layout.addWidget(label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        left_layout.addLayout(grid_layout)
        left_layout.addItem(QSpacerItem(20, 40))

        left_bottom_layout = QHBoxLayout()
        left_bottom_layout.addWidget(self.selectAllCheckbox)
        left_bottom_layout.addWidget(self.lockChechbox)
        left_layout.addLayout(left_bottom_layout)

        main_layout.addLayout(left_layout)

        # Ortada çizgi
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)

        # Sağ taraf
        right_layout = QVBoxLayout()
        label = QLabel("Kitlenecek Ajan", self)
        label.setStyleSheet("font-size: 18px;")
        right_layout.addWidget(label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # Ajan resmi
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("../images/default.jpg").scaled(150, 150))
        right_layout.addWidget(self.image_label)

        right_layout.addItem(QSpacerItem(20, 20))

        # Dropdown menüsü
        self.comboBox = QComboBox(self)
        right_layout.addWidget(self.comboBox)

        # Seç butonu
        self.selectButton = QPushButton("Seç", self)
        self.selectButton.clicked.connect(self.select_agent)
        right_layout.addWidget(self.selectButton)

        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)
        self.setWindowTitle("Valorant Ajan Seçici")
        self.setWindowIcon(QIcon("../images/icon.png"))
        self.setFixedSize(550, 330)

        for checkbox in self.checkboxes.values():
            checkbox.stateChanged.connect(self.updateDropdown)

        self.comboBox.currentIndexChanged.connect(self.update_image)

        # Kayıtlı verileri yükle
        self.load_selected_agents()
        self.load_lock_state()
        self.load_lock_agent()
        self.apply_dark_theme()

    def toggleAllCheckboxes(self, state):
        check = state == 2  # 2: Checked, 0: Unchecked
        for checkbox in self.checkboxes.values():
            checkbox.setChecked(check)

    def lockChechboxes(self, state):
        check = state == 2
        for checkbox in self.checkboxes.values():
            checkbox.setEnabled(not check)
        self.selectAllCheckbox.setEnabled(not check)
        self.save_lock_state()

    def updateDropdown(self):
        self.comboBox.clear()
        for ajan, checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                self.comboBox.addItem(ajan)
        self.save_selected_agents()

    def update_image(self):
        agent = self.comboBox.currentText()
        if not agent:
            self.image_label.setPixmap(QPixmap("../images/default.jpg").scaled(150, 150))
            return
        else:
            if agent == "kay/o":
                agent = "kayo"
            self.image_label.setPixmap(QPixmap(f"../images/{agent}.png").scaled(150, 150))
        self.image_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

    def select_agent(self):

        agent = self.comboBox.currentText()
        if not agent:
            return

        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

        index = self.comboBox.currentIndex()

        if index >= 24:
            pyautogui.moveTo(445, 850)
            pyautogui.click()

        timeout = time.time() + 30  # 15 saniye
        while True:
            if time.time() > timeout or keyboard.is_pressed('q'):  break
            pyautogui.moveTo(konumlar[index])
            pyautogui.click()
            pyautogui.moveTo(960, 760)
            pyautogui.click()

        self.save_lock_agent()

    def save_selected_agents(self):
        selected_agents = [agent for agent, checkbox in self.checkboxes.items() if checkbox.isChecked()]
        with open("../preferences/selected_agents.txt", "w") as file:
            for agent in selected_agents:
                file.write(f"{agent}\n")

    def load_selected_agents(self):
        try:
            with open("../preferences/selected_agents.txt", "r") as file:
                selected_agents = file.read().splitlines()
                for agent in selected_agents:
                    if agent in self.checkboxes:
                        self.checkboxes[agent].setChecked(True)
        except FileNotFoundError:
            pass

    def save_lock_state(self):
        with open("../preferences/lock_state.txt", "w") as file:
            file.write("locked" if self.lockChechbox.isChecked() else "unlocked")

    def load_lock_state(self):
        try:
            with open("../preferences/lock_state.txt", "r") as file:
                state = file.read().strip()
                self.lockChechbox.setChecked(state == "locked")
        except FileNotFoundError:
            pass

    def save_lock_agent(self):
        with open("../preferences/lock_agent.txt", "w") as file:
            file.write(self.comboBox.currentText())

    def load_lock_agent(self):
        try:
            with open("../preferences/lock_agent.txt", "r") as file:
                agent = file.read().strip()
                self.comboBox.setCurrentText(agent)
        except FileNotFoundError:
            pass

    def apply_dark_theme(self):
        dark_stylesheet = """
        QWidget {
            background-color: #2e2e2e;
            color: #ffffff;
        }
        QCheckBox, QLabel, QComboBox, QPushButton {
            background-color: #2e2e2e;
            color: #ffffff;
        }
        """
        self.setStyleSheet(dark_stylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ValorantPicker()
    window.show()
    sys.exit(app.exec_())

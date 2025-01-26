from PyQt6.QtWidgets import *
import data

def menu_window():
    window = QDialog()
    quest_lbl= QLabel("Введіть запитання")
    right_answer_lbl = QLabel("Правильна відповідь")
    Wrong1_answer_lbl = QLabel("Неправильна відповідь1")
    Wrong2_answer_lbl = QLabel("Неправильна відповідь2")
    Wrong3_answer_lbl = QLabel("Неправильна відповідь3")
    add_btn = QPushButton("Додати")
    back_btn = QPushButton("Назад")
    delette_btn = QPushButton("Видалити")

    quest_input = QLineEdit()
    right_answer_input = QLineEdit()
    wrong1_answer_input = QLineEdit()
    wrong2_answer_input = QLineEdit()
    wrong3_answer_input = QLineEdit()
    main_line = QVBoxLayout()

    h1 = QHBoxLayout()
    h2 = QHBoxLayout()
    h3 = QHBoxLayout()
    h4 = QHBoxLayout()
    h5 = QHBoxLayout()
    h6 = QHBoxLayout()
    h7 = QHBoxLayout()
    h8 = QHBoxLayout()

    h1.addWidget(quest_lbl)
    h1.addWidget(quest_input)
    h2.addWidget(right_answer_lbl)
    h2.addWidget(right_answer_input)
    h3.addWidget(Wrong1_answer_lbl)
    h3.addWidget(wrong1_answer_input)
    h4.addWidget(Wrong2_answer_lbl)
    h4.addWidget(wrong2_answer_input)
    h5.addWidget(Wrong3_answer_lbl)
    h5.addWidget(wrong3_answer_input)
    h6.addWidget(add_btn)
    h7.addWidget(back_btn)
    h8.addWidget(delette_btn)


    main_line.addLayout(h1)
    main_line.addLayout(h2)
    main_line.addLayout(h3)
    main_line.addLayout(h4)
    main_line.addLayout(h5)
    main_line.addLayout(h6)
    main_line.addLayout(h7)
    main_line.addLayout(h8)

    def add_func():
        quest = {
            "запитання": quest_input.text(),
            "Правильна відповідь": right_answer_input.text(),
            "Неправильна відповідь 1": wrong1_answer_input.text(),
            "Неправильна відповідь 2": wrong2_answer_input.text(),
            "Неправильна відповідь 3": wrong3_answer_input.text(),
        }
        data.questions.append(quest)


    def back_func():
        window.close()

    back_btn.clicked.connect(back_func)
    add_btn.clicked.connect(add_func)
    window.setLayout(main_line)
    window.exec()

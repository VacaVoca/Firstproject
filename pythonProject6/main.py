import random
from PyQt6.QtWidgets import *
import data
import menu
import time

app = QApplication([])
window = QWidget()

menu_btn = QPushButton("Меню")
break_btn = QPushButton("Відпочити")
xB_lbl = QLabel("хвилин")
question_lbl = QLabel("                                   Яблуко")
answer_btn = QPushButton("Відповісти")
next_quest_butn = QPushButton('Наступне Запитання')
result_lbl = QLabel('Результат:')
menu_btn.clicked.connect(menu.menu_window)

option_group = QGroupBox("Варіанти відповідей")
option_enter = QGroupBox("")
answer1_btn = QRadioButton("building")
answer3_btn = QRadioButton("application")
answer4_btn = QRadioButton("apple")
answer2_btn = QRadioButton("caterpiar")
main_line = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h1.addWidget(menu_btn)
main_line.addLayout(line_h1)
line_h1.addStretch(1)

answers = [answer1_btn, answer2_btn, answer3_btn, answer4_btn]


line_h1.addWidget(break_btn)
line_h1.addWidget(QSpinBox())
line_h1.addWidget(xB_lbl)
main_line.addWidget(question_lbl)

group_line = QVBoxLayout()
enter_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line1.addWidget(answer1_btn)
line1.addWidget(answer2_btn)
line2.addWidget(answer3_btn)
line2.addWidget(answer4_btn)
line3.addWidget(result_lbl)
group_line.addLayout(line1)
group_line.addLayout(line2)
group_line.addLayout(line3)
option_group.setLayout(group_line)
main_line.addWidget(option_group)
main_line.addWidget(answer_btn)
main_line.addWidget(next_quest_butn)
window.setLayout(main_line)


def set_quest():
    answers[0].show()
    answers[1].show()
    answers[2].show()
    answers[3].show()
    quest = data.questions[data.current_question]
    random.shuffle(answers)
    print(quest)
    question_lbl.setText(quest['запитання'])
    answers[0].setText(quest['Правильна відповідь'])
    answers[1].setText(quest['Неправильна відповідь 1'])
    answers[2].setText(quest['Неправильна відповідь 2'])
    answers[3].setText(quest['Неправильна відповідь 3'])
set_quest()

def next_quest_func():
    data.current_question += 1
    set_quest()

result_lbl.hide()
next_quest_butn.hide()
def answer_func():
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    answer_btn.hide()
    next_quest_butn.show()
    result_lbl.show()
    if answers[0].isChecked():
        result_lbl.setText("Правильно")
    else:
        result_lbl.setText("Неправильно")
# app.setStyleSheet("""
#     QWidget  {
#         background: #FFFFFF;
#     }
#
#     QPushButton
#     {
#         background-color: #F8F8FF;
#         border-style: outset;
#         font-family: Roboto;
#         min-width: 0en;
#         padding: 0px;
#     }
#     """)
answer_btn.clicked.connect(answer_func)
next_quest_butn.clicked.connect(next_quest_func)
window.show()
app.exec()
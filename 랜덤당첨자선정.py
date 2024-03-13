import sys
import pandas as pd
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, QLabel, QDateTimeEdit
from PyQt5.QtCore import pyqtSlot, QDateTime
import pyperclip

class LotteryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('랜덤 추첨 프로그램')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # 상단 툴바 레이아웃
        self.toolbarLayout = QHBoxLayout()
        
        # '추첨시작' 버튼
        self.btnDraw = QPushButton('추첨시작', self)
        self.btnDraw.clicked.connect(self.draw)
        self.toolbarLayout.addWidget(self.btnDraw)
        
        # '복사하기' 버튼
        self.btnCopy = QPushButton('복사하기', self)
        self.btnCopy.clicked.connect(self.copyResults)
        self.toolbarLayout.addWidget(self.btnCopy)
        
        # '초기화' 버튼
        self.btnReset = QPushButton('초기화', self)
        self.btnReset.clicked.connect(self.resetFields)
        self.toolbarLayout.addWidget(self.btnReset)
        
        # '추첨자수' 입력 필드
        self.numWinnersLabel = QLabel('추첨자수:')
        self.toolbarLayout.addWidget(self.numWinnersLabel)
        self.numWinnersInput = QLineEdit(self)
        self.toolbarLayout.addWidget(self.numWinnersInput)
        
        # '추첨자' 입력 필드
        self.entrantLabel = QLabel('추첨자:')
        self.toolbarLayout.addWidget(self.entrantLabel)
        self.entrantInput = QLineEdit(self)
        self.toolbarLayout.addWidget(self.entrantInput)
        
        # '추첨일시' 출력 필드
        self.drawDateLabel = QLabel('추첨일시:')
        self.toolbarLayout.addWidget(self.drawDateLabel)
        self.drawDateTime = QDateTimeEdit(self)
        self.drawDateTime.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.drawDateTime.setReadOnly(True)
        self.toolbarLayout.addWidget(self.drawDateTime)
        
        self.layout.addLayout(self.toolbarLayout)
        
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.setGeometry(100, 100, 800, 400)  # 화면 가로 크기 확장

    @pyqtSlot()
    def draw(self):
        num_selections = int(self.numWinnersInput.text())
        entrant = self.entrantInput.text()
        current_time = QDateTime.currentDateTime()
        self.drawDateTime.setDateTime(current_time)
        
        # 추첨 로직 (예시)
        try:
            data = pd.read_csv('C:/random_result/list.csv', encoding='CP949')
            if num_selections > len(data):
                raise ValueError("선택한 숫자가 데이터 범위를 초과하였습니다.")
            
            self.result = data.sample(n=num_selections)
            self.showResults(self.result)
            
            # 결과 엑셀에 기록
            with pd.ExcelWriter('C:/random_result/list_result.xlsx', mode='a', engine='openpyxl', encoding='CP949') as writer:
                self.result.to_excel(writer, index=False, sheet_name='Results')
                # 추첨자수, 추첨자, 추첨일시 하단에 기록
                df_footer = pd.DataFrame({'추첨자수': [num_selections], '추첨자': [entrant], '추첨일시': [current_time.toString("yyyy-MM-dd HH:mm:ss")]})
                df_footer.to_excel(writer, index=False, startrow=writer.sheets['Results'].max_row + 1)

        except Exception as e:
            print(f"추첨 오류: {e}")

    def showResults(self, data):
        self.table.setRowCount(data.shape[0])
        self.table.setColumnCount(data.shape[1])
        self.table.setHorizontalHeaderLabels(data.columns)
        
        for row in range(data.shape[0]):
            for column in range(data.shape[1]):
                item = QTableWidgetItem(str(data.iloc[row, column]))
                self.table.setItem(row, column, item)

    def copyResults(self):
        result_string = ""
        for row_index in range(self.table.rowCount()):
            row_data = []
            for column_index in range(self.table.columnCount()):
                item = self.table.item(row_index, column_index)
                row_data.append(item.text() if item else "")
            result_string += '\t'.join(row_data) + '\n'
        
        pyperclip.copy(result_string)
    
    def resetFields(self):
        # 필드 초기화
        self.numWinnersInput.clear()
        self.entrantInput.clear()
        self.drawDateTime.clear()
        # 결과 화면 초기화
        self.table.clearContents()
        self.table.setRowCount(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LotteryApp()
    ex.show()
    sys.exit(app.exec_())

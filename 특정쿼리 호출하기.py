import tkinter as tk
from tkinter import scrolledtext
import pymysql

# DB 접속 정보
host = "?"
user = "?"
password = "?"
database = "?"

# 쿼리 실행 함수
def execute_query():
    try:
        # DB에 연결
        connection = pymysql.connect(host=host, user=user, password=password, db=database)
        cursor = connection.cursor()

        # 실행할 쿼리
        query = "*"
        
        # 쿼리 실행
        cursor.execute(query)
        
        # 결과 출력
        result_text.delete(1.0, tk.END)  # 기존 결과 지우기
        for row in cursor.fetchall():
            result_text.insert(tk.END, str(row) + '\n')
            
    except Exception as e:
        result_text.delete(1.0, tk.END)  # 기존 결과 지우기
        result_text.insert(tk.END, "Error: " + str(e))
    finally:
        if connection:
            connection.close()

# GUI 설정
window = tk.Tk()
window.title("DB Query Executor")

query_button = tk.Button(window, text="Execute Query", command=execute_query)
query_button.pack()

result_text = scrolledtext.ScrolledText(window, width=60, height=20)
result_text.pack()

window.mainloop()

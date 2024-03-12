import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
import random
import pyperclip

def copy_to_clipboard(data):
    clipboard_string = ""
    for index, row in data.iterrows():
        clipboard_string += ", ".join(row.astype(str)) + "\n"
    pyperclip.copy(clipboard_string)
    messagebox.showinfo("알림", "클립보드에 복사되었습니다.")

def start_lottery():
    num_selections = simpledialog.askinteger("입력", "선정할 숫자를 입력하세요")
    
    try:
        data = pd.read_csv('C:/random_result/list.csv', encoding='CP949')
    except Exception as e:
        messagebox.showerror("오류", "파일 읽기 오류: " + str(e))
        return
    
    if num_selections and num_selections <= len(data):
        result = data.sample(n=num_selections)
        result.to_csv('C:/random_result/list_result.csv', index=False)
        
        # 결과를 표 형식으로 보여주기
        for widget in frame.winfo_children():
            widget.destroy()
        for i, column in enumerate(result.columns):
            tk.Label(frame, text=column).grid(row=0, column=i)
        for i, row in result.iterrows():
            for j, value in enumerate(row):
                tk.Label(frame, text=value).grid(row=i+1, column=j)
                
        # 복사 버튼 활성화
        copy_button["state"] = "normal"
        copy_button["command"] = lambda: copy_to_clipboard(result)
    else:
        messagebox.showerror("오류", "선택한 숫자가 데이터 범위를 초과하였습니다.")

window = tk.Tk()
window.title("랜덤 추첨 프로그램")

start_button = tk.Button(window, text="추첨시작", command=start_lottery)
start_button.pack()

copy_button = tk.Button(window, text="결과 복사", state="disabled")
copy_button.pack()

frame = tk.Frame(window)
frame.pack()

window.mainloop()

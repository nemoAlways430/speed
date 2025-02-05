import tkinter as tk

# 初始化全局变量
local_status = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

def show():
    # 更新 local_status 中的数据
    def update_status():
        local_status["name"] = name_entry.get()
        local_status["age"] = int(age_entry.get())
        local_status["email"] = email_entry.get()
        display_status()

    # 实时更新状态显示区域
    def display_status():
        status_text = f"Name: {local_status['name']}\nAge: {local_status['age']}\nEmail: {local_status['email']}"
        status_label.config(text=status_text)
        
    # 创建主窗口
    root = tk.Tk()
    root.title("Real-time Local Status Updater")

    # 显示当前状态的标签
    status_label = tk.Label(root, text="", justify=tk.LEFT)
    status_label.pack(pady=10)

    # 表单区域
    form_frame = tk.Frame(root)
    form_frame.pack(pady=10)

    # 表单字段
    tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1)
    name_entry.insert(0, local_status["name"])

    tk.Label(form_frame, text="Age:").grid(row=1, column=0, sticky="e")
    age_entry = tk.Entry(form_frame)
    age_entry.grid(row=1, column=1)
    age_entry.insert(0, local_status["age"])

    tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="e")
    email_entry = tk.Entry(form_frame)
    email_entry.grid(row=2, column=1)
    email_entry.insert(0, local_status["email"])

    # 提交按钮
    submit_button = tk.Button(root, text="Update Status", command=update_status)
    submit_button.pack(pady=10)

    # 初次显示状态
    display_status()

    # 启动主事件循环
    root.mainloop()

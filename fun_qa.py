from ollama import Client
import tkinter as tk
from tkinter import scrolledtext

# 从 ./api-key.txt 读取TOKEN
with open("./api-key.txt", "r") as f:
    TOKEN = f.read().strip()

# 获取 Ollama 客户端
def get_client(token: str = None):
    client = Client(
        host="https://myoi.ynuosa.org/ollama/",
        headers={"Authorization": f"Bearer {token}"},
    )
    return client

# 聊天接口：向 Ollama 发送消息
def chat_with_ollama(client, messages):
    try:
        response = client.chat(model="qwen2.5:14b", messages=messages)
        return response['message']['content']
    except Exception as e:
        return f"接口调用出错：{e}"

# GUI 界面实现
class QAApp:
    def __init__(self, root, client):
        self.client = client
        self.root = root
        self.root.title("智能问答助手")
        
        # 输入框标签
        self.input_label = tk.Label(root, text="请输入你的问题：", font=("Arial", 12))
        self.input_label.pack(pady=5)
        
        # 输入框
        self.input_box = tk.Entry(root, width=60, font=("Arial", 12))
        self.input_box.pack(pady=5)
        
        # 按钮区
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)
        
        self.joke_button = tk.Button(self.button_frame, text="趣味问答", command=lambda: self.get_answer("joke"))
        self.joke_button.grid(row=0, column=0, padx=5)
        
        self.story_button = tk.Button(self.button_frame, text="小故事生成", command=lambda: self.get_answer("story"))
        self.story_button.grid(row=0, column=1, padx=5)
        
        self.quote_button = tk.Button(self.button_frame, text="每日心灵鸡汤", command=lambda: self.get_answer("quote"))
        self.quote_button.grid(row=0, column=2, padx=5)
        
        # 输出框标签
        self.output_label = tk.Label(root, text="回答：", font=("Arial", 12))
        self.output_label.pack(pady=5)
        
        # 输出文本框
        self.output_box = scrolledtext.ScrolledText(root, width=60, height=10, font=("Arial", 12))
        self.output_box.pack(pady=5)
    
    def get_answer(self, mode):
        """根据模式生成不同的 Prompt 并调用 Ollama"""
        user_input = self.input_box.get()
        
        if mode == "joke":
            prompt = f"你现在是一个幽默大师，请用轻松、有趣的语气回答这个问题：{user_input}"
        elif mode == "story":
            prompt = f"请为我写一个简短的小故事，故事的主题是：{user_input}，字数在100-200字之间，生动有趣。"
        elif mode == "quote":
            prompt = "请生成一句充满正能量的励志句子，鼓励读者开始美好的一天。"
        else:
            prompt = user_input
        
        # 调用 Ollama API
        messages = [{"role": "user", "content": prompt}]
        response = chat_with_ollama(self.client, messages)
        
        # 显示输出结果
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, response)

# 主程序
if __name__ == "__main__":
    client = get_client(TOKEN)  # 初始化 Ollama 客户端
    root = tk.Tk()
    app = QAApp(root, client)
    root.mainloop()
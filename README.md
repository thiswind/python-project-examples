
# **实验讲义：智能问答助手项目**

## **实验目的**

1. 学会使用 **Gitee** 进行多人协作开发，掌握 **Fork** 和 **Pull Request** 的工作流程。  
2. 借助 **AI 辅助工具（Open-WebUI 和 qwen2.5-coder）**，实现 "翻译成文言文" 功能。  
3. 理解 Git 的分支管理与协作操作，包括创建分支、提交代码、合并代码等。  
4. 为后续任务打下基础，培养团队协作开发能力。

---

## **实验环境**

1. **操作系统**：Windows 10 / 11  
2. **开发工具**：VSCode  
3. **Python 版本**：3.8 及以上  
4. **依赖工具**：  
   - **Git**：用于代码版本管理与协作。  
   - **Gitee**：代码托管平台，提供 Fork 和 Pull Request 功能。  
   - **Open-WebUI**：AI 辅助工具，推荐使用 `qwen2.5-coder` 模型。  

---

## **项目初始化**

### **步骤 1：项目准备**

1. **组长 Fork 教师示例项目**  
   - 组长登录 **Gitee**，将教师提供的示例项目 **Fork** 到自己的账号。  
     教师项目地址：<https://gitee.com/thiswind/python-project-examples.git>  
   - 克隆 Fork 后的仓库到本地：  

     ```bash
     git clone https://gitee.com/<组长用户名>/python-project-examples.git
     cd python-project-examples
     ```

2. **组员 Fork 组长的项目**  
   - 每位组员登录 Gitee，将组长的仓库 **Fork** 到自己的账号。  
   - 克隆自己的 Fork 仓库到本地：  

     ```bash
     git clone https://gitee.com/<组员用户名>/python-project-examples.git
     cd python-project-examples
     ```

3. **安装项目依赖**  
   在项目根目录运行：  

   ```bash
   pip install ollama
   ```

4. **运行示例项目**  
   验证项目可以正常运行：  

   ```bash
   python main.py
   ```

---

## **实验任务：实现“翻译成文言文”功能**

### **步骤 2：创建个人分支**

组员在本地项目中创建新的功能分支：  

```bash
git checkout main
git pull origin main
git checkout -b feature/translate_to_classical_chinese
```

---

### **步骤 3：使用 AI 辅助编写代码**

1. 打开 **Open-WebUI**，选择 `qwen2.5-coder` 模型。  
2. 向 AI 提出需求：  
   > **“请帮我用 Python 实现一个功能：将输入的现代汉语句子翻译成文言文，返回 2~3 个不同版本。”**  
3. 根据 AI 提供的代码，按照以下步骤进行修改：

#### **修改 main.py**

1. **添加新按钮**  
   在 `QAApp` 类的 `__init__` 方法中，添加一个新按钮：  

   ```python
   self.translate_to_classical_chinese = tk.Button(
       self.button_frame,
       text="翻译成文言文",
       command=lambda: self.get_answer("translate_to_classical_chinese"),
   )
   self.translate_to_classical_chinese.grid(row=1, column=0, padx=5)
   ```

2. **修改 `get_answer` 方法**  
   在 `QAApp` 类的 `get_answer` 方法中，添加处理文言文翻译的逻辑：  

   ```python
   elif mode == "translate_to_classical_chinese":
       prompt = f"请把这段文字：'{user_input}'翻译成文言文。在你的回答中，你只输出翻译得到的文言文版本。你要给出2~3个不同的翻译版本。"
   ```

---

### **步骤 4：提交代码到个人分支**

1. **查看修改状态**  
   ```bash
   git status
   ```

2. **提交代码**  
   ```bash
   git add .
   git commit -m "新增翻译成文言文功能"
   ```

3. **推送分支到自己的远程仓库**  
   ```bash
   git push origin feature/translate_to_classical_chinese
   ```

---

### **步骤 5：向组长提交 Pull Request**

1. 打开 Gitee，进入自己的仓库页面。  
2. 找到刚刚推送的分支，点击 **“发起 Pull Request”**。  
3. 选择目标分支：**组长的 main 分支**。  
4. 填写 Pull Request 描述：  
   - 标题：**新增“翻译成文言文”功能**  
   - 内容：实现了文言文翻译功能，增加了按钮和调用逻辑。  
5. 提交 Pull Request，等待组长审核。

---

### **步骤 6：组长合并代码**

1. 组长进入自己的 Gitee 仓库，查看组员提交的 Pull Request。  
2. 审核代码，确认无误后点击 **“合并”**。  
3. 通知组员代码已合并到主分支。

---

### **步骤 7：组员同步更新主分支**

组员拉取组长的最新代码，保持本地与主分支同步：  

```bash
git checkout main
git pull upstream main  # upstream 指向组长的仓库
```

---

## **任务要求**

### **任务 1：金额转换为中文大写**

**功能描述**：  
将输入的金额数字转换为**中文大写**形式。  
- 输入：`12345.67`  
- 输出：`壹万贰仟叁佰肆拾伍元陆角柒分`  

**要求**：  
1. 在个人分支上实现功能。  
2. 提交 Pull Request 并合并到组长仓库。  

---

### **任务 2：小组自主设计并实现新功能**

**功能描述**：  
小组讨论并确定一个新的功能，设计并实现代码逻辑。  

**要求**：  
1. 每位成员负责一个子功能，使用分支管理开发。  
2. 提交 Pull Request 并合并代码，形成最终版本。

---

## **实验总结**

通过本次实验，你将掌握：  
1. Gitee 多层次协作流程：Fork、分支管理与 Pull Request。  
2. 使用 AI 辅助工具（Open-WebUI）完成功能开发。  
3. 团队协作开发新功能，锻炼沟通与协作能力。  

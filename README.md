

### 📝 To Do List with Gradio

A **user-based To Do List application** built with **Gradio** and **SQLite**.  
Users can **sign up, log in, add, edit, delete, and view tasks** through a simple **web interface**.

---

## 🌟 Features

- ✅ User Sign-Up & Log-In
- ✅ Add, Edit, Delete Tasks
- ✅ User-specific Task List
- ✅ Instant Task Refresh & View
- ✅ Log Out Functionality

---

## 💻 Requirements

- Python 3.8+
- Gradio
- SQLite (included with Python)

**Install Gradio:**
```bash
pip install gradio
```

---

## 🚀 Installation & Usage

```bash
# 1️⃣ Clone the repository
git clone https://github.com/eminbozgeyik27/TO-DO-List-with-Gradio.git
cd TO-DO-List-with-Gradio

# 2️⃣ Run the app
python todo-list.py   # Replace with your filename if different

# 3️⃣ Open Gradio interface
# Copy and open the link shown in the terminal in your browser
```

---

## 🛠️ How to Use

### 1️⃣ Sign-Up
- Enter a username & password
- Click **Sign Up**

### 2️⃣ Log-In
- Enter username & password
- Click **Log In**

### 3️⃣ To Do List
- Add new tasks
- List & refresh tasks

### 4️⃣ Delete Task
- Enter the task to delete
- Click **Delete Task**

### 5️⃣ Edit Task
- Enter the task to edit
- Type the new task
- Click **Edit Task**

### 6️⃣ Log-Out
- Log out the current user

---

## 🗄️ Database Structure

- **Database File:** `kullanicilar.db`
- **Tables:**
  - `kullanicilar` – stores usernames & passwords
  - `kullanici_portfoyu` – stores tasks belonging to each user

---

## 📌 Example

**Add a Task:**
```
Task: Do the shopping
Result: 'Do the shopping' added to your tasks.
Current Tasks:
- Do the shopping
```
**Delete a Task:**
```
Task: Do the shopping
Result: 'Do the shopping' task deleted.
```

---

## 🖼️ Visual Interface

- Sign-Up & Log-In window
- Task Add, Edit, Delete areas
- Buttons for instant task view

---

## 📜 License

This project is licensed under the MIT License.


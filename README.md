📝 To Do List with Gradio
This project is a user-based To Do List application developed using Gradio and SQLite. Users can sign up, log in, add, delete, and edit tasks, as well as view their task list.
🌟 Features
 * ✅ User sign-up and log-in functionalities
 * ✅ Task addition, deletion, and editing
 * ✅ User-specific task list
 * ✅ Task refresh and instant viewing
 * ✅ Ability to log out
💻 Requirements
 * Python 3.8 or higher
 * Gradio
 * SQLite (comes with Python)
Required package for installation:
pip install gradio

🚀 Installation and Usage
 * Clone or download the repository:
<!-- end list -->
git clone https://github.com/eminbozgeyik27/TO-DO-List-with-Gradio.git
cd TO-DO-List-with-Gradio

 * Create the database and start the application:
<!-- end list -->
python todo-list.py

> Note: If your file name is different, use your own file name.
> 
 * You can use the application from the Gradio interface that opens in your browser.
🛠️ Usage Steps
1️⃣ Sign-Up Tab
Create a new user:
 * Enter a username and password
 * Click the "Sign Up" button
2️⃣ Log-In Tab
Log in with an existing user:
 * Enter a username and password
 * Click the "Log In" button
3️⃣ To Do List Tab
 * Add a new task
 * List and refresh tasks
4️⃣ Delete Task Tab
 * Enter the task you want to delete
 * Click the "Delete Task" button
5️⃣ Edit Task Tab
 * Enter the task to be edited
 * Type the new task
 * Click the "Edit Task" button
6️⃣ Log-Out Tab
 * Log out the current user
🗄️ Database Structure
 * Database File: kullanicilar.db
 * Tables:
<!-- end list -->
 * kullanicilar – Username and password
 * kullanici_portfoyu – Tasks belonging to the user
📌 Example Usage
Adding a New Task:
Task: Do the shopping
Result: 'Do the shopping' added to your tasks.
Current Tasks:
- Do the shopping

Deleting a Task:
Task: Do the shopping
Result: 'Do the shopping' task deleted.

🖼️ Visual Interface
Thanks to Gradio, all operations can be performed through a web-based and visual interface.
 * Sign-up and log-in window
 * Task addition, deletion, and editing areas
 * Buttons for instant viewing of the task list
📜 License
This project is licensed under the MIT License.

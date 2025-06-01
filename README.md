# 🗂️ **Task Manager** ✅

An interactive task manager to add, delete, complete, modify, and recover tasks in a simple and organized way, using a friendly command-line menu.

---

## 🚀 **Project Overview**

This project is a **Python 3** application that allows users to manage tasks easily. The program enables you to:

* **Add Tasks**
* **Delete Tasks**
* **Complete Tasks**
* **Modify Tasks**
* **View tasks that are ongoing, completed, or deleted**
* **Recover deleted or completed tasks**

---

## 🛠️ **Main Features**

1. **Add Tasks**: Includes task name and deadline.
2. **Delete Tasks**: Removes tasks from the active task list.
3. **Complete Tasks**: Moves tasks to the completed task list.
4. **Modify Tasks**: Allows updating the name or deadline of a specific task.
5. **View Tasks**:

   * Active tasks
   * Completed tasks
   * Deleted tasks
6. **Recover Deleted Tasks**: Restores deleted tasks.
7. **Recover Completed Tasks**: Restores tasks marked as completed.

---

## 💾 **Setup**

### Prerequisites

* Python 3.x installed on your system.
* Environment compatible with running Python scripts.

---

## ▶️ **How to Run**

1. Clone the repository to your local environment:

```bash
git clone https://github.com/jp9141joao/task-manager.git
```

2. Navigate to the project directory:

```bash
cd task-manager
```

3. Run the script:

```bash
python filename.py
```

4. Interact through the menu displayed in the terminal.

---

## 🏆 **System Menu**

After starting the program, the menu will show the following options:

1. **Add Task**

   * Insert a new task with a deadline.

2. **Delete Task**

   * Allows deleting a task from the active task list.

3. **Complete Task**

   * Marks a task as completed.

4. **View Active Tasks**

   * Displays all ongoing tasks.

5. **View Deleted Tasks**

   * Lists all tasks that were deleted.

6. **View Completed Tasks**

   * Lists all tasks marked as completed.

7. **Modify Task**

   * Allows updating the name or deadline of a task.

8. **Recover Deleted Task**

   * Recovers a task that was deleted from the list.

9. **Recover Completed Task**

   * Recovers a completed task and moves it back to the active task list.

10. **Exit**

* Closes the program.

---

## 🧩 **Code Structure and Functionalities**

1. **Add Task**:

   * Inserts task name and deadline.

2. **Delete Task**:

   * Confirms task deletion after verification.

3. **Complete Task**:

   * Moves the task from the main list to the completed tasks list.

4. **Modify Task**:

   * Change the name or deadline of the task as needed.

5. **View Tasks**:

   * View lists of active, deleted, and completed tasks.

6. **Recover Deleted or Completed Tasks**:

   * Recovers tasks that were moved to deletion or completion lists.

---

## ⚙️ **Technologies Used**

* **Python 3.x**
* `os` library to clear the console.
* `time.sleep()` for allowing time to read messages.

Habit Tracker in Python

A simple command-line habit tracker built with Python.  
This program allows you to *add habits*, *view habits*, *mark them as done*, and *save your progress* to a text file (`habits.txt`).

---


  Table of content:-                                                                                                
 1 features                                                                                                                                               
 2 file struture                                                                                                                               
 3 How it work                                                                                                                                       
 4 Usage                                                                                                                             

 
---
 Features
- View Habits: See all your habits and their current status (DONE / NOT DONE YET).
- Add Habit: Add new habits to your list.
- Mark Habit as Done: Update the status of a habit once completed.
- Save Progress: Automatically saves your habits to `habits.txt` when you exit.

---


 File Structure
- `habit_tracker.py` → Main Python script.
- `habits.txt` → Text file where habits and their statuses are stored.

Example `habits.txt`:

 How It Works
1. When the program starts, it loads habits from `habits.txt` (if the file exists).
2. You interact with the menu:
3. Your choices update the habit list in memory.
4. When you exit, all changes are saved back to `habits.txt`.

---

Usage
Run the script in your terminal:

```bash
python habit_tracker.py


1. View Habits
2. Add Habit
3. Mark Habit as done
4. Exit
Choose an option: 2
Enter your habit name: Exercise
Added 'Exercise' to your habit list.


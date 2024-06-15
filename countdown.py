import tkinter as tk
from tkinter import messagebox

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("350x250")

        self.hours_label = tk.Label(self.master, text="Hours:", font=("Arial", 12))
        self.hours_label.grid(row=0, column=0, padx=10, pady=10)
        self.hours_entry = tk.Entry(self.master, font=("Arial", 12), width=5)
        self.hours_entry.grid(row=0, column=1)

        self.minutes_label = tk.Label(self.master, text="Minutes:", font=("Arial", 12))
        self.minutes_label.grid(row=1, column=0, padx=10, pady=10)
        self.minutes_entry = tk.Entry(self.master, font=("Arial", 12), width=5)
        self.minutes_entry.grid(row=1, column=1)

        self.seconds_label = tk.Label(self.master, text="Seconds:", font=("Arial", 12))
        self.seconds_label.grid(row=2, column=0, padx=10, pady=10)
        self.seconds_entry = tk.Entry(self.master, font=("Arial", 12), width=5)
        self.seconds_entry.grid(row=2, column=1)

        self.start_button = tk.Button(self.master, text="Start", font=("Arial", 12), command=self.start_timer)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.timer_label = tk.Label(self.master, text="", font=("Arial", 16, "bold"))
        self.timer_label.grid(row=4, column=0, columnspan=2)

        self.running = False
        self.remaining_time = 0
        self.countdown_id = None

    def start_timer(self):
        try:
            hours = int(self.hours_entry.get())
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())

            total_seconds = hours * 3600 + minutes * 60 + seconds

            if total_seconds <= 0:
                messagebox.showerror("Error", "Please enter a valid positive time.")
                return

            self.remaining_time = total_seconds
            self.update_timer_display()
            self.running = True
            self.countdown()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for hours, minutes, and seconds.")

    def countdown(self):
        if self.running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_timer_display()
            self.countdown_id = self.master.after(1000, self.countdown)
        elif self.remaining_time == 0:
            self.running = False
            messagebox.showinfo("Timer", "Time's up!")
            self.timer_label.config(text="")
            self.hours_entry.delete(0, tk.END)
            self.minutes_entry.delete(0, tk.END)
            self.seconds_entry.delete(0, tk.END)

    def update_timer_display(self):
        hours = self.remaining_time // 3600
        minutes = (self.remaining_time % 3600) // 60
        seconds = self.remaining_time % 60
        self.timer_label.config(text=f"Time Left: {hours:02}:{minutes:02}:{seconds:02}")

    def stop_timer(self):
        if self.countdown_id:
            self.master.after_cancel(self.countdown_id)
            self.countdown_id = None
            self.running = False

def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

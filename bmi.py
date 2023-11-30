import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        try:
            weight = float(self.weight)
            height = float(self.height)

            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")

            bmi = weight / (height ** 2)
            bmi_category = self.get_bmi_category(bmi)

            return f"Your BMI is: {bmi:.2f}\nCategory: {bmi_category}"

        except ValueError as e:
            raise ValueError(str(e))

    @staticmethod
    def get_bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.weight_label = tk.Label(root, text="Enter Weight (kg):")
        self.weight_label.pack()

        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        self.height_label = tk.Label(root, text="Enter Height (m):")
        self.height_label.pack()

        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate_bmi(self):
        weight = self.weight_entry.get()
        height = self.height_entry.get()

        try:
            bmi_calculator = BMICalculator(weight, height)
            result_text = bmi_calculator.calculate_bmi()
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()






















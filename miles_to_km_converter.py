
import tkinter

window =tkinter.Tk()
window.title("The Miles to Km Converter")
# window.geometry("500x500")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    output_label.config(text=f"{km}")

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

output_label_0 = tkinter.Label(text="Miles")
output_label_0.grid(column=2, row=0)
output_label_0.config(padx=10, pady=10)

output_label_1 = tkinter.Label(text="is equal to")
output_label_1.grid(column=0, row=1)
output_label_1.config(padx=10, pady=10)

output_label = tkinter.Label(text= "0")
output_label.grid(column=1, row=1)
output_label.config(padx=10, pady=10)

output_label_2 = tkinter.Label(text="Km")
output_label_2.grid(column=2, row=1)
output_label_2.config(padx=10, pady=10)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

window.mainloop()

import tkinter


def miles_to_kilometers():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_res_label.config(text=km)


window = tkinter.Tk()
window.title("Miles to km converter")

miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label2 = tkinter.Label(text="is equal to")
miles_label2.grid(column=0, row=1)
km_res_label = tkinter.Label(text="0")
km_res_label.grid(column=1, row=1)
km_label = tkinter.Label(text="km")
km_label.grid(column=3, row=1)

calc_button = tkinter.Button(window, text="Calculate",
                             command=miles_to_kilometers)
calc_button.grid(column=1, row=3)
window.mainloop()

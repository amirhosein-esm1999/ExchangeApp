from core.api_handler import fetch_graph_data , convert_to_dataframe , pair_conversion
from core.plotter import show_bar
import tkinter as tk
from tkinter import ttk,messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Main Tkinter interface
def show_on_tkinter():
    rates = fetch_graph_data()

    if rates is None:
        messagebox.showerror("Error", "Failed to fetch exchange rates. Please check your internet connection or API key.")
        return

    df = convert_to_dataframe(rates)
    fig = show_bar(df)

    # Configure the root window
    root = tk.Tk(className="Live Exchange Rate")
    root.geometry("415x300")
    root.resizable(False, False)


      # Hover effects
    def enter(event):
        event.widget["bg"] = "#035a25"

    def leave(event):
        event.widget["bg"] = "white"


    # Button to show the graph
    def click_btn1():
        graph_window = tk.Toplevel(master=root)
        graph_window.title("Live Graph")
        graph_window.resizable(False, False)
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="y", expand=True)

    # Button for pair conversion
    def click_btn2():
        conversion_window = tk.Toplevel(master=root)
        conversion_window.title("Pair Conversion")
        conversion_window.geometry("550x300")
        conversion_window.resizable(False, False)

        lbl2 = tk.Label(conversion_window, text="Select the source currency", font=("Yu Gothic", 8, "bold"))
        lbl2.grid(row=0, column=0, padx=65, pady=10)

        var1 = tk.StringVar()
        var1.set("USD")  # Set a default value for source currency
        cbox1 = ttk.Combobox(conversion_window, values=["USD", "EUR", "GBP", "JPY", "INR", "AUD", "CNY"],
                             textvariable=var1, state="readonly")
        
        var3 = tk.StringVar()
        var3.set("1")
        cbox1.grid(row=1, column=0, pady=5)
        ent1 = tk.Entry(master = conversion_window , textvariable=var3)
        ent1.grid(row = 1 , column=1 , sticky="e")
        lbl5 = tk.Label(master=conversion_window , text="amount" ,font=("Yu Gothic", 8, "bold"))
        lbl5.grid(row = 0  ,column=1)

        lbl3 = tk.Label(conversion_window, text="Select the target currency", font=("Yu Gothic", 8, "bold"))
        lbl3.grid(row=2, column=0, pady=10)

        var2 = tk.StringVar()
        var2.set("EUR")  # Set a default value for target currency
        cbox2 = ttk.Combobox(conversion_window, values=["USD", "EUR", "GBP", "JPY", "INR", "AUD", "CNY"],
                             textvariable=var2, state="readonly")
        cbox2.grid(row=3, column=0, padx=65, pady=5)
       
        lbl4 = tk.Label(conversion_window, text="", font=("Yu Gothic", 10, "bold"))
        lbl4.grid(row=5, column=0, padx=65, pady=15)
        #Placeholders for the source and target currencies are set dynamically.
        def click_btn3():
            source = cbox1.get()
            target = cbox2.get()
            try:
                amount = float(ent1.get())
            except ValueError:
                messagebox.showerror("Value error","Please Enter a valid Number for the amount.")
            
            if source == target:
                messagebox.showinfo("Source and Target currency are the same.")
                lbl4.config(text=f"{amount}")

            if not source or not target:
                messagebox.showwarning("Input Error", "Please select both source and target currencies.")
                return
            
            result = pair_conversion(source, target ,amount )

            if result is not None:
                lbl4.config(text=f"{result} {target}")
            else:
                messagebox.showerror("Error", "Conversion failed. Please check your input and connection or call the manufacturer.")

       

        btn3 = tk.Button(conversion_window, text="Convert", command=click_btn3, bg="white", fg="black",
                         relief="ridge", font=("Yu Gothic", 10, "bold"), padx=15, pady=10)
        btn3.grid(row=4, column=0, padx=65, pady=10)
        btn3.bind("<Enter>" , enter)
        btn3.bind("<Leave>" , leave)

    # Buttons on the main interface
    btn1 = tk.Button(root, text="Show Live Graph", bg="white", fg="black", command=click_btn1,
                     relief="ridge", padx=30, pady=20, font=("Yu Gothic", 8, "bold"))

    btn2 = tk.Button(root, text="Pair Conversion", bg="white", fg="black", command=click_btn2,
                     relief="ridge", padx=15, pady=12, font=("Yu Gothic", 8, "bold"))

  

    for button in [btn1, btn2]:
        button.bind("<Enter>", enter)
        button.bind("<Leave>", leave)

    btn1.grid(row=0, column=0, padx=20, pady=100)
    btn2.grid(row=0, column=1, padx=20, pady=100)

    root.mainloop()

if __name__ == "__main__":
    show_on_tkinter()

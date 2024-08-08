import shodan
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for Treeview

def search_shodan():
    api_key = api_key_entry.get()
    query = query_entry.get()

    try:
        api = shodan.Shodan(api_key)
        results = api.search(query)

        # Clear previous results
        for item in result_tree.get_children():
            result_tree.delete(item)

        # Insert results into Treeview
        for result in results['matches']:
            result_tree.insert("", tk.END, values=(result['ip_str'], result['port'], result['data']))

    except shodan.APIError as e:
        messagebox.showerror("Error", f"Shodan API Error: {e}")

# Create main window
window = tk.Tk()
window.title("Shodan GUI")

# API Key Label and Entry
api_key_label = tk.Label(window, text="API Key:")
api_key_label.grid(row=0, column=0, padx=5, pady=5)
api_key_entry = tk.Entry(window, width=40)
api_key_entry.grid(row=0, column=1, padx=5, pady=5)

# Query Label and Entry
query_label = tk.Label(window, text="Search Query:")
query_label.grid(row=1, column=0, padx=5, pady=5)
query_entry = tk.Entry(window, width=40)
query_entry.grid(row=1, column=1, padx=5, pady=5)

# Search Button
search_button = tk.Button(window, text="Search", command=search_shodan)
search_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Result Treeview
result_tree = ttk.Treeview(window, columns=("IP", "Port", "Data"), show="headings")
result_tree.heading("IP", text="IP Address")
result_tree.heading("Port", text="Port")
result_tree.heading("Data", text="Data")
result_tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()

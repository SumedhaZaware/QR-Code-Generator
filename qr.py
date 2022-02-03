'''
Created by: Sumedha Zaware
'''

# Import required libraries
import tkinter as tk
import qrcode

# Setup the screen
root = tk.Tk()
root.title('QR Code Generator')
root.geometry('400x200')
root.config(bg="#ECD6D1")

def save_qr():
    ''' Save the generated QR Code for the given input text or link
    '''
    data = link_entry.get()
    img = qrcode.make(data)
    img.save('output.png')

    text = tk.Label(root,text='QR Code generated and saved!!',bg="#ECD6D1")
    text.place(x=70,y=120)
    text.config(font=('Helvatical',10))

# Link label
link_label = tk.Label(root, text="Enter link or text:" ,bg="#ECD6D1")
link_label.place(x=20, y=20)
link_label.config(font=('calibri',14))

# Link or text entry
link_entry = tk.Entry(root)
link_entry.place(x=70, y=44)
link_entry.config(font=('Helvatical bold',12))

# Button to generate QR code
generate_button = tk.Button(root, text ="Generate QR Code", command = save_qr)
generate_button.place(x=100,y=80)

root.mainloop()

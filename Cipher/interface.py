from tkinter import*
from tkinter import messagebox
import cipher
root = Tk()
root.geometry("400x200")
root.title("Caesar Cipher")

key = StringVar()
plain_text = StringVar()
cipher_text = StringVar()



#Creating the layout of the GUI
key_Lable = Label(root, text= "Key:").place(relx= 0.33, rely= 0.01)
key_entry = Entry(root, textvariable= key, width=2).place(relx=0.41,rely=0.01)

encrypt_Lable = Label(root, text="Enter message to encrypt: ").place(relx = 0.05, rely=0.2)
encrypt_entry = Entry(root, textvariable= plain_text, width= 30).place(relx=0.41, rely=0.205)

decrypt_Lable = Label(root, text="Enter message to decrypt: ").place(relx = 0.05, rely=0.4)
decrypt_entry = Entry(root, textvariable= cipher_text, width= 30).place(relx=0.41, rely=0.405)

#command code for encryption
def encrypt():
    if key.get() == '':
        messagebox.showerror("ERROR", "Please enter a key")
    else:
        text = plain_text.get()
        if text == '':
            messagebox.showerror("ERROR", "Please enter a sentence")
        else:
            num = int(key.get())
            encrypted = cipher.Encryption(text,num)
            messagebox.showinfo("Encryption", encrypted)


#Command code for Decryption
def decrypt():
    if key.get() == '':
        messagebox.showerror("ERROR", "Please enter a key")
    else:
        text = cipher_text.get()
        if text == '':
            messagebox.showerror("ERROR", "Please enter a sentence")
        else:
            num = int(key.get())
            decrypt = cipher.Decryption(text,num)
            messagebox.showinfo("Decryption", decrypt)

encryptbutton = Button(root, text="Encrypt", command= encrypt, padx= 10, pady= 10).place(relx=0.35, rely=0.6)

decryptbutton = Button(root, text="Decrypt", command= decrypt, padx= 10, pady= 10).place(relx=0.55, rely=0.6)


root.mainloop()
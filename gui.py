import tkinter as tk
from tkinter import filedialog, messagebox
import os

class FileChooser:
    def __init__(self, root):
        self.root = root
        self.root.title("File Chooser")
        self.selected_file_path = None
        self.selected_file_type = None
        self.summarization = tk.BooleanVar()
        self.summarization.set(False)
        self.photo_to_text = tk.BooleanVar()
        self.photo_to_text.set(False)
        self.keywords = tk.BooleanVar()
        self.keywords.set(False)
        self.note = tk.BooleanVar()
        self.note.set(False)
        self.document_question = tk.BooleanVar()
        self.document_question.set(False)
        self.question = tk.StringVar()

        self.file_label = tk.Label(root, text="Selected File:")
        self.file_label.pack()

        self.file_entry = tk.Entry(root, width=50)
        self.file_entry.pack()

        self.select_button = tk.Button(root, text="Browse", command=self.select_file)
        self.select_button.pack()

        self.file_type_label = tk.Label(root, text="File Type:")
        self.file_type_label.pack()

        self.checkboxes_frame = tk.Frame(root)
        self.checkboxes_frame.pack()

        tk.Checkbutton(self.checkboxes_frame, text="Summarization", variable=self.summarization).pack(side=tk.LEFT)
        tk.Checkbutton(self.checkboxes_frame, text="Photo to Text", variable=self.photo_to_text).pack(side=tk.LEFT)
        tk.Checkbutton(self.checkboxes_frame, text="Keywords", variable=self.keywords).pack(side=tk.LEFT)
        tk.Checkbutton(self.checkboxes_frame, text="Note", variable=self.note).pack(side=tk.LEFT)
        tk.Checkbutton(self.checkboxes_frame, text="Document Question", variable=self.document_question, command=self.show_question_field).pack(side=tk.LEFT)

        self.question_label = tk.Label(root, text="Question:")
        self.question_label.pack_forget()

        self.question_entry = tk.Entry(root, width=50)
        self.question_entry.pack_forget()

        self.confirm_button = tk.Button(root, text="Confirm", command=self.confirm_file)
        self.confirm_button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)
        file_type = os.path.splitext(file_path)[1]
        self.file_type_label.config(text=f"File Type: {file_type}")

    def confirm_file(file_chooser):
        self = file_chooser
        self.selected_file_path = self.file_entry.get()
        if self.selected_file_path:
            self.selected_file_type = os.path.splitext(self.selected_file_path)[1]
            messagebox.showinfo("File Confirmed", f"You have selected: {self.selected_file_path}")
            checked_checkboxes = []
            if self.summarization.get():
                checked_checkboxes.append("Summarization")
            if self.photo_to_text.get():
                checked_checkboxes.append("Photo to Text")
            if self.keywords.get():
                checked_checkboxes.append("Keywords")
            if self.note.get():
                checked_checkboxes.append("Note")
            if self.document_question.get():
                checked_checkboxes.append("Document Question")
                checked_checkboxes.append(f"Question: {self.question_entry.get()}")
            print(f"Selected File Path: {self.selected_file_path}")
            print(f"Checked Checkboxes: {', '.join(checked_checkboxes)}")

            # Call get_file_content and print the file content
            file_content = self.get_file_content()
            print(f"File Content: {file_content}")

            # Close the main window
            self.root.destroy()

            # Create a new window to display the "Please wait" message
            wait_window = tk.Toplevel()
            wait_window.title("Please Wait")
            wait_label = tk.Label(wait_window, text="Please wait while we process your request...")
            wait_label.pack()

            # You can add your processing code here

            # Close the wait window after processing is complete
            # wait_window.destroy()
        else:
            messagebox.showerror("Error", "Please select a file first")

    def show_question_field(self):
        if self.document_question.get():
            self.question_label.pack()
            self.question_entry.pack()
        else:
            self.question_label.pack_forget()
            self.question_entry.pack_forget()

    def get_selected_file(self):
        return {
            "selected_file_path": self.selected_file_path,
            "selected_file_type": self.selected_file_type,
            "summarization": self.summarization.get(),
            "photo_to_text": self.photo_to_text.get(),
            "keywords": self.keywords.get(),
            "note": self.note.get(),
            "document_question": self.document_question.get(),
            "question": self.question_entry.get()
        }

    def get_file_content(self):
        if self.selected_file_path:
            file_type = os.path.splitext(self.selected_file_path)[1]
            if file_type in [".txt", ".text", ".md"]:  # adjust file types as needed
                with open(self.selected_file_path, "r") as file:
                    return file.read()
            else:
                return ""  # or handle other file types as needed
        else:
            return ""

if __name__ == "__main__":
    root = tk.Tk()
    file_chooser = FileChooser(root)
    root.mainloop()
    selected_file = file_chooser.get_selected_file()
    file_content = file_chooser.get_file_content
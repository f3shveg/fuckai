import os
import datetime
from datetime import date, time
from time import gmtime, strftime

path="/home/kali/Desktop/test/"
now = strftime("%d-%m-%Y\n%H:%M:%S")

def WriteToNote(note_name, content):
    try:
        with open(path+note_name+".md", 'a') as f:
            f.write(f"\n\n**{now}**\n"+content)
            print(f"Content added to {note_name} successfully.")
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to write to '{note_name}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred - {e}")
    
def CreateNote(new_note_name):
    try:
        with open(path+new_note_name+".md", 'x') as f:
            print(f"Note '{new_note_name}' created successfully.")
    except FileExistsError:
        print(f"Error: A note with the name '{new_note_name}' already exists.")
    except PermissionError:
        print(f"Error: Permission denied to create '{new_note_name}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred - {e}")

def RenameNote(note_name,new_name):
    for filename in os.listdir(path):
        if filename.endswith(".md"):
            filepath = os.path.join(path, filename)
            with open(filepath, 'r') as file:
                file_content = file.read()
            if "[["+note_name+"]]" in file_content:
                new_link = file_content.replace(note_name, new_name)
                with open(filepath, 'w') as file:
                    file.write(new_link)
                print(f"Replaced '{note_name}' with '{new_name}' in {filename}")
            else:
                print(f"No occurrences of '{note_name}' found in {filename}")
    try:
        os.rename(path+note_name+".md", path+new_name+".md")
        print(f"Note '{note_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"Error: The note '{note_name}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to rename '{note_name}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred - {e}")

def ChangeLinks(link_name,new_link):
    for filename in os.listdir(path):
        if filename.endswith(".md"):
            filepath = os.path.join(path, filename)
            with open(filepath, 'r') as file:
                file_content = file.read()
            if "[["+link_name+"]]" in file_content:
                new_link = file_content.replace(link_name, new_link)
                with open(filepath, 'w') as file:
                    file.write(new_link)
                print(f"Replaced '{link_name}' with '{new_link}' in {filename}")
            else:
                print(f"No occurrences of '{link_name}' found in {filename}")

def NoteConnection(first_note, second_note):
    try:
        with open(path + first_note + ".md", 'a') as file:
            with open(path + second_note + ".md", 'r') as second_file:
                file.write(f"\n >*MERGED FROM {second_note} NOTE* {second_file.read()}")
        os.remove(path + second_note + ".md")
        print(f"Merged '{second_note}' into '{first_note}' and deleted '{second_note}' successfully.")
    except FileNotFoundError:
        print(f"Error: One or both of the notes '{first_note}' and '{second_note}' do not exist.")
    except PermissionError:
        print(f"Error: Permission denied to modify '{first_note}' or delete '{second_note}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred - {e}")
# CRUD Project

import pathlib
import os
from pathlib import Path

def path_Files():
    p = Path.cwd()
    files = p.rglob("*")
    print("\n" + "="*40)
    print("FILES IN CURRENT DIRECTORY")
    print("="*40)
    for f in files:
        print(f"  📄 {f.name}")
    print("="*40 + "\n")

def creating_File():
    try:
        path_Files()
        fileName = input("Enter your new file name:- ")
        filePath = pathlib.Path(fileName)
        with open(filePath,"w") as file:
            print("\n" + "-"*40)
            print("1. Create Empty File")
            print("2. Add Content to File")
            print("-"*40)
            option = int(input("\nEnter your option:- "))
            if option == 1:
                file.close()
                print("\n✅ Empty File created successfully.")
            if option == 2:
                data = input("Enter your content here:- ")
                file.write(data)
                print("\n✅ File created successfully.")
    except Exception as err:
        print(f"Getting an err as {err}")

def reading_File():
    try:
        path_Files()
        fileName = input("Enter your file name:- ")
        filePath = pathlib.Path(fileName)
        
        with open(filePath, "r") as file:
            fileContent = file.read()
            print("\n" + "="*40)
            print("FILE CONTENT")
            print("="*40)
            print(fileContent)
            print("="*40 + "\n")
    except Exception as err:
        print(f"Getting an err as {err}")

def updating_File():
    try:
        path_Files()
        fileName = input("Enter your file name:- ")
        filePath = pathlib.Path(fileName)
        if filePath.exists():
            with open(filePath, "a") as file:
                newContent = input("Enter your new content:- ")
                file.write(f"\n{newContent}")
                print("\n✅ File content updated successfully!\n")
        else:
            print("\n⚠️  File doesn't exist!")
            print("\n1. Create new file")
            print("2. Go back")
            option = int(input("\nEnter your option:- "))
            if option == 1: 
                with open(filePath, "w") as file:
                    newContent = input("Enter your content:- ")
                    file.write(newContent)
                print("\n✅ File created and content added!\n")
            else:
                print("\n↩️  No changes made.\n")
                
    except Exception as err:
        print(f"Getting an err as {err}")

def deleting_File():
    try:
        path_Files()
        fileName = input("Enter your file name:- ")
        filePath = pathlib.Path(fileName)
        
        os.remove(filePath)
        print("\n✅ File deleted successfully!\n")
        
    except Exception as err:
        print(f"Getting an err as {err}")

print("\n" + "="*40)
print("       FILE MANAGEMENT SYSTEM")
print("="*40)
print("\n1. Create New File")
print("2. Read a File")
print("3. Update a File")
print("4. Delete a File")
print("\n" + "-"*40)

try:
    userSelection = int(input("Enter your option here:- "))

    if userSelection == 1:
        creating_File()
    if userSelection == 2:
        reading_File()
    if userSelection == 3:
        updating_File()
    if userSelection == 4:
        deleting_File()

except Exception as err:
    print(f"\n❌ Error: {err}")
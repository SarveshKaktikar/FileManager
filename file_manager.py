import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename}: created successfully!")
    except FileExistsError:
        print(f"File name {filename} already exists!")
    except Exception as e:
        print("An error occured!")

def view_all_files():
    files = os.listdir()

    if not files:
        print("No file found!")
    else:
        print("Files is directory!")
        for i in files:
            print(i)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print(f"{filename} does not exists!")
    except Exception as e:
        print("An error occured!")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Content of '{filename}' : \n{content}")
    except FileNotFoundError:
        print(f"{filename} does not exits!")
    except Exception as e:
        print("An error occured!")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Ente data to add = ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully!")
    except FileNotFoundError:
        print(f"{filename} does not exits!")
    except Exception as e:
        print("An error occured!")   
    
def main():
    while True:
        print("File Management App")
        print('1. Create File')
        print('2. View All Files')
        print('3. Delete File')
        print('4. Read File')
        print('5. Edit File')
        print('6. Exit')

        choice = input("Enter your choice(1-6): ")

        if choice == '1':
            filename = input("Enter file name you want to create: ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("Enter file name you want to delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter file name which you want to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter file name you want to edit: ")
            edit_file(filename)

        elif choice == '6':
            print("Closing the app...........")
            break

        else:
            print("In-valid choice select from (1-6)")

if __name__ == "__main__":
    main()
    
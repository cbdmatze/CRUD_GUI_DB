from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image



# Creating the main window
window = Tk()
window.geometry("600x270")
window.title("MovieWebApp")

# Display an image 
img = Image.open("coder's_heaven.png")
img.show()

# Adding Label Widgets with increased vertical spacing
userID = Label(window, text="User Id", font=("Serif", 12))
userID.place(x=20, y=30)

userName = Label(window, text="User Name", font=("Serif", 12))
userName.place(x=20, y=80)

# Adding Entry Widgets with increased vertical spacing
enterID = Entry(window)
enterID.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=80)


def insertData():
    # Read the data provided by the user
    id = enterID.get()
    name = enterName.get()

    if id == "" or name == "":
        messagebox.showwarning("Cannot Insert", "All the fields are required!")
    else:
        try:
            # Insert data in the users table
            conn = mysql.connector.connect(
                host="localhost", 
                user="root",
                password="Ma-294022275",
                database="moviewebapp"
            )
            
            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Execute the insert query
            cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (id, name))

            # Commit the transaction to the database
            conn.commit()

            # Close the cursor and connection
            cursor.close()
            conn.close()

            # Clear the entries from the fields filled by the user
            enterID.delete(0, "end")
            enterName.delete(0, "end")

            # Call show() method to display the data in the Listbox
            show()

            # Show confirmation message
            messagebox.showinfo("Success", "Data inserted successfully!")
        except mysql.connector.Error as err:
            # Handle any MySQL errors
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            # Handle any other errors
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def updateData():
    # Read the data provided by the user
    id = enterID.get()  # Ensure you are using the correct variable name
    name = enterName.get()

    if id == "" or name == "":
        messagebox.showwarning("Cannot Update", "All the fields are required!")
    else:
        try:
            # Update users table
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275", 
                database="moviewebapp"
            )

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Use parameterized queries to avoid SQL injection risks
            cursor.execute("UPDATE users SET name = %s WHERE id = %s", (name, id))

            # Commit the transaction to the database
            conn.commit()

            # Check if any row was updated
            if cursor.rowcount == 0:
                messagebox.showwarning("Update Failed", "No such user found with the given ID.")
            else:
                # Show confirmation message
                messagebox.showinfo("Success", "Data updated successfully!")

            # Close the cursor and connection
            cursor.close()
            conn.close()

            # Clear the entries from the fields filled by the user
            enterID.delete(0, "end")
            enterName.delete(0, "end")

            # Call show() method to display data in Listbox
            show()

        except mysql.connector.Error as err:
            # Handle any MySQL errors
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            # Handle any other errors
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def getData():
    # Combined reading and checking for empty data
    if enterID.get() == "":
        messagebox.showwarning("Fetch Status", "Please provide the userID to fetch the data!")
    else:
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost", 
                user="root", 
                password="Ma-294022275",
                database="moviewebapp"
            )

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Use parameterized queries to prevent SQL injection
            cursor.execute("SELECT * FROM users WHERE id = %s", (enterID.get(),))
            rows = cursor.fetchall()

            if rows:
                # Assuming the 'name' is in the second column (index 1)
                for row in rows:
                    enterName.insert(0, row[1])  # Insert the name into the entry field
            else:
                messagebox.showwarning("Fetch Status", "No user found with that ID.")

            # Close the connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            # Handle any MySQL errors
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            # Handle any other errors
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def deleteData():
    # Combined reading and checking for userID data
    if enterID.get() == "":
        messagebox.showwarning("Cannot Delete", "Please provide the userID to delete the data!")
    else:
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host="localhost", 
                user="root", 
                password="Ma-294022275", 
                database="moviewebapp"
            )

            # Create a cursor object to execute SQL queries
            cursor = conn.cursor()

            # Use parameterized queries to prevent SQL injection
            cursor.execute("DELETE FROM users WHERE id = %s", (enterID.get(),))

            # Commit the transaction to the database
            conn.commit()

            if cursor.rowcount > 0:
                # Only show confirmation if a row was affected
                messagebox.showinfo("Success", "User data deleted successfully!")
            else:
                messagebox.showwarning("Not Found", "No user found with the provided ID.")

            # Clear out data from all fields
            enterID.delete(0, "end")
            enterName.delete(0, "end")

            # Call show() method to display data in Listbox
            show()

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            # Handle any SQL errors
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            # Handle any other errors
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def show():
    try:
        # Establish the database connection
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="Ma-294022275", 
            database="moviewebapp"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the getData query
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        # Clear the Listbox
        showData.delete(0, END)

        if rows:
            # If there are rows, insert each into the Listbox
            for row in rows:
                addData = str(row[0]) + ' ' + row[1] + ' ' + row[2]
                showData.insert(END, addData)  # Use END to insert at the last position
        else:
            # If no rows, show a message in the Listbox
            showData.insert(END, "No data found")

    except mysql.connector.Error as err:
        # Handle SQL errors
        messagebox.showerror("Database Error", f"Error: {err}")
    except Exception as e:
        # Handle other unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    finally:
        # Ensure the cursor and connection are always closed
        cursor.close()
        conn.close()


def resetFields():
    # Clear the ID and Name entry widgets
    enterID.delete(0, END)
    enterName.delete(0, END)

    # Provide user feedback that fields have been reset
    messagebox.showinfo("Reset", "Fields have been reset successfully!")


# Creating the buttons we need with more space between them
insertBtn = Button(window, text="Insert", font=("Sans", 12), bg="white", command=insertData)
insertBtn.place(x=20, y=130)

updateBtn = Button(window, text="Update", font=("Sans", 12), bg="white", command=updateData)
updateBtn.place(x=80, y=130)

getBtn = Button(window, text="Fetch", font=("Sans", 12), bg="white", command=getData)
getBtn.place(x=150, y=130)

deleteBtn = Button(window, text="Delete", font=("Sans", 12), bg="white", command=deleteData)
deleteBtn.place(x=210, y=130)

resetBtn = Button(window, text="Reset", font=("Sans", 12), bg="white", command=resetFields)
resetBtn.place(x=20, y=170)

# Creating the Listbox Widget and giving more space around it
showData = Listbox(window)
showData.place(x=370, y=30, height=200, width=200)

# Call show() method to display data in Listbox after the box is created
show()

# Start the Tkinter main loop (must be placed after widget setup)
window.mainloop()

from tkinter import *
from tkinter import messagebox, END, Listbox
import mysql.connector
from PIL import ImageTk, Image


# Initialize the main window
window = Tk()
window.geometry("600x500")
window.title("MyBase")

# Load and display an image
img = Image.open("coder's_heaven.png")
img.show()


# Create entry fields and labels for user ID and user/movie details
Label(window, text="User ID", font=("monospace", 12)).place(x=20, y=20)
enterID = Entry(window, font=("monospace", 12))
enterID.place(x=150, y=20)

Label(window, text="User Name", font=("monospace", 12))
enterName = Entry(window, font=("monospace", 12))
enterName.place(x=150, y=60)

Label(window, text="Movie Title", font=("monospace", 12))
enterMovieTitle = Entry(window, font=("monospace", 12))
enterMovieTitle.place(x=150, y=100)

Label(window, text="Director", font=("monospace", 12))
enterDirector = Entry(window, font=("monospace", 12))
enterDirector.place(x=150, y=140)

Label(window, text="Year", font=("monospace", 12))
enterYear = Entry(window, font=("monospace", 12))
enterYear.place(x=150, y=180)

Label(window, text="Rating", font=("monospace", 12))
enterRating = Entry(window, font=("monospace", 12))
enterRating.place(x=150, y=220)


# Create a listbox to display user and movie details
listbox = Listbox(window, width=60, height=10)
listbox.place(x=20, y=400)


# Movie list to store movie IDs and titles
movie_list = []
movie_titles = []


# User CRUD operations
def insertUser():
    user_id = enterID.get()
    user_name = enterName.get()

    if user_id == "" or user_name == "":
        messagebox.showwarning("Cannot Insert", "All fields are required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="mybase"
            )
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (user_id, user_name))

            conn.commit()
            cursor.close()
            conn.close()

            enterID.delete(0, END)
            enterName.delete(0, END)
            messagebox.showinfo("Success", "User inserted successfully!")

            enterID.delete(0, END)
            enterName.delete(0, END)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def showData():
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


def updateUser():
    user_id = enterID.get()
    user_name = enterName.get()

    if user_id == "" or user_name == "":
        messagebox.showwarning("Cannot Update", "All fields are required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="mybase"
            )
            cursor = conn.cursor()

            cursor.execute("UPDATE users SET name = %s WHERE id = %s", (user_name, user_id))

            conn.commit()
            cursor.close()
            conn.close()

            enterID.delete(0, END)
            enterName.delete(0, END)
            messagebox.showinfo("Success", "User updated successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def fetchUser():
    user_id = enterID.get()

    if user_id == "":
        messagebox.showwarning("Cannot Fetch", "User ID is required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="mybase"
            )
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            row = cursor.fetchone()

            if row:
                enterName.delete(0, END)
                enterName.insert(0, row[1])
            else:
                messagebox.showwarning("Fetch Failed", "No user found with the given ID.")
            
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def deleteUser():
    user_id = enterID.get()

    if user_id == "":
        messagebox.showwarning("Cannot Delete", "User ID is required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="mybase"
            )
            cursor = conn.cursor()

            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))

            conn.commit()
            cursor.close()
            conn.close()

            enterID.delete(0, END)
            enterName.delete(0, END)
            messagebox.showinfo("Success", "User deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


# Movie CRUD operations
def insertMovie():
    user_id = enterID.get()
    movie_title = enterMovieTitle.get()
    director = enterDirector.get()
    year = enterYear.get()
    rating = enterRating.get()

    if user_id == "" or movie_title == "" or director == "" or year == "" or rating == "":
        messagebox.showwarning("Cannot Insert", "All fields are required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="mybase"
            )
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO movies (user_id, title, director, year, rating) VALUES (%s, %s, %s, %s, %s)",
                (user_id, movie_title, director, year, rating)
            )
            conn.commit()
            cursor.close()
            conn.close()

            showMovies()
            messagebox.showinfo("Success", "Movie inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def showMovies():
    user_id = enterID.get()

    if user_id == "":
        messagebox.showwarning("Cannot Show", "User ID is required!")
        return
    
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ma-294022275",
            database="mybase"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM movies WHERE user_id = %s", (user_id,))
        rows = cursor.fetchall()

        showData.delete(0, END)

        if rows:
            for row in rows:
                movie_info = f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}"
                showData.insert(END, movie_info)
        else:
            messagebox.showwarning("No Movies", "No movies found for the given user ID.")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


# Buttons for user methods
Button(window, text="Insert User", font=("monospace", 12), bg="grey", command=insertUser).place(x=20, y=270)
Button(window, text="Update User", font=("monospace", 12), bg="grey", command=updateUser).place(x=140, y=270)
Button(window, text="Fetch User", font=("monospace", 12), bg="grey", command=fetchUser).place(x=260, y=270)
Button(window, text="Delete User", font=("monospace", 12), bg="grey", command=deleteUser).place(x=380, y=270)

# Buttons for movie methods
Button(window, text="Insert Movie", font=("monospace", 12), bg="grey", command=insertMovie).place(x=20, y=310)
Button(window, text="Show Movies", font=("monospace", 12), bg="grey", command=showMovies).place(x=140, y=310)

# Run the main loop
window.mainloop()

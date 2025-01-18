from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image


# Creating the main window
window = Tk()
window.geometry("600x500")
window.title("MyBase")

# Display an image
img = Image.open("coder's_heaven.png")
img.show()

# User details Labels and Entries
userID = Label(window, text="User Id", font=("monospace", 12))
userID.place(x=20, y=30)

userName = Label(window, text="User Name", font=("monospace", 12))
userName.place(x=20, y=80)

enterID = Entry(window)
enterID.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=80)


# Movie details Labels and Entries
movieTitle = Label(window, text="Movie Title", font=("monospace", 12))
movieTitle.place(x=20, y=130)

director = Label(window, text="Director", font=("monospace", 12))
director.place(x=20, y=180)

year = Label(window, text="Year", font=("monospace", 12))
year.place(x=20, y=230)

rating = Label(window, title="Rating", font=("monospace", 12))
rating.place(x=20, y=280)

enterMovieTitle = Entry(window)
enterMovieTitle.place(x=170, y=130)

enterDirector = Entry(window)
enterDirector.place(x=170, y=180)

enterYear = Entry(window)
enterYear.place(x=170, y=230)

enterRating = Entry(window)
enterRating.place(x=170, y=280)

# Existing user methods
def inserUser():
    user_id = enterID.get()
    user_name = enterName.get()

    if user_id == "" or user_name == "":
        messagebox.showwarning("Cannot Insert", "All the fields are required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="moviewebapp"
            )
            cursor = conn.cursor()

            # Insert user data
            cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (user_id, user_name))

            conn.commit()
            cursor.close()
            conn.close()

            enterID.delete(0, END)
            enterName.delete(0, END)

            messagebox.showinfo("Success", "User data inserted successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def updateUser():
    user_id = enterID.get()
    user_name = enterName.get()

    if user_id == "" or user_name == "":
        messagebox.showwarning("Cannot Update", "All the fields are required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="moviewebapp"
            )
            cursor = conn.cursor()

            # Update user data
            cursor.execute("UPDATE users SET name=%s WHERE id=%s", (user_name, user_id))

            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "User data updated successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def fetch_user():
    user_id = enterID.get()

    if user_id == "":
        messagebox.showwarning("Cannot Fetch", "User ID is required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="moviewebapp"
            )
            cursor = conn.cursor()

            # Fetch user data
            cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))   # Note the comma after user_id
            row = cursor.fetchone()

            if row:
                enterName.delete(0, END)
                enterName.insert(0, row[1])  # Name is at index 1
            else:
                messagebox.showwarning("Fetch Failed", "No such user found with the given ID.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def delete_user():
    user_id = enterID.get()

    if user_id == "":
        messagebox.showwarning("Cannot Delete", "User ID is required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="moviewebapp"
            )
            cursor = conn.cursor()

            # Delete user data
            cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))

            conn.commit()
            cursor.close()
            conn.close()

            enterID.delete(0, END)
            enterName.delete(0, END)

            messagebox.showinfo("Success", "User data deleted successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


# Movie methods (Insert, Show) remain the same
def insertMovie():
    movie_id = enterID.get()
    movie_title = enterMovieTitle.get()
    movie_director = enterDirector.get()
    movie_year = enterYear.get()
    movie_rating = enterRating.get()

    if movie_id == "" or movie_title == "" or movie_director == "" or movie_year == "" or movie_rating == "":
        messagebox.showwarning("Cannot Insert", "All the fields are required!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="moviewebapp"
            )
            cursor = conn.cursor()

            # Insert movie data associated with the user
            cursor.execute(
                "INSERT INTO movies (movie_id, movie_title, movie_director, movie_year, movie_rating) VALUES (%s, %s, %s, %s, %s)",
                (movie_id, movie_title, movie_director, movie_year, movie_rating)
            )

            conn.commit()
            cursor.close()
            conn.close()

            enterMovieTitle.delete(0, END)
            enterDirector.delete(0, END)
            enterYear.delete(0, END)
            enterRating.delete(0, END)

            showMovies()

            messagebox.showinfo("Success", "Movie data inserted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def showMovies():
    user_id = enterID.get()
    if user_id == "":
        messagebox.showwarning("Display Error", "Please enter User ID to show movies!")
        return
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ma-294022275",
            database="moviewebapp"
        )
        cursor = conn.cursor()

        # Fetch movies for the specific user
        cursor.execute("SELECT * FROM movies WHERE user_id=%s", (user_id,)) # Note the comma after user_id
        rows = cursor.fetchall()

        showData.delete(0, END)

        if rows:
            for row in rows:
                # Display each movie in the format: "Movie Title ⎜ Director ⎜ Year ⎜ Rating"
                movie_info = f"{row[1]} ⎜ {row[2]} ⎜ {row[3]} ⎜ {row[4]}"
                showData.insert(END, movie_info)
        else:
            showData.insert(END, "No movies found for the user.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


# Buttons for user methods
insertUserBtn = Button(window, text="Insert User", font=("monospace", 12), bg="grey", command=inserUser)
insertUserBtn.place(x=20, y=370)

updateUserBtn = Button(window, text="Update User", font=("monospace", 12), bg="grey", command=updateUser)
updateUserBtn.place(x=140, y=370)

fetchUserBtn = Button(window, text="Fetch User", font=("monospace", 12), bg="grey", command=fetch_user)
fetchUserBtn.place(x=260, y=370)

deleteUserBtn = Button(window, text="Delete User", font=("monospace", 12), bg="grey", command=delete_user)
deleteUserBtn.place(x=380, y=370)

# Buttons for movie methods
insertMovieBtn = Button(window, text="Insert Movie", font=("monospace", 12), bg="grey", command=insertMovie)
insertMovieBtn.place(x=20, y=410)

showMoviesBtn = Button(window, text="Show Movies", font=("monospace", 12), bg="grey", command=showMovies)
showMoviesBtn.place(x=140, y=410)

# Listbox to display movies
showData = Listbox(window, width=40, height=10, font=("monospace", 12))
showData.place(x=20, y=450)


# Running the nain window loop
window.mainloop()
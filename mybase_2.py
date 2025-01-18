import tkinter as tk
from tkinter import messagebox, END, Listbox
import mysql.connector
from PIL import ImageTk, Image


# Initialize the main window
window = tk.Tk()
window.geometry("600x500")
window.title("MyBase")

# Load and display an image
img = Image.open("coder's_heaven.png")
img.show()


# Create entry fields and labels for user ID and movie details
tk.Label(window, text="User ID", font=("monospace", 12)).place(x=20, y=20)
enterID = tk.Entry(window, font=("monospace", 12))
enterID.place(x=150, y=20)

tk.Label(window, text="Movie Title", font=("monospace", 12)).place(x=20, y=60)
enterMovieTitle = tk.Entry(window, font=("monospace", 12))
enterMovieTitle.place(x=150, y=60)

tk.Label(window, text="Director", font=("monospace", 12)).place(x=20, y=100)
enterDirector = tk.Entry(window, font=("monospace", 12))
enterDirector.place(x=150, y=100)

tk.Label(window, text="Year", font=("monospace", 12)).place(x=20, y=140)
enterYear = tk.Entry(window, font=("monospace", 12))
enterYear.place(x=150, y=140)

tk.Label(window, text="Rating", font=("monospace", 12)).place(x=20, y=180)
enterRating = tk.Entry(window, font=("monospace", 12))
enterRating.place(x=150, y=180)

# Create a Listbox to display movies
listbox = Listbox(window, width=60, height=10)
listbox.place(x=20, y=250)

# List to store movie IDs and titles for easy reference
movie_list = []
movie_titles = []
selected_movie = None


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


def showMovies():
    """Fetch and display movies for the entered User ID"""
    global movie_ids, movie_titles
    user_id = enterID.get()

    if user_id == "":
        messagebox.showwarning("Cannot Show Movies", "User ID is required!")
        return
    
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ma-294022275",
            database="mybase"
        )
        cursor = conn.cursor()

        # Fetch movies for the specific user
        cursor.execute("SELECT * FROM movies WHERE user_id=%s", (user_id,))
        rows = cursor.fetchall()

        # Clear the listbox before displaying new movies
        listbox.delete(0, END)
        movie_list = []
        movie_titles = []

        if rows:
            for row in rows:
                movie_info = f"{row[1]} ⎜ {row[2]} ⎜ {row[3]} ⎜ {row[4]}"
                listbox.insert(END, movie_info)
                movie_list.append(row[0]) # Store the movie ID
                movie_titles.append(row[1]) # Store the movie title
        else:
            showData.insert(END, "No movies found for the user.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def on_movie_select(event):
    """Handle movie selection from the listbox"""
    global selected_movie_id
    if showData.curselection():
        index = showData.curselection()[0] # Get the selected index
        selected_movie_id = movie_ids[index] # Get the movie ID

        enterMovieTitle.delete(0, END)
        enterMovieTitle.insert(0, movie_titles[index]) # Pre-fill the movie title

        # Optionally, fetch and pre-fill director, year, and rating
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="mybase"
            )
            cursor = conn.cursor()

            # Fetch the selected movie details
            cursor.execute("SELECT * FROM movies WHERE movie_id=%s", (selected_movie_id,))
            movie = cursor.fetchone()

            if movie:
                enterMovieTitle.delete(0, END)
                enterMovieTitle.insert(0, movie[1])

                enterDirector.delete(0, END)
                enterDirector.insert(0, movie[2])

                enterYear.delete(0, END)
                enterYear.insert(0, movie[3])

                enterRating.delete(0, END)
                enterRating.insert(0, movie[4])

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def updateMovie():
    movie_title = enterMovieTitle.get()
    movie_director = enterDirector.get()
    movie_year = enterYear.get()
    movie_rating = enterRating.get()

    if selected_movie_id is None or movie_title == "" or movie_director == "" or movie_year == "" or movie_rating == "":
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

            # Update movie data
            cursor.execute(
                "UPDATE movies SET title=%s, director=%s, year=%s, rating=%s WHERE movie_id=%s",
                (movie_title, movie_director, movie_year, movie_rating, selected_movie_id)
            )
            conn.commit()

            cursor.close()
            conn.close()

            showMovies() # Refresh the movie list

            messagebox.showinfo("Success", "Movie data updated successfully!")
            clearFields()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def deleteMovie():
    if selected_movie_id is None:
        messagebox.showwarning("Cannot Delete", "No movie selected!")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ma-294022275",
                database="mybase"
            )
            cursor = conn.cursor()

            # Delete the selected movie
            cursor.execute("DELETE FROM movies WHERE movie_id=%s", (selected_movie_id,))
            conn.commit()

            cursor.close()
            conn.close()

            showMovies() # Refresh the movie list

            messagebox.showinfo("Success", "Movie data deleted successfully!")
            clearFields()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def refreshMovieList():
    """Refresh the Listbox with the latest movie data"""
    showMovies()


def clearFields():
    """Clear all entry fields"""
    enterID.delete(0, END)
    enterMovieTitle.delete(0, END)
    enterDirector.delete(0, END)
    enterYear.delete(0, END)
    enterRating.delete(0, END)
    global selected_movie_id
    selected_movie_id = None


# Bind movie selection from the Listbox to pre-fill movie details
listbox.bind("<<ListboxSelect>>", on_movie_select)

# Add buttons to trigger actions
tk.Button(window, text="Show Movies", font=("monospace", 12), bg="grey", command=showMovies).place(x=20, y=220)
tk.Button(window, text="Update Movie", font=("monospace", 12), bg="grey", command=updateMovie).place(x=260, y=410)
tk.Button(window, text="Delete Movie", font=("monospace", 12), bg="grey", command=deleteMovie).place(x=380, y=410)
tk.Button(window, text="Refresh List", font=("monospace", 12), bg="grey", command=refreshMovieList).place(x=500, y=410)

# Run the main loop
window.mainloop()

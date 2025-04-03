# Description: A simple library manager app to manage your personal library.
import streamlit as st
import json
import os

# File path to store data
FILE_PATH = 'library.json'

# Load library data from file
def load_library():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

# Save library data to file
def save_library(library):
    with open(FILE_PATH, 'w') as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

# Function to add a book
def add_book():
    st.subheader("📚 Add a New Book")
    title = st.text_input("Enter the book title")
    author = st.text_input("Enter the author")
    year = st.number_input("Enter the publication year", min_value=0, format="%d")
    genre = st.text_input("Enter the genre")
    read_status = st.radio("Have you read this book?", ("Yes", "No"))
    
    if st.button("Add Book"):
        if title and author and year and genre:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": True if read_status == "Yes" else False
            }
            library.append(book)
            save_library(library)
            st.success(f"'{title}' by {author} added successfully!")
        else:
            st.error("Please fill all the fields!")

# Function to remove a book
def remove_book():
    st.subheader("🗑️ Remove a Book")
    titles = [book['title'] for book in library]
    
    if not titles:
        st.warning("No books available to remove.")
        return
    
    book_to_remove = st.selectbox("Select book to remove", titles)
    
    if st.button("Remove Book"):
        for book in library:
            if book['title'] == book_to_remove:
                library.remove(book)
                save_library(library)
                st.success(f"'{book_to_remove}' removed successfully!")
                break

# Function to search for a book
def search_book():
    st.subheader("🔍 Search for a Book")
    search_by = st.radio("Search by:", ("Title", "Author"))
    query = st.text_input("Enter search query")

    if st.button("Search"):
        results = []
        if search_by == "Title":
            results = [book for book in library if query.lower() in book['title'].lower()]
        else:
            results = [book for book in library if query.lower() in book['author'].lower()]
        
        if results:
            for idx, book in enumerate(results, start=1):
                st.write(f"{idx}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found.")

# Function to display all books
def display_all_books():
    st.subheader("📖 All Books")
    if library:
        for idx, book in enumerate(library, start=1):
            st.write(f"{idx}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        st.info("No books available in the library.")

# Function to display statistics
def display_statistics():
    st.subheader("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    
    if total_books > 0:
        read_percentage = (read_books / total_books) * 100
    else:
        read_percentage = 0

    st.write(f"**Total Books:** {total_books}")
    st.write(f"**Percentage Read:** {read_percentage:.2f}%")

# Sidebar for Navigation
st.sidebar.title("📚 Personal Library Manager")
page = st.sidebar.radio("Go to", ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"])

# Routing
if page == "Add a Book":
    add_book()
elif page == "Remove a Book":
    remove_book()
elif page == "Search for a Book":
    search_book()
elif page == "Display All Books":
    display_all_books()
elif page == "Display Statistics":
    display_statistics()

# Save data on app close
save_library(library)
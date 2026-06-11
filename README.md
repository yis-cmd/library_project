# library project

## how to run the project

run the below commands in the terminal
step1: docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=l
ibrary_db -p 3306:3306 -v mysql-data:/var/lib/mysql -d mysql:latest
step2: python -m venv venv
step3:pip install -r requirements.txt
step4:uvicorn "main:app"

## project's directory structure

library-api/  
│  
├── app/  
│   ├── main.py  
│   ├── database/  
│   │   ├── db_connection.py  
│   │   ├── book_db.py  
│   │   └── member_db.py  
│   ├── routes/  
│   │   ├── book_routes.py  
│   │   ├── member_routes.py  
│   │   └── report_routes.py  
│   └── logs/  
│       └── app.log  
│  
├── README.md  
├── requirements.txt  
└── .gitignore

## database

### books table

column_name, type, description
id, primary key, identity
title, string max length 50, not null, book's title
author, string manlength 50, not null, book's author
genre, can only be of these valid genres ['Fiction', 'Non-Fiction', 'Science', History', 'Other'], not null, book genre
is_available: boolean, not null, is the book available
borrowed_by_member_id, number, null if is_available, the borrowing member's id

### members table

id: primary key, identity
name: string max length 50, not null, member's name
email: string max length 50, email has to be unique, not null, member's email
is_active: bool, not null, is mamber active
total_borrows: number, not null, how many books did the member borrow since his registration

## modules

### db_connection.py

#### pool

a connection pool

#### DBConnections class manages all the connecting to db

class parameters: connection_pool

function, description
initialize, initialize the pool and calls create_tables
create_tables, create the hardcoded tables
get_connection, pulls a connection and returns a DBConnection class

#### DBConnection class manages a single connection

function, description
cursor, get cursor
commit, commit the connection's changes
rollback, rollback connection changes
release, releases the connection back to the pool
__enter__, use the with statement
__exit__, exit the with statement cleanup logic

### book_db.py

#### BookDB class manages the book table

gets a db_connections as a parameter

method, caller, description
create_book(data), POST /books, INSERT into books table with defaults is_available=True borrowed_by=NULL
get_all_books(), GET /books, returns a list of all the books
get_book_by_id(id), GET /books/{id}, returns one or none book with this id
update_book(id, data), PUT /books/{id}, updates a book's data
set_available(id, val, member_id), PUT /books/{id}/return/{member_id} PUT /books/{id}/borrow/{member_id},\ update is_available and borrowed_by_member_id fields
count_total_books(), GET /reports/summary, counts the total number of books in the database
count_available_books(), GET /reports/summary, counts total number of books with is_available=true
count_borrowed_books(), GET /reports/summary, counts total number of books with is_available=false
count_by_genre(), GET /reports/books-by-genre, count total number of books in each genre
count_active_borrows_by_member(member_id), PUT /books/{id}/borrow/{member_id}, count how many books \
the member hold right now by reading the books's information

### member_db.py

### MemberDB class manages the member tables

gets a db_connections as a parameter

method, caller, description
create_member(data), POST /members, INSERT into members with defaults is_active=True total_borrows=0
get_all_members(), GET /members, return all members list
get_member_by_id(id), GET /members/{id}, returns one or none member by id
update_member(id, data), PUT /members/{id}, update a member data
deactivate_member(id), PUT /members/{id}/deactivate, updates is_active=False
activate_member(id), PUT /members/{id}/activate, set is_active=True
increment_borrows(id), PUT /books/{id}/borrow/{member_id}, raises total_borrows by one
count_active_members(), GET /reports/summary, return total count of members with is_active=true
get_top_member(), GET /reports/top-member, return the member th the highest total borrows

### config.env

holds db configurations

### config.py

passes configurations from config.env to the program

## logging

logs format asctime | level | message
logs are written on every start and end request on db changes and on error

## endpoints

### Books

method, endpoint, description
POST,/books, create book
GET,/books, get all books
GET,/books/{id}, get book by id
PUT,/books/{id}, update book data
PUT,/books/{id}/borrow/{member_id}, borrow book
PUT,/books/{id}/return/{member_id}, return book

### Members

method, endpoint, description
POST,/members, create member
GET,/members, get all members
GET,/members/{id}, get member by id
PUT,/members/{id}, update member data
PUT,/members/{id}/deactivate, deactivate member
PUT,/members/{id}/activate, activate member

### Reports

method, endpoint, description
GET, /reports/summary, overall report
GET, /reports/books-by-genre, book by genre
GET, /reports/top-member, the most active member

overall report example
{
"total_books": 0,
"available_books": 0,
"currently_borrowed": 0,
"active_members": 0
}

book by genre example
[
    {"Genre": "Science", "COUNT": 3},
    {"Genre": "History", "COUNT": 2}
]

most active member example
{
"member_id": 1,
"borrowed": 5
}

## flow charts

the program start
DBConnections initialzing
BookDB initializing
MemberDB initializing
    |create user
        log
        insert the user
        {
        "name": "Sara Cohen",
        "email": "<sara@example.com>"
        }
        log
        return the user
    |create book
        log
        insert the user
        {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Fiction"
        }
        log
        return the user
    |borrow book
        log
        validate ids
        check book availability
        check if member active
        check member has less than three books
        change the book state to not available
        change the book borrowing id
        increase number of borrowed books for the member
        log
    |return book
        log
        validate ids
        check book is unavailable
        check book's borrowed to whom returning it
        log

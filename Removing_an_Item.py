#A dictionry represents a phone book
phone_book ={
    "John": "123-456-7890",
    "Jane": "987-654-3210",
    "Bob": "555-555-5555"
}
#removing john's contact
del phone_book["John"]

#alternatively, using Bob()
removed_number = phone_book.pop("Bob")
print(phone_book)
print("removed number :", removed_number)
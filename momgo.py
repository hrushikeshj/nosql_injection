from pymongo import MongoClient
client = MongoClient()

""""user = client.hrushi.user
a = "0763754891' || '1' =='1"
u = user.find({'$where': "function(){return this.name == '%s'}" % a})
print(list(u))
"""

books = client.books_db.books
books.insert_many([
  {"ISBN":"2123455","title":"Pet Sematary","publisher_name":"Doubleday","date":"1998-03-20"},
  {"ISBN":"3124511","title":"Fahrenheit 451","publisher_name":"Ballantine Books","date":"2021-01-01"},
  {"ISBN":"4245566","title":"The God of Small Things","publisher_name":"IndiaInk","date":"2021-01-01"},
  {"ISBN":"99123461","title":"hrushi's book","publisher_name":"hh","date": "2021-020-01"}
  ]
)

import pymongo
password = 'horimiya1234'


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
        print(type(binaryData))
    return binaryData


name = "Tomato"
img_name = "tomato.png"
img_data = convertToBinaryData("./static/images/item.png")
price = "50"
rating = "⭐⭐⭐⭐"
desc = "Red Tomato"
available = "In Stock"
extra = "Green Capsicum. Flash Sale is on. The offer is on for a limited time."

client = pymongo.MongoClient(f"mongodb+srv://admin-ritesh:horimiya1234@cluster0.cuwyw.mongodb.net/"
                             f"myFirstDatabase?retryWrites=true&w=majority")
db = client['vegesDB']
coll = db['data']
data = {
        "name": name,
        "img": img_data,
    }
# coll.insert_one(data)
# for item in coll.find({'name': name}):
#     result = item['img']
#     with open('text.png', 'wb') as file:
#         file.write(result)

# database
# db = sqlite3.connect("data.db")
# db.row_factory = sqlite3.Row
# cur = db.cursor()
# cur.execute("select * from vegetables")
# data = cur.fetchall()
# cur.execute("CREATE TABLE vegetables(id INTEGER PRIMARY KEY, name varchar(250) NOT NULL UNIQUE, "
#             "img_name varchar(250) NOT NULL UNIQUE, img_data BLOB NOT NULL,"
#             "price varchar(250) NOT NULL UNIQUE, rating varchar(250) NOT NULL UNIQUE,"
#             "description varchar(250) NOT NULL, availability varchar(250) NOT NULL, extra varchar(250) NOT NULL)")
# cur.execute(f"INSERT INTO vegetables VALUES('{len(data) + 1}', '{generate_id()}', '{name}', '{img_name}', "
#             f"'{img_data}', '{price}', '{rating}', '{desc}', '{available}', '{extra}')")
# db.commit()

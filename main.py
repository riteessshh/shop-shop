from flask import Flask, render_template, request
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)
pw = "uLQZ5t42ZZV3vSpL"


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
        # print(type(binaryData))
    return binaryData


# creating and adding the data in the database
# data
# name = "Onion"
# img_name = "onion.png"
# img_data = "./static/images/items/onion.png"
# price = "50"
# rating = "⭐⭐⭐⭐"
# desc = "Fresh Onion"
# available = "Out of Stock"
# extra = "Fresh Onion. Flash Sale is on. The offer is on for a limited time."
# name = "ginger"
# img_data = convertToBinaryData('./static/images/items/ginger.png')

# client = pymongo.MongoClient(f"mongodb+srv://demonlord:{pw}@cluster0.csrk3.mongodb.net/"
#                              f"myFirstDatabase?retryWrites=true&w=majority")
# db = client['ShopShopDB']
# coll = db['images']
# data = {
#     "name": name,
#     "img_name": img_name,
#     "img_loc": img_data,
#     "price": price,
#     "rating": rating,
#     "description": desc,
#     "availability": available,
#     "additional_info": extra,
# }
# data = {
#     "name": name,
#     "img_data": img_data,
# }
# coll.insert_one(data)


def fetchData(collection):
    dataList = []
    client = pymongo.MongoClient(f"mongodb+srv://demonlord:{pw}@cluster0.csrk3.mongodb.net/"
                                 f"myFirstDatabase?retryWrites=true&w=majority")
    db = client['ShopShopDB']
    coll = db[collection]
    for f_item in coll.find({}):
        dataList.append(f_item)
    return dataList


def fetchVeges(prod_id):
    client = pymongo.MongoClient(f"mongodb+srv://demonlord:{pw}@cluster0.csrk3.mongodb.net/"
                                 f"myFirstDatabase?retryWrites=true&w=majority")
    db = client['ShopShopDB']
    coll = db['vegesData']
    try:
        for item in coll.find({'_id': ObjectId(prod_id)}):
            print('found')
            return item
    except:
        return None


def fetchHerbs(prod_id):
    client = pymongo.MongoClient(f"mongodb+srv://demonlord:{pw}@cluster0.csrk3.mongodb.net/"
                                 f"myFirstDatabase?retryWrites=true&w=majority")
    db = client['ShopShopDB']
    coll = db['herbsData']
    try:
        for item in coll.find({'_id': ObjectId(prod_id)}):
            print('found')
            return item
    except:
        return None


try:
    file = open(f"./static/images/items/potato.png", 'rb')
    print('files founded')
except:
    print("images not found!")
    data_list = fetchData('images')
    for item in data_list:
        with open(f"./static/images/items/{item['name']}.png", 'wb') as result:
            result.write(item['img_data'])
            print(f'{item["name"]} added.')


@app.route("/", methods=['GET', 'POST'])
def home():
    veges = fetchData('vegesData')
    herbs = fetchData('herbsData')
    return render_template("index.html", veges=veges, herbs=herbs)


@app.route("/products/<prod_id>", methods=['GET', 'POST'])
def products(prod_id):
    print(prod_id)
    if request.method == 'GET':
        print('post request')
        result1 = fetchVeges(prod_id=prod_id)
        result2 = fetchHerbs(prod_id=prod_id)
        if result1 is not None:
            related = []
            veges = fetchData('vegesData')
            for v_item in veges:
                if v_item['name'] == result1['name']:
                    pass
                else:
                    related.append(v_item)
            return render_template("product.html", product=result1, related=related)
        else:
            related = []
            herbs = fetchData('herbsData')
            for h_item in herbs:
                if h_item['name'] == result2['name']:
                    pass
                else:
                    related.append(h_item)
            return render_template("product.html", product=result2, related=related)
    return render_template("product.html")


if __name__ == "__main__":
    app.run(debug=True)

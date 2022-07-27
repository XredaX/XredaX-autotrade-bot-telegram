import pymongo
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
passd = config["Telegram"]["passd"]
named = config["Telegram"]["named"]

client = pymongo.MongoClient("mongodb+srv://test:"+passd+"@cluster1.9glic.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database(named)

# client = pymongo.MongoClient('mongodb://localhost:27017')
# db = client[named]

class user():
    def findacc(collection, Username):
        collection = db[collection]
        acc = {"Username":Username}
        data = collection.find(acc)
        for dt in data:
            if dt["Username"] == Username:
                Stat = dt["Stat"]
                Limit = dt["Limit Accounts"]
                Type = dt["Account Type"]
                expiration = dt["Subscription expiration"]
                Limit1 = dt["Limit Ads"]
                return Stat, Limit, Type, expiration, Limit1

    def addapi(collection, Name, Pkey, Skey, DateCreated, Owenr):
        collection = db[collection]
        new_api = {"Name":Name, "Pkey":Pkey, "Skey":Skey, "Date Created":DateCreated, "Owenr":Owenr}
        data = collection.insert_one(new_api)
        return data

    def findapi(collection, Username):
        collection = db[collection]
        api = {"Owenr":Username}
        data = collection.find(api)
        numbersapi = collection.count_documents(api)
        return data, numbersapi

    def addorder(collection, TransactionDate, Symbol, Stat, Quantity, USDTAmount, Price, Owenr):
        collection = db[collection]
        new_order = {"Transaction Date":TransactionDate, "Symbol":Symbol, "Stat":Stat, "Quantity":Quantity, "Amount USDT":USDTAmount, "Price":Price, "Owenr":Owenr}
        data = collection.insert_one(new_order)
        return data

    def findorders(collection, Username):
        collection = db[collection]
        orders = {"Owenr":Username}
        data = collection.find(orders)
        return data

    def deleteapi(collection, Username, Name):
        collection = db[collection]
        api = {"Owenr":Username, "Name":Name}
        data = collection.find(api)
        for dt in data:
            if dt["Owenr"] == Username and dt["Name"] == Name:
                data1 = collection.find_one_and_delete(api)
                return data1

    def deleteallapi(collection, Username):
        collection = db[collection]
        api = {"Owenr":Username}
        collection.delete_many(api)

    def editapi(collection, Username, Name, new_info):
        collection = db[collection]
        api = {"Owenr":Username, "Name":Name}
        api1 = {"$set":{"Name":new_info}}
        collection.update_one(api, api1)

    def findoneapi(collection, Username, Name):
        collection = db[collection]
        api = {"Owenr":Username, "Name":Name}
        numbersapi = collection.count_documents(api)
        data = collection.find(api)
        return numbersapi, data

    def countorders(collection, Username):
        collection = db[collection]
        api = {"Owenr":Username}
        numbersapi = collection.count_documents(api)
        return numbersapi

    def insertcomment(collection, Username, Comment, Name, Date):
        collection = db[collection]
        Comment = {"Owenr":Username, "Ads":Comment, "Name":Name, "Date":Date}
        collection.insert_one(Comment)

    def countcomment(collection, Username):
        collection = db[collection]
        Comment = {"Owenr":Username}
        numbercomment = collection.count_documents(Comment)
        return numbercomment

    def findspecificcomment(collection, Username, Name):
        collection = db[collection]
        specificcomment = {"Owenr":Username, "Name":Name}
        data = collection.find(specificcomment)
        numbercomment = collection.count_documents(specificcomment)
        return data, numbercomment

    def editspecificcomment(collection, Username, Name, new_info):
        collection = db[collection]
        api = {"Owenr":Username, "Name":Name}
        api1 = {"$set":{"Ads":new_info}}
        collection.update_one(api, api1)
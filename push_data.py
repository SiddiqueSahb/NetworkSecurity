# Importing the 'os' module to interact with the operating system, such as accessing environment variables and file paths
import os

# Importing the 'sys' module, used to handle system-specific parameters and functions
import sys

# Importing the 'json' module to work with JSON data, such as reading or writing JSON files
import json

# Importing the 'load_dotenv' function from 'dotenv' to load environment variables from a .env file into the application
from dotenv import load_dotenv

# Loading environment variables from the .env file
load_dotenv()

# Retrieving the MongoDB connection string from the environment variables
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Printing the MongoDB connection string to verify its retrieval
print(MONGO_DB_URL)

# Importing the 'certifi' module, which provides a set of trusted root CA certificates for secure SSL/TLS connections
import certifi

# Using the 'where' method of 'certifi' to get the location of the CA certificates file
ca = certifi.where()

# Importing the 'pandas' library for data manipulation and analysis
import pandas as pd

# Importing the 'numpy' library for numerical operations
import numpy as np

# Importing the 'pymongo' library to interact with MongoDB databases
import pymongo
from pymongo import MongoClient

# Importing the custom exception class 'NetworkSecurityException' from the application's exception module
from networksecurity.exception.exception import NetworkSecurityException

# Importing the custom logging module to log application messages
from networksecurity.logging.logger import logging

# Defining a class named 'NetworkDataExtract' for handling data extraction operations
class NetworkDataExtract():
    def __init__(self):
        try:
            # Placeholder for initialization logic (currently no logic implemented)
            pass
        except Exception as e:
            # Catching any exception that occurs during initialization and raising a custom exception
            raise NetworkSecurityException(e, sys)
    
    def cv_to_json_converter(self,file_path):
        try:
            # Placeholder for initialization logic (currently no logic implemented)
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            # Catching any exception that occurs during initialization and raising a custom exception
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[database]  # Get the database object
            self.collection = self.database[collection]  # Get the collection object
            self.records = records
            # Debugging: Print the records before inserting
            print(self.records[0])
            # Insert the records
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
             raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = 'siddiqueasim101'
    Collection = 'NetworkData'
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
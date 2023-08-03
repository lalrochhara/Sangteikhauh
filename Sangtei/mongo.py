import logging
from Sangtei import log as LOGGER
import asyncio
import sys
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Sangtei import MONGO_DB_URI, MONGO_PORT, MONGO_DB, log
from Sangtei.confing import get_int_key, get_str_key


MONGO_PORT = get_str_key("27017")
MONGO_DB_URI = get_str_key("mongodb+srv://sangteiubot:sangteiubot@cluster0.hnd2z.mongodb.net/?retryWrites=true&w=majority")
MONGO_DB = "sangteiubot"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["sangteiubot"]

from kafka import KafkaConsumer
# from pymongo import MongoClient
from json import loads
import json


consumer = KafkaConsumer(
    'test_consumer',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
    #  enable_auto_commit=True,
     group_id='my-group',
    #  value_deserializer=lambda x: loads(x.decode('utf-8')))
    )
for message in consumer:

    print(json.loads(message.value))
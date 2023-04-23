from datetime import datetime
from random import randint
import pandas
from os import path
import logging
import uuid
import json

logging.basicConfig(level=logging.INFO)

CATS = 100
ZOMBIES = 10000
PIRATES = 1000
CATNAMES = path.join("names", "cat", "cat.csv")
HUMAN_NAMES = path.join("names", "human", "human.csv")

logging.info(f"CATNAMES: {CATNAMES}")
logging.info(f"HUMAN_NAMES: {HUMAN_NAMES}")

cats = []
zombies = []
pirates = []

cat_names = pandas.read_csv(CATNAMES, usecols=["Name"])
human_names = pandas.read_csv(HUMAN_NAMES, delimiter="\t", usecols=["I", "MName", "Count", "FName", "Count"])

# some read tests
assert cat_names.loc[1] is not None
assert human_names.loc[1] is not None

logging.info(f"Human example {human_names.loc[1].MName}")
logging.info(f"Cat example {cat_names.sample().Name}")
logging.info(f"Cat example {cat_names.loc[1].Name}")

for i in range(0, CATS-1):
    cats.append({"id":str(uuid.uuid4()), "name": cat_names.sample().Name.values[0], "age": randint(0, 20), "created": datetime.now().isoformat()})

for i in range(0, ZOMBIES-1):
    zombies.append({"id":str(uuid.uuid4()), "name": human_names.sample().MName.values[0], "age": randint(0, 80), "created": datetime.now().isoformat()})

for i in range(0, PIRATES-1):
    pirates.append({"id": str(uuid.uuid4()), "name": human_names.sample().MName.values[0], "age": randint(0, 80), "created": datetime.now().isoformat()})

logging.info(f"Generated Cats")
logging.info(cats[0])

logging.info(f"Generated Pirates")
logging.info(zombies[0])

logging.info(f"Generated Zombies")
logging.info(pirates[0])

logging.info("Saving")
json.dump(obj=cats, fp=open(path.join("data", "cats.json"), "w"), indent=1)     
json.dump(obj=pirates, fp=open(path.join("data", "pirates.json"), "w"), indent=1)     
json.dump(obj=zombies, fp=open(path.join("data", "zombies.json"), "w"), indent=1)     

logging.info("Finished generating data")
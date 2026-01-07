from bson import ObjectId
from database import (
    members_collection,
    trainers_collection,
    plans_collection
)
from models import mongo_helper

# ---------- MEMBERS ----------


async def create_member(data):
    res = await members_collection.insert_one(data)
    return mongo_helper(await members_collection.find_one({"_id": res.inserted_id}))


async def get_members():
    return [mongo_helper(m) async for m in members_collection.find()]


async def update_member(id, data):
    await members_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    return mongo_helper(await members_collection.find_one({"_id": ObjectId(id)}))


async def delete_member(id):
    return await members_collection.delete_one({"_id": ObjectId(id)})

# ---------- TRAINERS ----------


async def create_trainer(data):
    res = await trainers_collection.insert_one(data)
    return mongo_helper(await trainers_collection.find_one({"_id": res.inserted_id}))


async def get_trainers():
    return [mongo_helper(t) async for t in trainers_collection.find()]

# ---------- PLANS ----------


async def create_plan(data):
    res = await plans_collection.insert_one(data)
    return mongo_helper(await plans_collection.find_one({"_id": res.inserted_id}))


async def get_plans():
    return [mongo_helper(p) async for p in plans_collection.find()]

from fastapi import APIRouter, HTTPException
from database import member_collection
from schemas import Member, UpdateMember
from bson import ObjectId

router = APIRouter()

# CREATE


@router.post("/members")
async def create_member(member: Member):
    member_dict = member.dict()
    result = await member_collection.insert_one(member_dict)
    member_dict["id"] = str(result.inserted_id)
    return member_dict


# READ ALL


@router.get("/members")
async def get_members():
    members = []
    async for member in member_collection.find():
        member["id"] = str(member["_id"])
        del member["_id"]
        members.append(member)
    return members


# READ ONE


@router.get("/members/{id}")
async def get_member(id: str):
    member = await member_collection.find_one({"_id": ObjectId(id)})
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    member["id"] = str(member["_id"])
    del member["_id"]
    return member


# UPDATE


@router.put("/members/{id}")
async def update_member(id: str, member: UpdateMember):
    update_data = {k: v for k, v in member.dict().items() if v is not None}

    await member_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": update_data}
    )

    updated = await member_collection.find_one({"_id": ObjectId(id)})
    updated["id"] = str(updated["_id"])
    del updated["_id"]
    return updated


# DELETE


@router.delete("/members/{id}")
async def delete_member(id: str):
    await member_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Member deleted successfully"}

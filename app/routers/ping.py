from fastapi import APIRouter

router = APIRouter(
    prefix="/ping",     # must not include a final `/`
    tags=["ping"],
)

@router.get("/{uuid}")
async def ping_by_get(uuid:str):
    pass

@router.post("/{uuid}")
async def ping_by_post(uuid:str):
    pass

@router.put("/{uuid}")
async def ping_by_put(uuid:str):
    pass
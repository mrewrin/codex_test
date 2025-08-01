from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# In-memory storage for clothes items being worn
current_clothes: List[str] = []

@app.get("/clothes", summary="Get currently worn clothes")
def get_clothes() -> Dict[str, List[str]]:
    """Return the list of currently worn clothes."""
    return {"clothes": current_clothes}

@app.post("/clothes/change", summary="Change clothes completely")
def change_clothes(clothes: List[str]) -> Dict[str, List[str]]:
    """Replace all currently worn clothes with a new set."""
    global current_clothes
    current_clothes = clothes
    return {"clothes": current_clothes}

@app.patch("/clothes/partial", summary="Change some clothes items")
def change_partial(clothes: List[str]) -> Dict[str, List[str]]:
    """Replace some of the currently worn clothes with provided items."""
    global current_clothes
    for item in clothes:
        if item not in current_clothes:
            current_clothes.append(item)
    return {"clothes": current_clothes}

@app.delete("/clothes/{item}", summary="Remove a piece of clothing")
def remove_item(item: str) -> Dict[str, List[str]]:
    """Remove a single piece of clothing if present."""
    global current_clothes
    if item in current_clothes:
        current_clothes.remove(item)
    return {"clothes": current_clothes}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/trending")
async def get_trending_products():
    return {
        "labels": ["아이템1", "아이템2", "아이템3"],
        "values": [23, 45, 67]
    }

products = [
    {"name": "스마트폰", "price": 500000},
    {"name": "노트북", "price": 1200000},
    {"name": "무선 이어폰", "price": 150000},
    {"name": "스마트워치", "price": 300000},
]

@app.get("/api/search")
async def search_products(query: str):
    result = [p for p in products if query in p["name"]]
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
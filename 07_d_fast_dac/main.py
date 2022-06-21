import uvicorn
from wsgiapp import app_fastapi

if __name__ == "__main__":
    uvicorn.run(
        'main:app_fastapi',
        host="0.0.0.0",
        port=8050,
        reload=True,
        workers=2
    )

import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from educhain import generate_mcq

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.post("/generate-mcq/")
async def generate_mcq_endpoint(topic: str, level: str, num: int = 1, api_key: str = Query(...)):
    try:
        # Set the OpenAI API key from the query parameter
        os.environ["OPENAI_API_KEY"] = api_key
        
        # Call the function from your existing package
        mcqs = generate_mcq(topic, level, num=num)
            
        return mcqs
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from educhain import generate_mcq, to_csv, to_json, to_pdf

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
async def generate_mcq_endpoint(topic: str, level: str, num: int = 1, pdf_file : str = " ", json_file : str = " ", csv_file : str = " ", api_key: str = Query(...)):
    try:
        # Set the OpenAI API key from the query parameter
        os.environ["OPENAI_API_KEY"] = api_key
        
        # Call the function from your existing package
        mcqs = generate_mcq(topic, level, num=num)
        
        if pdf_file != " ":
            to_pdf(mcqs, pdf_file)
            
        if json_file != " ":
            to_json(mcqs, json_file)
            
        if csv_file != " ":
            to_csv(mcqs, csv_file)
            
        return mcqs
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
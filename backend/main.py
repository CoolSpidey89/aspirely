# backend/main.py
from fastapi import FastAPI
from routers import quiz, career, colleges, timeline, mentor, resume, resources

app = FastAPI(title="Aspirely Backend", version="1.0")

# Register Routers
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(career.router, prefix="/career", tags=["Career Paths"])
app.include_router(colleges.router, prefix="/colleges", tags=["Colleges"])
app.include_router(timeline.router, prefix="/timeline", tags=["Timeline"])
app.include_router(mentor.router, prefix="/mentor", tags=["AI Mentor"])
app.include_router(resume.router, prefix="/resume", tags=["Resume"])
app.include_router(resources.router, prefix="/resources", tags=["Resources"])

@app.get("/")
def root():
    return {"message": "Welcome to Aspirely API 🚀"}

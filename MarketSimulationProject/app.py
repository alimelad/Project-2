from fastapi import FastAPI
from pydantic import BaseModel
from tournament import Tournament

app = FastAPI()

class EnvironmentConfig(BaseModel):
    name: str
    num_buyers: int
    num_sellers: int
    token_range: list

class TournamentInput(BaseModel):
    environments: dict
    num_rounds: int

@app.post("/run_tournament/")
def run_tournament(input: TournamentInput):
    tournament = Tournament(input.environments, input.num_rounds)
    results = tournament.run()
    return {"results": results}

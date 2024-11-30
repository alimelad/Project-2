

---

### 1. **Market Environments**
**Description**: Simulates multiple market environments to test strategy robustness:
- **Features**:
  - Vary the number of buyers and sellers.
  - Token values are sampled from customizable distributions.
  - Time-limited bidding rounds enforce structured decision-making.
- **Code**:
  - `market_environment.py`: Defines the `MarketEnvironment` class, which supports environment setup, buyer/seller additions, and market simulation.
  - `tournament.py`: Manages multiple environments and runs simulations across them.

---

### 2. **Strategy Complexity**
**Description**: Implements a variety of trading strategies, from simple heuristics to adaptive behaviors.
- **Features**:
  - **Predefined Strategies**:
    - `adaptive`: Learns from past bids and asks.
    - `random_choice`: Adds randomness to decisions.
    - `value_based`: Prioritizes token reservation values.
  - **User-Submitted Strategies**: Custom strategies can be uploaded via the FastAPI interface.
- **Code**:
  - `buyer.py`: Defines the `Buyer` class with strategy-specific behavior in the `bid` method.
  - `seller.py`: Defines the `Seller` class with strategy-specific behavior in the `ask` method.
  - `app.py`: Allows users to submit and test custom strategies through the `/run_tournament/` endpoint.

---

### 3. **Metrics**
**Description**: Evaluates strategy performance using key metrics:
- **Features**:
  - **Trade Ratio**: Tracks successful trades relative to total opportunities.
  - **Profit Distribution**: Summarizes profit trends across rounds.
  - **Efficiency**: Measures realized surplus compared to theoretical maximum.
- **Code**:
  - `market_environment.py`: Calculates trade results, including total profit and trade counts, in the `summarize_results` method.
  - `tournament.py`: Collects results across all environments and compiles them for output.

---

### 4. **Behavioral Rules**
**Description**: Implements realistic trading behaviors inspired by the paper:
- **Features**:
  - **Waiting Behavior**: Mimics "stealing the deal" strategies by acting when bid/ask prices converge.
  - **Stochastic Price Adjustments**: Introduces randomness into pricing decisions.
- **Code**:
  - `buyer.py`: Implements waiting and stochastic behaviors in the `bid` method.
  - `seller.py`: Implements stochastic price adjustments in the `ask` method.

---

### 5. **Game Details**
**Description**: Adds mechanics to better simulate the dynamics of double auctions:
- **Features**:
  - **Alternating Phases**: Bid/ask and buy/sell phases alternate for realism.
  - **Token Histories**: Tracks individual token trade histories to simulate Bayesian learning.
- **Code**:
  - `market_environment.py`: Tracks token histories during simulation in `simulate_market`.
  - `buyer.py` and `seller.py`: Update historical data after each trade via the `contract` method.

---

## How to Run the Project

### 1. Install Dependencies
pip install fastapi uvicorn
2. Start the API Server

Run the FastAPI server:

uvicorn app:app --reload

3. Test the API

Navigate to the Swagger documentation at:

http://127.0.0.1:8000/docs

Example Request

Submit a POST request to /run_tournament/ with the following sample input:

{
    "environments": {
        "BaseEnv": {
            "num_buyers": 4,
            "num_sellers": 3,
            "token_range": [10, 200]
        },
        "HighPressureEnv": {
            "num_buyers": 2,
            "num_sellers": 2,
            "token_range": [50, 100]
        }
    },
    "num_rounds": 50
}
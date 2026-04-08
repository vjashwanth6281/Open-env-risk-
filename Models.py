from pydantic import BaseModel

class Action(BaseModel):
    base_premium: float
    loading_factor: float
    reinsurance_percent: float

class Observation(BaseModel):
    policies_sold: int
    claims_incurred: float
    solvency_ratio: float

class State(BaseModel):
    episode_length: int = 10
    current_step: int = 0
    total_profit: float = 0.0
    base_market_rate: float = 1000.0

def reset() -> State:
    return State()

def step(action: Action, state: State) -> tuple[Observation, State, float, bool]:
    effective_premium = action.base_premium * (1 + action.loading_factor)
    competitiveness = state.base_market_rate / effective_premium
    policies_sold = int(100 * competitiveness)
    
    expected_claims = policies_sold * state.base_market_rate * 0.8
    actual_claims = expected_claims * (1 - action.reinsurance_percent)
    
    revenue = policies_sold * effective_premium
    reinsurance_cost = revenue * action.reinsurance_percent * 1.1
    profit = revenue - actual_claims - reinsurance_cost
    
    state.total_profit += profit
    state.current_step += 1
    
    assets = max(10000.0 + state.total_profit, 100.0)
    solvency_ratio = assets / max(actual_claims, 1.0)
    
    obs = Observation(
        policies_sold=policies_sold,
        claims_incurred=actual_claims,
        solvency_ratio=solvency_ratio
    )
    
    reward = profit / 1000.0
    if solvency_ratio < 1.5:
        reward -= 50.0 
        
    done = state.current_step >= state.episode_length
    return obs, state, reward, done

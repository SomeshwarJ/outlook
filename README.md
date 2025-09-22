
1. Install backend dependencies:
```bash
pip install -r requirements.txt
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

## Usage

### CLI Interface

Run the interactive CLI:
```bash
python backend/main.py
```

### REST API

Start the FastAPI server:
```bash
python backend/api.py
```

The API will be available at `http://localhost:8001`

### React Frontend

Start the React development server:
```bash
cd frontend
npm start
```

The frontend will be available at `http://localhost:3000`

**Features:**
- Interactive chatbot in the bottom-right corner
- Natural language processing for loan requests
- Real-time offers display in responsive grid tiles
- Integration with the FastAPI backend

#### API Endpoints

- `GET /health` - Health check
- `POST /process_loan` - Process loan application
- `GET /offers` - Get all stored loan offers (including rejected ones)

#### Example API Request

```bash
curl -X POST "http://localhost:8001/process_loan" \
     -H "Content-Type: application/json" \
     -d '{
       "amount": 500000,
       "duration": 36,
       "purpose": "coal mining operations"
     }'
```

#### Example API Response

```json
{
  "selected_bank": "bank_2",
  "total_score": 0.772,
  "carbon_adjusted_rate": 0.081,
  "amount_approved": 500000,
  "interest_rate": 0.09,
  "repayment_period": 36,
  "score_breakdown": {...},
  "reasoning": "...",
  "all_offers_comparison": [...]
}
```

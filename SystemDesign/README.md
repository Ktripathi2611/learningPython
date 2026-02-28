# System Design Assignment

Three mini-projects demonstrating core system design concepts using **Python + Flask**.

## Project Structure

```
SystemDesign/
├── requirements.txt
├── README.md
├── task1_url_shortener/
│   └── app.py            # URL Shortener (Flask + SQLite + Base62)
├── task2_rate_limiter/
│   └── app.py            # Rate Limiter (sliding-window, in-memory)
└── task3_load_balancer/
    ├── server1.py         # Mock backend server 1 (port 5001)
    ├── server2.py         # Mock backend server 2 (port 5002)
    ├── server3.py         # Mock backend server 3 (port 5003)
    └── load_balancer.py   # Round-robin load balancer (port 5000)
```

## Setup

```bash
pip install -r requirements.txt
```

---

## Task 1 – URL Shortener Lite

**Concepts:** API design, Data storage (SQLite), Base62 encoding

```bash
python task1_url_shortener/app.py
```

### Test with curl

```bash
# Shorten a URL
curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" -d "{\"url\": \"https://www.google.com\"}"

# Redirect (use the short_id from the response above)
curl -L http://localhost:5000/b
```

---

## Task 2 – Rate Limiter Mini

**Concepts:** Rate limiting, Sliding-window algorithm, Request tracking

```bash
python task2_rate_limiter/app.py
```

### Test with curl

```bash
# Send 6 rapid requests — the 6th should return 429
curl http://localhost:5001/data
curl http://localhost:5001/data
curl http://localhost:5001/data
curl http://localhost:5001/data
curl http://localhost:5001/data
curl http://localhost:5001/data   # → 429 Too Many Requests
```

---

## Task 3 – Load Balancer Simulation

**Concepts:** Load balancing, Round-robin algorithm

### Start backend servers (each in a separate terminal)

```bash
python task3_load_balancer/server1.py
python task3_load_balancer/server2.py
python task3_load_balancer/server3.py
```

### Start the load balancer

```bash
python task3_load_balancer/load_balancer.py
```

### Test round-robin distribution

```bash
curl http://localhost:5000/
curl http://localhost:5000/
curl http://localhost:5000/
curl http://localhost:5000/
curl http://localhost:5000/
curl http://localhost:5000/
# Expected output cycles: Server 1 → Server 2 → Server 3 → Server 1 → ...
```

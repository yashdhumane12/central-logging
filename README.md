# 📋 Central Logging — Loki + Promtail + Grafana

Find any failing request from any service without SSH-ing into boxes. All logs centralized in Loki, searchable via Grafana.

## Architecture
```
app-one logs ─┐
              ├→ Promtail (collector) → Loki (storage) → Grafana (query UI)
app-two logs ─┘
```

## Quick Start
```bash
docker compose up -d --build
```
Open Grafana: http://localhost:3000 (admin / admin123)

## Generate logs to explore
```bash
# Normal requests
curl http://localhost:5001/
curl http://localhost:5001/process

# Errors from app-one
curl http://localhost:5001/error

# Slow response from app-two
curl http://localhost:5002/slow

# Crash app-two
curl http://localhost:5002/crash
```

## Loki queries in Grafana

Go to Explore tab, select Loki datasource:

```logql
# All logs from app-one
{container="app-one"}

# Only errors across all services
{service=~"app-one|app-two"} |= "ERROR"

# Count errors per service in last 5m
sum by (service) (count_over_time({service=~"app.*"} |= "error" [5m]))

# Find slow requests
{container="app-two"} |= "slow"

# Parse JSON and filter by level
{service="app-one"} | json | level="ERROR"
```

## Key learning
- Promtail reads Docker container logs via Docker socket
- Labels (container, service, level) make filtering fast
- No SSH needed — find any error with a LogQL query

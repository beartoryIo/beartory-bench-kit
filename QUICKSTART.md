# Quickstart

## Requirements

- Python 3.10+ ;
- no external packages are required for the dry-run.

## Validate the kit without using quota

```bash
python3 runners/dry_run.py --cases cases/baseline-v1/cases.jsonl
```

The command returns a JSON summary and makes no network calls.

## Real execution

The kit provides no credentials or default provider adapter. Create an adapter outside this repository that reads secrets from your environment's secret manager. Add a budget, a maximum call count, and a checkpoint before any paid call.


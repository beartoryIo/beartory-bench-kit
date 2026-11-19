# Beartory Bench Kit

Public, anonymized kit for reproducing model and agent evaluations.

## Objectifs

- provide a `dry-run` mode with no network calls or secrets;
- document the five public benchmark references used by Bench Core;
- separate cases, scoring, and FinOps metrics;
- let everyone use their own models and credentials locally.

The kit contains no private data, production results, or access keys.

## Public references

Voir [`references/benchmarks.md`](references/benchmarks.md).

## Quick start

```bash
python3 runners/dry_run.py --cases cases/baseline-v1/cases.jsonl
```

The dry-run validates the cases and prints the planned calls. It contacts no provider.

For a real run, write your own local adapter. Never put secrets in repository files, arguments, or logs.

## Structure

- `cases/`: synthetic and anonymized cases;
- `references/`: public sources and licensing notes;
- `runners/`: secret-free runners, including the dry-run;
- `evaluation/`: rubrics and result schemas;
- `finops/`: metrics schema and calculations;
- `reports/`: synthetic examples, never private data.

## Status

Version 0.1 — demonstration and reproducibility kit. Example results are synthetic and are not published measurements.

## Security

Lire [`SECURITY.md`](SECURITY.md) avant toute exécution réelle.


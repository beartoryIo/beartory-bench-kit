# Beartory Bench Kit

Kit public et anonymisé pour reproduire des évaluations de modèles et d'agents.

## Objectifs

- fournir un mode `dry-run` sans appel réseau ni secret ;
- documenter les cinq références publiques utilisées par Bench Core ;
- séparer les cas, le scoring et les métriques FinOps ;
- permettre à chacun d'utiliser ses propres modèles et identifiants localement.

Le kit ne contient aucune donnée privée, aucun résultat de production et aucune clé d'accès.

## Références publiques

Voir [`references/benchmarks.md`](references/benchmarks.md).

## Démarrage

```bash
python3 runners/dry_run.py --cases cases/baseline-v1/cases.jsonl
```

Le mode dry-run valide les cas et affiche les appels prévus. Il ne contacte aucun fournisseur.

Pour une exécution réelle, l'utilisateur doit écrire son propre adaptateur local. Ne placez jamais de secret dans les fichiers du dépôt, les arguments ou les logs.

## Structure

- `cases/` : cas synthétiques et anonymisés ;
- `references/` : sources publiques et limites de licence ;
- `runners/` : runners sans secret, dont le dry-run ;
- `evaluation/` : rubriques et schémas de résultats ;
- `finops/` : schéma de métriques et calculs ;
- `reports/` : exemples synthétiques, jamais des données privées.

## Statut

Version 0.1 — kit de démonstration et de reproductibilité. Les résultats d'exemple sont synthétiques et ne constituent pas une mesure publiée.

## Sécurité

Lire [`SECURITY.md`](SECURITY.md) avant toute exécution réelle.


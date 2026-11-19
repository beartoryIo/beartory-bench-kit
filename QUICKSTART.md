# Quickstart

## Prérequis

- Python 3.10+ ;
- aucun paquet externe requis pour le dry-run.

## Vérifier le kit sans consommer de quota

```bash
python3 runners/dry_run.py --cases cases/baseline-v1/cases.jsonl
```

La commande retourne un résumé JSON et ne fait aucun appel réseau.

## Exécution réelle

Le kit ne fournit pas de credentials ni d'adaptateur fournisseur par défaut. Créez un adaptateur hors dépôt qui lit les secrets depuis le gestionnaire de secrets de votre environnement. Ajoutez un budget, un nombre maximal d'appels et un checkpoint avant tout appel payant.


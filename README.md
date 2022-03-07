# fast_api

## Description

Au cours de la formation CDTL parcours cloud, il nous a été demandé de développer une application pour l'agglomération de [Thouars](https://thouarsetmoi.fr/).

Cette application a pour but de faciliter les démarches et les procédures nécéssaires à la demande de subvention pour effectuer des travaux de rénovations d'habitations dans le but de la rendre plus écologique.

Cette application a été scindée en trois parties :

- **Propriétaire** : à destination des propriétaires souhaitant faire des travaux de rénovation.

- **Conseiller** : à destination des conseillers.

- **Architecture** : Gestion des données nécéssaires au fonctionnement des différentes parties.

## Scope

Dans ce projet notre équipe est en charge du développement de la partie Architecture. Les taches à effectuer seront la mise en place d'une base de données (Probablement MongoDB) et la gestion des communications entre les différentes parties de ce projet.

# Accès à l'API

Les branches `main` et `develop` de ce repo sont automatiquement déployées dans le cloud. Liens d'accès :
- [eq2-apiRenov_prod](https://equipe2.lp-cloud.tech/)
- [eq2-apiRenov_dev](https://equipe2-api-dev.lp-cloud.tech/)

**L'accès à l'API se fait par le biais d'une BasicAuth !**

## Interface API

Les endpoints suivants fournissent une interface :

- [/docs](https://equipe2.lp-cloud.tech/docs) permet de tester l'API avec SwaggerUI
- [/redoc](https://equipe2.lp-cloud.tech/redoc) permet de voir le format de données renvoyés sur chaque route

# Installation

Cloner le *repository* :
```bash
git clone git@github.com:projet-federateurE2/fast_api.git
cd fast_api
```

## Lancement dans Docker

Lancement du conteneur avec :
```bash
docker-compose up
```

Se rendre sur [http://localhost:8080](http://localhost:8080).

## Lancement dans un environnement Python (venv)

Création et installation d'un environnement virtuel avec :

```bash
python3 -m venv venv
pip install -r requirements.venv.txt
```

Lancement :

```bash
source venv/bin/activate
python3 run.py
```

Se rendre sur [http://localhost:8000](http://localhost:8000).


# Comment contribuer ?

Pour contribuer, voir le fichier [CONTRIBUTING.md](CONTRIBUTING.md).

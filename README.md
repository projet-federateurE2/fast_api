# fast_api

## Acteurs :
- Estéban CHACON
- Arsène REYMOND
- César RENAULT
- Théo TRIOU
- Corentin BELLEC
- Romain DELAGE

## Description

Au cours de la formation CDTL parcours cloud, il nous a été demandé de déveloper une application pour l'agglomération Thouars.

Cette application a pour but de faciliter les démarches et les procédures nécéssaires à la demande de subvention pour effectuer des travaux de rénovations d'habitations dans le but de la rendre plus écologique.

Cette application a été scindée en trois parties :

- **Propriétaire** : à destination des propriétaires souhaitant faire des travaux de renovation.

- **Conseiller** : à destination des conseillers

- **Architecture** : Gestion des données nécéssaires au fonctionnement des différentes parties

## Scope

Dans ce projet notre équipe est en charge du développement de la partie Architecture. Les taches à effectuer seront la mise en place d'une base de données (Probablement MongoDB) et la gestion des communications entre les différentes parties de ce projet.

## Liste des fonctions

- mongo
- route

# Installation

Clone the repository :
```bash
git clone git@github.com:projet-federateurE2/fast_api.git
cd fast_api
```

Build local docker image :

```bash
docker build -t fastapi .
```

Run image in container :

```bash
docker run -p 80:80 -v $(pwd):/app --name apiProjet fastapi
```

Browse [http://localhost:80](http://localhost:80).
The API is hot reloading !

# How to contribute ?

See the [CONTRIBUTING.md](CONTRIBUTING.md) file.

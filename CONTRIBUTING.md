# Comment contribuer ?

## Faire un commit

Pour les commit nous utiliserons la norme de messages suivante :

NEW: IMPERATIVE_MESSAGE

    Ajouter quelque chose de nouveau.
        exemple : NEW: Add Git ignore file

IMPROVE: IMPERATIVE_MESSAGE

    Amélioration, reécrire du code.
        exemple : IMPROVE: Remote API Function

FIX: IMPERATIVE_MESSAGE

    Corrections du code.
        exemple : FIX: Case converter

DOC: IMPERATIVE_MESSAGE

    Ajout et modification de la doc.
        exemple : DOC: API Interface Tutorial

RELEASE: IMPERATIVE_MESSAGE

    Ajout d'une nouvelle version.
        exemple : RELEASE: Version 2.0.0

TEST: IMPERATIVE_MESSAGE

    Utilisé pour les tests.
        exemple : TEST: Mock User Login/Logout


## Création de branche

Nous suivons le paterne [Git Flow](https://github.com/danielkummer/git-flow-cheatsheet).
Pour l'installation, lancer `apt install git-flow`.

![Git Workflow schema](https://wac-cdn.atlassian.com/dam/jcr:34c86360-8dea-4be4-92f7-6597d4d5bfae/02%20Feature%20branches.svg?cdnVersion=132)

Le développement se fait sur des branches `features`, créées à partir de la branche `develop`. La création de releases merge le code de la branche `develop` sur la branche `main`.

### Développement

Lors de la création d'une fonctionnalité, le nommage suit le format : feature/description.
Ce dernier est automatiquement généré par **git flow**. Le développement d'une fonctionalité se fait avec :

```bash
$ git flow feature start <name>
```

*Où <name> prend le nom de la feature. Exemple : "routeClient".*

A la fin, la commande `feature finish` ferme la branche et merge sur `develop`.

```bash
$ git flow feature finish <name>
```

### Release

Permet de construire une version finalisée sur la branche `main`, à partir de la branche `develop`.

```bash
$ git flow release
$ git flow release start <release> [<base>]
$ git flow release finish <release>
```
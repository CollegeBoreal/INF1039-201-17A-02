# GIT 

## Installation de la gestion de source

* git Client : https://git-scm.com/downloads  
* [Livre git](https://git-scm.com/book/fr/v2)

## Les premiers pas avec git

* Ouvrir la fenetre Git bash
* Creer un repertoire pour faire du developpement
```
$ mkdir Developer
```
* changer de repertoire pour faire du developpement
```
$ cd Developer
```
* Cloner votre premier repertoire git
```
$ git clone git@github.com:CollegeBoreal/INF1039-201-17A-02.git
$ cd INF1039-201-17A-02
```

## Creer son premier fichier sous git (utiliser vi)
* Creer un fichier et l'editer 
```
$ vi monfichier.md
```
* mettre le fichier en scene (add to stage)
```
$ git add monfichier.md
```
> Vérifier son status avec (doit etre vert)  
    ```
    $ git status
    ```

* donner un commentaire aux fichiers a enregistrer (commit)
```
$ git commit -m "Mon commentaire"
```
* envoyer les modifications locales au serveur github
```
$ git push origin master
```

## Metter a jour mon repertoire local (pull)
```
$ git pull 
```

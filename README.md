# API de Prédiction du Risque Cardiovasculaire



## Objectif du projet

Les maladies cardiovasculaires sont la première cause de mortalité dans le monde, responsables de 17,9 millions de décès par an.

L’objectif de ce projet est de fournir une API capable d’estimer le risque de maladie cardiovasculaire d’un patient à partir de ses données cliniques.


## Structure du projet
```
📦 project
│
├── 📁 ML
│   ├── eda_notebook.ipynb
│   ├── pipeline.py
│   └── 📁 data
│       └── data_sante.csv
│
├── 📁 models
│   └── model.py
│
├── 📁 tests
│   └── test_main.py
│
├── database.py
├── main.py
├── requirements.txt
└── README.md
```


---

## Installation

1. Cloner le dépôt GitHub :  

```shell
    git clone https://github.com/codehass/ml-health-api.git
    cd project
```

2. Créer un environnement virtuel :

 - Linux / Mac :
```shell
    python -m venv venv
    source venv/bin/activate
```
 - Windows :
```shell
    python -m venv venv
    venv\Scripts\activate
```

3. Installer les dépendances :

```shell
    pip install -r requirements.txt
```

4. Lancer l’API en mode développement :

```shell
    uvicorn main:app --reload
```

 - L’API sera accessible à l’adresse : http://127.0.0.1:8000

 - Documentation interactive Swagger : http://127.0.0.1:8000/docs

Astuce : Le paramètre --reload permet à l’API de se mettre à jour automatiquement à chaque modification du code, très pratique pour le développement.


## 🧠 Partie machine learning 
### Etapes principales :
 1- Chargement du dataset data_sante.csv

 2- Nettoyage et transformation des données (catégorielles / numériques)

 3- Séparation en X (features) et y (target)

 4-Création d’un Pipeline Scikit-learn

 5-Entraînement et sauvegarde du modèle avec joblib.dump()

 6- (Bonus) Optimisation des hyperparamètres via GridSearchCV

 7- Intégration du modèle dans FastAPI → endpoint /predict_risk

 ## 📊 Évaluation du modèle
 Deux modèles ont été testés pour la prédiction :

| Modèle                 | Accuracy | Precision | Recall | F1-Score |
| ---------------------- | -------- | --------- | ------ | -------- |
| RandomForestClassifier | 0.9811   | 0.9817    | 0.9877 | 0.9847   |
| KNeighborsClassifier   | 0.8447   | 0.9013    | 0.8405 | 0.8698   |

==> RandomForestClassifier a été retenu pour l’intégration dans l’API grâce à ses meilleures performances globales.

## 🧩 Endpoints FastAPI

| Méthode  | Endpoint        | Description                                     |
| -------- | --------------- | ----------------------------------------------- |
| **POST** | `/patients`     | Ajouter un nouveau patient                      |
| **GET**  | `/patients`     | Lister tous les patients enregistrés            |
| **Get**  | `/patient{id}`  | Récupère un patient par id                      |
| **Get**  | `/predict_risk` | Prédire le risque cardiovasculaire d’un patient |


## 🧪 Tests Unitaires

Les tests sont réalisés avec pytest et TestClient de FastAPI.
Ils permettent de vérifier que les endpoints fonctionnent correctement, notamment /predict_risk.

Lancer les tests :
```shell
    pytest
```

## 🗃️ Base de données

  - SQLite utilisée pour stocker les informations des patients.

  - Gérée via SQLAlchemy.

  - Modèles définis dans models/model.py.

## 📘 Documentation

 - Documentation interactive générée automatiquement par Swagger :
 ```shell
      http://127.0.0.1:8000/docs
```

## 🧩 Outils utilisés

 - FastAPI – Framework web rapide et moderne

 - SQLite – Base de données légère et intégrée

 - SQLAlchemy – ORM pour interagir avec la base

 - Scikit-learn – Entraînement du modèle ML

 - Pydantic – Validation des données d’entrée

 - Pytest – Tests unitaires

 - Swagger UI – Documentation automatique



 ## 🧠 Modalités pédagogiques

 - Projet réalisé en binôme favorisant la collaboration et la répartition des rôles.

 - Gestion des versions avec Git & Gitflow.

 - Suivi du planning sur Jira.

 - Durée du projet : 5 jours — du 27/10/2025 au 31/10/2025.


 ## Contributeurs

 El Ouardy Hassan

 El Hidari Nouhayla
# 🗣️Système de Commande Restaurant avec Reconnaissance Vocale

Ce projet permet de prendre des commandes vocales dans un restaurant et de les traiter avec l'IA Mistral pour une meilleure interaction avec les clients.

## Prérequis

- Un compte GitHub avec GitHub Codespaces activé
- Une clé API Mistral (à obtenir sur [la plateforme Mistral](https://mistral.ai))
- Python 3.x

## 📁  Structure du Projet

```
restaurant-commande/
│
├── main.py           # Code principal
├── menu.json         # Menu du restaurant
├── .env             # Configuration (clé API)
├── requirements.txt  # Dépendances Python
└── README.md        # Documentation
```

## Installation

1. Clonez ce repository :
```bash
git clone [URL_DU_REPO]
cd restaurant-commande
```

2.Configurer l'API Mistral :
```
MISTRAL_API_KEY=votre_clé_api_ici
```
➤ Option 1 : Ajouter directement dans .env
Créez un fichier .env et ajoutez votre clé API :

ini
Copier
Modifier
MISTRAL_API_KEY=votre_clé_api_ici

➤ Option 2 : Utiliser les secrets GitHub Codespaces
Ajoutez votre clé API en tant que secret :

Allez sur GitHub → Votre repo → ⚙️ Settings
Sélectionnez Secrets and variables → Codespaces
Cliquez sur Ajouter un secret
Remplissez :
Nom : MISTRAL_API_KEY
Valeur : votre clé API



3. Créez le fichier `requirements.txt` :
```
python-dotenv
SpeechRecognition
pyaudio
mistralai
```

4. Installez les dépendances système :
```bash
sudo apt-get update
sudo apt-get install python3-dev portaudio19-dev python3-pyaudio
```

5. Installez les dépendances Python :
```bash
pip install -r requirements.txt
```

## Configuration

1. Vérifiez que le fichier `menu.json` est présent et contient votre menu :
```json
{
    "entrées": {
        "Soupe du jour": 5,
        "Salade de chèvre chaud": 7
    },
    "plats principaux": {
        "Filet de saumon, riz sauvage": 15,
        "Poulet rôti, pommes de terre": 14,
        "Lasagnes maison": 12
    },
    "desserts": {
        "Mousse au chocolat": 6,
        "Tarte aux pommes": 5
    }
}
```

2. Assurez-vous que votre clé API Mistral est correctement configurée dans le fichier `.env`

## Utilisation

1. Lancez le programme :
```bash
python main.py
```

2. Le menu s'affichera et le système attendra votre commande vocale

3. Parlez clairement pour commander vos plats

4. Dites "quitter" pour arrêter le programme

## Notes importantes

- La reconnaissance vocale nécessite un microphone fonctionnel
- Une connexion Internet est requise pour la reconnaissance vocale et l'API Mistral
- Le système est configuré pour reconnaître le français

## Dépannage

Si vous rencontrez des erreurs lors de l'installation de PyAudio, assurez-vous d'avoir bien installé toutes les dépendances système nécessaires (étape 4 de l'installation).

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

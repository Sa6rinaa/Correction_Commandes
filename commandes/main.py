import os
import json

import requests



MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def verifier_api_key():
    """Vérifie si la clé API Mistral est valide."""
    if not MISTRAL_API_KEY:
        print("\n❌ Erreur : Clé API Mistral non trouvée")
        print("➡️  Créez un fichier .env avec votre clé :")
        print("   MISTRAL_API_KEY=votre_clé_api_ici")
        return False
    
    try:
        # Test simple de l'API
        headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "mistral-tiny",
            "messages": [{"role": "user", "content": "Test de connexion"}]
        }
        
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        
        print("✅ Connexion à l'API Mistral réussie!")
        return True
    except Exception as e:
        print(f"\n❌ Erreur de connexion à l'API : {str(e)}")
        return False

def charger_menu(fichier='menu.json'):
    """Charge le menu depuis un fichier JSON."""
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            menu = json.load(f)
            print("✅ Menu chargé avec succès!")
            return menu
    except FileNotFoundError:
        print(f"❌ Erreur: Le fichier {fichier} est introuvable.")
        return None

def afficher_menu(menu):
    """Affiche le menu formaté."""
    print("\n📋 === MENU DU JOUR ===")
    for categorie, plats in menu.items():
        print(f"\n{categorie.upper()}:")
        for plat, prix in plats.items():
            print(f"  - {plat}: {prix}€")
    print("\n==================")

def traiter_commande(commande, menu):
    """Traite la commande avec l'API Mistral."""
    try:
        headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }
        
        print("🤖 Traitement de votre commande en cours...")
        
        prompt = f"""
        Voici le menu disponible:
        {json.dumps(menu, indent=2, ensure_ascii=False)}
        
        Commande du client: {commande}
        
        En tant que serveur, veuillez:
        1. Vérifier si les plats demandés sont bien au menu
        2. Calculer le total
        3. Donner une réponse naturelle et professionnelle en français, avec:
           - Confirmation des plats commandés
           - Prix de chaque plat
           - Total de la commande
        """
        
        data = {
            "model": "mistral-tiny",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        
        return response.json()["choices"][0]["message"]["content"]
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement: {str(e)}")
        return "Désolé, une erreur est survenue lors du traitement de votre commande."

def prendre_commande():
    """Prend la commande via entrée texte."""
    try:
        commande = input("\n🗣️  Entrez votre commande (ou 'quitter' pour arrêter) : ")
        return commande.strip()
    except Exception as e:
        print(f"❌ Erreur lors de la saisie: {str(e)}")
        return None

def main():
    """Fonction principale."""
    print("\n🍽️  Système de Commande Restaurant")
    print("=================================")
    
    # Vérifier la clé API
    if not verifier_api_key():
        return
    
    menu = None
    
    # Boucle principale
    while True:
        try:
            if not menu:
                charger = input("Voulez-vous charger le menu ? (oui/non) : ")
                if charger.lower() == "oui":
                    menu = charger_menu()
                    if not menu:
                        print("❌ Impossible de continuer sans menu valide.")
                        return
            
            if menu:
                afficher_menu(menu)
            
            # Prendre la commande
            commande = prendre_commande()
            
            if not commande:
                continue
                
            if commande.lower() in ['quitter', 'stop', 'fin']:
                print("\n👋 Au revoir!")
                break
            
            # Traiter la commande
            resultat = traiter_commande(commande, menu)
            print("\n📝 Confirmation de la commande:")
            print(resultat)
            print("\n" + "="*50)
            
        except KeyboardInterrupt:
            print("\n👋 Programme arrêté par l'utilisateur")
            break
        except Exception as e:
            print(f"\n❌ Erreur inattendue: {str(e)}")

if __name__ == "__main__":
    main()

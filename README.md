# Guide d'utilisation
Ce script Python permet de réaliser plusieurs attaques sur un réseau SDN à l'aide du contrôleur ONOS.
- usurpation d'un controleur
- usurpation d'un equipement
- empoisonnement de la memoire de gestion des equipement par le controleur 


## Prérequis
Avant d'exécuter ce script, assurez-vous d'avoir les éléments suivants installés :

- Python 3.x
- Scapy
- ONOS Controller

## Installation des dépendances

Pour installer Scapy, vous pouvez utiliser pip :
```bash
pip install scapy

##Comment exécuter le script
avec la commande suivante, vous pouvez obtenir de l'aide sur comment executer le script
python3 att.py --help

##Attaque de port stealing
python3 att.py -I <interface> -s <ip_cible>

##Attaque d'empoisonnement de la mémoire de gestion des équipements du contrôleur SDN
python3 att.py -I <interface> -c <nombre_de_faux_equipements>

##Attaque de contrôleur stealing
python3 att.py -I <interface> -s <ip_controleur_cible>

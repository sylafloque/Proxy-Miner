# Proxy-Miner
SImple proxy 
Ce code crée un proxy qui écoute sur toutes les interfaces sur le port 5678. Lorsqu'un mineur se connecte, le proxy établit une connexion avec le daemon sur l'hôte et le port spécifiés (localhost:1234 dans cet exemple) et redirige toutes les données envoyées par le mineur vers le daemon, et vice versa. Le code gère également la fermeture des sockets.

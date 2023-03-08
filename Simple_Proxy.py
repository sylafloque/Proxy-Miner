import socket

# Paramètres de connexion du daemon
daemon_host = 'localhost'
daemon_port = 1234

# Paramètres de connexion du proxy
proxy_host = '0.0.0.0'  # Toutes les interfaces
proxy_port = 5678

# Création d'une socket pour écouter les connexions des mineurs
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.bind((proxy_host, proxy_port))
proxy_socket.listen()

print(f'Le proxy écoute sur {proxy_host}:{proxy_port}...')

# Boucle principale : accepter les connexions des mineurs et les rediriger vers le daemon
while True:
    miner_socket, miner_address = proxy_socket.accept()
    print(f'Le proxy a reçu une connexion du mineur {miner_address}')

    # Connexion au daemon
    daemon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    daemon_socket.connect((daemon_host, daemon_port))
    print(f'Le proxy se connecte au daemon {daemon_host}:{daemon_port}')

    # Redirection de la connexion du mineur vers le daemon
    while True:
        data = miner_socket.recv(4096)
        if not data:
            break
        daemon_socket.sendall(data)
        response = daemon_socket.recv(4096)
        miner_socket.sendall(response)

    # Fermeture des sockets
    miner_socket.close()
    daemon_socket.close()

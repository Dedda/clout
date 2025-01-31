sudo apt update
sudo apt install python3 python3-jinja2 python3-yaml docker.io docker-compose
sudo usermod -aG docker $(whoami)
sudo newgrp docker


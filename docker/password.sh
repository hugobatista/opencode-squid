docker exec squid apt-get update
docker exec squid apt-get install -y apache2-utils
docker exec squid htpasswd -bc /etc/squid/passwords user password

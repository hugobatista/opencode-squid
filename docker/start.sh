docker run -d \
  --name squid \
  --restart always \
  -p 3128:3128 \
  -v ./squid.conf:/etc/squid/squid.conf:Z \
  -v ./passwords:/etc/squid/passwords:Z \
  ubuntu/squid:latest

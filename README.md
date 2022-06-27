# KX Problem solving exercise Balint Feher

## What is this?
This is a distributed HTTP service written in Python, has a loadbalancer and multiple worker nodes. With HTTP GET queries to the following paths a JSON will be served:
1) **/data** Picks a random backend server and serves stored data
2) **/status** Checks all the backend servers and returns the statuses of those
3) If no backend servers are available it returns a HTTP 503
4) If you ask for a non existing path, it returns a HTTP 404

### How to run, ninja way
Via docker compose and docker hub you can easily run the environment
1) **docker compose pull** - Downloads the prebuilt x86 containers
2) **docker compose up -d** - It creates the network and instaces from the previously downloaded docker images
3) **docker compose down** - Stops the services and cleans up

### How to run, build your own images
If you want you can build your own containers, both app has a Dockerfile just use the following method:
** docker build -t <your tag> .**
*In this case don't forget to set your tags in docker-compose.yaml before deployment!

### Docker compose hints
You can control the worker instance names via environment variables in docker-compose, if you wish even the quantity can be set too, just create new sections for app.
Backend node pool can be set via environment variables, just create a list and use space as a delimiter  
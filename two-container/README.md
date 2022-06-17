# Usage
### To Communicate two isolated containers, we will use a user defined birdge network.
**Create a bridge network, named *fn*.**

`
docker network create -d bridge fn
`

**Build node1 image** *pwd must be ./app1*

`
docker build -t node1 .
`

**Build flask1 image** *pwd must be ./app2*

`
docker build -t flask1 .
`

**Create a container from node1 image with a hostname and add to the bridge network**

`
docker run -d --name express1 -p 8080:8080 --network fn --hostname nodeexp node1
`

**Create a container from flask1 image add it to the bridge network**

`
docker run -d --name pyclient -p 3000:3000 --network fn flask1
`

**Now running from the host**

`
curl -i localhost:3000
`

*Request the pyclient app(localhost:3000) and pyclinet app will fetch from the express app through the defined bridge network(fn) using the address(nodeexp:8080) as it can't direct access(localhost:8080) and return the the result*
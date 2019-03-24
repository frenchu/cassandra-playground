# Cassandra playground

The repository contains short tutorial describing how to setup cassandra cluster on your local machine with Docker. Handy docker-compose.yaml is included, it is based on 
[examples from DataStax](https://github.com/datastax/docker-images/tree/master/example_compose_yamls).

Additionally it has some example CQL schemas and simple clients written in Python which make use of DataStax Cassandra driver.

## Setup Cassandra cluster

1. Navigate to repository root folder

1. Tweak docker-compose.yaml settings (especially memory limits for nodes)

1. Get the Cassandra Docker images from docker hub (DSE = DataStax Enterprise, one of Cassandra distributions, free of charge for development use)

        docker pull datastax/dse-server:latest
        docker pull datastax/dse-studio:latest

1. Run DSE studio (management tool) and cassandra cluster with 4 nodes (one seed node and three others)

        docker-compose up --scale node=3

    If you want to run docker containers in background (detached mode), try instead 

        docker-compose up -d --scale node=3

    Above command is similar to executing these two sets of commands, one for running the cluster

        docker run -e DS_LICENSE=accept -e JVM_EXTRA_OPTS="-Xms1g -Xmx4g" --name cassandra-node1 -d datastax/dse-server
        docker run -e DS_LICENSE=accept -e JVM_EXTRA_OPTS="-Xms1g -Xmx4g" -e SEEDS=cassandra-node1 --name cassandra-node2 --link cassandra-node1 -d datastax/dse-server 
        docker run -e DS_LICENSE=accept -e JVM_EXTRA_OPTS="-Xms1g -Xmx4g" -e SEEDS=cassandra-node1 --name cassandra-node3 --link cassandra-node1 -d datastax/dse-server
        docker run -e DS_LICENSE=accept -e JVM_EXTRA_OPTS="-Xms1g -Xmx4g" -e SEEDS=cassandra-node1 --name cassandra-node4 --link cassandra-node1 -d datastax/dse-server

    and another for running the DataStax Studio

        docker run -e DS_LICENSE=accept -e JVM_EXTRA_OPTS="-Xms512m -Xmx1g" --link cassandra-node1 -p 9091:9091 --name dse-studio -d datastax/dse-studio

1. Shutdown the cluster and DSE studio

        docker-compose down

## Useful commands

```bash
docker exec -it cassandra-playground_seed-node_1 nodetool status
docker exec -it cassandra-playground_seed-node_1 nodetool getendpoints shopping purchase_history 'Gdansk'
```

## Resources

- [More on cassandra docker images](https://github.com/datastax/docker-images)

- [5 min Cassandra on Docker tutorial](https://medium.com/@michaeljpr/five-minute-guide-getting-started-with-cassandra-on-docker-4ef69c710d84)

- [How to setup windows virtualization for docker](https://docs.docker.com/docker-for-windows/troubleshoot)
#!/bin/bash

init_virtual_environment()
{
    echo "call virtual env"
    virtualenv --python=python3.7 .env && source .env/bin/activate && pip install -r requirements.txt
}

init_dockers_tool()
{
    echo "init docker tool"
    cd finance_tool
    docker-compose run
    cd ..
}

start_crawl()
{
    echo "start crawl"
    cd fin_scrapy
    scrapy crawl -a tickers=GOOG,AAPL,MSFT,AMZN,FB,HP,TEAM,CSCO,INTC,CRM --nolog -o - -t json finance
    cd ..
}

create_mongo_charts()
{
    echo "create mongo charts"
    mkdir mongodb-charts
    cd mongodb-charts
    docker swarm init
    docker pull quay.io/mongodb/charts:v0.12.0
    docker run --rm quay.io/mongodb/charts:v0.12.0 charts-cli test-connection mongodb://host.docker.internal:27017
    echo "<Verified connection string URI from step 5>" | docker secret create charts-mongodb-uri -

    docker exec -it \
      $(docker container ls --filter name=_charts -q) \
      charts-cli add-user --first-name "Admin" --last-name "Admin" \
      --email "admin@admin.com" --password "123456" \
      --role "UserAdmin"

    cd ..
}

start_crawl



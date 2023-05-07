# Prompt Engineers - API Proxy Server
https://promptengineers.ai

### Run Development environment by running the following...
```bash
## Setup virutal env
python3 -m venv .venv
source env/bin/activate
pip3 install -r requirements.txt

## Run dev environment
bash scripts/dev.sh

## Run tests
bash scripts/test.sh

## Build docker image
bash scripts/build.sh

## Deploy using kubernetes and helm
bash scripts/upgrade.sh $APP_ENV $NAMESPACE $IMAGE_REPO

## Start Docker Environment
docker-compose up --build
```
docker network create gtsb

docker container run \
  -d \
  --rm \
  --name djangodb \
  --network gtsb   \
  --env MYSQL_ROOT_PASSWORD=123456 \
  --env MYSQL_DATABASE=blog \
  mysql:5.7 \
  --character-set-server=utf8

docker container run -d \
  --rm \
  --name django_blog \
  --network gtsb \
  -p 8000:8000 \
  djangowithmysql
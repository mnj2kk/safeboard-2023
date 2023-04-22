docker build -t safeboard-api .
docker run --name safeboard-api -d -p 80:80 safeboard-api
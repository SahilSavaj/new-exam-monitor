aws_service_container_name="elegant_hawking"
IMAGE_NAME="exam-monitoring/backend"
# docker push $IMAGE_NAME:latest
# docker pull $IMAGE_NAME:latest
aws_service_api_container_id=$(docker ps -aqf "name=$aws_service_container_name")
if [ ! -z "$aws_service_api_container_id" ]
then
	docker stop $aws_service_api_container_id
	docker rm $aws_service_api_container_id
	docker build -t $IMAGE_NAME .
fi
# docker run -d --name $aws_service_container_name $IMAGE_NAME:latest
docker run --name $aws_service_container_name $IMAGE_NAME:latest
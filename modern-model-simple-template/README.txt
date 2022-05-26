MODEL DEPLOYMENT STEPS

1-Copy your model into models directory.

2-Save test data into data.json file.

3-Develop and package lambda main function using development.ipynb

4-Save main.py file

5-Edit test.py file for testing main.py from terminal.

6-Run test.py file from terminal.

7-Edit requirements.txt file according to library needs.

8-Build the docker image:

	docker build --tag modern_karton_basit:latest .

9-Test your code using test.py inside the docker image.

10-Push docker image to AWS ECR (you need to create a repo on AWS if you do not already have):

	aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 423888860501.dkr.ecr.eu-central-1.amazonaws.com/modern_karton_basit
	
	docker tag modern_model_basit:latest 423888860501.dkr.ecr.eu-central-1.amazonaws.com/modern_karton_basit

	docker push 423888860501.dkr.ecr.eu-central-1.amazonaws.com/modern_karton_basit
	
11-Create or update the lambda function on AWS UI

12-Test Lambda function on AWS UI

13-Create or add API endpoint using AWS API GATEWAY.

14- Test API using Postman.

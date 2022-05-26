FROM amazon/aws-lambda-python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY ./ ./

RUN chmod -R 0777 ./models

CMD [ "main.lambda_handler"]
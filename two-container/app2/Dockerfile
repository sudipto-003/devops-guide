FROM python:3.9

WORKDIR /code
COPY ./requirments.txt /code/requirments.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirments.txt

COPY ./api /code/app

CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:3000"]
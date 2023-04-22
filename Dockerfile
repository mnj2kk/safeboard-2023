FROM python:3.11.2

WORKDIR /src

COPY ./requirements /src/requirements

RUN pip install --no-cache-dir --upgrade -r /src/requirements

COPY ./app /src/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
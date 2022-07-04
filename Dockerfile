FROM python:3.9-slim

COPY ./src /fastapi/src
COPY ./requirements.txt /fastapi/requirements.txt

WORKDIR /fastapi

RUN python -m venv venv

CMD ["source", "venv/bin/activate"]

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]
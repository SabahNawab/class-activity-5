FROM python:3.8

WORKDIR /app

COPY app.py /app/app.py
COPY pricemodel.pkl /app/pricemodel.pkl
COPY templates /app/templates
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]
FROM python:3.8.12-slim

WORKDIR /app

RUN pip install --upgrade pip && pip --no-cache-dir install numpy pandas scikit-learn flask requests

COPY ["main.py",  "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "main:app"]
# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "main:app"]
# To run : waitress-serve --listen=0.0.0.0:9696 main:app
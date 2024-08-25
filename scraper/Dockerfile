FROM python:3.9

RUN pip3 install Flask
RUN pip3 install docker

WORKDIR /app

COPY scraper.py /app/scraper.py

EXPOSE 5000
CMD ["python", "/app/scraper.py"]

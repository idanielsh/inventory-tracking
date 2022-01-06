FROM python:3.9

EXPOSE 8000

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

COPY ./app /app

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD ["./start.sh"]
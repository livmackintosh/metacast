FROM python:3.7-alpine
WORKDIR /app
ADD metacast.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_APP=metacast.py
ENTRYPOINT ["python", "-m", "flask"]
CMD ["run"]

FROM python:3.7
RUN pip install pipenv
WORKDIR /app
COPY . /app
RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]
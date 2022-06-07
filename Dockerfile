FROM python:3.9-bullseye

WORKDIR /usr/src/app

COPY dep.txt ./
RUN pip install --no-cache-dir -r dep.txt

COPY . .

EXPOSE 5000
CMD [ "python", "app.py" ]
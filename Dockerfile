FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]



# | RUN                                   | CMD                                      |
# | ------------------------------------- | ---------------------------------------- |
# | Executes while **building** the image | Executes when the **container starts**   |
# | Used to install software              | Used to start the application            |
# | Runs once during `docker build`       | Runs every time `docker run` is executed |

FROM python:3.8-alpine
COPY ./app/requirements.txt app/requirements.txt
WORKDIR /app
RUN apk add --update \ 
&& pip install --upgrade pip \ 
&& pip install -r requirements.txt \ 
&& rm -rf /var/cache/apk/*
COPY ./app/. .
EXPOSE 5057
<<<<<<< HEAD
CMD ["python","Modulus.py"]
=======
CMD ["python","modulus.py"]

>>>>>>> 41b0828ec655feba5624de84a1744a2a7c3486ac

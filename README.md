## creacion

## 1. se hace primero un sudo apt update:
bash
sudo apt update

## 2.se le instala el docker:
bash
sudo apt install docker-compose -y


## 3. se clona este repositorio en la maquina:
bash
git clone https://github.com/andresvle/exam3-teoria


## 4. Entramos a app/
bash
cd app/


## 5. Construye la imagen Docker 
bash
sudo docker build -t web:01 .



## 6. se ejecuta el Contenedor:

bash
sudo docker run -d -p 80:80 web:01


## 7. Verificamos si esto si se creo

bash
sudo docker ps

## 8. se accede a la web con la ip publica 

bash
http://ip publica



FROM ubuntu/apache2:latest
ARG PORT=8081
RUN a2enmod rewrite
RUN sed -i "s/^Listen 80/Listen $PORT/" /etc/apache2/ports.conf
RUN sed -i "s/^<VirtualHost \*:80>/<VirtualHost *:$PORT>/" /etc/apache2/sites-available/000-default.conf
EXPOSE $PORT

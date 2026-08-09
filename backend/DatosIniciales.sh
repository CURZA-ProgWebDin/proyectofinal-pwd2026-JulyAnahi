#!/bin/sh
echo "Asegurando que este lista la base"
while ! nc -z db 5432; do
    sleep 1
done

echo "base de datos conectada con exito"

echo "aplicando migraciones"
flask db upgrade

echo "Ejecutando migracion inicial"
python seed.py

echo "Iniciando Flask..."
python run.py
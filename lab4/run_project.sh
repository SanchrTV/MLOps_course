#!/bin/bash

# Остановить скрипт при любой ошибке
set -e

# Проверка наличия DVC
if ! command -v dvc &> /dev/null
then
    echo "DVC could not be found, please install it before running this script."
    exit 1
fi

# Инициализация DVC, если еще не инициализирована
if [ ! -d ".dvc" ]; then
    dvc init
    git commit -m "Initialize DVC"
fi

# Добавление Google Drive как удаленного хранилища DVC, если оно еще не добавлено
if ! dvc remote list | grep -q 'myremote'; then
    dvc remote add -d myremote gdrive://1FeLT99BHVSAS0DhIi1YAqP82KOLkaltk
else
    echo "Remote 'myremote' already exists. Skipping remote addition."
fi

# Запуск скрипта Python для создания датасетов
python /Users/alex/Desktop/Studies/MLOps_course/lab4/prepare_data.py

# Удаление файла из Git если он уже отслеживается, и добавление его в DVC
for version in titanic_v1.csv titanic_v2.csv titanic_v3.csv
do
    if git ls-files --error-unmatch $version > /dev/null 2>&1; then
        git rm -r --cached $version
        git commit -m "Stop tracking $version"
    fi
    dvc add $version
done

git add /Users/alex/Desktop/Studies/MLOps_course/lab4/prepare_data.py .gitignore
git commit -m "Add script and .gitignore"
dvc push

# Переключение между версиями
dvc checkout titanic_v1.csv.dvc
dvc checkout titanic_v2.csv.dvc
dvc checkout titanic_v3.csv.dvc

echo "Project setup and data versions have been handled successfully."

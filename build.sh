#!/usr/bin/env bash
# exit on error
set -o errexit

# تثبيت المكتبات على السيرفر
pip install -r requirements.txt

# تجميع ملفات الاستايل والثوابت
python manage.py collectstatic --no-input

# ترحيل وتأكيد قاعدة البيانات على السيرفر
python manage.py migrate

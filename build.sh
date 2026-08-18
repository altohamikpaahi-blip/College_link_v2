#!/usr/bin/env bash
# exit on error
set -o errexit

# تثبيت المكتبات على السيرفر
pip install -r requirements.txt

# تجميع وتخزين ملفات الاستايل والثوابت لـ Tailwind CSS
python manage.py collectstatic --no-input

# ترحيل وتأكيد جداول قاعدة البيانات السحابية
python manage.py migrate

# تهيئة حساب الآدمن (altohami) بذكاء وأمان سواء كان موجوداً أو جديداً لتفادي أي انهيار في البناء
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u, created = User.objects.get_or_create(username='altohami', defaults={'email': 'admin@email.com', 'is_superuser': True, 'is_staff': True}); u.set_password('univ_pass_2026'); u.is_superuser = True; u.is_staff = True; u.save(); print('تمت تهيئة حساب الآدمن بنجاح')"

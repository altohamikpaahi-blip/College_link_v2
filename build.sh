#!/usr/bin/env bash
# exit on error
set -o errexit

# تثبيت المكتبات على السيرفر
pip install -r requirements.txt

# تجميع وتخزين ملفات الاستايل والثوابت لـ Tailwind CSS
python manage.py collectstatic --no-input

# ترحيل وتأكيد جداول قاعدة البيانات السحابية
python manage.py migrate

# إعادة تعيين كلمة المرور للمستخدم altohami تلقائياً وتحديثها في قاعدة البيانات
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.get(username='eltohami'); u.set_password('univ_pass_2026'); u.save(); print('تمت إعادة تعيين كلمة المرور بنجاح')"

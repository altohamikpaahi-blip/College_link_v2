from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    attachment = forms.FileField(required=False, label="إرفاق ملف (اختياري)")

    class Meta:
        model = Document
        fields = ['recipient_college', 'recipient_user', 'title', 'content']
        widgets = {
            'recipient_college': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'recipient_user': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'title': forms.TextInput(attrs={'placeholder': 'مثال: طلب تنسيق لقاء علمي مشترك', 'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'content': forms.Textarea(attrs={'rows': 6, 'placeholder': 'اكتب نص الخطاب هنا...', 'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }

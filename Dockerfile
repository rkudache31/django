FROM rkudache31/django_web
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD [ "python","./homefood/manage.py","runserver","0.0.0.0:8000" ]

FROM rkudache31/djangoweb:v1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD [ "python","./homefood/manage.py","runserver","0.0.0.0:8000" ]


FROM python:3.6.4

RUN pip3 install tensorflow-cpu==2.5.0
RUN pip3 install DeepFace==0.0.50
RUN pip3 install Pillow
RUN pip3 install werkzeug
RUN pip3 install Flask
RUN pip3 install requests
RUN pip3 install keras
RUN pip3 install jsonify

CMD ["python", "app.py"]

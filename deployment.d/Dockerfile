#--AUTOMATE-BUILD--
#Deploy image for RandFIng
FROM python:3.12.4

WORKDIR /RandFIng

ENV PYTHONUNBUFFERED=1
ENV RANDFING_KEY=""
ENV RANDFING_DEBUG=True
ENV RANDFING_DB=""
ENV RANDFING_USER=""
ENV RANDFING_PASS=""

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#RUN chmod +x simple_start.sh
RUN ["chmod", "+x", "deployment.d/simple_start.sh"]

EXPOSE 8150

CMD ["deployment.d/simple_start.sh"]

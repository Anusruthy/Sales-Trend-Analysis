FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --default-timeout=100 --retries=10 --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "sale_trend_view.py"]
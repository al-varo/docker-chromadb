FROM python:3.9

WORKDIR /app

# Salin file proyek ke dalam container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua skrip ke dalam container
COPY scripts/ /app/scripts/

# Jalankan skrip utama saat container dimulai
CMD ["python", "/app/scripts/query_ollama.py"]

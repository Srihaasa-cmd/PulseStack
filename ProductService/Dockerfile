#builder stage 
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Final Stage 
FROM python:3.12-slim 
WORKDIR /app
COPY --from=builder /app /app
RUN pip install --no-cache-dir -r requirements.txt
COPy . . 
RUN useradd -m appuser
USER appuser
EXPOSE 5002
CMD ["python","app.py"]
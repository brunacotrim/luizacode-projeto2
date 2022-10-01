FROM python:3.10.5-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "shopping_cart.app:app", "--host", "0.0.0.0", "--port", "8000"]
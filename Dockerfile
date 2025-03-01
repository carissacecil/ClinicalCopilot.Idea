FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl gcc python3-dev

# Install Poetry using pip
RUN pip install poetry

# Set up working directory
WORKDIR /app

# Copy all code first
COPY . .

# Configure poetry
RUN poetry config virtualenvs.create false

# Generate a fresh lock file and then install dependencies
RUN poetry lock && \
    poetry install --without dev --no-interaction --no-ansi

# Run the application
CMD ["poetry", "run", "uvicorn", "clinical_mind_sidekick.main:app", "--host", "0.0.0.0", "--port", "8000"]
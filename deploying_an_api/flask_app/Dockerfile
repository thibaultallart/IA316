# Inherit from Python 3.6 image
FROM python:3.6

# Update pip, setuptools, and wheel to ensure that we have the latest versions.
RUN pip --no-cache-dir --disable-pip-version-check install --upgrade pip setuptools wheel

# Set a working directory
WORKDIR /usr/src

# Copy requirements
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# Copy current folder
COPY . .

# Run python code
CMD python app.py
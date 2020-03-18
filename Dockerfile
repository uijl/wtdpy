# Start with docker image from anaconda
FROM continuumio/miniconda3

# Then install rest via pip
RUN pip install --upgrade pip

ADD . /wtdpy
WORKDIR /wtdpy

# Install the application
RUN pip install -e .

# expose port 5000
EXPOSE 5000
# Serve on port 5000
CMD wtdpy serve --port 5000

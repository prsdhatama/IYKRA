FROM python:3.9


# Install nano editor just in case we need to write some file
RUN apt-get update 
RUN apt-get -y install nano 

# Install the python dependencies
COPY requirements.txt ./

# Read the requirement file and installing the package without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the folder into this specific path
WORKDIR /usr/src/app
COPY . .

# Export google application credentials to have the necessary permission
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/feisty-outlet-362916-29300cba76c1.json"

CMD [ "python", "/usr/src/app/practice_case1_using_python.py" ]
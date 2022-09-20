FROM python:3.9

# Install the python dependencies
COPY requirements.txt ./

# Read the requirement file and installing the package without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the folder into this specific path
WORKDIR /usr/src/app

# Copy all folder to the images folder
COPY . .

# Export google application credentials to have the necessary permission
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/feisty-outlet-362916-29300cba76c1.json"

# Running the python file
CMD [ "python", "/usr/src/app/practice-case1_usingdocker_frominternet.py" ]
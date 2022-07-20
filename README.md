# Base Flask Backend App
This project is intended as a skeletal flask-based backend, which should be used with an SQL database.

## Programming Tools
This project uses the following:

### Anaconda
[Download link for windows](https://www.anaconda.com/products/distribution)
Plain conda probably can do just fine, since I'm using Python 3.10 and it's not officially supported by Anaconda as of now.

### Python 3.10
Using Python 3.10 (latest Python version as of time of writing)
`conda create -n myenv python=3.10`
`conda activate myenv`

- Flask: `pip install flask`
- [Placeholder](https://xkcd.com/323/)

#### Interfacing Python-Flask with SQL DB
- MySQL: `pip install mysql-connector-python`
- SQLAlchemy: `pip install sqlalchemy`. ORM for initializing and dealing with SQL DB.

- [Basic tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)
- [Engine initiation strings](https://docs.sqlalchemy.org/en/14/core/engines.html#mysql)
- [Documentation regarding querying etc](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying). In retrospect, this is REALLY like pulling teeth. Maybe running plain manual SQL queries would've been better, since the IDE ain't helping much with this.

- Tables should correspond to classes defined in `orm_classes`
- An empty DB can be initialized with these definitions

#### Interfacing Flask with Frontend
- Flask CORS: `pip install flask_cors`. This is required for communicating with a separate React frontend.
- JWT: `pip install pyjwt`. This is used for user authentication.
- [Flask JWT example](https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/)

## Deployment options

### Windows VM on AWS Lightsail
This is the convenient option.

#### If no existing Lightsail instance or DB:
1. Set up a Lightsail instance (so ludicrously easy that this doesn't require a guide)
2. Set up a Lightsail DB instance (ditto)

#### When Lightsail instance is running:
1. When Lightsail instance is running, click on instance and enter Connect tab
2. In Windows, open Remote Desktop Connection (start menu -> 'rdc')
3. Paste IPv4 address from Lightsail Connect tab, set username to Administrator. Continue.
4. Get default PW from Lightsail Connect tab (recommended to NOT CHANGE THIS EVER), paste into RDC
5. Connect and be done

#### When DB is running:
1. Go to Lightsail DB instance, go to Networking tab, set Public mode to enabled (temporarily)
2. Go to Connect tab and get connection details, endpoint and port
3. Open DB GUI (e.g. DBeaver, HeidiSQL), apply parameters as necessary
4. (Use GUI and make life easier, don't be the suicidal fool with commandline)

#### Setting up the Lightsail Instance:

##### Setting up a proper browser
1. In RDC, open Server Manager (start menu -> 'server manager')
2. In Server Manager, go to Local Server in the left bar, set IE Security Configuration to Off for all (this is a temporary measure)
3. Open Internet Explorer, download Edge (for convenience. Firefox doesn't work for Windows Server)
4. Install Edge.
5. In Server Manager, go to Local Server in the left bar, set IE Security Configuration to On for all... and don't ever use IE again!

##### Setting Timezone
1. Right-click the date-time section of the taskbar, set timezone in settings.

##### Other tools to install
- Notepad++
- VS Code, ideally with Python and Sonarlint extensions
- SQL DB GUI, e.g HeidiSQL or DBeaver
- Postman
- Anaconda
- Github Desktop

#### Timezone in Lightsail DB
Requires [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
Lightsail DBs have default timezone UTC, this CANNOT be changed outside of AWS CLI (ugh)

1. [Set up access keys for other organisational users (troublesome)](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/lightsail-how-to-set-up-access-keys-to-use-sdk-api-cli)
2. In Lightsail page, click on Account at the top. Go to Advanced, click on Go to the IAM console.
3. Go to Access keys tab, create an access key. Save the key file.
4. [Follow this to configure AWS CLI for access](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/lightsail-how-to-set-up-access-keys-to-use-sdk-api-cli)
- `aws configure`
5. [Follow this to get param details and update](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-updating-database-parameters#get-database-parameters). Parameters to look out for: time_zone and max_connections (this can be a problem with multi-threaded code)
- `aws lightsail update-relational-database-parameters --relational-database-name DatabaseName --parameters "parameterName=ParameterName,parameterValue=NewParameterValue,applyMethod=ApplyMethod"`

This is like pulling teeth!

### Linux VM on AWS
Not now lol



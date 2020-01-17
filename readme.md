# MEDIUMSCRAPPER BY CYOTER

A simple Flask wrapper that scrapes a Medium article and returns JSON.

Requires Python 3.6+ 

### Installation
    git clone 
    cd MEDIUMSCRAPPER
    #### Create a virtualenv (Optional but reccomended)
    $ python3 -m venv myvirtualenv
    #### Activate the virtualenv
    $ source myvirtualenv/bin/activate
    #### Install all dependencies
    pip install -r requirements.txt
    ####Then set debbug mode
    export FLASK_ENV=development
    
    
    
### Usage

#####Run locally

    python app.py
    
#####Or on Flask server 

    Flask run

    http://127.0.0.1:5000/

Response

    {
        message: "To use the API goto http://127.0.0.1:5000/medium?url=PASTE YOUR URL HERE "
    }
    
Supply a Medium article's url

    http://127.0.0.1:5000/medium?url=PASTE YOUR URL HERE
    
Response:
                  
       # IN JSON FORMAT

```

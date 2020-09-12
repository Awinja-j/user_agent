from flask import Flask, request
from user_agents import parse

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    ua_string = request.headers.get('User-Agent')
    user_agent = parse(ua_string)

    # Accessing user agent's browser attributes
    browser = user_agent.browser
    browser.family = user_agent.browser.family
    browser.version = user_agent.browser.version
    browser.version_string = user_agent.browser.version_string

    # Accessing user agent's operating system properties
    os = user_agent.os  
    os.family = user_agent.os.family 
    os.version = user_agent.os.version 
    os.version_string = user_agent.os.version_string  

    # Accessing user agent's device properties
    device = user_agent.device  
    device.family  = user_agent.device.family 
    device.model  = user_agent.device.model 
    device.brand = user_agent.device.brand # returns 'Apple'


    data = {
        "browser": browser,
        "browser.family": browser.family,
        "browser.version": browser.version,
        "browser.version_string": browser.version_string,
        "os": os,
        "os.family": os.family,
        "os.version": os.version,
        "os.version_string": os.version_string,
        "device": device,
        "device.brand": device.brand,  
        "device.family": device.family ,
        "device.mode": device.model
    
    }
    return data


if __name__ == '__main__':
    app.run(debug=True)
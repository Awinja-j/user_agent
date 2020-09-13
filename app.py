from flask import Flask, request
from user_agents import parse

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    ua_string = request.headers.get('User-Agent')
    user_agent = parse(ua_string)

    data = {
        # Accessing user agent's browser attributes
        "browser": user_agent.browser,
        "browser_family": user_agent.browser.family,
        "browser_version": user_agent.browser.version,
        "browser_version_string": user_agent.browser.version_string,

        # Accessing user agent's operating system properties
        "os": user_agent.os, 
        "os_family": user_agent.os.family,
        "os_version": user_agent.os.version,
        "os_version_string": user_agent.os.version_string,

        # Accessing user agent's device properties
        "device": user_agent.device,
        "device_brand": user_agent.device.brand,  
        "device_family": user_agent.device.family ,
        "device_model": user_agent.device.model
    
    }
    return data


if __name__ == '__main__':
    app.run(debug=True)
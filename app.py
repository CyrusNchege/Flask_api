from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('cyrus chege')
    track = request.args.get('backend')
    
    current_day = datetime.datetime.utcnow().strftime("%A")
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    github_file_url = "https://github.com/CyrusNchege/Flask_api/app.py"
    github_repo_url = "https://github.com/CyrusNchege/Flask_api"
    
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
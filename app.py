from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app

# Dummy function to get crimps based on selected parameters
def getCrimps(selected_cable_size, selected_tool):
    # Replace this with your actual implementation
    # This is just a dummy response
    return f"Crimps for {selected_cable_size} using {selected_tool}"

# Proxy route to fetch cable sizes from external API
@app.route('/proxy/getCableList', methods=['GET'])
def proxy_get_cable_list():
    response = requests.get('https://test-lugs-api.onrender.com/getCableList')
    return jsonify(response.json())

# Proxy route to fetch tools from external API
@app.route('/proxy/getTools', methods=['GET'])
def proxy_get_tools():
    response = requests.get('https://test-lugs-api.onrender.com/getTools')
    return jsonify(response.json())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy/getCrimps', methods=['GET'])
def proxy_get_crimps():
    selected_cable_size = request.args.get('cable')
    selected_tool = request.args.get('tool')

    # Construct the URL with selected cable and tool
    api_url = f'https://test-lugs-api.onrender.com/getCrimps?cable={selected_cable_size}&tool={selected_tool}'

    response = requests.get(api_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

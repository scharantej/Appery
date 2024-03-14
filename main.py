
# Import necessary libraries
from flask import Flask, request, render_template, jsonify, send_file
import io
from PIL import Image
from diagram_builder import draw_diagram

# Create a Flask application
app = Flask(__name__)

# Main route for the application
@app.route('/', methods=['GET', 'POST'])
def home():
    # Handle GET requests
    if request.method == 'GET':
        return render_template('index.html')

    # Handle POST requests
    elif request.method == 'POST':
        # Extract form data
        app_name = request.form.get('app_name')
        app_type = request.form.get('app_type')
        components = request.form.getlist('components')

        # Build the application architecture diagram
        diagram = draw_diagram(app_name, app_type, components)

        # Send the diagram to the client
        return render_template('canvas.html', image_data=diagram)

# API endpoint for generating the application architecture diagram
@app.route('/diagram', methods=['POST'])
def generate_diagram():
    # Extract JSON data from the request
    data = request.get_json()

    # Build the application architecture diagram
    diagram = draw_diagram(data['app_name'], data['app_type'], data['components'])

    # Convert diagram to image data
    image_data = io.BytesIO()
    diagram.save(image_data, format='PNG')

    # Return the image data as a response
    return send_file(image_data, mimetype='image/png')

# API endpoint for downloading the application architecture diagram
@app.route('/download_diagram', methods=['GET'])
def download_diagram():
    # Get the filename from the query string
    filename = request.args.get('filename')

    # Build the application architecture diagram
    diagram = draw_diagram()

    # Convert diagram to image data
    image_data = io.BytesIO()
    diagram.save(image_data, format='PNG')

    # Return the image data as a download
    return send_file(image_data, as_attachment=True, attachment_filename=filename)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

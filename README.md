## Flask APP Design for Web 應用開發架構與製圖

### HTML Files

- **index.html:**
    - Homepage of the application.
    - Provides a form for the user to input the details of the web application architecture they want to visualize.
    - Includes HTML elements for displaying the resulting diagram.

- **canvas.html:**
    - A blank HTML page that serves as the canvas for drawing the application architecture diagram.

### Routes

- **@app.route('/', methods=['GET', 'POST'])**:
    - The main route for the application.
    - Handles the HTTP request for the home page.
    - On POST requests, it processes the form data, constructs the application architecture diagram using a Python library, and renders the 'canvas.html' template with the resulting diagram.

- **@app.route('/diagram', methods=['POST'])**:
    - An API endpoint for generating the application architecture diagram.
    - Accepts a JSON payload with the diagram details.
    - Generates the diagram using a Python library and returns the image data in the response.

- **@app.route('/download_diagram', methods=['GET'])**:
    - An API endpoint for downloading the application architecture diagram as an image.
    - Accepts a filename parameter.
    - Retrieves the image data from the server and sends it to the client for download.
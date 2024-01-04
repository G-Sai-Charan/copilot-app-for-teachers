from flask import Flask, render_template, request, jsonify
import openai
from flask_cors import CORS 

app = Flask(__name__)
cors = CORS(app)

openai.api_key = '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'

@app.route('/', methods=['GET', 'POST'])
# @cors.cross_origin()
def index():
    if request.method == 'POST':
        message = request.json.get('message')
        if message:
            response = generate_image(message)
        else:
            response = "Please enter a message"
        return jsonify({'response': response})
    else:
        return render_template('index.html')

def generate_image(prompt):
    try:
        response = openai.Image.create(
            model="image-alpha-001",
            prompt=prompt,
            n=1,
            size="512x512"
        )

        return response.data[0].url if response.data else None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
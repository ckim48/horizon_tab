from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    # Renders the main dashboard/hero page
    return render_template('index.html')


@app.route('/simulate', methods=['POST'])
def simulate():
    # Placeholder for your AI Model logic
    data = request.json
    policy_choice = data.get('policy', 'Default')

    # Mock response showing long-term effects
    return jsonify({
        "status": "success",
        "future_impact": f"Analyzing '{policy_choice}'... Projected outcome: 25% increase in sustainable energy by 2040.",
        "ai_confidence": 0.92
    })


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

def alternating_caps(s):
    result = []
    upper = True
    for c in s:
        if c.isalpha():
            result.append(c.upper() if upper else c.lower())
            upper = not upper
    return ''.join(result)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.get_json().get('data', [])
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        sum_of_numbers = 0
        alpha_concat = []

        for item in data:
            item_str = str(item)
            if item_str.isdigit():
                number = int(item_str)
                if number % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
                sum_of_numbers += number
            elif item_str.isalpha():
                # Add full word (uppercased) to alphabets
                alphabets.append(item_str.upper())
                # Add each character individually to alpha_concat
                for ch in item_str:
                    alpha_concat.append(ch)
            else:
                special_characters.append(item_str)

        # Build concat_string from characters, reversed + alternating caps
        concat_input = ''.join(alpha_concat)[::-1]
        concat_string = alternating_caps(concat_input)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_of_numbers),
            "concat_string": concat_string
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"message": "Use POST method at /bfhl"}), 200

if __name__ == '__main__':
    app.run(debug=True)

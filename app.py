from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        try:
            # Safe access to form data
            num = request.form.get("temperature", "").strip()
            unit = request.form.get("unit", "").strip().upper()

            if num == "":
                result = "Please enter a temperature value."
            else:
                num = float(num)

                if unit == "C":
                    temp = (num * 9/5) + 32
                    result = f"{temp:.2f} °F"
                elif unit == "F":
                    temp = (num - 32) * 5/9
                    result = f"{temp:.2f} °C"
                else:
                    result = "Invalid unit. Use C or F."

        except ValueError:
            result = "Invalid number entered."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

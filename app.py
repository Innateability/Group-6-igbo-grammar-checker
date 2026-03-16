from flask import Flask, render_template, request
from grammar_engine import check_sentence
from dictionary import dictionary

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    errors = []
    sentence = ""
    correct = False
    invalid = False

    if request.method == "POST":

        sentence = request.form["text"].strip()

        # check for empty submission
        if sentence == "":
            invalid = True

        else:
            errors = check_sentence(sentence, dictionary)

            if len(errors) == 0:
                correct = True

    return render_template(
        "index.html",
        errors=errors,
        sentence=sentence,
        correct=correct,
        invalid=invalid
    )

app.run(debug=True)


from flask import Flask, render_template, request, jsonify
# from gingerit import GingerIt
from textblob import TextBlob
from chat import chatbot

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():

    message = str(request.form['messageText'])
    # # Handle the grammar correction
    # parser = GingerIt()
    # corrected_text = parser.parse(message)
    # print(corrected_text['result'])
    
    # bot_response = chatbot(corrected_text['result'])
    # Handle the spelling correction using TextBlob
    blob = TextBlob(message)
    corrected_text = blob.correct()
    print(corrected_text)  # Print the corrected text
    
    bot_response = chatbot(str(corrected_text))  # Pass the corrected text to the chatbot

    # print(bot_response)
    return jsonify({'status':'OK','answer':bot_response})


if __name__ == "__main__":
    app.run()
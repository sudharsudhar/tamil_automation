# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Ramayanam --> Jai Sri RAM & Sita & Lava & Kusa --> Hunuman --> Guhan--> valmiki --> Ravanan --> lakshmanan--> Kausalya'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

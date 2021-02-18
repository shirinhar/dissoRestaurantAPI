from flask import request
from flask import Flask
import requests
import json

full_results = []
# main_db = {}

def get_db():

    x = requests.get('https://40435.wayscript.io/main')
    # print("HERE")
    # print(x.json())

    return x.json()

def params_dict(tracker):
    search_params = dict()

    params = ["area", "name", "pricerange", "food"]

    for param in params:
        try:
            slot = tracker[param]
            if slot != None:
                search_params[param] = slot
        except:
            pass

    return search_params

def get_corresponding_value(params):

    res = []

    main_db = get_db()

    for k, val in main_db.items():
        full_match = True

        for p_k, p_val in params.items():

            if not val[p_k] == p_val:
                full_match = False

        if full_match:
            res.append(val)
    # print(res)
    return res

def action_suggest(tracker):

    search_params = params_dict(tracker)
    full_results = get_corresponding_value(search_params)

    if bool(full_results):
        # ret = {}
        for r in full_results:

            return json.dumps({"name": r['name'], "phone": r['phone'], "address": r['addr']})



    return json.dumps({})


app = Flask(__name__)

@app.route('/hi', methods=['GET'])
def api_root():
    return 'Welcome to the chatbot from hell'

@app.route('/get_reccomendations', methods=['POST'])
def api_gh_message():
    # main_db = get_db()
    # print()
    return action_suggest(request.json)



# if __name__ == '__main__':
#     # main_db = get_db()
#     # print("Here")
#     app.run(debug=True)
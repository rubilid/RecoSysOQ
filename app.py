from flask import Flask, render_template, request, flash, abort, Markup
from recoSystem import RecoSystem
app = Flask(__name__)

app.secret_key = "manbearpig_MUDMAN888"


@app.route("/")
def hello():
    # return "Hello, World!"
    return render_template("index.html")

# import recoSystem
# from flask import Flask, render_template, request, flash, abort, Markup

# app = Flask(__name__)
# app.secret_key = "manbearpig_MUDMAN888"


# @app.route("/")
# def index():
#     return render_template("index.html")


@app.route("/extract_data", methods=['POST', 'GET'])
def extract_keywords_from_landing_page():
    reco = RecoSystem()
    url = str(request.form['url'])
    # result = reco.extract_keywords_from_landing_page(url)
    # res_title = reco.extract_title_from_landing_page(url)
    result = reco.scrap_page(url)
    list_of_images = []
    for k in result["keywords"]:
        result_images = reco.recommend_n_photos_by_keywords("pixable", [k], 1)
        if result_images:
            list_of_images.append(result_images[0])
    # if len(result) == 0:
    #     return func.HttpResponse("Can't extract the data from this url... working on it:)")
    if not result:
        flash("Can't extract the data from this url... working on it:)")
        return render_template("index.html")
    res_txt = "<b>Title: </b><br>"
    res_txt += result["title"]
    res_txt += "<br>"
    res_txt += "<br><b>Description:</b><br>"
    res_txt += result["description"]
    res_txt += "<br><br><b>Keywords:</b><br>"
    for kw in result["keywords"]:
        res_txt += kw + "<br>"
    res_txt += "<br><b>Recommended Images:</b>"
    flash(Markup(res_txt))
    return render_template("index.html", output=list_of_images)

# check2
if __name__ == '__main__':
    app.run()
#     # reco = recoSystem.RecoSystem()
#     # url = "https://www.sonoviastore.co.il/blogs/news/%D7%94%D7%9E%D7%A1%D7%9B%D7%94-%D7%94%D7%98%D7%95%D7%91%D7%94-%D7%91%D7%99%D7%95%D7%AA%D7%A8-%D7%9C%D7%98%D7%99%D7%A1%D7%95%D7%AA-%D7%91%D7%A9%D7%A0%D7%AA-2021-%D7%A1%D7%95%D7%A0%D7%95%D7%91%D7%99%D7%94?utm_source=taboola&utm_medium=referral&utm_campaign=TB_Blog_AirTravel_IL_PC&tblci=GiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyDq3U8oxaqc6ZT4jY_QAQ#tblciGiDbJRndUImP9rc80Mls7KW1gFpDdEMCGlkTelmGFUrFzyDq3U8oxaqc6ZT4jY_QAQ"
#     # result = reco.extract_keywords_from_landing_page(url)
#     # print(result)

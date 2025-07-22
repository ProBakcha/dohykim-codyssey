# add-image!!#
#dd-image!!#222
#This is main
from flask import Flask, request, render_template
from io import BytesIO
from gtts import gTTS
import base64
import datetime


app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def home():
    error = None
    audio = None

    if request.method == "POST":
        text = request.form.get("input_text")
        lang = request.form.get("lang", "ko")

        if not text.strip():
            error = "!! 텍스트를 입력하세요 !!"
        else:
            try:
                with open("input_log.txt", "a", encoding="utf-8") as f:
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"[{now}] lang={lang} input_text={text}\n")
                tts = gTTS(text=text, lang=lang)
                fp = BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                audio = base64.b64encode(fp.read()).decode("utf-8")
            except Exception as e:
                error = f"음성변환 중 오류 발생: {str(e)}"      

    return render_template("index.html", error=error, audio=audio)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)

from flask import Flask, request, render_template
from gtts import gTTS
from io import BytesIO
import base64

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    audio = None

    if request.method == "POST":
        text = request.form.get("input_text")
        lang = request.form.get("lang", "ko")  # 기본값 'ko'

        if not text.strip():
            error = "⚠️ 텍스트를 입력하세요."
        else:
            try:
                tts = gTTS(text=text, lang=lang)
                fp = BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                audio = base64.b64encode(fp.read()).decode("utf-8")
            except Exception as e:
                error = f"음성 변환 중 오류 발생: {str(e)}"

    return render_template("index.html", error=error, audio=audio)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

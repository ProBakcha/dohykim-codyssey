from flask import Flask, request, render_template
import os
from io import BytesIO
from gtts import gTTS
import base64

DEFAULT_LANG = os.getenv("DEFAULT_LANG", "ko")
app = Flask(__name__)

# 지원 언어 목록
SUPPORTED_LANGUAGES = {"ko": "한국어", "en": "영어", "ja": "일본어", "es": "스페인어"}


@app.route("/", methods=["GET", "POST"])
def home():
    """
    GET: 입력 폼 페이지 렌더링
    POST: TTS 변환 및 결과 페이지 렌더링
    """

    if request.method == "GET":
        # GET 요청 시 빈 폼 페이지 반환
        return render_template("index.html")

    elif request.method == "POST":
        # POST 요청 시 TTS 처리
        input_text = request.form.get("input_text", "").strip()
        lang = request.form.get("lang", DEFAULT_LANG)

        # 입력 값 검증
        if not input_text:
            return render_template(
                "index.html", error="텍스트를 입력해주세요.", selected_lang=lang
            )

        if lang not in SUPPORTED_LANGUAGES:
            return render_template(
                "index.html",
                error="지원하지 않는 언어입니다.",
                input_text=input_text,
                selected_lang=DEFAULT_LANG,
            )

        try:
            # gTTS로 음성 변환
            fp = BytesIO()
            tts = gTTS(text=input_text, lang=lang, slow=False)
            tts.write_to_fp(fp)
            fp.seek(0)

            # 음성 데이터를 base64로 인코딩
            audio_data = fp.getvalue()
            audio_base64 = base64.b64encode(audio_data).decode("utf-8")

            # 결과 페이지 렌더링
            return render_template(
                "index.html",
                audio=audio_base64,
                input_text=input_text,
                selected_lang=lang,
            )

        except Exception as e:
            # gTTS 실패 시 오류 메시지
            error_message = f"음성 변환에 실패했습니다: {str(e)}"
            return render_template(
                "index.html",
                error=error_message,
                input_text=input_text,
                selected_lang=lang,
            )


@app.route("/api/tts")
def api_tts():
    """
    API 엔드포인트: 직접 음성 파일 반환 (기존 기능 유지)
    사용 예: /api/tts?text=안녕하세요&lang=ko
    """
    from flask import Response

    text = request.args.get("text", "Hello, DevOps")
    lang = request.args.get("lang", DEFAULT_LANG)

    try:
        fp = BytesIO()
        gTTS(text, lang=lang).write_to_fp(fp)
        return Response(fp.getvalue(), mimetype="audio/mpeg")
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)

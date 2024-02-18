import json
import playsound
import speech_recognition as sr


def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        playsound.playsound(
            r"C:/Users/buildpc.shop/Desktop/speech2/bat_dau_ghi_am.mp3", True)
        audio = ear_robot.listen(source, timeout=None)

        try:
            text = ear_robot.recognize_google(audio, language="vi-VN")
            result = {"text": text}
            return json.dumps(result)
        except Exception as ex:
            result = {"error": "Speech recognition failed"}
            return json.dumps(result)


print(get_audio())

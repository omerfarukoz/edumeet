from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)

# Webcam'i aç
video_capture = cv2.VideoCapture(0)

# Video kaydı için VideoWriter nesnesi oluştur
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec ayarları
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Video dosyası ismi, fps, boyut

def generate_frames():
    while True:
        success, frame = video_capture.read()  # Kameradan görüntü oku
        if not success:
            break
        else:
            # Görüntüyü dosyaya kaydet
            out.write(frame)  # Çerçeveyi dosyaya yaz
            # Görüntüyü JPEG formatında kodla
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Görüntüyü yanıt olarak ver
            f = open("daha.png","w")
            f.write(frame)
            f.flush()
            f.close()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')  # HTML sayfasını döndür

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=3000)
    finally:
        # Uygulama kapandığında video dosyasını serbest bırak
        video_capture.release()
        out.release()

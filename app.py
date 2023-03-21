from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files.get('video')
    if video:
        video_filename = video.filename
        video.save(os.path.join('uploads', video_filename))
        return 'La vidéo a été enregistrée avec succès', 200
    else:
        return 'Aucun fichier vidéo trouvé', 400


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(host='0.0.0.0', port=5000)

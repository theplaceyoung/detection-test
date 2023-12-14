from flask import Flask, request, render_template
import os

app = Flask(__name__)

# 업로드된 파일을 저장할 디렉터리 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 파일이 업로드되었는지 확인
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        # 파일이 선택되지 않았을 경우 처리
        if file.filename == '':
            return "No selected file"

        # 파일이 올바르게 업로드되었을 경우 저장
        if file:
            # 파일 경로 설정
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)  # file_path로 저장

            # 결과 페이지에 파일 경로 전달
            return render_template('result.html', file_path=file_path)  
        
    # GET 요청일 때는 파일 업로드 폼을 보여줌
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from email.mime import application
from flask import Flask, render_template, url_for
import sys
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('p1_홈화면.html')

@app.route('/login')
def login():
    return render_template('p2_로그인.html')

@app.route('/register')
def register():
    return render_template('p3_회원가입.html')

@app.route('/choose')
def choose():
    return render_template('p4_선택페이지.html')


@app.route('/input')
def input():
    return render_template('p5_환자입력.html')


@app.route('/result_deep')
def result_deep():
    return render_template('p6_진단결과(딥러닝).html')


@app.route('/result_doc')
def result_doc():
    return render_template('p7_진단결과(의사).html')


@app.route('/review')
def review():
    return render_template('p8_사용자후기.html')

if __name__ == '__main__':
    app.run()
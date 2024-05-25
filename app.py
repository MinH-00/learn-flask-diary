from diary import create_app

# Create App
app = create_app()

# run
if __name__ == '__main__':#파일의 시작점일때
    app.run(debug=True)
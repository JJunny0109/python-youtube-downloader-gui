# python-youtube-downloader-gui
A simple and intuitive GUI-based YouTube video downloader built with Python.

# 1️⃣ 왜 yt-dlp인가?
유튜브는 무단 다운로드를 막기 위해 주기적으로 알고리즘을 변경합니다. yt-dlp는 오픈 소스 커뮤니티에서 가장 빠르게 대응 패치를 내놓는 라이브러리입니다. 만약 나중에 코드가 작동하지 않는다면 pip install -U yt-dlp 명령어로 라이브러리만 업데이트하면 해결되는 경우가 많습니다.

# 2️⃣ 쓰레딩(Threading) 사용
GUI 앱에서 다운로드처럼 시간이 걸리는 작업을 그냥 실행하면 다운로드 도중 창이 "응답 없음" 상태가 됩니다. threading 모듈을 사용해 다운로드 로직을 별도로 실행함으로써 UI가 계속 반응하도록 만들었습니다.

# 3️⃣ CustomTkinter
기존의 Tkinter는 90년대 프로그램 같은 투박한 디자인이지만, CustomTkinter를 사용하면 윈도우/맥 OS의 다크 모드와 연동되는 세련된 버튼과 입력창을 아주 쉽게 만들 수 있습니다.
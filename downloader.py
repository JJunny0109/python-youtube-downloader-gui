import yt_dlp

class YoutubeManager:
    # 1. 초기화할 때 progress_callback과 error_callback 두 개를 받습니다.
    def __init__(self, progress_callback, error_callback):
        self.progress_callback = progress_callback
        self.error_callback = error_callback

    def download(self, url):
        ydl_opts = {
            # 플레이리스트 주소여도 현재 영상 하나만 받도록 설정 (중요!)
            'noplaylist': True, 
            'format': 'bestvideo+bestaudio/best',
            'progress_hooks': [self.progress_callback],
            'outtmpl': '%(title)s.%(ext)s',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            # 2. 에러가 나면 메인 GUI에 정의된 에러 알림 함수를 실행합니다.
            self.error_callback(str(e))
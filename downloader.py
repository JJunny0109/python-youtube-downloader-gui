import yt_dlp

class YoutubeManager:
    # done_callback을 인자에 추가합니다.
    def __init__(self, progress_callback, error_callback, done_callback):
        self.progress_callback = progress_callback
        self.error_callback = error_callback
        self.done_callback = done_callback

    def download(self, url):
        ydl_opts = {
            'noplaylist': True,
            'format': 'bestvideo+bestaudio/best',
            'progress_hooks': [self.progress_callback],
            'outtmpl': '%(title)s.%(ext)s',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            # 위 줄(download)이 에러 없이 끝나면, 병합까지 다 된 것입니다!
            self.done_callback() 
        except Exception as e:
            self.error_callback(str(e))
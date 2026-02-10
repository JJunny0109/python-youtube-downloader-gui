import customtkinter as ctk
import threading
from downloader import YoutubeManager

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("2026 YouTube Downloader (v1.2)")
        self.geometry("500x350")

        # UI 요소
        self.label = ctk.CTkLabel(self, text="YouTube URL을 입력하세요", font=("Arial", 14))
        self.label.pack(pady=15)

        self.url_entry = ctk.CTkEntry(self, width=400)
        self.url_entry.pack(pady=10)

        self.download_btn = ctk.CTkButton(self, text="다운로드", command=self.run_download)
        self.download_btn.pack(pady=15)

        self.status_label = ctk.CTkLabel(self, text="대기 중...", text_color="gray")
        self.status_label.pack(pady=5)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # 이제 세 개의 함수(진행, 에러, 완료)를 넘겨줍니다.
        self.manager = YoutubeManager(self.update_progress, self.show_error, self.finish_download)

    def update_progress(self, d):
        if d['status'] == 'downloading':
            p_str = d.get('_percent_str', '0%').replace('%', '').strip()
            try:
                self.progress_bar.set(float(p_str) / 100)
                self.status_label.configure(text=f"다운로드 중... {p_str}%")
            except: pass
        elif d['status'] == 'finished':
            # 여기서 멈춰있던 이유: 이 이후에 병합 과정이 남아있기 때문!
            self.status_label.configure(text="병합 중... 잠시만 기다리세요.", text_color="orange")

    def show_error(self, message):
        self.status_label.configure(text="❌ 에러 발생!", text_color="red")
        self.download_btn.configure(state="normal")

    # [새로 추가된 함수] 완전히 끝났을 때 호출됩니다.
    def finish_download(self):
        self.status_label.configure(text="✅ 다운로드 완료!", text_color="cyan")
        self.progress_bar.set(1) # 바를 100%로 채움
        self.download_btn.configure(state="normal") # 버튼 다시 활성화

    def run_download(self):
        url = self.url_entry.get()
        if not url: return
        self.download_btn.configure(state="disabled")
        self.status_label.configure(text="분석 중...", text_color="white")
        
        thread = threading.Thread(target=self.manager.download, args=(url,))
        thread.daemon = True
        thread.start()
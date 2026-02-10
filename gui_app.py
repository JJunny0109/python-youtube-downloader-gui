import customtkinter as ctk
import threading
from downloader import YoutubeManager

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("2026 YouTube Downloader (v1.1)")
        self.geometry("500x350")

        # --- UI 요소들 ---
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

        # 3. 중요: 매니저를 만들 때 '진행알림함수'와 '에러알림함수'를 둘 다 알려줍니다.
        self.manager = YoutubeManager(self.update_progress, self.show_error)

    # [기능 1] 진행률 업데이트
    def update_progress(self, d):
        if d['status'] == 'downloading':
            p_str = d.get('_percent_str', '0%').replace('%', '').strip()
            # UI 업데이트는 안전하게 숫자로 변환
            try:
                progress_val = float(p_str) / 100
                self.progress_bar.set(progress_val)
                self.status_label.configure(text=f"다운로드 중... {p_str}%")
            except:
                pass
        elif d['status'] == 'finished':
            self.status_label.configure(text="병합 중... 잠시만 기다리세요.", text_color="orange")

    # [기능 2] 에러 발생 시 처리 (새로 추가된 부분!)
    def show_error(self, message):
        self.status_label.configure(text="❌ 에러 발생!", text_color="red")
        self.download_btn.configure(state="normal") # 버튼 다시 활성화
        print(f"상세 에러 내용: {message}")

    # [기능 3] 다운로드 실행 (쓰레드 활용)
    def run_download(self):
        url = self.url_entry.get()
        if not url:
            self.status_label.configure(text="URL을 입력해 주세요!", text_color="red")
            return

        self.download_btn.configure(state="disabled") # 중복 클릭 방지
        self.status_label.configure(text="분석 중...", text_color="white")
        
        # 별도 쓰레드에서 실행
        thread = threading.Thread(target=self.manager.download, args=(url,))
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    app = App()
    app.mainloop()
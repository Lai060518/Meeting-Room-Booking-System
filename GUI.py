import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta

# 導入你提供的所有核心模組
from room import SmallRoom, BigRoom 
from employee import Employee
from booking import Booking
from schedule import Scheduler
from utils import DateUtils

class MeetingRoomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HKMU 會議室預定系統")
        self.root.geometry("800x600")

        # 1. 初始化後端邏輯 (來自 schedule.py)
        self.scheduler = Scheduler()
        
        # 2. 初始化數據 (來自 room.py)
        self.rooms = [
            SmallRoom("R101", "小型會議室 A", 10, has_projector=True),
            BigRoom("R202", "大型演講廳 B", 50, video_system=True),
            SmallRoom("R103", "小組討論室 C", 4, has_projector=False)
        ]
        
        # 3. 模擬當前登錄用戶 (來自 employee.py)
        self.current_user = Employee("E001", "張三", "IT部門")

        self.create_widgets()

    def create_widgets(self):
        # 標題
        tk.Label(self.root, text="會議室預定管理系統", font=("微軟正黑體", 20, "bold"), pady=20).pack()

        # 主容器
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        # --- 左側：房間列表 ---
        left_frame = tk.LabelFrame(main_frame, text="可用會議室", padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.room_tree = ttk.Treeview(left_frame, columns=("ID", "Name", "Capacity"), show="headings")
        self.room_tree.heading("ID", text="編號")
        self.room_tree.heading("Name", text="名稱")
        self.room_tree.heading("Capacity", text="容納人數")
        self.room_tree.column("ID", width=50)
        self.room_tree.pack(fill=tk.BOTH, expand=True)

        for r in self.rooms:
            self.room_tree.insert("", tk.END, values=(r.get_room_id(), r.get_name(), r.get_capacity()))

        # --- 右側：操作面板 ---
        right_frame = tk.Frame(main_frame, padx=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        btn_style = {"width": 20, "pady": 10, "font": ("微軟正黑體", 10)}
        tk.Button(right_frame, text="新建預定", command=self.open_booking_window, bg="#e1f5fe", **btn_style).pack(pady=5)
        tk.Button(right_frame, text="查看所有預定", command=self.show_all_bookings, **btn_style).pack(pady=5)
        tk.Button(right_frame, text="房間詳細信息", command=self.show_room_detail, **btn_style).pack(pady=5)
        tk.Button(right_frame, text="退出系統", command=self.root.quit, bg="#ffebee", **btn_style).pack(side=tk.BOTTOM, pady=10)

    def open_booking_window(self):
        """打開一個新的窗口來處理預定邏輯"""
        selected = self.room_tree.selection()
        if not selected:
            messagebox.showwarning("提示", "請先從左側列表中選擇一個房間")
            return

        room_values = self.room_tree.item(selected[0])['values']
        room_id = str(room_values[0])
        selected_room = next(r for r in self.rooms if r.get_room_id() == room_id)

        # 彈出預定輸入窗口
        booking_win = tk.Toplevel(self.root)
        booking_win.title(f"預定 - {selected_room.get_name()}")
        booking_win.geometry("300x250")

        tk.Label(booking_win, text="日期 (YYYY-MM-DD):").pack(pady=5)
        date_entry = tk.Entry(booking_win)
        date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        date_entry.pack()

        tk.Label(booking_win, text="開始時間 (HH:MM):").pack(pady=5)
        time_entry = tk.Entry(booking_win)
        time_entry.insert(0, "14:00")
        time_entry.pack()

        def confirm_booking():
            try:
                # 使用 DateUtils 解析時間
                start_str = f"{date_entry.get()} {time_entry.get()}"
                start_dt = DateUtils.parse_datetime(start_str)
                end_dt = start_dt + timedelta(hours=1) # 預設預定1小時

                # 建立 Booking 對象
                new_booking = Booking(self.current_user, selected_room, start_dt, end_dt)

                # 呼叫 Scheduler 進行衝突檢查
                if self.scheduler.add_booking(new_booking):
                    messagebox.showinfo("成功", f"房間 {room_id} 預定成功！")
                    booking_win.destroy()
                else:
                    messagebox.showerror("衝突", "該時段已被佔用，請選擇其他時間")
            except Exception as e:
                messagebox.showerror("錯誤", f"輸入格式不正確: {e}")

        tk.Button(booking_win, text="確認提交", command=confirm_booking, bg="#c8e6c9", pady=10).pack(pady=20)

    def show_all_bookings(self):
        """顯示目前的預定清單"""
        bookings = self.scheduler.get_all_bookings()
        if not bookings:
            messagebox.showinfo("信息", "目前沒有任何預定記錄")
            return
        
        # 這裡會自動觸發你 booking.py 裡的 __str__ 方法
        info = "\n".join([str(b) for b in bookings])
        messagebox.showinfo("所有預定", info)

    def show_room_detail(self):
        """展示多態性 (Polymorphism)"""
        selected = self.room_tree.selection()
        if not selected: return
        room_id = str(self.room_tree.item(selected[0])['values'][0])
        selected_room = next(r for r in self.rooms if r.get_room_id() == room_id)
        
        # 呼叫各類別自定義的 display_info()
        messagebox.showinfo("房間詳情", selected_room.display_info())

if __name__ == "__main__":
    root = tk.Tk()
    app = MeetingRoomApp(root)
    root.mainloop()

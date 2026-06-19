import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import socket
import threading
import time

# AC's Port Scanner - Vibe Coded 🔥
# Python 3.14 ready | Single file | No external deps | Pure chaos

class ACsPortScanner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AC's Port Scanner")
        self.root.geometry("800x600")
        self.root.configure(bg="#000022")  # Deep blue-black hue
        
        # Style
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TLabel", background="#000022", foreground="#00BFFF")
        style.configure("TButton", background="#001133", foreground="#00BFFF")
        style.configure("TEntry", fieldbackground="#000033", foreground="#00BFFF")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header = tk.Label(self.root, text="🔥 AC's Port Scanner 🔥", 
                         font=("Courier", 24, "bold"), 
                         fg="#00FFFF", bg="#000022")
        header.pack(pady=10)
        
        # Target frame
        target_frame = tk.Frame(self.root, bg="#000022")
        target_frame.pack(pady=5, fill="x", padx=20)
        
        tk.Label(target_frame, text="Target IP / Host:", 
                font=("Courier", 12), fg="#00BFFF", bg="#000022").pack(side="left")
        self.target_entry = tk.Entry(target_frame, width=40, 
                                    font=("Courier", 12), bg="#000033", fg="#00FFFF", insertbackground="#00FFFF")
        self.target_entry.pack(side="left", padx=10)
        self.target_entry.insert(0, "127.0.0.1")
        
        # Ports
        ports_frame = tk.Frame(self.root, bg="#000022")
        ports_frame.pack(pady=5, fill="x", padx=20)
        
        tk.Label(ports_frame, text="Start Port:", 
                font=("Courier", 12), fg="#00BFFF", bg="#000022").pack(side="left")
        self.start_entry = tk.Entry(ports_frame, width=10, 
                                   font=("Courier", 12), bg="#000033", fg="#00FFFF", insertbackground="#00FFFF")
        self.start_entry.pack(side="left", padx=5)
        self.start_entry.insert(0, "1")
        
        tk.Label(ports_frame, text="End Port:", 
                font=("Courier", 12), fg="#00BFFF", bg="#000022").pack(side="left", padx=(20,5))
        self.end_entry = tk.Entry(ports_frame, width=10, 
                                 font=("Courier", 12), bg="#000033", fg="#00FFFF", insertbackground="#00FFFF")
        self.end_entry.pack(side="left", padx=5)
        self.end_entry.insert(0, "1024")
        
        # Buttons
        btn_frame = tk.Frame(self.root, bg="#000022")
        btn_frame.pack(pady=10)
        
        self.scan_btn = tk.Button(btn_frame, text="🚀 START SCAN", font=("Courier", 14, "bold"),
                                 bg="#001144", fg="#00FFFF", activebackground="#003366",
                                 command=self.start_scan_thread, width=20, height=2)
        self.scan_btn.pack(side="left", padx=10)
        
        self.stop_btn = tk.Button(btn_frame, text="🛑 STOP", font=("Courier", 14, "bold"),
                                 bg="#440000", fg="#FF4444", activebackground="#660000",
                                 command=self.stop_scan, width=15, height=2, state="disabled")
        self.stop_btn.pack(side="left", padx=10)
        
        # Output
        self.output = scrolledtext.ScrolledText(self.root, height=20, width=90,
                                               font=("Courier", 11), bg="#000011", fg="#00BFFF",
                                               insertbackground="#00FFFF")
        self.output.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Status
        self.status = tk.Label(self.root, text="Ready to scan 💙", 
                              font=("Courier", 10), fg="#00FFAA", bg="#000022")
        self.status.pack(pady=5)
        
        self.is_scanning = False
        self.stop_flag = False
        
    def log(self, message):
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)
        self.root.update_idletasks()
    
    def scan_port(self, host, port):
        if self.stop_flag:
            return
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            sock.close()
            if result == 0:
                self.log(f"[OPEN] Port {port} 🔥 Service might be vibing")
                return True
        except:
            pass
        return False
    
    def start_scan(self):
        self.is_scanning = True
        self.stop_flag = False
        self.scan_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.output.delete(1.0, tk.END)
        
        host = self.target_entry.get().strip()
        try:
            start_port = int(self.start_entry.get())
            end_port = int(self.end_entry.get())
        except:
            messagebox.showerror("Error", "Ports must be numbers!")
            self.reset_ui()
            return
        
        self.log(f"🌐 Starting AC Holdings Port Scan on {host}")
        self.log(f"📡 Range: {start_port} - {end_port}")
        self.log("=" * 60)
        
        open_ports = []
        start_time = time.time()
        
        for port in range(start_port, end_port + 1):
            if self.stop_flag:
                self.log("\n🛑 Scan stopped!")
                break
            if self.scan_port(host, port):
                open_ports.append(port)
            # Progress vibe
            if port % 50 == 0:
                self.status.config(text=f"Scanning port {port}/{end_port}... nyaa~")
        
        duration = time.time() - start_time
        self.log("=" * 60)
        if open_ports:
            self.log(f"🎉 Found {len(open_ports)} open ports: {open_ports}")
        else:
            self.log("😿 No open ports found in range... more ports next time?")
        self.log(f"✅ Scan completed in {duration:.2f} seconds")
        self.log("AC Holdings supremacy achieved 💙")
        
        self.reset_ui()
    
    def start_scan_thread(self):
        thread = threading.Thread(target=self.start_scan, daemon=True)
        thread.start()
    
    def stop_scan(self):
        self.stop_flag = True
        self.log("Stopping scan... purr~")
    
    def reset_ui(self):
        self.is_scanning = False
        self.scan_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status.config(text="Scan finished 💙 Ready for more?")

if __name__ == "__main__":
    # Mrrp~ Tool is ready
    app = ACsPortScanner()
    app.root.mainloop()

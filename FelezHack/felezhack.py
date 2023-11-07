import requests
import colorama
import os
import time
import sys
import curses
import subprocess

__title__ = "FelezHack"

def init(stdscr):
    colorama.init()
    curses.curs_set(0)
    stdscr.clear()

def login(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 5, "FelezHack", curses.A_BOLD)
    stdscr.addstr(10, 5, "Kullanıcı adı: ")
    stdscr.refresh()
    username = stdscr.getstr(10, 21).decode('utf-8')
    stdscr.addstr(12, 5, "Şifre: ")
    stdscr.refresh()
    password = stdscr.getstr(12, 13).decode('utf-8')

    if username == "admin" and password == "123456":
        return True
    else:
        return False

def main_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 5, "FelezHack", curses.A_BOLD)
    stdscr.addstr(10, 5, "1. Nmap")
    stdscr.addstr(11, 5, "2. SQLMap")
    stdscr.addstr(12, 5, "3. Wpscan")
    stdscr.addstr(13, 5, "4. Nikto")
    stdscr.addstr(14, 5, "5. Amass")
    stdscr.addstr(15, 5, "6. Dmitry")
    stdscr.addstr(16, 5, "7. Çıkış")
    stdscr.refresh()

    option = stdscr.getch()

    if option == ord('1'):
        execute_tool("nmap", stdscr)
    elif option == ord('2'):
        execute_tool("sqlmap", stdscr)
    elif option == ord('3'):
        execute_tool("wpscan", stdscr)
    elif option == ord('4'):
        execute_tool("nikto", stdscr)
    elif option == ord('5'):
        execute_tool("amass", stdscr)
    elif option == ord('6'):
        execute_tool("dmitry", stdscr)
    elif option == ord('7'):
        sys.exit()
    elif option == 18:  # Ctrl+r
        return
    elif option == 24:  # Ctrl+x
        sys.exit()

def execute_tool(tool_name, stdscr):
    os.system("clear")
    stdscr.clear()
    stdscr.addstr(5, 5, f"{tool_name.capitalize()} Aracı", curses.A_BOLD)
    stdscr.addstr(10, 5, "Hedefi Belirtin (URL veya IP): ")
    stdscr.refresh()
    target = stdscr.getstr(10, 33).decode('utf-8')

    if tool_name == "nmap":
        subprocess.run(["nmap", "-sV", "-sC", "-oN", "nmap_scan.txt", target])
    elif tool_name == "sqlmap":
        subprocess.run(["sqlmap", "-u", target, "--dbs"])
    elif tool_name == "wpscan":
        subprocess.run(["wpscan", "--url", target])
    elif tool_name == "nikto":
        subprocess.run(["nikto", "-h", target])
    elif tool_name == "amass":
        subprocess.run(["amass", "enum", "-o", "amass_scan.txt", "-i", target])
    elif tool_name == "dmitry":
        subprocess.run(["dmitry", "-r", target, "-o", "dmitry_scan.txt"])
    
    stdscr.addstr(12, 5, f"{tool_name.capitalize()} aracı başarıyla çalıştırıldı.")
    stdscr.refresh()
    stdscr.getch()

def install():
    os.system("clear")
    print("FelezHack'i kullanmak için lütfen kurulumu tamamlayın.")
    print("Kurulumu yapmak için 'install' komutunu girin.")

def run(stdscr):
    init(stdscr)

    if login(stdscr):
        while True:
            main_menu(stdscr)
    else:
        stdscr.clear()
        stdscr.addstr(5, 5, "Giriş başarısız.")
        stdscr.refresh()
        stdscr.getch()

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 5, "FelezHack", curses.A_BOLD)
    stdscr.addstr(10, 5, "Kurulumu yapmak için 'install' komutunu girin.")
    stdscr.addstr(11, 5, "Çıkmak için 'exit' komutunu girin.")
    stdscr.refresh()

    option = stdscr.getstr(12, 5).decode('utf-8')

    if option == "install":
        install()
    elif option == "exit":
        sys.exit()

if __name__ == "__main__":
    curses.wrapper(run)

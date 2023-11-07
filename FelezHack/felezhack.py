import requests
import colorama
import os
import time
import sys
import curses

__title__ = "FelezHack"

def init(stdscr):
    """Programın başlatılmasını sağlar."""
    colorama.init()
    curses.curs_set(0)
    stdscr.clear()

def login(stdscr):
    """Kullanıcıdan giriş bilgilerini alır."""
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
    """Ana menüyü gösterir."""
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
        nmap()
    elif option == ord('2'):
        sqlmap()
    elif option == ord('3'):
        wpscan()
    elif option == ord('4'):
        nikto()
    elif option == ord('5'):
        amass()
    elif option == ord('6'):
        dmitry()
    elif option == ord('7'):
        sys.exit()
    elif option == 18:  # Ctrl+r
        return
    elif option == 24:  # Ctrl+x
        sys.exit()

def nmap():
    """Nmap aracını çalıştırır."""
    os.system("clear")
    print("Nmap aracını çalıştırılıyor...")
    time.sleep(2)
    os.system("nmap -sV -sC -oN nmap_scan.txt 192.168.1.1-255")
    print("Nmap aracı başarıyla çalıştırıldı.")

def sqlmap():
    """SQLMap aracını çalıştırır."""
    os.system("clear")
    print("SQLMap aracını çalıştırılıyor...")
    time.sleep(2)
    os.system("sqlmap -u http://example.com --dbs")
    print("SQLMap aracı başarıyla çalıştırıldı.")

def wpscan():
    """WPScan aracını çalıştırır."""
    os.system("clear")
    print("WPScan aracını çalıştırılıyor...")
    time.sleep(2)
    os.system("wpscan --url http://example.com")
    print("WPScan aracı başarıyla çalıştırıldı.")

def nikto():
    """Nikto aracını çalıştırır."""
    os.system("clear")
    print("Nikto aracını çalıştırılıyor...")
    time.sleep(2)
    os.system("nikto -h http://example.com")
    print("Nikto aracı başarıyla çalıştırıldı.")

def amass():
    """Amass aracını çalıştırır."""
    os.system("clear")
    print("Amass aracını çalıştırılıyor...")
    time.sleep(2)
    os.system("amass enum -o amass_scan.txt -i http://example.com")
    print("Amass aracı başarıyla çalıştırıldı.")

def dmitry():
    """Dmitry aracını çalıştırır."""
    os.system("clear")
    print("Dmitry aracını çalıştırılıyor...")
    time.sleep(2)
    os.system("dmitry -r http://example.com -o dmitry_scan.txt")
    print("Dmitry aracı başarıyla çalıştırıldı.")

def install():
    """Programın altında çalışan tüm araçları kullanıcının sistemine indirir."""
    os.system("clear")
    print("FelezHack'i kullanmak için lütfen kurulumu tamamlayın.")
    print("Kurulumu yapmak için 'install' komutunu girin.")

def run(stdscr):
    """Programın ana işlevini gerçekleştirir."""
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
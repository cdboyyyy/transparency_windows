from pywinauto import Desktop	
from win32gui import GetWindowText, GetForegroundWindow
import win32gui
import win32con
import winxpgui
import win32api
import subprocess
import time

list = ['ThumbnailDeviceHelperWnd','Shell_TrayWnd','Shell_SecondaryTrayWnd','Shell_SecondaryTrayWnd','Chrome_WidgetWin_1','CabinetWClass','Chrome_WidgetWin_1','PseudoConsoleWindow',
        'CASCADIA_HOSTING_WINDOW_CLASS','CabinetWClass','Notepad++','TeamsWebView','Chrome_WidgetWin_1', 'Notepad']

def enum_windows_callback(hwnd, lparam):
    # Get the window title
    title = win32gui.GetWindowText(hwnd)
    # Get the window class name
    class_name = win32gui.GetClassName(hwnd)
    window_name = ''    
    if win32gui.IsWindowVisible(hwnd) == 1:
        correct_window = GetWindowText(GetForegroundWindow())
        if class_name in list:
            if correct_window == title:
                win32gui.SetWindowLong (hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED )
                winxpgui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 255, win32con.LWA_ALPHA)
            else:
                win32gui.SetWindowLong (hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED )
                # winxpgui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 180, win32con.LWA_ALPHA)
                winxpgui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 200, win32con.LWA_ALPHA)
        # print(class_name)

while True:
    win32gui.EnumWindows(enum_windows_callback, None)
    time.sleep(0.1)


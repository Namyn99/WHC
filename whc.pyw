import ctypes
import winreg
import os

def get_accent_color_rgb():
    dwmapi = ctypes.WinDLL("dwmapi")
    color = ctypes.c_uint()
    opaque = ctypes.c_bool()
    result = dwmapi.DwmGetColorizationColor(ctypes.byref(color), ctypes.byref(opaque))
    if result != 0:
        raise ctypes.WinError(result)

    color_value = color.value
    r = (color_value >> 16) & 0xFF
    g = (color_value >> 8) & 0xFF
    b = color_value & 0xFF
    return r, g, b

def set_registry_colors(r, g, b):
    rgb_string = f"{r} {g} {b}"
    key_path = r"Control Panel\Colors"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, "Highlight", 0, winreg.REG_SZ, rgb_string)
        winreg.SetValueEx(key, "HotTrackingColor", 0, winreg.REG_SZ, rgb_string)
        winreg.SetValueEx(key, "Hilight", 0, winreg.REG_SZ, rgb_string)

def prompt_restart_windows_api():
    MB_YESNO = 0x04
    MB_ICONQUESTION = 0x20
    IDYES = 6

    user32 = ctypes.windll.user32
    response = user32.MessageBoxW(
        0,
        "Изменения цвета применены.\nПерезагрузить компьютер сейчас?",
        "Перезагрузка",
        MB_YESNO | MB_ICONQUESTION
    )

    if response == IDYES:
        os.system("shutdown /r /t 0")

if __name__ == "__main__":
    r, g, b = get_accent_color_rgb()
    set_registry_colors(r, g, b)
    prompt_restart_windows_api()

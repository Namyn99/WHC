# 🎨 Windows Highlight Color Sync (WHC)

> A tiny, blazing-fast utility that syncs your Windows UI highlight colors with your system accent color — and does it with style! 🌈✨

---

## 🌟 Features

| Feature 💡                  | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 🎯 **Accent Sync**         | Automatically fetches your Windows accent color and applies it to UI highlights. |
| 🧠 **Smart Registry Edit** | Updates `Highlight`, `HotTrackingColor`, and `Hilight` in one go.           |
| 💬 **User Prompt**         | Asks the user if they want to reboot to apply changes immediately.         |
| 🧩 **No Dependencies**     | Pure Python + Windows API = zero bloat.                                     |
| 🧼 **Silent Build**        | Compiles into a clean `.exe` with no console window.                        |

---

## ⚡ Why It's So Fast

| Optimization 🚀              | Explanation                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| 🧬 **ctypes over wrappers** | Direct Windows API calls via `ctypes` avoid overhead from external libs.   |
| 🧠 **Minimal logic**        | No loops, no fluff — just straight-to-the-point system calls.              |
| 🧰 **No GUI overhead**      | Uses native `MessageBoxW` instead of bloated UI frameworks.                |
| 🧼 **Single-file build**    | PyInstaller packs everything into one `.exe`, reducing I/O and load time.  |

---

## 🛠 Build System: `pybuildw.bat`

Your kawaii build script is as efficient as it is adorable! Here's what it does:

| Step 🛠️                     | What It Does                                                                 |
|-----------------------------|------------------------------------------------------------------------------|
| 🐍 Activate venv            | Ensures isolated environment for clean builds.                              |
| 📦 Install PyInstaller      | Automatically installs the required build tool.                             |
| 🧪 Compile to `.exe`        | Uses `--onefile --noconsole` for a sleek, silent binary.                    |
| 💖 ASCII Art Celebration    | Because every successful build deserves a little anime magic! ✨             |

---

## 🧸 Kawaii Touches

- 💚 Terminal colors for each build stage
- 🖼️ Adorable ASCII art at the end of the build
- 🧼 Clean console output (no pip spam!)
- 🐾 Lightweight and portable — fits in your pocket (well, almost)

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute, as long as you give credit to the original author: **Uladzislau** 💖

---

## 📦 Example Usage

```bash
# Run the script
python whc.pyw

# Or use the compiled binary
whc.exe
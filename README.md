
# 📁 Conjo – OneDrive Photo Organizer and Cleaner

**Conjo** is a smart, automated Python tool designed to manage, backup, and clean your phone’s photos and videos stored in **OneDrive**, especially those synced via **Samsung Gallery**. The script transfers all media from OneDrive to your local PC, organizes them neatly by **album and month**, and then deletes them from the cloud to **free up space**.

It’s the perfect monthly assistant for anyone who regularly takes photos on their phone and needs a reliable, local backup without manual hassle.

## ✅ Features

- 🔄 **Auto Transfer:** Moves all photos and videos from your OneDrive photo folders to your PC.
- 🗂 **Album & Month Organization:** Sorts content into subfolders like `Family/2025-06`, `DCIM/2025-06`, etc.
- ❌ **Duplicate Protection:** Skips files that already exist in the destination.
- 💾 **Frees Up Cloud Space:** Deletes files from OneDrive after a successful move to save space.
- 🧠 **Fully Offline:** No internet or external services required (e.g., no SMS/email dependencies).
- 🗓️ **Ready for Automation:** Can be scheduled to run monthly via Windows Task Scheduler.

## 📁 Example Folder Structure

```
C:\Photos of Phone\Samsung_Gallery\
├── Family\
│   └── 2025-06\
│       ├── IMG_001.jpg
│       └── IMG_002.jpg
├── DCIM\
│   └── 2025-06\
│       ├── IMG_010.jpg
```

## 💻 Requirements

- Windows OS
- Python 3.7+
- OneDrive linked with Samsung Gallery (auto-upload enabled)

## 🚀 How It Works

1. Samsung Gallery syncs selected photo albums to OneDrive.
2. This script checks OneDrive folders (`DCIM`, `Pictures`, `Family`, etc.).
3. All media files are moved to your PC, sorted into folders based on album name and current month.
4. Original files in OneDrive are deleted after successful transfer.
5. Output summary is printed in the terminal.

## 📌 Why “Conjo”?

> "Conjo" is your **photo organization assistant** — a smart, simple name for a tool that takes care of messy backup work so you don’t have to.

---

This project is for personal use and automation only. For any improvements or features, feel free to fork and contribute!


## 🚧 Work in Progress / Known Issues

This project is still under development. Here are some limitations and features that I plan to address in the future:

- ❗ **OneDrive sync deletes from phone:** When OneDrive is linked with Samsung Gallery, deleting or moving files from OneDrive may also delete them from the phone. I'm exploring safer options like using copy instead of move, or disconnecting sync after upload.
- 🔁 **Automation Scheduling:** The script is ready, but monthly automation via Task Scheduler is not yet built into the script itself.
- 📂 **Deep Folder Handling Improvements:** Some edge cases with deeply nested folders may still need better detection.
- 🖥️ **UI or Executable Version:** A simple GUI or one-click `.exe` is planned for future usability.

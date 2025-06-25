# 🧠 Conjo Project: Automated Photo Backup System

## ✅ Phase 1: Idea & Problem Identification
- 🔍 Realized that phone storage was running out due to too many photos and videos.
- 💡 Identified that OneDrive auto-upload via Samsung Gallery could be used as the transfer bridge.
- 🎯 Goal set: Automatically move those OneDrive files to the PC monthly, organized and cleaned.

---

## ✅ Phase 2: Basic File Transfer Logic
- 📁 Built Python script to:
  - Scan OneDrive folders like DCIM, Pictures, Family, etc.
  - Move all photos and videos to PC folder `C:\Photos of Phone\Samsung_Gallery\`
  - Create subfolders by album name and month (YYYY-MM)
- ✅ Ensured duplicate protection (no overwriting existing files)

---

## ✅ Phase 3: Storage Cleanup Logic
- ✂️ After transferring, all files are removed from OneDrive to free up space.

---

## ✅ Phase 4: Testing
- 🧪 Tested on folders with different album names and formats
- ✅ Verified only valid photo/video formats are moved
- ✅ Confirmed OneDrive is cleaned only after successful move

---

## ✅ Phase 5: Basic User Feedback
- 🖥️ Added simple terminal messages (e.g., Total files moved: 20)
- ❌ Removed SMS and email alerts for simplicity and privacy

---

## 🧩 Current Status
- ✅ Stable script working for all base functionality
- 🧪 Manual testing complete
- ⚙️ User can now run script manually or monthly with Task Scheduler

---

## 🔜 Next Phase: Future Additions (See `FUTURE_PLANS.md`)
- 🖱️ One-click `.exe` version
- 🗃️ Smarter album detection using metadata
- 📈 Dashboard or analytics of what’s being moved
- 🕒 Auto-schedule setup during install
- ☁️ Support for Google Drive / Dropbox / External drive
- 🔐 Add optional encryption

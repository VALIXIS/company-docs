import os
import shutil

SOURCE_DIR = r"c:\Users\nagas\Documents\antigravity\resilient-heisenberg"
TARGET_DIR = os.path.join(SOURCE_DIR, "VALIXIS WEBSITE")

os.makedirs(TARGET_DIR, exist_ok=True)

# List of folders to transfer
FOLDERS = [
    "about",
    "leadership",
    "ecosystem",
    "projects",
    "contact",
    "assets",
    "client-sites",
    "cafe_portfolio_html"
]

# List of root website files
FILES = [
    "index.html",
    "valixis_company_homepage.html",
    "current_showcase_index.html",
    "VALIXIS_Services_Catalogue_and_Charter.html",
    "VALIXIS_Client_Service_Agreement.html",
    "robots.txt",
    "sitemap.xml",
    "favicon.ico",
    "favicon_16.png",
    "favicon_32.png",
    "favicon_48.png",
    "favicon_180.png",
    "favicon_192.png",
    "favicon_512.png",
    "valixis_horizontal_lockup.png",
    "valixis_horizontal_lockup_hd.png",
    "valixis_emblem_trans.png",
    "valixis_emblem_trans_hd.png",
    "valixis_text_trans.png",
    "preview_lockup_dark.png",
    "github_valixis_logo_transparent.png",
    "github_cropped.png",
    "launch-valixis-studio.bat"
]

print(f"Creating and transferring website files to: {TARGET_DIR}")

copied_files = 0
copied_dirs = 0

for folder in FOLDERS:
    src_folder = os.path.join(SOURCE_DIR, folder)
    dst_folder = os.path.join(TARGET_DIR, folder)
    if os.path.exists(src_folder):
        if os.path.exists(dst_folder):
            shutil.rmtree(dst_folder)
        shutil.copytree(src_folder, dst_folder)
        copied_dirs += 1
        print(f"  [COPIED FOLDER] {folder} -> VALIXIS WEBSITE/{folder}")
    else:
        print(f"  [SKIPPED FOLDER - Not Found] {folder}")

for filename in FILES:
    src_file = os.path.join(SOURCE_DIR, filename)
    dst_file = os.path.join(TARGET_DIR, filename)
    if os.path.exists(src_file):
        shutil.copy2(src_file, dst_file)
        copied_files += 1
        print(f"  [COPIED FILE] {filename} -> VALIXIS WEBSITE/{filename}")
    else:
        print(f"  [SKIPPED FILE - Not Found] {filename}")

print("\n--- TRANSFER SUMMARY ---")
print(f"Total Folders Transferred: {copied_dirs}")
print(f"Total Root Files Transferred: {copied_files}")

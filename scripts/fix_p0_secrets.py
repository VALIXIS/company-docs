import os
import re

pattern = re.compile(r'gho_[a-zA-Z0-9]{30,}')

files_to_clean = [
    'ai_agents/.env',
    'ai_agents/agent_tools.py',
    'ai_agents/auto_enforce_https.py',
    'cropper_tool/server.py',
    'scratch/check_diff_and_commits.py',
    'scratch/check_early_commits.py',
    'scratch/deploy_alignment_update.py',
    'scratch/deploy_awwwards_masterpiece.py',
    'scratch/deploy_final_3d_masterpiece.py',
    'scratch/deploy_full_fix.py',
    'scratch/deploy_hero_update.py',
    'scratch/deploy_new_crops.py',
    'scratch/deploy_production.py',
    'scratch/deploy_remove_box.py',
    'scratch/deploy_restoration.py',
    'scratch/deploy_three_upgrades.py',
    'scratch/fetch_3d7d80d.py',
    'scratch/find_tab_panels.py',
    'scratch/remove_portraits.py',
    'scratch/replace_emojis_with_designer_svgs.py',
    'scratch/search_git_diffs.py',
    'scratch/update_cco_title.py',
]

cleaned_count = 0
for f in files_to_clean:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8', errors='ignore') as fl:
            content = fl.read()
        if f.endswith('.env'):
            new_content = pattern.sub('YOUR_GITHUB_TOKEN_HERE', content)
        else:
            # Replace token inside python code with os.environ call or placeholder
            new_content = pattern.sub('os.environ.get("GITHUB_TOKEN", "")', content)
            # In cases where it was in a string: "os.environ.get(...)" -> fix quotes if nested
            new_content = new_content.replace('"os.environ.get("GITHUB_TOKEN", "")"', 'os.environ.get("GITHUB_TOKEN", "")')
            new_content = new_content.replace("'os.environ.get(\"GITHUB_TOKEN\", \"\")'", 'os.environ.get("GITHUB_TOKEN", "")')
        
        with open(f, 'w', encoding='utf-8') as fl:
            fl.write(new_content)
        cleaned_count += 1
        print(f"Sanitized: {f}")

print(f"Total files sanitized: {cleaned_count}")

# Write comprehensive .gitignore
gitignore_content = """# Environment & Secret files
.env
.env.local
.env.*.local
*.env
ai_agents/.env

# Logs and runtime caches
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/

# Operating system artifacts
.DS_Store
Thumbs.db
desktop.ini

# Scratch and temporary investigation directories
scratch/
.system_generated/
tasks/
"""

for gitignore_path in ['.gitignore', 'VALIXIS WEBSITE/.gitignore']:
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    print(f"Wrote {gitignore_path}")

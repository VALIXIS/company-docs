import os
import re

def get_env_loader_snippet():
    return '''def get_github_token():
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        return token
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('GITHUB_TOKEN='):
                    return line.strip().split('=', 1)[1]
    return ''
TOKEN = get_github_token()
'''

target_scripts = [
    'scripts/deploy_to_github_pages.py',
    'scripts/execute_live_deployment.py'
]

# Generic regex pattern matching any hardcoded token assignment or fallback literal without storing secrets
token_assignment_pattern = re.compile(
    r"TOKEN\s*=\s*(?:'[^']*'|\"[^\"]*\"|os\.environ\.get\([^)]+\))"
)

for script_path in target_scripts:
    if not os.path.exists(script_path):
        continue
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'def get_github_token():' in content:
        content = re.sub(r"TOKEN\s*=\s*['\"][A-Za-z0-9_]+['\"]", "TOKEN = get_github_token()", content)
    else:
        content = token_assignment_pattern.sub(get_env_loader_snippet(), content, count=1)
        
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Sanitized deploy scripts successfully!')

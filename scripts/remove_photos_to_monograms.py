import os

files_to_update = [
    ('index.html', 'VALIXIS WEBSITE/index.html'),
    ('valixis_company_homepage.html', 'VALIXIS WEBSITE/valixis_company_homepage.html'),
    ('leadership/index.html', 'VALIXIS WEBSITE/leadership/index.html'),
    ('leadership/subhash-annam/index.html', 'VALIXIS WEBSITE/leadership/subhash-annam/index.html'),
    ('leadership/jyothsna-sri/index.html', 'VALIXIS WEBSITE/leadership/jyothsna-sri/index.html')
]

# 1. Update index.html and valixis_company_homepage.html
for p1, p2 in [('index.html', 'VALIXIS WEBSITE/index.html'), ('valixis_company_homepage.html', 'VALIXIS WEBSITE/valixis_company_homepage.html')]:
    for path in [p1, p2]:
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Replace subhash img
        text = text.replace(
            '<img src="assets/subhash-annam.jpg" alt="Subhash Annam — Founder &amp; CEO of VALIXIS" class="leader-avatar-img" width="600" height="600">',
            '<div class="leader-avatar-initials" style="color: var(--valixis-cyan);" aria-label="Subhash Annam Initials">SA</div>'
        )
        # Replace jyothsna img
        text = text.replace(
            '<img src="assets/jyothsna-sri.jpg" alt="Jyothsna Sri — Co-Founder &amp; CCO of VALIXIS" class="leader-avatar-img" width="600" height="600">',
            '<div class="leader-avatar-initials" style="color: var(--valixis-magenta);" aria-label="Jyothsna Sri Initials">JS</div>'
        )
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated {path}")

# 2. Update leadership/index.html
leadership_css = """
    .avatar-initials {
      width: 100%;
      height: 100%;
      background: #0A0E14;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 2.2rem;
      color: var(--valixis-cyan);
      letter-spacing: 0.05em;
    }
    .avatar-initials.jyothsna {
      color: var(--valixis-magenta);
    }
"""

for path in ['leadership/index.html', 'VALIXIS WEBSITE/leadership/index.html']:
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Inject CSS before </style>
    if '.avatar-initials' not in text:
        text = text.replace('</style>', leadership_css + '\n  </style>')
    
    # Replace subhash img
    text = text.replace(
        '<img src="../assets/subhash-annam.jpg" alt="Subhash Annam — Founder &amp; CEO of VALIXIS" class="avatar-img" width="600" height="600">',
        '<div class="avatar-initials" aria-label="Subhash Annam Initials">SA</div>'
    )
    # Replace jyothsna img
    text = text.replace(
        '<img src="../assets/jyothsna-sri.jpg" alt="Jyothsna Sri — Co-Founder &amp; CCO of VALIXIS" class="avatar-img" width="600" height="600">',
        '<div class="avatar-initials jyothsna" aria-label="Jyothsna Sri Initials">JS</div>'
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated {path}")

# 3. Update leadership/subhash-annam/index.html
subhash_css = """
    .profile-photo-initials {
      width: 100%;
      height: 100%;
      background: #0A0E14;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 2.8rem;
      color: var(--valixis-cyan);
      letter-spacing: 0.05em;
    }
"""

for path in ['leadership/subhash-annam/index.html', 'VALIXIS WEBSITE/leadership/subhash-annam/index.html']:
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if '.profile-photo-initials' not in text:
        text = text.replace('</style>', subhash_css + '\n  </style>')
        
    text = text.replace(
        '<img src="../../assets/subhash-annam.jpg" alt="Subhash Annam — Founder &amp; CEO at VALIXIS" class="profile-photo-img" width="170" height="170">',
        '<div class="profile-photo-initials" aria-label="Subhash Annam Initials">SA</div>'
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated {path}")

# 4. Update leadership/jyothsna-sri/index.html
jyothsna_css = """
    .profile-photo-initials {
      width: 100%;
      height: 100%;
      background: #0A0E14;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 2.8rem;
      color: var(--valixis-cyan);
      letter-spacing: 0.05em;
    }
    .profile-photo-initials.jyothsna {
      color: var(--valixis-magenta);
    }
    .profile-photo-wrapper.jyothsna {
      background: linear-gradient(135deg, var(--valixis-purple) 0%, var(--valixis-magenta) 100%);
      box-shadow: 0 0 35px rgba(255, 46, 214, 0.45);
    }
"""

for path in ['leadership/jyothsna-sri/index.html', 'VALIXIS WEBSITE/leadership/jyothsna-sri/index.html']:
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if '.profile-photo-initials' not in text:
        text = text.replace('</style>', jyothsna_css + '\n  </style>')
        
    text = text.replace(
        '<div class="profile-photo-wrapper">',
        '<div class="profile-photo-wrapper jyothsna">'
    )
    text = text.replace(
        '<img src="../../assets/jyothsna-sri.jpg" alt="Jyothsna Sri — Co-Founder &amp; CCO at VALIXIS" class="profile-photo-img" width="170" height="170">',
        '<div class="profile-photo-initials jyothsna" aria-label="Jyothsna Sri Initials">JS</div>'
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated {path}")

print("All avatar image replacements finished!")

import os

target = """        <div class="contact-channels">

          <a href="mailto:official.valixis@gmail.com" class="contact-pill" style="border-color: var(--valixis-cyan);">

            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>

            <span>official.valixis@gmail.com</span>

          </a>



          <a href="https://wa.me/919603416707?text=Hello%20Subhash,%20I%20am%20reaching%20out%20regarding%20VALIXIS." target="_blank" class="contact-pill" style="border-color: var(--valixis-magenta);">

            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.174.086.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.144.39-.086s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.392-10.216c-5.503 0-9.969 4.467-9.969 9.97 0 1.76.459 3.477 1.332 4.992l-1.417 5.178 5.305-1.391c1.465.799 3.12 1.221 4.749 1.221 5.503 0 9.97-4.467 9.97-9.97 0-5.503-4.467-9.97-9.97-9.97zm0 18.127c-1.488 0-2.946-.4-4.22-1.155l-.303-.18-3.136.822.837-3.056-.197-.314c-.829-1.319-1.267-2.852-1.267-4.419 0-4.505 3.666-8.17 8.172-8.17 4.505 0 8.171 3.665 8.171 8.17s-3.666 8.172-8.171 8.172z"/></svg>

            <span>WhatsApp: +91 9603416707</span>

          </a>

        </div>"""

replacement = """        <div class="contact-channels">

          <a href="mailto:official.valixis@gmail.com" class="contact-pill" style="border-color: var(--valixis-cyan);">

            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>

            <span>official.valixis@gmail.com</span>

          </a>



          <a href="https://wa.me/919603416707?text=Hello%20Subhash,%20I%20am%20reaching%20out%20regarding%20VALIXIS." target="_blank" class="contact-pill" style="border-color: var(--valixis-magenta);">

            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.174.086.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.144.39-.086s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.099.824zm-3.392-10.216c-5.503 0-9.969 4.467-9.969 9.97 0 1.76.459 3.477 1.332 4.992l-1.417 5.178 5.305-1.391c1.465.799 3.12 1.221 4.749 1.221 5.503 0 9.97-4.467 9.97-9.97 0-5.503-4.467-9.97-9.97-9.97zm0 18.127c-1.488 0-2.946-.4-4.22-1.155l-.303-.18-3.136.822.837-3.056-.197-.314c-.829-1.319-1.267-2.852-1.267-4.419 0-4.505 3.666-8.17 8.172-8.17 4.505 0 8.171 3.665 8.171 8.17s-3.666 8.172-8.171 8.172z"/></svg>

            <span>WhatsApp: +91 9603416707</span>

          </a>

        </div>

        <div style="margin-top: 32px; text-align: center;">
          <a href="contact/#booking" class="btn-primary-gradient" style="padding: 14px 30px; font-size: 0.95rem; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; border-radius: 8px; color: #FFF; font-family: var(--font-display); font-weight: 700; box-shadow: 0 0 25px rgba(0, 217, 255, 0.4);">
            <span>Book 15-Min Scoping Session &amp; Submit Inquiry &rarr;</span>
          </a>
        </div>"""

for p in ['index.html', 'VALIXIS WEBSITE/index.html']:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'contact/#booking' not in content and target in content:
            content = content.replace(target, replacement)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {p}")

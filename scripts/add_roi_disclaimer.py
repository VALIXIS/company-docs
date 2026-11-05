import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('client-sites/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the end of roi-cards-display
target = '''          <div class="roi-card success">
            <span class="roi-card-tag">Annual Profit Retained</span>
            <h4 id="annualSavedDisplay">+₹40,50,000</h4>
            <p>100% owned customer database, phone numbers, and zero middleman dependency.</p>
          </div>
        </div>'''

replacement = '''          <div class="roi-card success">
            <span class="roi-card-tag">Annual Profit Retained</span>
            <h4 id="annualSavedDisplay">+₹40,50,000</h4>
            <p>100% owned customer database, phone numbers, and zero middleman dependency.</p>
          </div>
        </div>
        <p style="font-size: 0.78rem; color: var(--text-muted); margin-top: 14px; line-height: 1.5; font-style: italic; border-top: 1px dashed var(--border-dark); padding-top: 10px;">
          * Illustrative Demonstration: Projected savings and commission recovery calculations are indicative financial simulations based on typical third-party aggregator commissions (22%&ndash;28%) and direct UPI settlement assumptions. Individual commercial returns vary based on actual order volumes, average ticket sizes, and merchant operations.
        </p>'''

if target in text:
    text = text.replace(target, replacement)
    with open('client-sites/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('VALIXIS WEBSITE/client-sites/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added illustrative demonstration disclaimer to client-sites/index.html!")
else:
    print("Target block not found in client-sites/index.html!")

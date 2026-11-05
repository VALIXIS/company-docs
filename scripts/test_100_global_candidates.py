import sys
import os
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("ai_agents"))
from email_verifier import verify_email_deliverability

candidates = [
    # Category 1: AI, DevTools & B2B SaaS Startups (US & Global)
    {"company": "Modal Labs", "email": "support@modal.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Groq", "email": "support@groq.com", "country": "USA", "city": "Mountain View, CA"},
    {"company": "ElevenLabs", "email": "support@elevenlabs.io", "country": "USA", "city": "New York, NY"},
    {"company": "Weights & Biases", "email": "support@wandb.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Scale AI", "email": "support@scale.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Cohere", "email": "support@cohere.com", "country": "Canada / USA", "city": "Toronto / San Francisco"},
    {"company": "Stability AI", "email": "platform@stability.ai", "country": "UK / USA", "city": "London / San Francisco"},
    {"company": "Synthesia", "email": "support@synthesia.io", "country": "UK / USA", "city": "London / New York"},
    {"company": "CesiumAstro", "email": "media@cesiumastro.com", "country": "USA", "city": "Austin, TX"},
    {"company": "SparkCognition", "email": "info@sparkcognition.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Restream", "email": "support@restream.io", "country": "USA", "city": "Austin, TX"},
    {"company": "Rev.com", "email": "support@rev.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Spot Pet Insurance", "email": "marketing@spotpet.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Vercel", "email": "sales@vercel.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Supabase", "email": "support@supabase.io", "country": "Singapore / USA", "city": "San Francisco, CA"},
    {"company": "Railway", "email": "contact@railway.app", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Fly.io", "email": "support@fly.io", "country": "USA", "city": "Chicago, IL"},
    {"company": "Render", "email": "support@render.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "PostHog", "email": "hey@posthog.com", "country": "USA / UK", "city": "San Francisco, CA"},
    {"company": "Cal.com", "email": "support@cal.com", "country": "USA / Global", "city": "San Francisco, CA"},
    {"company": "Linear", "email": "support@linear.app", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Cursor", "email": "hi@cursor.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Pinecone", "email": "support@pinecone.io", "country": "USA", "city": "New York, NY"},
    {"company": "LangChain", "email": "support@langchain.dev", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Replit", "email": "contact@replit.com", "country": "USA", "city": "San Francisco, CA"},

    # Category 2: Specialty Coffee Roasters & High-Volume Cafes (US, UK, Canada, Australia)
    {"company": "Greater Goods Coffee Roasters", "email": "hello@ggroasting.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Mozart's Coffee Roasters", "email": "customerservice@mozartscoffee.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Flat Track Coffee", "email": "events@flattrackcoffee.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Cuvée Coffee", "email": "info@cuveecoffee.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Merit Coffee", "email": "info@meritcoffee.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Radio Coffee & Beer", "email": "trey@radiocoffeeandbeer.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Civil Goat Coffee", "email": "info@civilgoats.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Medici Roasting", "email": "hello@mediciroasting.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Barrett's Coffee", "email": "Orders@barrettscoffee.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Cosmic Coffee + Beer Garden", "email": "howdy@cosmiccoffeebeer.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Verve Coffee Roasters", "email": "info@vervecoffee.com", "country": "USA", "city": "Santa Cruz / LA, CA"},
    {"company": "Sightglass Coffee", "email": "orders@sightglasscoffee.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Ritual Coffee Roasters", "email": "info@ritualroasters.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Devoción Coffee", "email": "contact@devocion.com", "country": "USA", "city": "New York, NY"},
    {"company": "Birch Coffee", "email": "info@birchcoffee.com", "country": "USA", "city": "New York, NY"},
    {"company": "Joe Coffee Company", "email": "support@joecoffeecompany.com", "country": "USA", "city": "New York, NY"},
    {"company": "Gregorys Coffee", "email": "info@gregoryscoffee.com", "country": "USA", "city": "New York, NY"},
    {"company": "Equator Coffees", "email": "info@equatorcoffees.com", "country": "USA", "city": "San Rafael, CA"},
    {"company": "Caravan Coffee Roasters", "email": "wholesale@caravancoffeeroasters.co.uk", "country": "UK", "city": "London, UK"},
    {"company": "Workshop Coffee", "email": "info@workshopcoffee.com", "country": "UK", "city": "London, UK"},
    {"company": "Origin Coffee", "email": "info@origincoffee.co.uk", "country": "UK", "city": "London, UK"},
    {"company": "Monmouth Coffee Company", "email": "coffee@monmouthcoffee.co.uk", "country": "UK", "city": "London, UK"},
    {"company": "Pilot Coffee Roasters", "email": "info@pilotcoffeeroasters.com", "country": "Canada", "city": "Toronto, Canada"},
    {"company": "49th Parallel Coffee", "email": "support@49thcoffee.com", "country": "Canada", "city": "Vancouver, Canada"},
    {"company": "Industry Beans", "email": "mail@industrybeans.com", "country": "Australia", "city": "Melbourne, Australia"},

    # Category 3: Premier Hospitality, Dining & Beverage Groups (US, UK, International)
    {"company": "Hai Hospitality", "email": "info@haihospitality.com", "country": "USA", "city": "Austin, TX"},
    {"company": "MML Hospitality", "email": "info@mmlcatering.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Emmer & Rye Hospitality Group", "email": "info@emmerandrye.com", "country": "USA", "city": "Austin, TX"},
    {"company": "New Waterloo", "email": "marketing@newwaterloo.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Berg Hospitality Group", "email": "party@berghospitality.com", "country": "USA", "city": "Houston, TX"},
    {"company": "Goode Company", "email": "holidays@goodecompany.com", "country": "USA", "city": "Houston, TX"},
    {"company": "JuiceLand", "email": "contact@juiceland.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Amy's Ice Creams", "email": "howdy@amysicecreams.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Lick Honest Ice Creams", "email": "info@ilikelick.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Tacodeli", "email": "marketing@tacodeli.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Jester King Brewery", "email": "office@jesterkingbrewery.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Austin Beerworks", "email": "info@austinbeerworks.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Live Oak Brewing Company", "email": "taproom@liveoakbrewing.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Waterloo Ice House", "email": "info@waterlooicehouse.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Major Food Group", "email": "info@majorfood.com", "country": "USA", "city": "New York, NY"},
    {"company": "Union Square Hospitality Group", "email": "info@ushg.com", "country": "USA", "city": "New York, NY"},
    {"company": "Boka Restaurant Group", "email": "info@bokagrp.com", "country": "USA", "city": "Chicago, IL"},
    {"company": "Hogsalt", "email": "info@hogsalt.com", "country": "USA", "city": "Chicago, IL"},
    {"company": "Dishoom", "email": "info@dishoom.com", "country": "UK", "city": "London, UK"},
    {"company": "Hawksmoor", "email": "enquiries@thehawksmoor.com", "country": "UK / USA", "city": "London / New York"},

    # Category 4: Architecture, Interior Design & Custom Builders (US, UK, Europe)
    {"company": "Michael Hsu Office of Architecture", "email": "info@hsuoffice.com", "country": "USA", "city": "Austin / Houston, TX"},
    {"company": "Clayton Korte", "email": "hello@claytonkorte.com", "country": "USA", "city": "Austin / San Antonio, TX"},
    {"company": "Lake|Flato Architects", "email": "marketing@lakeflato.com", "country": "USA", "city": "San Antonio, TX"},
    {"company": "Miró Rivera Architects", "email": "info@mirorivera.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Dick Clark + Associates", "email": "dca@dcarch.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Alterstudio Architecture", "email": "info@alterstudio.net", "country": "USA", "city": "Austin, TX"},
    {"company": "Matt Fajkus Architecture", "email": "info@mfarchitecture.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Escobedo Group", "email": "dario@escobedogroup.com", "country": "USA", "city": "Austin, TX"},
    {"company": "SHoP Architects", "email": "studio@shoparc.com", "country": "USA", "city": "New York, NY"},
    {"company": "Marmol Radziner", "email": "info@marmol-radziner.com", "country": "USA", "city": "Los Angeles, CA"},
    {"company": "Feldman Architecture", "email": "info@feldmanarch.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Oppenheim Architecture", "email": "info@oppenoffice.com", "country": "USA / Switzerland", "city": "Miami / Basel"},
    {"company": "Olson Kundig", "email": "info@olsonkundig.com", "country": "USA", "city": "Seattle, WA"},
    {"company": "Foster + Partners", "email": "mail@fosterandpartners.com", "country": "UK / USA", "city": "London / New York"},
    {"company": "Heatherwick Studio", "email": "mail@heatherwick.com", "country": "UK", "city": "London, UK"},

    # Category 5: Luxury Aesthetics, Cosmetic Dermatology & Wellness (US, UK)
    {"company": "Westlake Dermatology", "email": "appointments@westlakedermatology.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Viva Day Spa + Med Spa", "email": "info@vivadayspa.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Halcyon Med Spa", "email": "info@halcyonmedspa.com", "country": "USA", "city": "Corpus Christi, TX"},
    {"company": "NassifMD Skincare", "email": "CustomerCare@DrNassifSkincare.com", "country": "USA", "city": "Beverly Hills, CA"},
    {"company": "Cadogan Clinic", "email": "info@cadoganclinic.com", "country": "UK", "city": "London, UK"},
    {"company": "Karidis Clinic", "email": "enquiries@karidis.co.uk", "country": "UK", "city": "London, UK"},
    {"company": "Dr. Barbara Sturm", "email": "service@drsturm.com", "country": "Germany / USA", "city": "Düsseldorf / New York"},
    {"company": "111SKIN", "email": "enquiries@111skin.com", "country": "UK", "city": "London, UK"},
    {"company": "Augustinus Bader", "email": "contact@augustinusbader.com", "country": "UK / USA", "city": "London / New York"},
    {"company": "SkinCeuticals", "email": "support@skinceuticals.com", "country": "USA", "city": "Dallas / New York"},

    # Category 6: High-End DTC, Lifestyle, Performance Automotive & Law (US, UK, Global)
    {"company": "Austin Speed Shop", "email": "info@AustinSpeedShop.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Tecovas", "email": "howdy@tecovas.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Rambler Goods", "email": "info@ramblergoods.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Varghese Summersett Law", "email": "benson@versustexas.com", "country": "USA", "city": "Fort Worth / Dallas, TX"},
    {"company": "Singer Vehicle Design", "email": "info@singervehicledesign.com", "country": "USA", "city": "Los Angeles, CA"},
    {"company": "Gunther Werks", "email": "info@guntherwerks.com", "country": "USA", "city": "Huntington Beach, CA"},
    {"company": "Tracksmith", "email": "support@tracksmith.com", "country": "USA", "city": "Boston, MA"},
    {"company": "Rapha Racing", "email": "enquiries@rapha.cc", "country": "UK", "city": "London, UK"},
    {"company": "Castore", "email": "customerservices@castore.co.uk", "country": "UK", "city": "Manchester, UK"},
    {"company": "Rimowa", "email": "clientcare@rimowa.com", "country": "Germany / USA", "city": "Cologne / New York"},
    {"company": "Taylor Stitch", "email": "hello@taylorstitch.com", "country": "USA", "city": "San Francisco, CA"},
    {"company": "Huckberry", "email": "support@huckberry.com", "country": "USA", "city": "Austin, TX"},
    {"company": "Filson", "email": "customerservice@filson.com", "country": "USA", "city": "Seattle, WA"},
    {"company": "Dagne Dover", "email": "support@dagnedover.com", "country": "USA", "city": "New York, NY"},
    {"company": "Bellroy", "email": "support@bellroy.com", "country": "Australia", "city": "Melbourne, Australia"}
]

print(f"Testing deliverability for {len(candidates)} candidates across US, UK, Canada, Australia, Europe...\n")

valid = []
invalid = []

for c in candidates:
    email = c["email"]
    is_deliv, reason = verify_email_deliverability(email)
    if is_deliv:
        valid.append(c)
        print(f"✅ [OK] {c['company'][:28]:28} | {c['country'][:10]:10} | {email:36} | {reason}")
    else:
        invalid.append((c, reason))
        print(f"❌ [INVALID] {c['company'][:28]:28} | {c['country'][:10]:10} | {email:36} | {reason}")

print(f"\nDeliverability results: {len(valid)} VALID, {len(invalid)} INVALID")

with open("ai_agents/data/verified_global_candidates.json", "w", encoding="utf-8") as f:
    json.dump(valid, f, indent=2)

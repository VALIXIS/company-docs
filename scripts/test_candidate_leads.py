import sys
import os
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("ai_agents"))
from email_verifier import verify_email_deliverability

candidates = [
    # Specialty Coffee & Cafes (Austin)
    {"company": "Greater Goods Coffee Roasters", "email": "hello@ggroasting.com", "city": "Austin, TX"},
    {"company": "Mozart's Coffee Roasters", "email": "customerservice@mozartscoffee.com", "city": "Austin, TX"},
    {"company": "Flat Track Coffee", "email": "events@flattrackcoffee.com", "city": "Austin, TX"},
    {"company": "Cuvée Coffee", "email": "info@cuveecoffee.com", "city": "Austin, TX"},
    {"company": "Merit Coffee", "email": "info@meritcoffee.com", "city": "Austin / San Antonio, TX"},
    {"company": "Radio Coffee & Beer", "email": "trey@radiocoffeeandbeer.com", "city": "Austin, TX"},
    {"company": "Civil Goat Coffee", "email": "info@civilgoats.com", "city": "Austin, TX"},
    {"company": "Medici Roasting", "email": "hello@mediciroasting.com", "city": "Austin, TX"},
    {"company": "Barrett's Coffee", "email": "Orders@barrettscoffee.com", "city": "Austin, TX"},
    {"company": "Cosmic Coffee + Beer Garden", "email": "howdy@cosmiccoffeebeer.com", "city": "Austin, TX"},
    {"company": "Figure 8 Coffee Purveyors", "email": "figure8coffeepurveyors@gmail.com", "city": "Austin, TX"},
    
    # Premier Hospitality & Dining Groups (Texas)
    {"company": "Hai Hospitality", "email": "info@haihospitality.com", "city": "Austin, TX"},
    {"company": "MML Hospitality", "email": "info@mmlcatering.com", "city": "Austin, TX"},
    {"company": "Emmer & Rye Hospitality Group", "email": "info@emmerandrye.com", "city": "Austin, TX"},
    {"company": "New Waterloo", "email": "marketing@newwaterloo.com", "city": "Austin, TX"},
    {"company": "Berg Hospitality Group", "email": "party@berghospitality.com", "city": "Houston, TX"},
    {"company": "Goode Company", "email": "holidays@goodecompany.com", "city": "Houston, TX"},
    
    # High-Growth Food & Beverage Chains (Austin)
    {"company": "JuiceLand", "email": "contact@juiceland.com", "city": "Austin, TX"},
    {"company": "Amy's Ice Creams", "email": "howdy@amysicecreams.com", "city": "Austin, TX"},
    {"company": "Lick Honest Ice Creams", "email": "info@ilikelick.com", "city": "Austin, TX"},
    {"company": "Tacodeli", "email": "marketing@tacodeli.com", "city": "Austin, TX"},
    {"company": "Torchy's Tacos", "email": "guestrelations@torchystacos.com", "city": "Austin, TX"},
    {"company": "Hopdoddy Burger Bar", "email": "media@hopdoddy.com", "city": "Austin, TX"},
    {"company": "Tiny Pies", "email": "info@tinypies.com", "city": "Austin, TX"},
    {"company": "Waterloo Ice House", "email": "info@waterlooicehouse.com", "city": "Austin, TX"},
    {"company": "Jester King Brewery", "email": "office@jesterkingbrewery.com", "city": "Austin, TX"},
    {"company": "Austin Beerworks", "email": "info@austinbeerworks.com", "city": "Austin, TX"},
    {"company": "Live Oak Brewing Company", "email": "taproom@liveoakbrewing.com", "city": "Austin, TX"},
    
    # Luxury Medical, MedSpa & Plastic Surgery (Austin/Texas)
    {"company": "Westlake Dermatology", "email": "appointments@westlakedermatology.com", "city": "Austin, TX"},
    {"company": "Viva Day Spa + Med Spa", "email": "info@vivadayspa.com", "city": "Austin, TX"},
    {"company": "Halcyon Med Spa", "email": "info@halcyonmedspa.com", "city": "Corpus Christi, TX"},
    
    # Top Architecture & Luxury Builders (Texas)
    {"company": "Michael Hsu Office of Architecture", "email": "info@hsuoffice.com", "city": "Austin, TX"},
    {"company": "Clayton Korte", "email": "hello@claytonkorte.com", "city": "Austin, TX"},
    {"company": "Lake|Flato Architects", "email": "marketing@lakeflato.com", "city": "San Antonio, TX"},
    {"company": "Miró Rivera Architects", "email": "info@mirorivera.com", "city": "Austin, TX"},
    {"company": "Dick Clark + Associates", "email": "dca@dcarch.com", "city": "Austin, TX"},
    {"company": "Alterstudio Architecture", "email": "info@alterstudio.net", "city": "Austin, TX"},
    {"company": "Matt Fajkus Architecture", "email": "info@mfarchitecture.com", "city": "Austin, TX"},
    {"company": "Escobedo Group", "email": "dario@escobedogroup.com", "city": "Austin, TX"},
    
    # Luxury Specialty Brands & Automotive (Austin)
    {"company": "Austin Speed Shop", "email": "info@AustinSpeedShop.com", "city": "Austin, TX"},
    {"company": "Rambler Goods", "email": "info@ramblergoods.com", "city": "Austin, TX"},
    {"company": "Tecovas", "email": "howdy@tecovas.com", "city": "Austin, TX"},
    {"company": "Tito's Handmade Vodka", "email": "support@titoshandmadevodka.com", "city": "Austin, TX"},
    
    # Law & Professional Services (Texas)
    {"company": "Varghese Summersett Law", "email": "benson@versustexas.com", "city": "Fort Worth / Dallas / Austin, TX"},
    
    # Venture-Backed Tech & AI Scaleups (Austin)
    {"company": "data.world", "email": "sales@data.world", "city": "Austin, TX"},
    {"company": "CesiumAstro", "email": "media@cesiumastro.com", "city": "Austin, TX"},
    {"company": "Spot Pet Insurance", "email": "marketing@spotpet.com", "city": "Austin, TX"},
    {"company": "SparkCognition", "email": "info@sparkcognition.com", "city": "Austin, TX"},
    {"company": "Restream", "email": "support@restream.io", "city": "Austin, TX"},
    {"company": "Rev.com", "email": "support@rev.com", "city": "Austin, TX"},
    
    # Elite Multi-State Candidates (CA, NY, FL, WA)
    {"company": "Verve Coffee Roasters", "email": "info@vervecoffee.com", "city": "Santa Cruz / LA, CA"},
    {"company": "Sightglass Coffee", "email": "orders@sightglasscoffee.com", "city": "San Francisco, CA"},
    {"company": "Ritual Coffee Roasters", "email": "info@ritualroasters.com", "city": "San Francisco, CA"},
    {"company": "Devoción Coffee", "email": "contact@devocion.com", "city": "New York, NY"},
    {"company": "Birch Coffee", "email": "info@birchcoffee.com", "city": "New York, NY"},
    {"company": "Joe Coffee Company", "email": "support@joecoffeecompany.com", "city": "New York, NY"},
    {"company": "Gregorys Coffee", "email": "info@gregoryscoffee.com", "city": "New York, NY"},
    {"company": "Equator Coffees", "email": "info@equatorcoffees.com", "city": "San Rafael, CA"},
    {"company": "Groq", "email": "support@groq.com", "city": "Mountain View, CA"},
    {"company": "Modal Labs", "email": "support@modal.com", "city": "San Francisco, CA"},
    {"company": "ElevenLabs", "email": "support@elevenlabs.io", "city": "New York, NY"},
    {"company": "Synthesia", "email": "support@synthesia.io", "city": "New York, NY"},
    {"company": "Weights & Biases", "email": "support@wandb.com", "city": "San Francisco, CA"},
    {"company": "Scale AI", "email": "support@scale.com", "city": "San Francisco, CA"},
    {"company": "Cohere", "email": "support@cohere.com", "city": "San Francisco, CA"},
    {"company": "Stability AI", "email": "platform@stability.ai", "city": "San Francisco, CA"},
    {"company": "SHoP Architects", "email": "studio@shoparc.com", "city": "New York, NY"},
    {"company": "Marmol Radziner", "email": "info@marmol-radziner.com", "city": "Los Angeles, CA"},
    {"company": "Feldman Architecture", "email": "info@feldmanarch.com", "city": "San Francisco, CA"},
    {"company": "Oppenheim Architecture", "email": "info@oppenoffice.com", "city": "Miami, FL"},
    {"company": "Olson Kundig", "email": "info@olsonkundig.com", "city": "Seattle, WA"},
    {"company": "NassifMD Skincare", "email": "CustomerCare@DrNassifSkincare.com", "city": "Beverly Hills, CA"}
]

print(f"Testing {len(candidates)} candidate emails with deliverability engine...\n")
valid = []
invalid = []

for c in candidates:
    email = c["email"]
    is_deliv, reason = verify_email_deliverability(email)
    if is_deliv:
        valid.append(c)
        print(f"✅ [OK] {c['company'][:30]:30} | {email:36} | {reason}")
    else:
        invalid.append((c, reason))
        print(f"❌ [INVALID] {c['company'][:30]:30} | {email:36} | {reason}")

print(f"\nDeliverability results: {len(valid)} VALID, {len(invalid)} INVALID")
with open("ai_agents/data/tested_valid_leads.json", "w", encoding="utf-8") as f:
    json.dump(valid, f, indent=2)

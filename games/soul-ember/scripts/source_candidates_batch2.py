import sys
import os
import sqlite3
import dns.resolver

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PUBLIC_DNS = ["8.8.8.8", "1.1.1.1"]

def verify_mx(email_addr: str) -> tuple[bool, str]:
    if not email_addr or "@" not in email_addr:
        return False, "INVALID_FORMAT"
    domain = email_addr.split("@")[1].strip().lower()
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = PUBLIC_DNS
    resolver.timeout = 5.0
    resolver.lifetime = 5.0
    try:
        answers = resolver.resolve(domain, 'MX')
        mx_hosts = [str(r.exchange).rstrip('.').lower() for r in answers]
        if not mx_hosts:
            return False, "NO_MX_RECORDS"
        return True, f"MX: {mx_hosts[0]}"
    except Exception as e:
        return False, str(e)

# Fetch existing DB emails to avoid duplicates
conn = sqlite3.connect('ai_agents/data/leads.db')
c = conn.cursor()
c.execute("SELECT email, company FROM leads")
existing_emails = set(r[0].lower().strip() for r in c.fetchall() if r[0])
conn.close()
print(f"Loaded {len(existing_emails)} existing contacted/staged emails to exclude.")

candidates = [
    # --- 1. AI, DEVTOOLS & CLOUD INFRASTRUCTURE (55 candidates) ---
    {"company": "Mintlify", "email": "support@mintlify.com", "country": "USA", "niche": "AI & DevTools", "site": "https://mintlify.com"},
    {"company": "Inngest", "email": "support@inngest.com", "country": "USA", "niche": "AI & DevTools", "site": "https://inngest.com"},
    {"company": "Loops", "email": "support@loops.so", "country": "USA", "niche": "AI & DevTools", "site": "https://loops.so"},
    {"company": "Neon", "email": "support@neon.tech", "country": "USA", "niche": "AI & DevTools", "site": "https://neon.tech"},
    {"company": "PlanetScale", "email": "support@planetscale.com", "country": "USA", "niche": "AI & DevTools", "site": "https://planetscale.com"},
    {"company": "Turso", "email": "support@turso.tech", "country": "USA", "niche": "AI & DevTools", "site": "https://turso.tech"},
    {"company": "Convex", "email": "support@convex.dev", "country": "USA", "niche": "AI & DevTools", "site": "https://convex.dev"},
    {"company": "Upstash", "email": "support@upstash.com", "country": "USA", "niche": "AI & DevTools", "site": "https://upstash.com"},
    {"company": "Axiom", "email": "support@axiom.co", "country": "USA", "niche": "AI & DevTools", "site": "https://axiom.co"},
    {"company": "Tinybird", "email": "support@tinybird.co", "country": "Spain / USA", "niche": "AI & DevTools", "site": "https://tinybird.co"},
    {"company": "Dub.co", "email": "support@dub.co", "country": "USA", "niche": "AI & DevTools", "site": "https://dub.co"},
    {"company": "Trigger.dev", "email": "hello@trigger.dev", "country": "UK / USA", "niche": "AI & DevTools", "site": "https://trigger.dev"},
    {"company": "Novu", "email": "support@novu.co", "country": "USA", "niche": "AI & DevTools", "site": "https://novu.co"},
    {"company": "Clerk", "email": "support@clerk.com", "country": "USA", "niche": "AI & DevTools", "site": "https://clerk.com"},
    {"company": "Svix", "email": "support@svix.com", "country": "USA", "niche": "AI & DevTools", "site": "https://svix.com"},
    {"company": "Langfuse", "email": "support@langfuse.com", "country": "Germany / USA", "niche": "AI & DevTools", "site": "https://langfuse.com"},
    {"company": "Helicone", "email": "contact@helicone.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://helicone.ai"},
    {"company": "Portkey", "email": "hello@portkey.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://portkey.ai"},
    {"company": "Arize AI", "email": "support@arize.com", "country": "USA", "niche": "AI & DevTools", "site": "https://arize.com"},
    {"company": "Together AI", "email": "support@together.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://together.ai"},
    {"company": "Anyscale", "email": "support@anyscale.com", "country": "USA", "niche": "AI & DevTools", "site": "https://anyscale.com"},
    {"company": "Fireworks AI", "email": "support@fireworks.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://fireworks.ai"},
    {"company": "Replicate", "email": "support@replicate.com", "country": "USA", "niche": "AI & DevTools", "site": "https://replicate.com"},
    {"company": "Baseten", "email": "support@baseten.co", "country": "USA", "niche": "AI & DevTools", "site": "https://baseten.co"},
    {"company": "Deepgram", "email": "support@deepgram.com", "country": "USA", "niche": "AI & DevTools", "site": "https://deepgram.com"},
    {"company": "Cartesia", "email": "hello@cartesia.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://cartesia.ai"},
    {"company": "AssemblyAI", "email": "support@assemblyai.com", "country": "USA", "niche": "AI & DevTools", "site": "https://assemblyai.com"},
    {"company": "RunPod", "email": "support@runpod.io", "country": "USA", "niche": "AI & DevTools", "site": "https://runpod.io"},
    {"company": "Lambda Labs", "email": "support@lambdalabs.com", "country": "USA", "niche": "AI & DevTools", "site": "https://lambdalabs.com"},
    {"company": "Vast.ai", "email": "support@vast.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://vast.ai"},
    {"company": "CoreWeave", "email": "support@coreweave.com", "country": "USA", "niche": "AI & DevTools", "site": "https://coreweave.com"},
    {"company": "Mistral AI", "email": "contact@mistral.ai", "country": "France", "niche": "AI & DevTools", "site": "https://mistral.ai"},
    {"company": "Qdrant", "email": "support@qdrant.com", "country": "Germany / USA", "niche": "AI & DevTools", "site": "https://qdrant.com"},
    {"company": "Chroma", "email": "support@trychroma.com", "country": "USA", "niche": "AI & DevTools", "site": "https://trychroma.com"},
    {"company": "Weaviate", "email": "support@weaviate.io", "country": "Netherlands / USA", "niche": "AI & DevTools", "site": "https://weaviate.io"},
    {"company": "LiveKit", "email": "support@livekit.io", "country": "USA", "niche": "AI & DevTools", "site": "https://livekit.io"},
    {"company": "Daily.co", "email": "help@daily.co", "country": "USA", "niche": "AI & DevTools", "site": "https://daily.co"},
    {"company": "Cerebras", "email": "info@cerebras.net", "country": "USA", "niche": "AI & DevTools", "site": "https://cerebras.net"},
    {"company": "SambaNova", "email": "info@sambanova.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://sambanova.ai"},
    {"company": "Tenstorrent", "email": "info@tenstorrent.com", "country": "Canada / USA", "niche": "AI & DevTools", "site": "https://tenstorrent.com"},
    {"company": "Unstructured.io", "email": "support@unstructured.io", "country": "USA", "niche": "AI & DevTools", "site": "https://unstructured.io"},
    {"company": "LlamaIndex", "email": "support@llamaindex.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://llamaindex.ai"},
    {"company": "Deepset", "email": "info@deepset.ai", "country": "Germany / USA", "niche": "AI & DevTools", "site": "https://deepset.ai"},
    {"company": "Phidata", "email": "hello@phidata.com", "country": "USA", "niche": "AI & DevTools", "site": "https://phidata.com"},
    {"company": "CrewAI", "email": "support@crewai.com", "country": "USA", "niche": "AI & DevTools", "site": "https://crewai.com"},
    {"company": "Perplexity AI", "email": "support@perplexity.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://perplexity.ai"},
    {"company": "Voyage AI", "email": "contact@voyageai.com", "country": "USA", "niche": "AI & DevTools", "site": "https://voyageai.com"},
    {"company": "Mem0", "email": "support@mem0.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://mem0.ai"},
    {"company": "Decart", "email": "info@decart.ai", "country": "USA / Israel", "niche": "AI & DevTools", "site": "https://decart.ai"},
    {"company": "Black Forest Labs", "email": "info@blackforestlabs.ai", "country": "Germany", "niche": "AI & DevTools", "site": "https://blackforestlabs.ai"},
    {"company": "Hyperbolic", "email": "support@hyperbolic.xyz", "country": "USA", "niche": "AI & DevTools", "site": "https://hyperbolic.xyz"},
    {"company": "GroqCloud", "email": "contact@groq.com", "country": "USA", "niche": "AI & DevTools", "site": "https://groq.com"},
    {"company": "Together Compute", "email": "contact@together.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://together.ai"},
    {"company": "Krea AI", "email": "support@krea.ai", "country": "USA", "niche": "AI & DevTools", "site": "https://krea.ai"},
    {"company": "Magnific AI", "email": "support@magnific.ai", "country": "Spain", "niche": "AI & DevTools", "site": "https://magnific.ai"},

    # --- 2. SPECIALTY COFFEE & ARTISAN DTC (55 candidates) ---
    {"company": "Stumptown Coffee Roasters", "email": "info@stumptowncoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://stumptowncoffee.com"},
    {"company": "Intelligentsia Coffee", "email": "customerservice@intelligentsiacoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://intelligentsiacoffee.com"},
    {"company": "Blue Bottle Coffee", "email": "support@bluebottlecoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://bluebottlecoffee.com"},
    {"company": "Counter Culture Coffee", "email": "support@counterculturecoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://counterculturecoffee.com"},
    {"company": "Onyx Coffee Lab", "email": "info@onyxcoffeelab.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://onyxcoffeelab.com"},
    {"company": "La Colombe Coffee Roasters", "email": "help@lacolombe.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://lacolombe.com"},
    {"company": "Philz Coffee", "email": "support@philzcoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://philzcoffee.com"},
    {"company": "Coava Coffee Roasters", "email": "info@coavacoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://coavacoffee.com"},
    {"company": "Heart Roasters", "email": "info@heartroasters.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://heartroasters.com"},
    {"company": "Olympia Coffee Roasting", "email": "info@olympiacoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://olympiacoffee.com"},
    {"company": "Camber Coffee", "email": "orders@cambercoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://cambercoffee.com"},
    {"company": "Passenger Coffee", "email": "info@passengercoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://passengercoffee.com"},
    {"company": "Brandywine Coffee Roasters", "email": "info@brandywinecoffeeroasters.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://brandywinecoffeeroasters.com"},
    {"company": "Black & White Coffee Roasters", "email": "support@blackwhiteroasters.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://blackwhiteroasters.com"},
    {"company": "Sey Coffee", "email": "support@seycoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://seycoffee.com"},
    {"company": "Sweet Bloom Coffee Roasters", "email": "info@sweetbloomcoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://sweetbloomcoffee.com"},
    {"company": "Methodical Coffee", "email": "info@methodicalcoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://methodicalcoffee.com"},
    {"company": "Metric Coffee", "email": "info@metriccoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://metriccoffee.com"},
    {"company": "Dark Matter Coffee", "email": "support@darkmattercoffee.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://darkmattercoffee.com"},
    {"company": "Huckleberry Roasters", "email": "info@huckleberryroasters.com", "country": "USA", "niche": "Specialty Coffee Roasters", "site": "https://huckleberryroasters.com"},
    {"company": "Proud Mary Coffee", "email": "info@proudmarycoffee.com", "country": "USA / Australia", "niche": "Specialty Coffee Roasters", "site": "https://proudmarycoffee.com"},
    {"company": "Square Mile Coffee Roasters", "email": "webshop@squaremilecoffee.com", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://squaremilecoffee.com"},
    {"company": "Colonna Coffee", "email": "help@colonnacoffee.com", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://colonnacoffee.com"},
    {"company": "Climpson & Sons", "email": "orders@climpsonandsons.com", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://climpsonandsons.com"},
    {"company": "Ozone Coffee Roasters", "email": "orders@ozonecoffee.co.uk", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://ozonecoffee.co.uk"},
    {"company": "WatchHouse", "email": "hello@watchhouse.com", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://watchhouse.com"},
    {"company": "Kiss the Hippo Coffee", "email": "info@kissthehippo.com", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://kissthehippo.com"},
    {"company": "Rosslyn Coffee", "email": "hello@rosslyncoffee.com", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://rosslyncoffee.com"},
    {"company": "Grind", "email": "hello@grind.co.uk", "country": "UK", "niche": "Specialty Coffee Roasters", "site": "https://grind.co.uk"},
    {"company": "The Barn Berlin", "email": "shop@thebarn.de", "country": "Germany", "niche": "Specialty Coffee Roasters", "site": "https://thebarn.de"},
    {"company": "Five Elephant", "email": "info@fiveelephant.com", "country": "Germany", "niche": "Specialty Coffee Roasters", "site": "https://fiveelephant.com"},
    {"company": "Bonanza Coffee Roasters", "email": "info@bonanzacoffee.de", "country": "Germany", "niche": "Specialty Coffee Roasters", "site": "https://bonanzacoffee.de"},
    {"company": "Tim Wendelboe", "email": "post@timwendelboe.no", "country": "Norway", "niche": "Specialty Coffee Roasters", "site": "https://timwendelboe.no"},
    {"company": "Coffee Collective", "email": "mail@coffeecollective.dk", "country": "Denmark", "niche": "Specialty Coffee Roasters", "site": "https://coffeecollective.dk"},
    {"company": "Drop Coffee", "email": "info@dropcoffee.se", "country": "Sweden", "niche": "Specialty Coffee Roasters", "site": "https://dropcoffee.se"},
    {"company": "Nomad Coffee", "email": "hola@nomadcoffee.es", "country": "Spain", "niche": "Specialty Coffee Roasters", "site": "https://nomadcoffee.es"},
    {"company": "Single O", "email": "orders@singleo.com.au", "country": "Australia", "niche": "Specialty Coffee Roasters", "site": "https://singleo.com.au"},
    {"company": "Market Lane Coffee", "email": "orders@marketlane.com.au", "country": "Australia", "niche": "Specialty Coffee Roasters", "site": "https://marketlane.com.au"},
    {"company": "Seven Seeds Coffee Roasters", "email": "orders@sevenseeds.com.au", "country": "Australia", "niche": "Specialty Coffee Roasters", "site": "https://sevenseeds.com.au"},
    {"company": "Patricia Coffee Brewers", "email": "hello@patriciacoffee.com.au", "country": "Australia", "niche": "Specialty Coffee Roasters", "site": "https://patriciacoffee.com.au"},
    {"company": "Reuben Hills", "email": "info@reubenhills.com.au", "country": "Australia", "niche": "Specialty Coffee Roasters", "site": "https://reubenhills.com.au"},
    {"company": "Detour Coffee Roasters", "email": "support@detourcoffee.com", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://detourcoffee.com"},
    {"company": "Rosso Coffee Roasters", "email": "info@rossocoffeeroasters.com", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://rossocoffeeroasters.com"},
    {"company": "Monogram Coffee", "email": "orders@monogramcoffee.com", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://monogramcoffee.com"},
    {"company": "Phil & Sebastian Coffee Roasters", "email": "orders@philsebastian.com", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://philsebastian.com"},
    {"company": "Dispatch Coffee", "email": "info@dispatchcoffee.ca", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://dispatchcoffee.ca"},
    {"company": "Balzac's Coffee Roasters", "email": "info@balzacs.com", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://balzacs.com"},
    {"company": "Java Blend Coffee", "email": "info@javablendcoffee.com", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://javablendcoffee.com"},
    {"company": "Matchstick Coffee", "email": "info@matchstickcoffee.com", "country": "Canada", "niche": "Specialty Coffee Roasters", "site": "https://matchstickcoffee.com"},
    {"company": "Kurasu Kyoto", "email": "hello@kurasu.kyoto", "country": "Japan / Global", "niche": "Specialty Coffee Roasters", "site": "https://kurasu.kyoto"},
    {"company": "Glitch Coffee & Roasters", "email": "info@glitchcoffee.com", "country": "Japan", "niche": "Specialty Coffee Roasters", "site": "https://glitchcoffee.com"},
    {"company": "Leaves Coffee Roasters", "email": "contact@leavescoffee.jp", "country": "Japan", "niche": "Specialty Coffee Roasters", "site": "https://leavescoffee.jp"},
    {"company": "Fuglen Coffee Roasters", "email": "coffee@fuglen.no", "country": "Norway / Japan", "niche": "Specialty Coffee Roasters", "site": "https://fuglen.no"},
    {"company": "Supreme Coffee", "email": "online@coffeesupreme.com", "country": "New Zealand / Australia", "niche": "Specialty Coffee Roasters", "site": "https://coffeesupreme.com"},
    {"company": "Allpress Espresso", "email": "orders@allpressespresso.com", "country": "New Zealand / UK", "niche": "Specialty Coffee Roasters", "site": "https://allpressespresso.com"},

    # --- 3. PREMIER HOSPITALITY & LUXURY DINING (45 candidates) ---
    {"company": "Nobu Hospitality", "email": "info@nobuhospitality.com", "country": "Global", "niche": "Premier Hospitality & Dining", "site": "https://nobuhospitality.com"},
    {"company": "Tao Group Hospitality", "email": "info@taogroup.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://taogroup.com"},
    {"company": "Momofuku Group", "email": "info@momofuku.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://momofuku.com"},
    {"company": "Starr Restaurants", "email": "info@starr-restaurants.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://starr-restaurants.com"},
    {"company": "Lettuce Entertain You", "email": "comments@leye.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://leye.com"},
    {"company": "Hillstone Restaurant Group", "email": "hrg@hillstone.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://hillstone.com"},
    {"company": "Thomas Keller Restaurant Group", "email": "info@thomaskeller.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://thomaskeller.com"},
    {"company": "Eleven Madison Park", "email": "info@elevenmadisonpark.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://elevenmadisonpark.com"},
    {"company": "Alinea Group", "email": "hospitality@thealineagroup.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://thealineagroup.com"},
    {"company": "Wolfgang Puck Fine Dining", "email": "info@wolfgangpuck.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://wolfgangpuck.com"},
    {"company": "Mina Group", "email": "info@minagroup.net", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://minagroup.net"},
    {"company": "Daily Provisions", "email": "info@dailyprovisions.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://dailyprovisions.com"},
    {"company": "Standard International", "email": "info@standardhotels.com", "country": "USA / Global", "niche": "Premier Hospitality & Dining", "site": "https://standardhotels.com"},
    {"company": "Ace Hotel Group", "email": "info@acehotel.com", "country": "USA / Global", "niche": "Premier Hospitality & Dining", "site": "https://acehotel.com"},
    {"company": "Proper Hospitality", "email": "info@properhotel.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://properhotel.com"},
    {"company": "Bunkhouse Group", "email": "info@bunkhousegroup.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://bunkhousegroup.com"},
    {"company": "Graduate Hotels", "email": "info@graduatehotels.com", "country": "USA / UK", "niche": "Premier Hospitality & Dining", "site": "https://graduatehotels.com"},
    {"company": "Line Hotels", "email": "info@thelinehotel.com", "country": "USA", "niche": "Premier Hospitality & Dining", "site": "https://thelinehotel.com"},
    {"company": "1 Hotels", "email": "info@1hotels.com", "country": "USA / Global", "niche": "Premier Hospitality & Dining", "site": "https://1hotels.com"},
    {"company": "Montage International", "email": "info@montage.com", "country": "USA / Global", "niche": "Premier Hospitality & Dining", "site": "https://montage.com"},
    {"company": "Auberge Resorts Collection", "email": "info@aubergeresorts.com", "country": "USA / Global", "niche": "Premier Hospitality & Dining", "site": "https://aubergeresorts.com"},
    {"company": "The Hoxton", "email": "info@thehoxton.com", "country": "UK / Europe / USA", "niche": "Premier Hospitality & Dining", "site": "https://thehoxton.com"},
    {"company": "Firmdale Hotels", "email": "info@firmdale.com", "country": "UK / USA", "niche": "Premier Hospitality & Dining", "site": "https://firmdale.com"},
    {"company": "The Wolseley Hospitality Group", "email": "enquiries@wolseleyhospitalitygroup.com", "country": "UK", "niche": "Premier Hospitality & Dining", "site": "https://wolseleyhospitalitygroup.com"},
    {"company": "Big Mamma Group", "email": "contact@bigmammagroup.com", "country": "France / UK", "niche": "Premier Hospitality & Dining", "site": "https://bigmammagroup.com"},
    {"company": "The Social Company", "email": "info@thesocialcompany.co.uk", "country": "UK", "niche": "Premier Hospitality & Dining", "site": "https://thesocialcompany.co.uk"},
    {"company": "Gordon Ramsay Restaurants", "email": "guestrelations@gordonramsay.com", "country": "UK / Global", "niche": "Premier Hospitality & Dining", "site": "https://gordonramsay.com"},
    {"company": "The Fat Duck Group", "email": "reservations@thefatduck.co.uk", "country": "UK", "niche": "Premier Hospitality & Dining", "site": "https://thefatduck.co.uk"},
    {"company": "Hakkasan Group", "email": "info@hakkasan.com", "country": "UK / USA", "niche": "Premier Hospitality & Dining", "site": "https://hakkasan.com"},
    {"company": "Zuma Restaurants", "email": "info@zumarestaurant.com", "country": "UK / Global", "niche": "Premier Hospitality & Dining", "site": "https://zumarestaurant.com"},
    {"company": "Sexy Fish", "email": "enquiries@sexyfish.com", "country": "UK / USA", "niche": "Premier Hospitality & Dining", "site": "https://sexyfish.com"},
    {"company": "Annabel's Mayfair", "email": "enquiries@annabels.co.uk", "country": "UK", "niche": "Premier Hospitality & Dining", "site": "https://annabels.co.uk"},
    {"company": "Soho House Group", "email": "membership@sohohouse.com", "country": "UK / Global", "niche": "Premier Hospitality & Dining", "site": "https://sohohouse.com"},
    {"company": "Chiltern Firehouse", "email": "reservations@chilternfirehouse.com", "country": "UK", "niche": "Premier Hospitality & Dining", "site": "https://chilternfirehouse.com"},
    {"company": "Edition Hotels", "email": "info@editionhotels.com", "country": "Global", "niche": "Premier Hospitality & Dining", "site": "https://editionhotels.com"},
    {"company": "Aman Resorts", "email": "info@aman.com", "country": "Global", "niche": "Premier Hospitality & Dining", "site": "https://aman.com"},
    {"company": "Six Senses Hotels", "email": "info@sixsenses.com", "country": "Global", "niche": "Premier Hospitality & Dining", "site": "https://sixsenses.com"},
    {"company": "Rosewood Hotels", "email": "info@rosewoodhotels.com", "country": "Global", "niche": "Premier Hospitality & Dining", "site": "https://rosewoodhotels.com"},
    {"company": "Belmond", "email": "info@belmond.com", "country": "Global", "niche": "Premier Hospitality & Dining", "site": "https://belmond.com"},
    {"company": "Mandarin Oriental Hotel Group", "email": "info@mohg.com", "country": "Global", "niche": "Premier Hospitality & Dining", "site": "https://mohg.com"},
    {"company": "Corinthia Hotels", "email": "info@corinthia.com", "country": "Europe / UK", "niche": "Premier Hospitality & Dining", "site": "https://corinthia.com"},
    {"company": "Oetker Collection", "email": "info@oetkercollection.com", "country": "Europe / Global", "niche": "Premier Hospitality & Dining", "site": "https://oetkercollection.com"},
    {"company": "Rocco Forte Hotels", "email": "enquiries@roccofortehotels.com", "country": "UK / Europe", "niche": "Premier Hospitality & Dining", "site": "https://roccofortehotels.com"},
    {"company": "Dorchester Collection", "email": "info.UK@dorchestercollection.com", "country": "UK / Europe", "niche": "Premier Hospitality & Dining", "site": "https://dorchestercollection.com"},
    {"company": "Maybourne Hotel Group", "email": "info@maybourne.com", "country": "UK / USA", "niche": "Premier Hospitality & Dining", "site": "https://maybourne.com"},

    # --- 4. LUXURY ARCHITECTURE & SPATIAL DESIGN (35 candidates) ---
    {"company": "Bjarke Ingels Group", "email": "big@big.dk", "country": "Denmark / USA", "niche": "Luxury Architecture & Design", "site": "https://big.dk"},
    {"company": "Snøhetta", "email": "contact@snohetta.com", "country": "Norway / USA", "niche": "Luxury Architecture & Design", "site": "https://snohetta.com"},
    {"company": "Zaha Hadid Architects", "email": "press@zaha-hadid.com", "country": "UK / Global", "niche": "Luxury Architecture & Design", "site": "https://zaha-hadid.com"},
    {"company": "Perkins&Will", "email": "info@perkinswill.com", "country": "USA / Global", "niche": "Luxury Architecture & Design", "site": "https://perkinswill.com"},
    {"company": "Gensler", "email": "info@gensler.com", "country": "USA / Global", "niche": "Luxury Architecture & Design", "site": "https://gensler.com"},
    {"company": "Skidmore, Owings & Merrill", "email": "press@som.com", "country": "USA / Global", "niche": "Luxury Architecture & Design", "site": "https://som.com"},
    {"company": "HKS Architects", "email": "info@hksinc.com", "country": "USA / Global", "niche": "Luxury Architecture & Design", "site": "https://hksinc.com"},
    {"company": "Kohn Pedersen Fox", "email": "info@kpf.com", "country": "USA / Global", "niche": "Luxury Architecture & Design", "site": "https://kpf.com"},
    {"company": "NBBJ", "email": "info@nbbj.com", "country": "USA / Global", "niche": "Luxury Architecture & Design", "site": "https://nbbj.com"},
    {"company": "Studio Gang", "email": "info@studiogang.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://studiogang.com"},
    {"company": "Rockwell Group", "email": "info@rockwellgroup.com", "country": "USA / Spain", "niche": "Luxury Architecture & Design", "site": "https://rockwellgroup.com"},
    {"company": "AvroKO", "email": "info@avroko.com", "country": "USA / UK / Thailand", "niche": "Luxury Architecture & Design", "site": "https://avroko.com"},
    {"company": "Meyer Davis", "email": "info@meyerdavis.com", "country": "USA / UK", "niche": "Luxury Architecture & Design", "site": "https://meyerdavis.com"},
    {"company": "Yabu Pushelberg", "email": "info@yabupushelberg.com", "country": "Canada / USA", "niche": "Luxury Architecture & Design", "site": "https://yabupushelberg.com"},
    {"company": "Roman and Williams", "email": "info@romanandwilliams.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://romanandwilliams.com"},
    {"company": "Kelly Wearstler", "email": "info@kellywearstler.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://kellywearstler.com"},
    {"company": "Peter Marino Architect", "email": "info@petermarinoarchitect.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://petermarinoarchitect.com"},
    {"company": "Woods Bagot", "email": "info@woodsbagot.com", "country": "Australia / USA / UK", "niche": "Luxury Architecture & Design", "site": "https://woodsbagot.com"},
    {"company": "Populous", "email": "info@populous.com", "country": "USA / UK", "niche": "Luxury Architecture & Design", "site": "https://populous.com"},
    {"company": "Safdie Architects", "email": "info@msafdie.com", "country": "USA / Israel / Singapore", "niche": "Luxury Architecture & Design", "site": "https://msafdie.com"},
    {"company": "Diller Scofidio + Renfro", "email": "info@dsrny.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://dsrny.com"},
    {"company": "Robert A.M. Stern Architects", "email": "info@ramsa.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://ramsa.com"},
    {"company": "MAD Architects", "email": "press@i-mad.com", "country": "China / USA / Italy", "niche": "Luxury Architecture & Design", "site": "https://i-mad.com"},
    {"company": "MVRDV", "email": "info@mvrdv.com", "country": "Netherlands", "niche": "Luxury Architecture & Design", "site": "https://mvrdv.com"},
    {"company": "UNStudio", "email": "info@unstudio.com", "country": "Netherlands / Germany / China", "niche": "Luxury Architecture & Design", "site": "https://unstudio.com"},
    {"company": "Grimshaw Architects", "email": "info@grimshaw.global", "country": "UK / USA / Australia", "niche": "Luxury Architecture & Design", "site": "https://grimshaw.global"},
    {"company": "WilkinsonEyre", "email": "info@wilkinsoneyre.com", "country": "UK", "niche": "Luxury Architecture & Design", "site": "https://wilkinsoneyre.com"},
    {"company": "BDP", "email": "bdp@bdp.com", "country": "UK / Global", "niche": "Luxury Architecture & Design", "site": "https://bdp.com"},
    {"company": "Allies and Morrison", "email": "info@alliesandmorrison.com", "country": "UK", "niche": "Luxury Architecture & Design", "site": "https://alliesandmorrison.com"},
    {"company": "Studio Gang Architects", "email": "studio@studiogang.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://studiogang.com"},
    {"company": "Marmol Radziner Architecture", "email": "office@marmol-radziner.com", "country": "USA", "niche": "Luxury Architecture & Design", "site": "https://marmol-radziner.com"},
    {"company": "Shim-Sutcliffe Architects", "email": "office@shim-sutcliffe.com", "country": "Canada", "niche": "Luxury Architecture & Design", "site": "https://shim-sutcliffe.com"},
    {"company": "Patkau Architects", "email": "info@patkau.ca", "country": "Canada", "niche": "Luxury Architecture & Design", "site": "https://patkau.ca"},
    {"company": "Kohn Shnier Architects", "email": "info@kohnshnierarchitects.com", "country": "Canada", "niche": "Luxury Architecture & Design", "site": "https://kohnshnierarchitects.com"},
    {"company": "MacKay-Lyons Sweetapple", "email": "info@mlsarchitects.ca", "country": "Canada", "niche": "Luxury Architecture & Design", "site": "https://mlsarchitects.ca"},

    # --- 5. HIGH-END DTC, LUXURY LIFESTYLE & DESIGN (35 candidates) ---
    {"company": "Our Place", "email": "hello@fromourplace.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://fromourplace.com"},
    {"company": "Great Jones", "email": "care@greatjonesgoods.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://greatjonesgoods.com"},
    {"company": "Material Kitchen", "email": "hello@materialkitchen.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://materialkitchen.com"},
    {"company": "Caraway Home", "email": "hello@carawayhome.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://carawayhome.com"},
    {"company": "Fellow Products", "email": "hello@fellowproducts.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://fellowproducts.com"},
    {"company": "Ember", "email": "support@ember.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://ember.com"},
    {"company": "Aarke", "email": "support@aarke.com", "country": "Sweden / Global", "niche": "High-End DTC & Performance", "site": "https://aarke.com"},
    {"company": "Breville", "email": "support@breville.com", "country": "Australia / USA", "niche": "High-End DTC & Performance", "site": "https://breville.com"},
    {"company": "Balmuda", "email": "support@balmuda.com", "country": "Japan / USA", "niche": "High-End DTC & Performance", "site": "https://balmuda.com"},
    {"company": "Snow Peak", "email": "info@snowpeak.com", "country": "Japan / USA", "niche": "High-End DTC & Performance", "site": "https://snowpeak.com"},
    {"company": "Filson", "email": "customerservice@filson.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://filson.com"},
    {"company": "Shinola", "email": "customercare@shinola.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://shinola.com"},
    {"company": "Best Made Co", "email": "support@bestmadeco.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://bestmadeco.com"},
    {"company": "Tanner Goods", "email": "service@tannergoods.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://tannergoods.com"},
    {"company": "Saddleback Leather", "email": "ihaveaquestion@saddlebackleather.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://saddlebackleather.com"},
    {"company": "Hardgraft", "email": "support@hardgraft.com", "country": "UK / Austria", "niche": "High-End DTC & Performance", "site": "https://hardgraft.com"},
    {"company": "Craighill", "email": "support@craighill.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://craighill.com"},
    {"company": "Peak Design", "email": "info@peakdesign.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://peakdesign.com"},
    {"company": "Nomatic", "email": "support@nomatic.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://nomatic.com"},
    {"company": "Mission Workshop", "email": "support@missionworkshop.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://missionworkshop.com"},
    {"company": "Goruck", "email": "team@goruck.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://goruck.com"},
    {"company": "Satisfy Running", "email": "support@satisfyrunning.com", "country": "France / USA", "niche": "High-End DTC & Performance", "site": "https://satisfyrunning.com"},
    {"company": "District Vision", "email": "service@districtvision.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://districtvision.com"},
    {"company": "Bandit Running", "email": "support@banditrunning.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://banditrunning.com"},
    {"company": "Article Furniture", "email": "service@article.com", "country": "Canada / USA", "niche": "High-End DTC & Performance", "site": "https://article.com"},
    {"company": "Floyd Home", "email": "hello@floydhome.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://floydhome.com"},
    {"company": "Burrow", "email": "support@burrow.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://burrow.com"},
    {"company": "Maiden Home", "email": "support@maidenhome.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://maidenhome.com"},
    {"company": "Industry West", "email": "info@industrywest.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://industrywest.com"},
    {"company": "Schoolhouse", "email": "customerservice@schoolhouse.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://schoolhouse.com"},
    {"company": "DWR / Design Within Reach", "email": "support@dwr.com", "country": "USA", "niche": "High-End DTC & Performance", "site": "https://dwr.com"},
    {"company": "HAY Design", "email": "support@hay.com", "country": "Denmark / USA", "niche": "High-End DTC & Performance", "site": "https://hay.com"},
    {"company": "Muuto", "email": "contact@muuto.com", "country": "Denmark / USA", "niche": "High-End DTC & Performance", "site": "https://muuto.com"},
    {"company": "Vitra", "email": "info@vitra.com", "country": "Switzerland / USA", "niche": "High-End DTC & Performance", "site": "https://vitra.com"},
    {"company": "Fritz Hansen", "email": "info@fritzhansen.com", "country": "Denmark / USA", "niche": "High-End DTC & Performance", "site": "https://fritzhansen.com"},
]

print(f"Total candidate leads loaded: {len(candidates)}")

valid_candidates = []
excluded_count = 0
invalid_dns_count = 0

for item in candidates:
    em = item["email"].lower().strip()
    if em in existing_emails:
        excluded_count += 1
        continue
    
    is_valid, reason = verify_mx(em)
    if is_valid:
        item["mx_reason"] = reason
        valid_candidates.append(item)
    else:
        invalid_dns_count += 1
        print(f"DNS failed for {item['company']} ({em}): {reason}")

print(f"\n==========================================")
print(f"Candidate Verification Results:")
print(f"  Total Valid & Fresh Candidates: {len(valid_candidates)}")
print(f"  Already in DB (Excluded): {excluded_count}")
print(f"  DNS MX Failed: {invalid_dns_count}")
print(f"==========================================")

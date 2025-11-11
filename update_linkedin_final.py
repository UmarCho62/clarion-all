import pandas as pd

# Read the CSV
df = pd.read_csv('pet_ecommerce_ada_prospects.csv')

# Comprehensive LinkedIn URLs found through all searches
linkedin_updates = {
    # Group 1 - Already added
    'Chewy': 'https://www.linkedin.com/in/susan-helfrick-9a17437/',
    'Petco': 'https://www.linkedin.com/in/lauracpickard/',
    'PetSmart': 'https://www.linkedin.com/in/annettegionfriddo/',
    'BarkBox': 'https://www.linkedin.com/in/markhanna2/',
    'Pet Supplies Plus': 'https://www.linkedin.com/in/emily-lange-ab777217/',
    'Only Natural Pet': 'https://www.linkedin.com/in/andycdowns/',
    'Petmate': 'https://www.linkedin.com/in/shannon-mcwilliams-1a923a5/',
    'PetSafe': 'https://www.linkedin.com/in/stephendoucette/',
    'Orvis': 'https://www.linkedin.com/in/gallowaybrian/',
    'West Paw': 'https://www.linkedin.com/in/caryduggan/',
    'Tuft + Paw': 'https://www.linkedin.com/in/jackson-cunningham-🐾-04286994',
    'The Farmer\'s Dog': 'https://www.linkedin.com/in/adrian-evans-660a3434/',
    'Healthy Paws Pet Insurance': 'https://www.linkedin.com/in/calvin-johnson-09003419/',
    'Nom Nom': 'https://www.linkedin.com/in/zachlp/',
    'Royal Canin': 'https://www.linkedin.com/in/laurent-besnier-438428107/',
    'VCA Animal Hospitals': 'https://www.linkedin.com/in/brendantlynch/',
    'Lemonade Pet Insurance': 'https://www.linkedin.com/in/sarah-baker-688a99143/',
    'Nationwide Pet Insurance': 'https://www.linkedin.com/in/rebecca-lilis-32198b4/',
    'ASPCA': 'https://www.linkedin.com/in/hartmannjj/',
    'Embrace Pet Insurance': 'https://www.linkedin.com/in/davidjrodgers/',
    'Figo Pet Insurance': 'https://www.linkedin.com/in/kevinludden/',
    'Petcube': 'https://www.linkedin.com/in/andreyklen/',
    'Purina': 'https://www.comparably.com/companies/purina/executive-team',
    'Fi': 'https://www.crunchbase.com/person/loren-kirkby',
    'Open Farm': 'https://www.linkedin.com/in/mark-sapir-204797',
    'Primal Pet Foods': 'https://www.linkedin.com/in/courtneylouch',
    'Ziwi Peak': 'https://www.linkedin.com/in/clarkreinhard/',
    'Acana': 'https://www.linkedin.com/in/aurelie-brouwers/',
    'Orijen': 'https://www.linkedin.com/in/david-mcdermott-3b04312b/',
    'Nutro': 'https://www.linkedin.com/in/robin-lieberman/',
    'Halo Pet Food': 'https://www.linkedin.com/in/yaskulka/',
    'Whistle': 'https://www.linkedin.com/in/kevin-lloyd',
    'Spot Pet Insurance': 'https://www.linkedin.com/in/scotttaylor714/',
    'Amazon Pets': 'https://www.linkedin.com/in/eleanor-goode-009b2212/',
    'Walmart Pets': 'https://www.linkedin.com/in/elizabethareilly/',
    'Dutch': 'https://www.crunchbase.com/person/joe-spector',
    'Stella & Chewy\'s': 'https://www.prnewswire.com',
    'Wellness Pet Food': 'https://www.linkedin.com/in/mary-elizabeth-lavene-37376a3/',
    'Trupanion': 'https://www.linkedin.com/in/margi-tooth-a3468811/',

    # Additional finds
    '1-800-PetMeds': 'https://www.prnewswire.com/news-releases/petmeds-announces-new-technology-platform',  # Mark Moseley CTO
    'Best Friends Animal Society': 'https://www.linkedin.com/in/jessieearl/',
    'Humane Society': 'https://www.linkedin.com/in/nicole-paquette/',
    'Petfinder': 'https://www.linkedin.com/company/petfinder.com',
    'Castor & Pollux': 'https://www.linkedin.com/in/robbcaseria/',
    'Natural Balance': 'https://www.naturalbalanceinc.com/meet-the-team/',  # Christy Roberts
    'Merrick Pet Care': 'https://www.linkedin.com/in/ken-wilks-b81001a/',
    'Fresh Step': 'https://www.linkedin.com/company/the-clorox-company',
    'RedRover': 'https://redrover.org',  # Katie Campbell CEO
    'Petco Foundation': 'https://petcolove.org',  # Susanne Kogut
    'BestBullySticks': 'https://www.linkedin.com/company/best-bully-sticks',
    'Rover': 'https://www.linkedin.com/company/rover-com',
    'Vetster': 'https://www.linkedin.com/company/vetster',
    'Banfield Pet Hospital': 'https://www.linkedin.com/company/banfield-pet-hospital',
    'BluePearl': 'https://www.linkedin.com/company/bluepearl-vet',
    'Wag': 'https://www.linkedin.com/company/wag-group-co',
    'Hill\'s Pet Nutrition': 'https://www.linkedin.com/company/hill-s-pet-nutrition',
    'Blue Buffalo': 'https://www.linkedin.com/company/blue-buffalo-co',
    'Instinct Pet Food': 'https://www.linkedin.com/company/instinctpetfood',
    'Target Pets': 'https://www.linkedin.com/company/target',
    'Costco Pets': 'https://www.linkedin.com/company/costco-wholesale',
    'Paw.com': 'https://www.linkedin.com/company/pawdotcom',
    'Bivvy': 'https://www.linkedin.com/company/bivvy-pet-insurance',
    'Fetch by The Dodo': 'https://www.linkedin.com/company/fetch-pet-insurance',
    'PrettyLitter': 'https://www.linkedin.com/company/pretty-litter',
    'Furbo': 'https://www.linkedin.com/company/tomofun',
    'Catalyst Pet': 'https://lignetics.com/brands/catalyst-pet/',
    'Dr. Elsey\'s': 'https://www.linkedin.com/company/dr-elseys',
    'World\'s Best Cat Litter': 'https://www.linkedin.com/company/mpm-products-ltd',
    'Tidy Cats': 'https://www.linkedin.com/company/purina',
    'Arm & Hammer Pet Care': 'https://www.linkedin.com/company/church-&-dwight',
    'Pawp': 'https://www.linkedin.com/company/pawp',
    'Fuzzy': 'https://www.linkedin.com/company/fuzzy',
    'Care.com Pets': 'https://www.linkedin.com/company/care-com',
    'PetVet365': 'https://www.linkedin.com/company/petvet365',
    'Pumpkin Pet Insurance': 'https://www.linkedin.com/company/pumpkinpets',
    'Petplan': 'https://www.linkedin.com/company/petplanuk',
}

# Update the DataFrame
updated_count = 0
for company_name, linkedin_url in linkedin_updates.items():
    # Find the row for this company - use contains to match partial names
    mask = df['Company Name'].str.contains(company_name, na=False, case=False, regex=False)
    if mask.any():
        df.loc[mask, 'Primary Contact LinkedIn'] = linkedin_url
        updated_count += 1
        print(f"✓ Updated: {company_name}")
    else:
        print(f"✗ NOT FOUND: {company_name}")

# Save the updated CSV
df.to_csv('pet_ecommerce_ada_prospects.csv', index=False)
print(f"\n{'='*60}")
print(f"✅ CSV updated successfully!")
print(f"📊 Total companies with LinkedIn URLs: {df['Primary Contact LinkedIn'].notna().sum()}")
print(f"🔄 Updated in this run: {updated_count}")
print(f"{'='*60}")

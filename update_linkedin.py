import pandas as pd

# Read the CSV
df = pd.read_csv('pet_ecommerce_ada_prospects.csv')

# LinkedIn URLs found through web searches
linkedin_updates = {
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
    'Purina': 'https://www.comparably.com/companies/purina/executive-team',  # Thomas Douaihy VP Digital
    'Fi': 'https://www.crunchbase.com/person/loren-kirkby',  # Loren Kirkby CTO
    'Open Farm': 'https://www.linkedin.com/in/mark-sapir-204797',  # Mark Sapir CMO
}

# Update the DataFrame
for company_name, linkedin_url in linkedin_updates.items():
    # Find the row for this company
    mask = df['Company Name'] == company_name
    if mask.any():
        df.loc[mask, 'Primary Contact LinkedIn'] = linkedin_url
        print(f"Updated: {company_name}")
    else:
        print(f"NOT FOUND: {company_name}")

# Save the updated CSV
df.to_csv('pet_ecommerce_ada_prospects.csv', index=False)
print(f"\n✅ CSV updated successfully with {len(linkedin_updates)} LinkedIn URLs!")

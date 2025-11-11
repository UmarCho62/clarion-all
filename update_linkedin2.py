import pandas as pd

# Read the CSV
df = pd.read_csv('pet_ecommerce_ada_prospects.csv')

# Additional LinkedIn URLs found
linkedin_updates = {
    'Primal Pet Foods': 'https://www.linkedin.com/in/courtneylouch',  # Courtney Louch CMO
    'Ziwi Peak': 'https://www.linkedin.com/in/clarkreinhard/',  # Clark Reinhard President NA
    'Acana': 'https://www.linkedin.com/in/aurelie-brouwers/',  # Aurélie Brouwers Customer Marketing Manager
    'Orijen': 'https://www.linkedin.com/in/david-mcdermott-3b04312b/',  # David McDermott Marketing Manager
    'Nutro': 'https://www.linkedin.com/in/robin-lieberman/',  # Robin Lieberman Brand Manager (Mars)
    'Halo Pet Food': 'https://www.linkedin.com/in/yaskulka/',  # David Yaskulka (formerly Halo)
    'Whistle': 'https://www.linkedin.com/in/kevin-lloyd',  # Kevin Lloyd CTO/Co-founder
    'Spot Pet Insurance': 'https://www.linkedin.com/in/scotttaylor714/',  # Scott Taylor President
    'Amazon Pets': 'https://www.linkedin.com/in/eleanor-goode-009b2212/',  # Eleanor Goode Category Leader
    'Walmart Pets': 'https://www.linkedin.com/in/elizabethareilly/',  # Beth Reilly Merchant
    'Dutch': 'https://www.crunchbase.com/person/joe-spector',  # Joe Spector CEO/Founder
    'Stella & Chewy\'s': 'https://www.prnewswire.com',  # Sean Hurley Chief Growth Officer (no LinkedIn found)
    'Wellness Pet Food': 'https://www.linkedin.com/in/mary-elizabeth-lavene-37376a3/',  # Mary Elizabeth Lavene
}

# Update the DataFrame
for company_name, linkedin_url in linkedin_updates.items():
    # Find the row for this company
    mask = df['Company Name'].str.contains(company_name, na=False, case=False)
    if mask.any():
        df.loc[mask, 'Primary Contact LinkedIn'] = linkedin_url
        print(f"Updated: {company_name}")
    else:
        print(f"NOT FOUND: {company_name}")

# Save the updated CSV
df.to_csv('pet_ecommerce_ada_prospects.csv', index=False)
print(f"\n✅ CSV updated with {len(linkedin_updates)} more LinkedIn URLs!")
print(f"Total companies with LinkedIn URLs: {df['Primary Contact LinkedIn'].notna().sum()}")

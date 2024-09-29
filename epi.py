# Jamie Smith
# Find the EPIs

def identify_essential_prime_implicants(prime_implicants, minterm_mapping):
    """Identify essential prime implicants."""
    essential_implicants = set()
    covered_minterms = set()
    
    # Create a dictionary to count coverage of each minterm
    minterm_count = {minterm: 0 for minterm in minterm_mapping.keys()}
    
    # Debug: Print the initial mapping of minterms
    print("Minterm Mapping:", minterm_mapping)

    # Count the number of prime implicants covering each minterm
    for implicant in prime_implicants:
        # Check if the implicant is in the mapping
        if implicant in minterm_mapping:
            for minterm in minterm_mapping[implicant]:
                # Check if the minterm is valid
                if minterm in minterm_count:
                    minterm_count[minterm] += 1
                else:
                    print(f"Warning: Minterm {minterm} not found in minterm_count.")

    # Find essential prime implicants
    for implicant in prime_implicants:
        if implicant in minterm_mapping:
            for minterm in minterm_mapping[implicant]:
                if minterm_count[minterm] == 1:  # If this minterm is only covered by this implicant
                    essential_implicants.add(implicant)
                    covered_minterms.add(minterm)
                    
    return essential_implicants, covered_minterms

def create_prime_implicant_chart(prime_implicants, minterms):
    """Create a prime implicant chart."""
    chart = {implicant: [] for implicant in prime_implicants}
    
    for minterm in minterms:
        for implicant in prime_implicants:
            if minterm in minterm_mapping[implicant]:  # Check if the implicant covers the minterm
                chart[implicant].append(minterm)
                
    return chart

def select_essential_prime_implicants(chart):
    """Select essential prime implicants from the chart."""
    essential_implicants = set()
    
    while True:
        # Find any minterm that is covered by exactly one prime implicant
        minterm_to_implicant = {minterm: [] for minterm in chart.values()}
        
        for implicant, covered_minterms in chart.items():
            for minterm in covered_minterms:
                minterm_to_implicant[minterm].append(implicant)
        
        essential_found = False
        
        for minterm, implicants in minterm_to_implicant.items():
            if len(implicants) == 1:  # If there's only one implicant covering this minterm
                essential_implicants.add(implicants[0])
                essential_found = True
                # Remove this implicant from the chart
                for m in chart[implicants[0]]:
                    chart[implicants[0]].remove(m)
        
        if not essential_found:  # No more essential prime implicants can be found
            break
    
    return essential_implicants

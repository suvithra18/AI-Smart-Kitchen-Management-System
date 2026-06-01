from .models import KitchenItem


# =========================
# CARBON DATA
# CO2 PER KG
# =========================

CARBON_DATA = {

    'rice': 2.7,

    'chicken': 6.9,

    'beef': 27.0,

    'milk': 3.2,

    'vegetables': 1.5,

    'egg': 4.8,

    'bread': 1.3,

    'fish': 5.4,

    'wheat': 1.4,

    'paneer': 8.0
}


# =========================
# ECO IMPACT AI
# =========================

def calculate_carbon_footprint():

    items = KitchenItem.objects.all()

    total_carbon = 0

    waste_score = 0

    sustainability_score = 100

    reports = []

    for item in items:

        ingredient = item.name.lower()

        quantity = item.quantity

        # =====================
        # CARBON CALCULATION
        # =====================

        if ingredient in CARBON_DATA:

            carbon_value = CARBON_DATA[
                ingredient
            ]

            carbon_output = (
                quantity / 1000
            ) * carbon_value

            total_carbon += carbon_output

            reports.append({

                'ingredient': ingredient,

                'carbon':
                    round(carbon_output, 2)
            })

        # =====================
        # FOOD WASTE
        # =====================

        if quantity > 1000:

            waste_score += 10

            sustainability_score -= 5

        # =====================
        # HIGH EMISSION FOODS
        # =====================

        if ingredient in [

            'beef',
            'chicken'
        ]:

            sustainability_score -= 10

    # =====================
    # FINAL ECO STATUS
    # =====================

    if total_carbon < 10:

        eco_status = 'Excellent 🌱'

    elif total_carbon < 25:

        eco_status = 'Moderate 🌿'

    else:

        eco_status = 'High Emission ⚠'

    return {

        'total_carbon':
            round(total_carbon, 2),

        'waste_score':
            waste_score,

        'sustainability_score':
            sustainability_score,

        'eco_status':
            eco_status,

        'reports':
            reports
    } 
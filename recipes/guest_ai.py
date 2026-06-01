# =========================
# INGREDIENT SCALING AI
# =========================

def scale_recipe(

    original_persons,

    target_persons,

    ingredients
):

    scaled_items = []

    for item in ingredients:

        ingredient_name = item['name']

        quantity = float(
            item['quantity']
        )

        unit = item['unit']

        # =====================
        # SCALING FORMULA
        # =====================

        new_quantity = (

            target_persons /

            original_persons

        ) * quantity

        scaled_items.append({

            'name': ingredient_name,

            'old_quantity': quantity,

            'new_quantity':

                round(new_quantity, 2),

            'unit': unit
        })

    return scaled_items
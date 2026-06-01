def health_recommendation(nutrition):

    recommendations = []

    # =====================
    # LOW PROTEIN
    # =====================

    if nutrition['protein'] < 50:

        recommendations.append({

            'type': 'Low Protein',

            'foods': [

                'Egg',

                'Chicken',

                'Paneer',

                'Soya',

                'Peanuts'
            ]
        })

    # =====================
    # LOW IRON
    # =====================

    if nutrition['iron'] < 10:

        recommendations.append({

            'type': 'Low Iron',

            'foods': [

                'Spinach',

                'Dates',

                'Beetroot',

                'Pomegranate'
            ]
        })

    # =====================
    # HIGH FAT
    # =====================

    if nutrition['fat'] > 80:

        recommendations.append({

            'type': 'High Fat',

            'foods': [

                'Salad',

                'Fruits',

                'Green Tea',

                'Oats'
            ]
        })

    # =====================
    # LOW VITAMINS
    # =====================

    if nutrition['vitamins_count'] < 2:

        recommendations.append({

            'type': 'Low Vitamins',

            'foods': [

                'Orange',

                'Carrot',

                'Tomato',

                'Banana'
            ]
        })

    return recommendations
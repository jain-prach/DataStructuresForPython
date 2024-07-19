import pandas as pd
import numpy as np
# cake recommendation system

## this code is incomplete but explains usage of boolean values by designing a compatibility matrix
# sweet baked goods - the list is only made taking in mind ingredients accessible to my mom

""" sweet_bakes = ['muffins', 'brownies', 'cakes', 'cookies', 'cheese-cakes', 'donuts', 'cupcakes', 'jar-cakes']
flavors = ['butterscotch', 'strawberry', 'pineapple', 'blueberry', 'vanilla', 'chocolate', 'red velvet', 'coffee', 'coconut', 'pistachio', 'rose', 'walnut', 'raisin', 'lemon', 'oreo', 'black forest', 'biscoff', 'nutella', 'caramel']
flour = ['wheat', 'all purpose', 'ragi', 'jowar', 'oats']
sweetners = ['sugar', 'gud', 'dates', 'honey']
dairy = ['oil', 'ghee', 'water', 'milk', 'plant-based milk']
occasions = ['office party', 'Promotion', 'diwali gifts', 'return gifts', 'birthday party', 'christmas', 'new year', 'Baby showers', 'wedding party', 'Couple Anniversary party', 'closed one\'s birthday', 'just because..', 'Valentine\'s Day celebration', 'Mother\'s Day', 'Father\'s Day', 'Friendship Day', 'Galentine\'s Day', 'Teacher\'s Day', 'Daughter\'s Day', 'Children\'s Day', 'Grandparent\'s Day', 'House party', 'Fresher\'s Party', 'Farewell Party', 'Corporate Anniversary party', 'Reunion Party', 'Graduation Party', 'Alumni Meet', 'Grand Opening', 'Engagement Party']
decorations = ['designer toppers', 'designer boxes', 'designer base', 'flowers', 'budget toppers', 'budget boxes', 'budget base', 'overloaded cake'] """

def set_combination(matrix, combination_list, value):
    for item in combination_list:
        matrix.at[item[0], item[1]] = value
        matrix.at[item[1], item[0]] = value

# compatibility matrix of flavors and flours
flavor_flour_list = ['butterscotch', 'strawberry', 'pineapple', 'blueberry', 'vanilla', 'chocolate', 'red velvet', 'coffee', 'coconut', 'pistachio', 'rose', 'walnut', 'raisin', 'lemon', 'oreo', 'black forest', 'biscoff', 'nutella', 'caramel', 'wheat', 'all purpose', 'ragi', 'jowar', 'oats']
compatibility_matrix = pd.DataFrame(False, index=flavor_flour_list, columns=flavor_flour_list, dtype=bool)

#set all purpose flour to true for all
compatibility_matrix.loc['all purpose', :] = True
compatibility_matrix.loc[:, 'all purpose'] = True
# flavors that goes well with each other
true_combinations = [('butterscotch', 'vanilla'), ('strawberry', 'vanilla'), ('strawberry', 'chocolate'), ('pineapple', 'vanilla'), ('blueberry', 'vanilla'), ('blueberry', 'lemon'), ('vanilla', 'chocolate'), ('vanilla', 'raisin'), ('vanilla', 'biscoff'), ('vanilla', 'caramel'), ('vanilla', 'wheat'), ('vanilla', 'oats'), ('chocolate', 'coffee'), ('chocolate', 'coconut'), ('chocolate', 'walnut'), ('chocolate', 'black forest'), ('chocolate', 'nutella'), ('chocolate', 'wheat'), ('chocolate', 'oats'), ('coffee', 'walnut'), ('coffee', 'raisin'), ('coffee', 'biscoff'), ('coffee', 'nutella'), ('coffee', 'caramel'), ('coconut', 'rose'), ('pistachio', 'rose'), ('walnut', 'biscoff'), ('walnut', 'nutella'), ('walnut', 'caramel')]
set_combination(compatibility_matrix, true_combinations, True)

np.fill_diagonal(compatibility_matrix.values, False)
# print(compatibility_matrix)

print(flavor_flour_list, end="\n\n")
selection1 = str(input("Select your flavor or flour (string input): ")).lower()

if selection1 in flavor_flour_list:
    available_options = compatibility_matrix.columns[compatibility_matrix.loc[selection1] == True]
    print(f"Available options for flavor combinations: {available_options.tolist()}\n\n")
    selection2 = str(input("Select another flavor if you desire (string input) or type 0 if you want to explore all cakes for selected flavor: ")).lower()

    cakes_dict = {flavor: [] for flavor in flavor_flour_list}
    
    #add cakes
    cakes_dict['butterscotch'] = ['butterscotch mania', 'butterscotch delight']
    cakes_dict['strawberry'] = []
    cakes_dict['pineapple'] = []
    cakes_dict['blueberry'] = []
    cakes_dict['vanilla'] = []

    if selection2 == str(0):
        print(f"Cakes available for {selection1}: {cakes_dict[selection1]}\n\n")
    else:
        #compare selected_flavor and selection2 dict values and print the values that intersect with each other
        if selection2 in cakes_dict:
            common_cakes = list(set(cakes_dict[selection1]) & set(cakes_dict[selection2]))
            print(f"Cakes available for {selection1} and {selection2}: {common_cakes}")
        else:
            print("Invalid selection")
else:
    print("Invalid Selection")

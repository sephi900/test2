import pandas as pd
import numpy as np
import timeit
import random
import collections

def random_gen(numberof_fam, fam = []):
    for i in range(numberof_fam):
        fam.append(random.randint(1, 5))
    return fam

def range_prices(variance=int, price=int):
        if variance == 0:
            min_price = 1
            max_price = 5
        elif variance == 1 and price == 1:
            min_price = 1
            max_price = 2
        elif variance == 1 and price == 5:
            min_price = 4
            max_price = 5
        elif variance == 2 and price == 1:
            min_price = 1
            max_price = 3
        elif variance == 2 and price == 5:
            min_price = 3
            max_price = 5
        elif variance == 1 and price == 2:
            if random.randint(1, 2) == 1:
                min_price = 1
                max_price = 2
            else:
                min_price = 2
                max_price = 3
        elif variance == 1 and price == 3:
            if random.randint(1, 2) == 1:
                min_price = 2
                max_price = 3
            else:
                min_price = 3
                max_price = 4
        elif variance == 1 and price == 4:
            if random.randint(1, 2) == 1:
                min_price = 3
                max_price = 4
            else:
                min_price = 4
                max_price = 5
        elif variance == 2 and price == 2:
            if random.randint(1, 2) == 1:
                min_price = 1
                max_price = 3
            else:
                min_price = 2
                max_price = 4
        elif variance == 2 and price == 3:
            if random.randint(1, 3) == 1:
                min_price = 1
                max_price = 3
            elif random.randint(2, 3) == 2:
                min_price = 2
                max_price = 4
            else:
                min_price = 3
                max_price = 5
        elif variance == 2 and price == 4:
            if random.randint(1, 2) == 1:
                min_price = 2
                max_price = 4
            else:
                min_price = 3
                max_price = 5
        elif variance == 99:
            min_price = 1
            max_price = 5
        return min_price, max_price

    # initiate timer
starttime = timeit.default_timer()

    # read CSV Files
design_df = pd.read_csv("OriginalDesignV2.csv")
prices_df = pd.read_csv("Prices.csv")
info_df = pd.read_csv("info.csv")

    # Initiate variables/arrays in Design
version_d = design_df.iloc[0:, 0:1].values
task_d = design_df.iloc[0:, 1:2].values
concept_d = design_df.iloc[0:, 2:3].values
SKU_d = design_df.iloc[0:, 3:4].values

    # Initiate Variables/Arrays in Prices
SKU_p = prices_df.iloc[0:, 0:1].values
family_p = prices_df.iloc[0:, 2:3].values

    # Initiate Variables/Arrays in Info
task_i = info_df.iloc[0:, 0:1].values
variance_i = info_df.iloc[0:, 2:3].values

number_of_designs = max(version_d).item()   # Versions
number_of_tasks = max(task_d).item()        # Tasks
number_of_concepts = max(concept_d).item()  # concepts
number_of_SKUs = max(SKU_p).item()
number_of_fam = max(family_p).item()        # Number of families
number_of_pp = 5
max_pp_SKU = [None]*number_of_SKUs

for z in range(number_of_SKUs):
    max_pp_SKU[z] = round((np.count_nonzero(SKU_d == z+1, axis=0).item()/number_of_pp)+0.5,0)

position = 0
price = []
new_price = 0
starting_price = []
fam = []

pp = np.zeros((number_of_SKUs,number_of_pp))

for i in range(number_of_designs):
    current_design = i
    for k in range(number_of_tasks):
        fam = []
        a = []
        for q in range(number_of_fam):
            fam.append(random.randint(1, 5))
        starting_price = []
        min_pricex = [0]*11
        max_pricex = [0]*11
        current_variance = variance_i[k].item()
        # if current_variance == 0:
        #     fam = []
        #     for q in range(number_of_fam):
        #         fam.append(random.randint(1, 5))
        for w in range(number_of_fam):
            if current_variance == 0:
                starting_price.append(fam[w])
            else:
                min_pricex[w], max_pricex[w] = range_prices(current_variance,fam[w])
        # print(min_pricex, max_pricex)
            # elif  current_variance == 1 and fam[w] ==1:
            #     min_price[w] = 1
            #     max_price[w] = 2
            # elif  current_variance == 1 and fam[w] ==5:
            #     min_price[w] = 4
            #     max_price[w] = 5
            # elif  current_variance == 2 and fam[w] ==1:
            #     min_price[w] = 1
            #     max_price[w] = 3
            # elif  current_variance == 2 and fam[w] ==5:
            #     min_price[w] = 3
            #     max_price[w] = 5
            # elif current_variance == 1 and fam[w] == 2:
            #     if random.randint(1,2) == 1:
            #         min_price[w] = 1
            #         max_price[w] = 2
            #     else:
            #         min_price[w] = 2
            #         max_price[w] = 3
            # elif current_variance == 1 and fam[w] == 3:
            #     if random.randint(1,2) == 1:
            #         min_price[w] = 2
            #         max_price[w] = 3
            #     else:
            #         min_price[w] = 3
            #         max_price[w] = 4
            # elif current_variance == 1 and fam[w] == 4:
            #     if random.randint(1,2) == 1:
            #         min_price[w] = 3
            #         max_price[w] = 4
            #     else:
            #         min_price[w] = 4
            #         max_price[w] = 5
            # elif current_variance == 2 and fam[w] == 2:
            #     if random.randint(1,2) == 1:
            #         min_price[w] = 2
            #         max_price[w] = 4
            #     else:
            #         min_price[w] = 1
            #         max_price[w] = 3
            # elif current_variance == 2 and fam[w] == 3:
            #     if random.randint(1,3) == 1:
            #         min_price[w] = 3
            #         max_price[w] = 5
            #     elif random.randint(2,3) == 2:
            #         min_price[w] = 1
            #         max_price[w] = 3
            #     else:
            #         min_price[w] = 2
            #         max_price[w] = 4
            # elif current_variance == 2 and fam[w] == 4:
            #     if random.randint(1,2) == 1:
            #         min_price[w] = 3
            #         max_price[w] = 5
            #     else:
            #         min_price[w] = 2
            #         max_price[w] = 4
            # elif current_variance == 99:
            #     min_price[w] = 1
            #     max_price[w] = 5
            # print(starting_price)
        for y in range(number_of_concepts):                         # current Concept
            start = 0
            current_sku = SKU_d[position].item()
            current_family = family_p[current_sku-1].item()
            if current_variance == 0:
                starting_price2 = starting_price[current_family-1]
                # if pp[current_sku - 1, starting_price2 - 1] <= max_pp_SKU[current_sku - 1]:
                start = starting_price2
                pp[current_sku - 1, start - 1] += 1
                # else:
                #     correct = False
                #     p=0
                #     while correct == False:
                #         starting_price[current_family - 1] = random.randint(1, 5)
                #         starting_price2 = starting_price[current_family - 1]
                #         p += 1
                #         if p >= 5:
                #             start = starting_price2
                #             pp[current_sku - 1, start - 1] += 1
                #             break
                #         elif pp[current_sku - 1, starting_price2 - 1] <= max_pp_SKU[current_sku - 1]:
                #             correct = True
                #             start = starting_price2
                #             pp[current_sku - 1, start - 1] += 1
            else:
                starting_price2 = random.randint(min_pricex[current_family-1],max_pricex[current_family-1])
                if pp[current_sku-1, starting_price2-1]<= max_pp_SKU[current_sku-1]:
                    start = starting_price2
                    pp[current_sku - 1, start - 1] += 1
                else:
                    correct = False
                    p=0
                    while correct == False:
                        starting_price2 = random.randint(min_pricex[current_family - 1], max_pricex[current_family - 1])
                        p += 1
                        if p >= 2:
                            start = starting_price2
                            pp[current_sku - 1, start - 1] += 1
                            break
                        elif pp[current_sku - 1, starting_price2 - 1] <= max_pp_SKU[current_sku - 1]:
                            correct = True
                            start = starting_price2
                            pp[current_sku - 1, start - 1] += 1
            price.append(start)
            position += 1

            # else:
            #     starting_price2 = random.randint(min_price[current_family-1],max_price[current_family-1])
            #     if pp[current_sku-1, starting_price2-1]<= max_pp_SKU[current_sku-1]:
            #         start = starting_price2
            #         pp[current_sku - 1, start - 1] += 1
print(pp)
#
    # Add Price Column to Original Design
design_df.loc[:,'Price'] = price

    # Write Final Design to CSV
design_df.to_csv('FinalDesign.csv')

    # Print processing time
print("Run Time was:", round((timeit.default_timer() - starttime)*1000, 2), "ms or ", round((timeit.default_timer() - starttime),2), "s")

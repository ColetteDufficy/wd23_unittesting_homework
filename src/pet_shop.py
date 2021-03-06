# WRITE YOUR FUNCTIONS HERE
from logging import addLevelName


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
        pet_shop["admin"]["total_cash"] = pet_shop["admin"]["total_cash"] + cash
        return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num_of_pets_sold):    
    pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + num_of_pets_sold
    return pet_shop["admin"]["pets_sold"]
    
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_type):
    same_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_type:
            same_breed.append(pet)
    return same_breed


# def get_pets_by_breed(pet_shop, animal_breed):
    # num_of_breed = []
    # for pets in pet_shop["pets"][0]["breed"]:
    #     for pet in pets:
    #         if breed_type != None:
    #             num_of_breed.append(pet)
    # return len(num_of_breed)
        

# def get_pets_by_breed(pet_shop, animal_breed):
#     num_of_breed = []
#     for pet in pet_shop:
#         if animal_breed in pet:
#             # for animal_breed in "breed".items():
#             #     return animal_breed
#             num_of_breed.append(animal_breed)
#             return len(num_of_breed)



                
def find_pet_by_name(pet_shop, pet_name):
    # breakpoint()
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet  # ***** why does this return JUST a name, rather than the whole dict????**** 


def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)
    find_pet_by_name(pet_shop, pet_name)
    return pet 

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    get_stock_count(pet_shop)
        
def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash_to_remove):
    cash_to_remove = 100
    customers["cash"] -= cash_to_remove

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)    
    get_customer_pet_count(customer)


# --- OPTIONAL ---
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"]>= new_pet["price"]:
        return True
    return False

# These are 'integration' tests so we want multiple asserts.
def sell_pet_to_customer(pet_shop, pet_name, customer):
    
    # input_record_store["money"] += record_to_sell["price"]
    # input_record_store["records"].remove(record_to_sell)   
    
    
    # breakpoint()
    find_pet_by_name(pet_shop, pet_name)
    add_pet_to_customer(customer, pet_name)
    get_customer_pet_count(customer)
    get_pets_sold(pet_shop)
    get_customer_cash(customer)
    get_total_cash(pet_shop)


    




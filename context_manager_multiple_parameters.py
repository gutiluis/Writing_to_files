import logging
import os
import sys

logging.basicConfig(level=logging.INFO)

def update_inventory():
    if not os.path.exists("database.txt"):
        with open("database.txt", "w") as file:
            file.write("product_id,product_quantity,product_price,date_updated\n")
        logging.info("Database initialized.")
    else:
        logging.info("Database already exists.")    

def add_inventory(product_id,product_quantity,product_price,date_updated):
    with open("database.txt", "a") as file:
        file.write(f"{product_id},{product_quantity},{product_price},{date_updated}\n")        
    logging.info("Product added.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        update_inventory()
    
    elif len(sys.argv) == 5:
        update_inventory()
        add_inventory(*sys.argv[1:])
    
    else:
        logging.info("How to use:")
        logging.info("- python3 script.py               # initialize database")
        logging.info("""- python3 script.py <product_id> <product_quantity> <product_price> <date_updated>
                     Running the the script with the 4 arguments afterwards will automatically add the headers
                     from the update_inventory() function""")
# Create an empty dictionary
rental_properties = {}

# Set a flag to indicate we taking applications
rental_open = True

while rental_open:
    username = input("\nY tu nombre :3? ")
    rental_property = input("Menciona tu direccion...)



    #store the responses in a dictionary
    rental-properties[username] = rental_property



# ask if the user knows anyone else looking to rent a property
    repeat = input("\n ¿Conoce a alguien a quien le gustaría alquilar?)
    if repeat = 'no':
                rental_open = False



    # adding property is complete



print("\n—Property to rent—")
for username, rental_property in rental_properties.items():
    print(username + " has " + rental_property + " to rent.")
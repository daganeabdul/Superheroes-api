from app import app, db
from models import Hero, Power

with app.app_context():

    db.drop_all()
    db.create_all()

  
    heroes = [
        Hero(name="Abdirahman Hassan", super_name="The Desert Falcon"),
        Hero(name="Amina Noor", super_name="Shadow Queen"),
        Hero(name="Juma Mwangi", super_name="Iron Fist"),
        Hero(name="Fatuma Ali", super_name="Storm Caller"),
        Hero(name="Otieno Odhiambo", super_name="Mind Bender"),
        Hero(name="Njeri Wambui", super_name="Night Watcher"),
        Hero(name="Khalid Musa", super_name="Blaze"),
        Hero(name="Zainab Omar", super_name="Wind Whisperer"),
        Hero(name="Said Abdalla", super_name="Ocean Guard"),
        Hero(name="Halima Farah", super_name="Light Weaver")
    ]

   
    powers = [
        Power(
            name="super strength",
            description="Gives the hero extraordinary physical strength beyond human limits."
        ),
        Power(
            name="flight",
            description="Allows the hero to fly freely through the sky at very high speeds."
        ),
        Power(
            name="mind control",
            description="Enables the hero to influence and control the thoughts of others."
        ),
        Power(
            name="weather manipulation",
            description="Allows the hero to control wind, rain, thunder, and lightning."
        )
    ]

    db.session.add_all(heroes + powers)
    db.session.commit()

    print("Database seeded successfully!")

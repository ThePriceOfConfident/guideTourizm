from django.core.management.base import BaseCommand
from Destination.models import Destination
 

class Command(BaseCommand):
    help = 'Populates the database with predefined destination data'

    def handle(self, *args, **options):
        destinations_data = [
            {"name": "Galata Tower", "location": "Istanbul", "description": "An iconic medieval stone tower that dominates the skyline of Istanbul, offering panoramic vistas of the Old City and the surrounding areas.", "address": "Bereketzade, Galata Kulesi, 34421 Beyoğlu/İstanbul", "contact_phone": "+902122450050", "contact_email": "info@galatatower.com", "website": "https://www.galatatower.com", "cover_image": "galata_tower.jpg"},
            {"name": "Mount Nemrut", "location": "Adıyaman", "description": "A high mountain hosting large statues erected around what is believed to be a royal tomb from the 1st century BC. The site offers stunning sunrise and sunset views.", "address": "Kahta, Adıyaman Province", "contact_phone": "+904122312345", "contact_email": "info@nemrut.com", "website": "http://www.nemrut.com", "cover_image": "mount_nemrut.jpg"},
            {"name": "Aspendos Theatre", "location": "Antalya", "description": "A remarkably well-preserved Roman theatre known for its magnificent acoustics, hosting many international opera and ballet festivals.", "address": "Aspendos, Serik, Antalya", "contact_phone": "+902422561234", "contact_email": "contact@aspendos.com", "website": "http://www.aspendostheatre.com", "cover_image": "aspendos_theatre.jpg"},
            {"name": "Patara Beach", "location": "Antalya", "description": "One of the longest beaches in the Mediterranean, famous for its golden sand and historical ruins, including a well-preserved amphitheatre and lighthouse.", "address": "Patara, Gelemiş, Antalya Province", "contact_phone": "+902856123456", "contact_email": "info@patarabeach.com", "website": "http://www.patarabeach.com", "cover_image": "patara_beach.jpg"},
            {"name": "Sumela Monastery", "location": "Trabzon", "description": "A stunning Greek Orthodox monastery built into the cliffs of the Altındere Valley in Trabzon, offering breathtaking views and rich frescoes inside.", "address": "Altındere Valley National Park, Maçka, Trabzon", "contact_phone": "+904622345678", "contact_email": "info@sumelamonastery.com", "website": "http://www.sumelamonastery.com", "cover_image": "sumela_monastery.jpg"},
            {"name": "Ani Ruins", "location": "Kars", "description": "The hauntingly beautiful remains of Ani, a medieval Armenian city that stood on various trade routes, showcasing numerous churches, mosques, and caravanserais.", "address": "Ocaklı, Kars", "contact_phone": "+904742312345", "contact_email": "info@aniruins.com", "website": "http://www.aniruins.com", "cover_image": "ani_ruins.jpg"},
            {"name": "Library of Celsus", "location": "Ephesus, Izmir", "description": "An ancient Roman building in Ephesus, originally built to store thousands of scrolls and serve as a monumental tomb for Celsus, a Roman senator.", "address": "Ephesus, Selçuk, İzmir", "contact_phone": "+902328965432", "contact_email": "info@libraryofcelsus.com", "website": "http://www.libraryofcelsus.com", "cover_image": "library_of_celsus.jpg"},
            {"name": "Pergamon Acropolis", "location": "Bergama, Izmir", "description": "The ancient acropolis of Pergamon, an important cultural center of the Hellenistic period, containing temples, theatres, and a famous library.", "address": "Bergama, Izmir", "contact_phone": "+902327676543", "contact_email": "contact@pergamonacropolis.com", "website": "http://www.pergamonacropolis.com", "cover_image": "pergamon_acropolis.jpg"},
            {"name": "Hierapolis", "location": "Pamukkale, Denizli", "description": "An ancient Greco-Roman city located on hot springs in classical Phrygia, famous for its sacred hot springs and large necropolis.", "address": "Pamukkale, Denizli", "contact_phone": "+902582713456", "contact_email": "info@hierapolis.com", "website": "http://www.hierapolis.com", "cover_image": "hierapolis.jpg"},
            {"name": "Troy", "location": "Çanakkale", "description": "The legendary city of Troy, known for the Trojan War described in the Greek Epic Cycle and especially in the Iliad, one of the two epic poems attributed to Homer.", "address": "Tevfikiye, Çanakkale Province", "contact_phone": "+902862145678", "contact_email": "info@troy.com", "website": "http://www.troy.com", "cover_image": "troy.jpg"}
            # Add more entries as needed...
        ]

        for data in destinations_data:
            destination = Destination(
                name=data['name'],
                description=data['description'],
                location=data['location'],
                address=data['address'],
                contact_phone=data['contact_phone'],
                contact_email=data['contact_email'],
                website=data['website'],
                # Assuming images are manually handled or script-uploaded separately
            )
            destination.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created destination {destination.name}'))

        # Uncomment and modify the following if you manage images:
        # with open('path/to/your/local/static/images/' + data['cover_image'], 'rb') as f:
        #     destination.cover_image.save(data['cover_image'], File(f), save=True)

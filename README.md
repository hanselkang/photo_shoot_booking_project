<div align="center">
  
# Photo Shoot Booking App
## Book a photo shoot in Edinburgh

</div>
  
## Features
----------
* Clients can register their information then book a photo shoot. The booking will go into booking waiting list in Photographer's page.
* CRUD for DB of Photographers, Bookings, Clients, and Services in photorapher's page.
* Photographers can reach clients information and booking waiting list.
* Photographers can confirm/edit/delete bookings.
* Confirmed booking list is shown on clients' page with hidden information.
* Photo shoot places map for Photographers and Clients (No API)

## Technology
----------
* Python
* Flask
* Jinja 
* PostgreSQL
* Psycopg
* HTML
* CSS

<div align="center">

![1](https://user-images.githubusercontent.com/43307207/166240099-abe35a13-3fb6-4415-b891-cd6bc8369702.gif)

  Client's Demo
  
  
  <br>
  <br>
  <br>
  <br>
  

![2](https://user-images.githubusercontent.com/43307207/166240124-14bd6e2e-4ea9-4a8c-9ffb-eb2db5bdcebf.gif)
  
  Photographer's Demo
  
  
  <br>
  <br>
  <br>
  <br>
  

![3](https://user-images.githubusercontent.com/43307207/166240150-05c530e4-4e5c-4f4d-8f99-9988dc14268e.gif)

  CRUD in Photographer's page
  
  
  <br>
  <br>
  <br>
  <br>
  

![4](https://user-images.githubusercontent.com/43307207/166240205-0a877c0e-4bd1-4f02-8c88-2a699197874e.gif)
            
  Process of designing photo shoot spots in booking page
  
  <br>
  <br>
  <br>
  <br>
  
  
![wireframe](https://user-images.githubusercontent.com/43307207/166315200-b4280490-f6e4-47d6-babb-ce40c50aa6b0.gif)

  Wireframe Design
  
  
  <br>
  <br>
            
</div>


## Deployment
----------
### To deploy this project run

```

Your local machine terminal:
- git clone https://github.com/hanselkang/photo_shoot_booking_project.git
- createdb photoshoot.sql (create db)
- psql -d photoshoot -f db/photoshoot.sql (reset tables)
- python3 console.py (insert sql dummy data)
- flask run

```

## Code for Photo shoot spots on the map in bookings_controller.py
----------

```

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    name = request.form["name"]
    places = []
    if request.form.get("circuslane"):
        places.append("CircusLane ")
    if request.form.get("deanvillage"):
        places.append("DeanVillage ")
    if request.form.get("newtown"):
        places.append("NewTown ")
    if request.form.get("caltonhill"):
        places.append("CaltonHill ")
    if request.form.get("princesstreet"):
        places.append("PrincesStreetGarden ")
    if request.form.get("oldtown"):
        places.append("OldTown ")
    if request.form.get("grassmarket"):
        places.append("Grassmarket ")
    if request.form.get("holyroodpark"):
        places.append("HolyroodPark ")
    str_places = ''
    for place in places:
        str_places += place
    num_of_group = request.form["num_of_group"]
    photoshoot_start_time = request.form["photoshoot_start_time"]
    photoshoot_end_time = request.form["photoshoot_end_time"]

    client_id = request.form["client_id"]
    service_id = request.form["service_id"]
    photographer_id = request.form["photographer_id"]

    client = client_repository.select(client_id)
    service = service_repository.select(service_id)
    photographer = service_repository.select(photographer_id)
    new_booking = Booking(name, str_places, num_of_group, photoshoot_start_time,
                          photoshoot_end_time, client, service, photographer)
    booking_repository.save(new_booking)
    return redirect("/bookings/clients_booking_list")
   
```


## Table HTML for photo shoot spots on the map
----------

```
<table class="map">
    <thead>
        <tr>
            <th colspan="6"></th>
        </tr>
    </thead>
    <tbody>
        <tr class="tr1">
            <td></td>
            <td>{% if "CircusLane" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">Circus Lane</div class="map">
                {% endif %}
            </td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td>{% if "NewTown" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">New Town</div class="map">
                {% endif %}
            </td>
            </td>
            <td>{% if "CaltonHill" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">Calton Hill</div class="map">
                {% endif %}
            </td>
            </td>
            <td></td>
            <td></td>
        </tr>
        <tr class="tr3">
            <td>{% if "DeanVillage" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">DeanVillage</div class="map">
                {% endif %}
            </td>
            </td>
            <td></td>
            <td>{% if "PrincesStreetGarden" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">Prices Street Garden</div class="map">
                {% endif %}
            </td>
            </td>
            <td>{% if "OldTown" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">Old Town</div class="map">
                {% endif %}
            </td>
            </td>
            <td></td>
            <td></td>
        </tr>
        <tr class="tr3">
            <td></td>
            <td></td>
            <td>{% if "Grassmarket" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">Grassmarket</div class="map">
                {% endif %}
            </td>
            </td>
            <td></td>
            <td>{% if "HolyroodPark" in booking_confirmation.places
                :%}
                <div class="dot">●</div>
                <div class="map">Holyrood Park</div class="map">
                {% endif %}
            </td>
            </td>
            <td></td>
        </tr>
        <tr class="tr4">
            <td colspan="6"></td>
        </tr>
    </tbody>
</table>
            
 
```

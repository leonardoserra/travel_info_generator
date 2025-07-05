import os
import sys
import argparse

from pathlib import Path

def main(args):
    try:
        generate_markdown(args)
        return 0

    except Exception as e:
        print(str(e))
        return 1


def generate_markdown(params):

    content = generate_content(params)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = f"{current_dir}/reports/"
    Path(reports_dir).mkdir(parents=True, exist_ok=True)
    file_name = f"{params.destination}.md"
    with open(os.path.join(reports_dir, file_name), 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"{file_name} generated!")


def generate_notes(notes):
    return f"""__Notes__: 
>{notes}
"""


def generate_content(params):
    notes = generate_notes(params.notes) if params.notes else ""
    desire_to_visit = params.desire_lv_to_visit / params.number_of_people

    tot = round(
        (
            params.avg_nightly_cost 
            * params.number_of_nights
        ) 
        + params.car_rental_cost
        + params.price_outward_journey
        + params.price_return_journey
        + params.home_airport_journey_cost,
        2
    )

    return f"""# {params.destination}

*Voglia di andarci*: _{desire_to_visit}/10_  
*Numero Notti*: _{params.number_of_nights}_  

### Andata: **{params.departure_date}** - _{params.price_outward_journey}€_  
>**Partenza**: {params.departure_airport_outward_journey} **{params.departure_time_outward_journey}**  
>**Arrivo**: {params.arrival_airport_outward_journey} **{params.arrival_time_outward_journey}**  

### Ritorno: **{params.return_date}** - _{params.price_return_journey}€_  
>**Partenza**: {params.departure_airport_return_journey} **{params.departure_time_return_journey}**  
>**Arrivo**: {params.arrival_airport_return_journey} **{params.arrival_time_return_journey}**  

__Bagaglio__  
>10kg: {params.baggage_cost}€  

__Costo Medio a notte__  
>{params.avg_nightly_cost}€ per {params.number_of_people} persone.  

__Costo Noleggio Veicolo__  
>{params.car_rental_cost}€ per {params.number_of_nights - 1 } giorni.  

__Costo Tragitto Casa Aeroporto__  
>{params.home_airport_journey_cost}€ treno o auto + casello + taxi o bus o navette varie.  

__COSTI per {params.number_of_nights} notti__  
>Totale: {tot}€  
>Tot a persona: {round(tot / params.number_of_people, 2)}€  
>Tot a notte per persona : {round(tot / params.number_of_people / params.number_of_nights)}€  

{notes}"""


def cli():
    parser = argparse.ArgumentParser(description="It generates a travel report based on the input provided.")

    parser.add_argument('destination')

    parser.add_argument('number_of_people', type=int, default=1)
    parser.add_argument('number_of_nights', type=int, default=1)
    parser.add_argument('desire_lv_to_visit', type=int, default=1)
    parser.add_argument('departure_date')
    parser.add_argument('return_date')

    parser.add_argument('departure_airport_outward_journey')
    parser.add_argument('departure_time_outward_journey')
    parser.add_argument('arrival_airport_outward_journey')
    parser.add_argument('arrival_time_outward_journey')
    parser.add_argument('price_outward_journey', type=float, default=0.00)

    parser.add_argument('departure_airport_return_journey')
    parser.add_argument('departure_time_return_journey')
    parser.add_argument('arrival_airport_return_journey')
    parser.add_argument('arrival_time_return_journey')
    parser.add_argument('price_return_journey', type=float, default=0.00)

    parser.add_argument('baggage_cost', type=float, default=0.00)
    parser.add_argument('avg_nightly_cost', type=float, default=0.00)
    parser.add_argument('car_rental_cost', type=float, default=0.00)
    parser.add_argument('home_airport_journey_cost', type=float, default=0.00)
    parser.add_argument('--notes', required=False)

    return parser.parse_args()


if __name__ == '__main__':

    args = cli()

    code = main(args)

    sys.exit(code)

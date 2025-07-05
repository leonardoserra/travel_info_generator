# What's that:
It takes info about your next travel and generate a small report, so you can think about different destinations with some comparison.  

then you can merge the single reports into a big one.  

For info on how to use write in terminal  
- `python travel_info_generator.py --help`  

```bash
It generates a travel report based on the input provided.

positional arguments:
  destination
  number_of_people
  number_of_nights
  desire_lv_to_visit
  departure_date
  return_date
  departure_airport_outward_journey
  departure_time_outward_journey
  arrival_airport_outward_journey
  arrival_time_outward_journey
  price_outward_journey
  departure_airport_return_journey
  departure_time_return_journey
  arrival_airport_return_journey
  arrival_time_return_journey
  price_return_journey
  baggage_cost
  avg_nightly_cost
  car_rental_cost
  home_airport_journey_cost

options:
  -h, --help            show this help message and exit
  --notes NOTES
```

Example usage  
`python travel_info_generator.py "Valencia" 2 7 16 Sabato-27/09 Domenica-05/10 "Milano Bergamo" 14:40 "Valencia" 16:40 36.99 "Valencia" 09:10 "Milano Bergamo" 11:00 26.19 27.75 90 0 130 --notes "Ricorda di controllare il gli scioperi dei voli"`  

> This will generate a file called `Valencia.md` in the `reports` folder. Like this:

___

# Valencia

*Voglia di andarci*: _8.0/10_  
*Numero Notti*: _7_  

### Andata: **Sabato-27/09** - _36.99€_  
>**Partenza**: Milano Bergamo **14:40**  
>**Arrivo**: Valencia **16:40**  

### Ritorno: **Domenica-05/10** - _26.19€_  
>**Partenza**: Valencia **09:10**  
>**Arrivo**: Milano Bergamo **11:00**  

__Bagaglio__  
>10kg: 27.75€  

__Costo Medio a notte__  
>90.0€ per 2 persone.  

__Costo Noleggio Veicolo__  
>0.0€ per 6 giorni.  

__Costo Tragitto Casa Aeroporto__  
>130.0€ treno o auto + casello + taxi o bus o navette varie.  

__COSTI per 7 notti__  
>Totale: 823.18€  
>Tot a persona: 411.59€  
>Tot a notte per persona : 59€  

__Notes__: 
>Ricorda di controllare il gli scioperi dei voli
___

## How to Merge your report

Simply write this command  
`python merge_reports.py`

You will find a merged file into the `/merged` directory.
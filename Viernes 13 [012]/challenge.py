"""
DESCRIPTION:

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""

# IMPORTS -----
import calendar


# FUNCTIONS -----

def there_is_friday_13():
    
    # Solicitamos al usuario un mes y un año
    month = int(input("Introduce un mes: "))
    year = int(input("Introduce un año: "))
    
    # Evaluamos si existe un viernes 13 en el mes y año indicados
    text_calendar = calendar.TextCalendar()
    fridays13_in_month = [day[0] for day in text_calendar.itermonthdays2(year, month) if ((day[0] == 13) and (day[1] == 4))]
    if (len(fridays13_in_month) > 0):
        print('*'*30)
        print()
        text_calendar.prmonth(year, month)
        print()
        print('Hay un viernes 13 en el mes y año indicados.')
        print('*'*30)
        return True
    else:
        print('*'*30)
        print()
        text_calendar.prmonth(year, month)
        print()
        print('No hay un viernes 13 en el mes indicado.')
        print('*'*30)
        return False



if __name__ == '__main__':
    
    there_is_friday_13()
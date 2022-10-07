
def get_temperature():
    temperature=input("Enter the temperature:") 
    try:
        temp_number = float(temperature)
        return temp_number
    except:
        print("please enter a number!!")
        return get_temperature() #recursive function
    

def get_unit():
    unit=input("(F)ahrenheit or (C)ilsius or (K)elvin? ")
    if unit.upper() == "K" or unit.upper() == "C" or unit.upper() == "F":
        return unit.upper()
    else:
        print("please enter 'K' or 'F' or 'C'!!")
        return get_unit() #recursive function


def c_otput(temperature, unit):
  if unit == "F":
      print((temperature - 32) / 1.8, "°c and ",((temperature - 32) / 1.8) + 273, "K")
  if unit == "K":
      print((temperature - 273) * 1.8 + 32, "°F and ",(temperature - 273), "°C")
  if unit == "C":
      print((temperature * 1.8 + 32), "°F and ",(temperature+273), "K")







if __name__ == "__main__":

 temperature = get_temperature()
 unit = get_unit()
 c_otput(temperature, unit)
 
input("press any key to exit...")

    








    

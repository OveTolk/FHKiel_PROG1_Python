from flask import Flask, request

app = Flask(__name__)

@app.route("/temperatur")
def umrechnen():
    inFahrenheit = request.args.get("fahrenheit", type=float)
    inCelsius = request.args.get("celsius", type=float)
    inKelvin = request.args.get("kelvin", type=float)
    calcFahrenheit = 0
    calcCelsius = 0
    calcKelvin = 0
    if inFahrenheit:
        calcCelsius = (inFahrenheit - 32) * (5 / 9)
        calcKelvin = calcCelsius + 273.15
        calcFahrenheit = inFahrenheit
    elif inCelsius:
        calcFahrenheit = (inCelsius * (9 / 5)) + 32
        calcKelvin = calcFahrenheit + 273.15
        calcCelsius = inCelsius
    elif inKelvin:
        calcCelsius = inKelvin - 273.15
        calcFahrenheit = (calcCelsius * (9/5)) + 32
        calcKelvin = inKelvin

    return {
            "fahrenheit": calcFahrenheit,
            "celsius": calcCelsius,
            "kelvin": calcKelvin
        }
    
if __name__ == '__main__':
   app.run()

        
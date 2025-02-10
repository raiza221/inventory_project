abstract class TemperatureConverter {
  double convert(double value);
}

class CelsiusToFahrenheit extends TemperatureConverter {
  @override
  double convert(double value) => (value * 9 / 5) + 32;
}

class CelsiusToKelvin extends TemperatureConverter {
  @override
  double convert(double value) => value + 273.15;
}

class TemperatureConversion {
  static double convert(double value, TemperatureConverter converter) {
    return converter.convert(value);
  }
}

void main() {
  var fahrenheitConverter = CelsiusToFahrenheit();
  var kelvinConverter = CelsiusToKelvin();

  print("25°C to Fahrenheit: ${TemperatureConversion.convert(25, fahrenheitConverter)}");
  print("25°C to Kelvin: ${TemperatureConversion.convert(25, kelvinConverter)}");
}

import 'package:test/test.dart';
import 'temperature_converter.dart';

void main() {
  test('Konversi ke Fahrenheit', () {
    expect(TemperatureConversion.convert(25, CelsiusToFahrenheit()), equals(77.0));
  });

  test('Konversi ke Kelvin', () {
    expect(TemperatureConversion.convert(25, CelsiusToKelvin()), equals(298.15));
  });
}

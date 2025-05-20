import xml.etree.ElementTree as ET
import os
print(os.getcwd())

class TemperatureConverter:
       def convert_celsius_to_fahrenheit (self, temperatura_in_celsius):
        """Функция переводит температуру из Цельсия в Фаренгейты по формуле: F = C × 9/5 + 32
    Arguments:
    temperatura_in_celsius - температура в градусах Цельсия
    Returns:
    Tемпература в градусах Фаренгейта
    """
        return 9.0/5.0*temperatura_in_celsius +32 
    
    
class ForecastXMLParser:
    def __init__(self, temperature_convertor):
        """В конструктор передаётся объект класса TemperatureConverter, чтобы использовать его метод конвертации."""
        self.temperature_convertor = temperature_convertor
        
    def parse (self, file):
        """Загружает и парсит XML-файл"""
        # получаем абсолютный путь относительно текущего файла
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, file)
        
        tree = ET.parse(file_path)
        root = tree.getroot()
        for child in root:
            day = child.find("day").text
            temperatura_in_celsius = int(child.find("temperature_in_celsius").text) 
            temperatura_in_fahrenheit = round (self.temperature_convertor.convert_celsius_to_fahrenheit(temperatura_in_celsius), 1)
            # print ("{0}: {1} Celcius, {2} Fahrenheit".format(day, temperatura_in_celsius, temperatura_in_fahrenheit))
            print (f"{day}: {temperatura_in_celsius} Celcius, {temperatura_in_fahrenheit} Fahrenheit")


if __name__== "__main__":
    print ("temp_conv.py запущен по F5 или вручную")
    temperature_convertor = TemperatureConverter()
    forecast_xml_parser=ForecastXMLParser(temperature_convertor)
    forecast_xml_parser.parse("forecast.xml")
    print ()
else:
    print ("temp_conv.py запущен через импорт в другой моуль")
    
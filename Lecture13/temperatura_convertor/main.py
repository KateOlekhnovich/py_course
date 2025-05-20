import temp_conv as tp
def main():
    """Функция создаёт экземпляры классов для конвертации температуры 
    и парсинга прогноза погоды из XML-файла"""
    temperature_convertor = tp.TemperatureConverter()
    forecast_xml_parser=tp.ForecastXMLParser(temperature_convertor)
    forecast_xml_parser.parse("forecast.xml")

if __name__ == "__main__":
    print ("main.py was started \n")
    main()
    
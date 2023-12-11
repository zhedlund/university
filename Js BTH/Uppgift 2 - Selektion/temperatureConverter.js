function convertTemperature(temperature, fromUnit, toUnit) {
	let result;
  
	if (fromUnit === 'Celsius') {
	  if (toUnit === 'Fahrenheit') {
		result = (temperature * 9/5) + 32;
	  } else if (toUnit === 'Kelvin') {
		result = temperature + 273.15;
	  } else {
		result = temperature;
	  }
	} else if (fromUnit === 'Fahrenheit') {
	  if (toUnit === 'Celsius') {
		result = (temperature - 32) * 5/9;
	  } else if (toUnit === 'Kelvin') {
		result = (temperature - 32) * 5/9 + 273.15;
	  } else {
		result = temperature;
	  }
	} else if (fromUnit === 'Kelvin') {
	  if (toUnit === 'Celsius') {
		result = temperature - 273.15;
	  } else if (toUnit === 'Fahrenheit') {
		result = (temperature - 273.15) * 9/5 + 32;
	  } else {
		result = temperature;
	  }
	} else {
	  result = temperature;
	}
  
	return result;
  }
  

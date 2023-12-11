// This file tests the temperatureConverter.js file
const { convertTemperature } = require('./temperatureConverter');

describe('a series of test on temperatureConverter()', () => {
     test('0C should be 32F', () => {
         expect(convertTemperature(0, 'C', 'F')).toEqual(32);
     });

    test('32F should be 0C', () => {
            expect(convertTemperature(32, 'F', 'C')).toEqual(0);
    });

    test('0C should be 273.15K', () => {
        expect(convertTemperature(0, 'C', 'K')).toEqual(273.15);
    });

    test('273.15K should be 0C', () => {
        expect(convertTemperature(273.15, 'K', 'C')).toEqual(0);
    });

    test('32F should be 273.15K', () => {
        expect(convertTemperature(32, 'F', 'K')).toEqual(273.15);
    });

    test('273.15K should be 32F', () => {
        expect(convertTemperature(273.15, 'K', 'F')).toEqual(32);
    });

    test('0C should be 0C', () => {
        expect(convertTemperature(0, 'C', 'C')).toEqual(0);
    });

    test('32F should be 32F', () => {
        expect(convertTemperature(32, 'F', 'F')).toEqual(32);
    });

    test('273.15K should be 273.15K', () => {
        expect(convertTemperature(273.15, 'K', 'K')).toEqual(273.15);
    });
});

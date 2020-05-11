# PythonProjects
A bunch of projects I'm working on to make my life easier with python




## WeatherNotifications.py
A script that uses beautifulsoup, requests and webbrowser modules to get weather data for a given location.
The program uses an apple scripting component to send a text message containing the found weather data to my iphone. 
Location Data is found by scraping for gps coordinates from mylocation.org. 
Weather data is aquired for the location data via an openweathermap API call.



## RSA ENCRYPTION

This project is an exploration into cryptography. 

In rsa.py:
 - An asymmetric encryption function using euclid's extended algorithm, as well as pseudo-random number generator were created
 - This selects prime numbers to be used in the encryption process, and produces a public and private key set for encryption and decryption

In hash.py:
 - The fernet library is used in order to create a password encrypted keyfile (symmetric encryption) in json format
 - the end goal is to be able to store encrypted RSA key sets in a way such that they cannot be infiltrated
 
This project is a work in progress. 
Some User interface features have been added, but there is more that needs to be done to make this a fully usable and secure project.

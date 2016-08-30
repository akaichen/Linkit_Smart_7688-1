#include <Bridge.h>
#include "DHT.h"
#define DHTPIN A0     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11 
DHT dht(DHTPIN, DHTTYPE);

// LED
int ledPin = 5; 

// Dust Sensor
int dustPin = 8; 
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 30000;//sampe 30s ;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;
float concentrationPM25_ugm3;

void setup() 
{
    Serial.begin(9600); 
    dht.begin();
    Bridge.begin();

    // LED
    pinMode(ledPin, OUTPUT);
    //digitalWrite(ledPin, 1);
    //digitalWrite(ledPin, 0);

    // Dust Sensor
    pinMode(dustPin, INPUT);
    starttime = millis();//get the current time;
}

void loop() 
{
    
    float h = dht.readHumidity();
    float t = dht.readTemperature();

    // check if returns are valid, if they are NaN (not a number) then something went wrong!
    if (t >= 25) 
    {
        digitalWrite(ledPin, 1);
    } 
    else 
    {
        digitalWrite(ledPin, 0);
    }

    // check if returns are valid, if they are NaN (not a number) then something went wrong!
    if (isnan(t) || isnan(h)) 
    {
        Serial.println("Failed to read from DHT");
    } 
    else 
    {
        // Dust Sensor
        duration = pulseIn(dustPin, LOW);
        lowpulseoccupancy = lowpulseoccupancy+duration;
        ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
        concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
       
        //concentrationPM25_ugm3 = conversion25(concentration);
        //Serial.print("PM25: ");
        //Serial.print(concentrationPM25_ugm3);
        //Serial.println(" ug/m3");
        //Serial.print("\n");
  
        lowpulseoccupancy = 0;
        starttime = millis();

        Serial.print("concentration: ");
        Serial.print(concentration);
        Serial.print(" pcs/0.01cf");
        Serial.print(" \t");
        Serial.print("Humidity: "); 
        Serial.print(h);
        Serial.print(" %\t");
        Serial.print("Temperature: "); 
        Serial.print(t);
        Serial.println(" *C");

        Bridge.put("d", String(concentration));
        Bridge.put("h", String(h));
        Bridge.put("t", String(t));
        
    }
    delay(1000); //每秒回傳一次資料
}

// convert from particles/0.01 ft3 to μg/m3
float conversion25(long concentrationPM25) {
  double pi = 3.14159;
  double density = 1.65 * pow (10, 12);
  double r25 = 0.44 * pow (10, -6);
  double vol25 = (4/3) * pi * pow (r25, 3);
  double mass25 = density * vol25;
  double K = 3531.5;
  return (concentrationPM25) * K * mass25;
}


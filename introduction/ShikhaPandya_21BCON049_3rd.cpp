#include <Wire.h>
#define commonAnode true
int buzzer = 9;

// Putting RGB which normal eyes recognise

byte gammatable[256];

void longBeep(int freq) 
{

  tone(buzzer, freq, 600);
  delay(900);

  noTone(buzzer);

}


void shortBeep(int freq) {

  tone(buzzer, freq, 200);
  delay(700);
  noTone(buzzer);


}


int convtodecnum(String num)
{
  const int base = 16;     
  unsigned long decnum = 0;
  int i;
  for (i = 0; num.c_str()[i] != '\0' && i < num.length(); i++)
  {

    if (num.c_str()[i] >= 48 && num.c_str()[i] <= 57)   
    {
      decnum += ((num.c_str()[i]) - 48) * pow(base, num.length() - i - 1);
    }
    else if ((num.c_str()[i] >= 65 && num.c_str()[i] <= 70))  
    {
      decnum += (((num.c_str()[i])) - 55) * pow(base, num.length() - i - 1);
    }
    else if (num.c_str()[i] >= 97 && num.c_str() <= 102)  
    {
      decnum += (((num.c_str()[i])) - 87) * pow(base, num.length() - i - 1);
    }

  }
  return decnum;
}

Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);


void setup() {
  Serial.begin(9600);
  Serial.println("Color View Test!");
  pinMode(buzzer, OUTPUT);

  if (tcs.begin()) {
    
  } else {
    Serial.println("No TCS34725 found ... check your connections");
    while (1); 
  }
  
  for (int i = 0; i < 256; i++) {
    float x = i;
    x /= 255;
    x = pow(x, 2.5);
    x *= 255;

    if (commonAnode) {
      gammatable[i] = 255 - x;
    } else {
      gammatable[i] = x;
    }
  }
}

void loop() {
  int rColors[] = {255, 255, 255, 153,
                   255, 255, 255, 153,
                   255, 255, 255, 153, 102,
                   229, 204, 204, 178, 102, 102, 128, 0, 0, 76, 0, 0, 51, 0, 0,
                   204, 204, 102, 102, 102, 0, 0, 0, 0, 0, 0,
                   204, 229, 153, 204, 178, 127, 51,
                   255, 255, 255, 255, 102, 102,
                   255, 224, 192, 160,
                   128, 96, 64, 32, 0
                  };

  int gColors[] = {204, 102, 0, 0,
                   229, 178, 128, 176,
                   255, 255, 255, 153, 102,
                   255, 255, 255, 255, 255, 255, 255, 255, 255, 153, 153, 153, 102, 102, 102,
                   255, 229, 255, 178, 102, 255, 128, 0, 76, 0,
                   204, 204, 153, 153, 102, 0, 0,
                   204, 102, 0, 0, 0, 0,
                   255, 224, 192, 160,
                   128, 96, 64, 32, 0
                  };

  int bColors[] = { 204, 201, 0, 0,
                    204, 102, 0, 0,
                    204, 102, 0, 0, 0,
                    204, 204, 229, 102, 102, 178, 0, 0, 128, 0, 0 , 76, 0, 0, 51,
                    255, 255, 255, 255, 255, 255, 255, 255, 153, 153, 153,
                    255, 255, 255, 255, 255, 255, 102,
                    255,  178, 255, 127, 102, 51,
                    255, 224, 192, 160,
                    128, 96, 64, 32, 0
                  };

  int group[] = {0, 0, 0, 0,
                 1, 1, 1 , 1,
                 2, 2, 2, 2, 2,
                 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
                 5, 5, 5, 5, 5, 5, 5,
                 0,  0, 5, 0, 5, 5,
                 6, 6, 6, 6,
                 7, 7, 7, 7, 7
                };

  int dark[] = {0, 0, 1, 1,
                0, 0, 1, 1,
                0, 0, 0, 1, 1,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                0, 0, 0, 0, 1, 1, 1,
                0,  0, 0, 1, 1,
                0, 0, 1, 1,
                0, 0, 1, 1, 1,
               };
  /*
    int groups[] = { 6, 6, 4, 3, 4, 6, 6, 7, 9, 4, 5, 6, 6,
                   4, 3, 1, 1, 4, 6, 0, 4, 4, 2, 7, 3,
                   3, 5, 3, 1, 5, 0, 0, 3, 7, 1, 4,
                   5, 0, 4, 7, 44, 0, 6, 3, 0, 6, 2, 2, 7,
                   7, 3, 2, 3, 0, 0, 5, 6, 2, 5, 5, 3, 3, 4, 0, 4,
                   2, 7, 7, 3, 0, 1, 4, 4, 7, 7, 4, 2
                 };
    char *hexes[] = { "f0f8ff", "faebd7", "00ffff", "7fffd4", "f0ffff", "f5f5dc", "ffe4c4", "000000", "ffebcd", "0000ff", "8a2be2", "a52a2a", "deb887", "5f9ea0",
                    "7fff00", "d2691e", "ff7f50", "6495ed", "fff8dc", "dc143c", "00ffff", "008b8b", "b8860b", "a9a9a9", "006400", "bdb76b", "8b008b", "556b2f", "ff8c00",
                    "9932cc", "8b0000", "e9967a", "8fbc8f", "483d8b", "2f4f4f", "00ced1", "9400d3", "ff1493", "00bfff", "696969", "1e90ff", "b22222", "fffaf0", "228b22",
                    "ff00ff", "dcdcdc", "f8f8ff", "ffd700", "daa520", "808080",  "008000", "adff2f", "f0fff0", "ff69b4", "cd5c5c", "4b0082", "fffff0", "f0e68c", "e6e6fa", "fff0f5",
                    "7cfc00", "fffacd", "add8e6", "f08080", "e0ffff", "fafad2", "d3d3d3", "d3d3d3", "90ee90", "ffb6c1", "ffa07a", "20b2aa", "87cefa", "778899", "778899", "b0c4de", "ffffe0"
                  };
    /*String hexes[145] = { "f0f8ff", "faebd7", "00ffff", "7fffd4", "f0ffff", "f5f5dc", "ffe4c4", "000000", "ffebcd", "0000ff", "8a2be2", "a52a2a", "deb887", "5f9ea0",
                     "7fff00", "d2691e", "ff7f50", "6495ed", "fff8dc", "dc143c", "00ffff", "008b8b", "b8860b", "a9a9a9", "006400", "bdb76b", "8b008b", "556b2f", "ff8c00",
                     "9932cc", "8b0000", "e9967a", "8fbc8f", "483d8b", "2f4f4f", "00ced1", "9400d3", "ff1493", "00bfff", "696969", "696969", "1e90ff", "b22222", "fffaf0", "228b22",
                     "ff00ff", "dcdcdc", "f8f8ff", "ffd700", "daa520", "808080", "808080", "008000", "adff2f", "f0fff0", "ff69b4", "cd5c5c", "4b0082", "fffff0", "f0e68c", "e6e6fa", "fff0f5",
                     "7cfc00", "fffacd", "add8e6", "f08080", "e0ffff", "fafad2", "d3d3d3", "d3d3d3", "90ee90", "ffb6c1", "ffa07a", "20b2aa", "87cefa", "778899", "778899", "b0c4de", "ffffe0",
                     "00ff00", "32cd32", "faf0e6", "ff00ff", "800000", "66cdaa", "0000cd", "ba55d3", "9370db", "3cb371", "7b68ee", "00fa9a", "48d1cc", "c71585", "191970", "f5fffa", "ffe4e1",
                     "ffe4b5", "ffdead", "000080", "fdf5e6", "808000", "6b8e23", "ffa500", "ff4500", "da70d6", "eee8aa", "98fb98", "afeeee", "db7093", "ffefd5", "ffdab9", "cd853f", "ffc0cb",
                     "dda0dd", "b0e0e6", "800080", "663399", "ff0000", "bc8f8f", "4169e1", "8b4513", "fa8072", "f4a460", "2e8b57", "fff5ee", "a0522d", "c0c0c0", "87ceeb", "6a5acd", "708090",
                     "708090", "fffafa", "00ff7f", "4682b4", "d2b48c", "008080", "d8bfd8", "ff6347", "40e0d0", "ee82ee", "f5deb3", "ffffff", "f5f5f5", "ffff00", "9acd32"
                   };*/
  /*  int groups[145] = { 6, 6, 4, 3, 4, 6, 6, 7, 9, 4, 5, 6, 6,
     4, 3, 1, 1, 4, 6, 0, 4, 4, 2, 7, 3,
     3, 5, 3, 1, 5, 0, 0, 3, 7, 1, 4,
     5, 0, 4, 7, 4, 0, 6, 3, 0, 6, 6, 2, 2, 7,
     7, 3, 2, 3, 0, 0, 5, 6, 2, 5, 5, 3, 3, 4, 0, 4,
     2, 7, 7, 3, 0, 1, 4, 4, 7, 7, 4, 2, 3,
     3, 6, 5, 0, 3, 4, 6, 6, 3, 4, 3, 3, 0,
     4, 6, 0, 2, 6, 4, 6, 3, 3, 1, 1, 5, 2, 3,
     4, 0, 6, 6, 1, 0, 5, 4, 5, 5, 0, 0, 4, 1, 0, 1,
     3, 6, 1, 7, 4, 4, 7, 7, 0, 3, 4, 1, 3, 5, 0, 3, 5, 6,
     6, 6, 2, 3
    };*/

  float red, green, blue;

  tcs.setInterrupt(false);  /

  delay(60); 

  tcs.getRGB(&red, &green, &blue);

  tcs.setInterrupt(true);  

  Serial.print("R:\t"); Serial.print(int(red));
  Serial.print("\tG:\t"); Serial.print(int(green));
  Serial.print("\tB:\t"); Serial.print(int(blue));

  // Serial.print("\t");
  // Serial.print((int)red, HEX); Serial.print((int)green, HEX); Serial.print((int)blue, HEX);
  
  Serial.print("\n");
  int index = 0;
  int smallestDiff = 255;
  int difference = 0;
  for (int x = 0; x < 64; x++) {
    difference = abs(int(red) - rColors[x]) + abs(int(green) - gColors[x]) + abs(int(blue) - bColors[x]);
    if (difference < smallestDiff) {
      smallestDiff = difference;
      index = x;
    }
  }


  Serial.println(group[index]);
  Serial.println(dark[index]);
  int shade = dark[index];
  int type = group[index];
  //Serial.println(hexes[index]);

  switch (type) {

    case 0 : { 
        tone(buzzer, 1200, 200);
        delay(300);
        tone(buzzer, 1200, 900);
        delay(1000);
        tone(buzzer, 1200, 200);
        delay(900);
        break;
      }

    case 1 : {
        tone(buzzer, 1100, 900);
        delay(1000);
        tone(buzzer, 1100, 900);
        delay(1000);
        tone(buzzer, 1100, 900);
        delay(1500);
        break;
      }
    case 2 : {
        tone(buzzer, 1000, 900);
        delay(1000);
        tone(buzzer, 1000, 200);
        delay(300);
        tone(buzzer, 1000, 900);
        delay(1000);
        tone(buzzer, 1000, 900);
        delay(1500);
        break;

      }

    case 3 : {
        tone(buzzer, 900, 900);
        delay(1000);
        tone(buzzer, 900, 900);
        delay(1000);
        tone(buzzer, 900, 200);
        delay(900);
        break;
      }

    case 4 : {

        tone(buzzer, 800, 900);
        delay(1000);
        tone(buzzer, 800, 200);
        delay(300);
        tone(buzzer, 800, 200);
        delay(300);
        tone(buzzer, 800, 200);
        delay(900);
        break;

      }

    case 5 : {

        tone(buzzer, 700, 200);
        delay(300);
        tone(buzzer, 700, 200);
        delay(300);
        tone(buzzer, 700, 200);
        delay(300);
        tone(buzzer, 700, 900);
        delay(1500);
        break;
      }

    case 6 : {

        tone(buzzer, 600, 200);
        delay(300);
        tone(buzzer, 600, 900);
        delay(1000);
        tone(buzzer, 600, 900);
        delay(1500);
        break;

      }

    case 7 : {
        tone(buzzer, 500, 900);
        delay(1000);
        tone(buzzer, 500, 200);
        delay(300);
        tone(buzzer, 500, 200);
        delay(300);
        tone(buzzer, 500, 200);
        delay(900);
        break;
      }


  }
}

//  Serial.print("C:\t"); Serial.print(int(clear));
//  Serial.print("R:\t"); Serial.print(int(red));
//  Serial.print("\tG:\t"); Serial.print(int(green));
//  Serial.print("\tB:\t"); Serial.print(int(blue));
//  Serial.println();

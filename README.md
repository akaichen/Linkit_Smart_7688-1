# Programs running on LinkIt Smart 7688 Duo that connects to IoT Platform
     
## 【 Overview 】       
                                                                  
* 物聯網架構與應用                 
                                                                                                                                           
![Imgur](http://i.imgur.com/xLnaQpC.png)
                                  
* 通訊協定與網路服務提供商             
                            
| 通訊協定 | 網路服務提供商 |
|---|---|
| HTTP | ThingSpeak、MediaTek Cloud Sandbox (MCS)、Google Firebase |
| MQTT | ThingSpeak、LASS、MediaTek Cloud Sandbox (MCS)、AWS IoT、IBM Bluemix IoT Platform |
| WebSocket | WoT.City |
                
* 實作架構  
![Imgur](http://i.imgur.com/WFNcC1p.png)
    
## 【 檔案說明 】
      
| 編號 | 資料夾 |  檔案名稱 | 說明  |
|---|---|---|---|
|1| /Basic  |  /ApMode_StationMode/apModeToStationMode.sh | 將 AP Mode 轉 Station Mode  |
|2| /Basic  |  /ApMode_StationMode/stationModeToApMode.sh | 將 Station Mode 轉 AP Mode  |
|3| /Basic  | /Get_MacAddress/Arduino/sketch_get_macAddress.ino  | 透過 Wi-Fi 按鈕取得 IP 或 Mac Address  |
|4| /IoT Cloud  |  /Arduino/getDHT/getDHT.ino | 取得 DHT 資料  |
|5| /IoT Cloud  |  /Arduino/DHT_OLED/DHT_OLED.ino |  將 DHT 資料顯示於 OLED |
|6| /IoT Cloud  |  /Arduino/getDUST/getDUST.ino |  取得 DUST 資料 |
|7| /IoT Cloud  |  /Arduino/DHT_DUST_OLED/DHT_DUST_OLED.ino |  將 DHT 與 DUST 資料顯示於 OLED |
|8| /IoT Cloud  |  /Arduino/getDHT_Bridge/getDHT_Bridge.ino |  將 DHT 的資料傳送到 MPU |
|9| /IoT Cloud  |  /Python/getSensorData.py | 從 MCU 取得 Sensor Data |
|10| /IoT Cloud  |  /Python/linkit_Smart_7688_MCS_MQTT.py | 將  Sensor Data 透過 MQTT 傳送到 MCS |
|11| /IoT Cloud  |  /Python/get_data_from_mcs_mqtt.py | 從 MCS 取得  Sensor Data |
|12| /IoT Cloud  |  /Python/linkit_Smart_7688_MCS.py | 將  Sensor Data 透過 API 傳送到 MCS |
|13| /IoT Cloud  |  /Python/linkit_Smart_7688_Thingspeak.py | 將  Sensor Data 傳送到 ThingSpeak |
|14| /IoT Cloud  |  /Python/linkit_Smart_7688_LASS.py | 將  Sensor Data 傳送到 LASS |
|15| /IoT Cloud  |  /Python/lass_to_thingspeak.py | 將 LASS 的資料傳送到 ThingSpeak |
|16| /IoT Cloud  |  /Python/linkit_Smart_7688_AWS_IoT.py | 將 Sensor Data 傳送到  AWS IoT |
|17| /IoT Cloud  |  /Python/linkit_Smart_7688_WoTCity.py | 將  Sensor Data 傳送到   WoT.City |
|18| /IoT Cloud  |  /Python/get_data_from_wot.py | 從 WoT.City 取得資料 |
|19| /IoT Cloud  |  /Python/linkit_Smart_7688_IBM_Bluemix_Publish.py | 將  Sensor Data 傳送到  IBM Bluemix |
|20| /IoT Cloud  |  /Python/linkit_Smart_7688_IBM_Bluemix_Subscribe.py | 從 IBM Bluemix 取得資料 |
|21| /IoT Cloud  |  /Python/linkit_Smart_7688_Firebase.py | 將  Sensor Data 傳送到 Google Firebase |

## 【 Board and Sensor 】

* [LinkIt Smart 7688 Duo](https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html)
* [Arduino Breakout for LinkIt Smart 7688 Duo](https://www.seeedstudio.com/Arduino-Breakout-for-LinkIt-Smart-7688-Duo-p-2576.html)
* [Grove - Temperature & Humidity Sensor](https://www.seeedstudio.com/Grove-Temp%26Humi-Sensor-p-745.html)
* [Grove - Dust Sensor](https://www.seeedstudio.com/Grove-Dust-Sensor-p-1050.html)
* [Grove - OLED Display 1.12"](https://www.seeedstudio.com/Grove-OLED-Display-1.12%22-p-824.html)

## 【 Pin-out Diagram 】
![Imgur](http://i.imgur.com/3fXpr8O.png)

## 【 Integrated Development Environment - IDE 】
 
 * Arduino
   *  [Arduino IDE v1.6.4](https://www.arduino.cc/en/Main/OldSoftwareReleases)
 * Python
   * [Sublime Text](https://www.sublimetext.com/)
   * [Visual Studio Code](https://code.visualstudio.com/b?utm_expid=101350005-27.GqBWbOBuSRqlazQC_nNSRg.1&utm_referrer=https%3A%2F%2Fwww.google.com.tw%2F)
   * [Jupyter](http://jupyter.org/)
     * Command: ipython notebook

## 【 Firmware 】
* [Download](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/downloads)

## 【 Library 】

* DHT ( DHT sensor library by Adafruit Version: 1.2.3 )
   *  在 Arduino Sketch 中點選```草稿碼``` ➙ ```匯入程式庫``` ➙ ```管理程式庫``` ➙ 右上角搜尋欄位輸入 ```DHT``` ➙ 選擇 ```DHT sensor library by Adafruit Version: 1.2.3```
* Seeed OLED Display 128*64 library
   *  到 [Seeed OLED library Github](https://github.com/Seeed-Studio/OLED_Display_128X64) 頁面中的右上角下載整個 ZIP 檔
   *  在 Arduino Sketch 中點選```草稿碼``` ➙ ```匯入程式庫``` ➙ ```加入 .ZIP 程式庫```  ➙ 選擇上一步驟所下載的 ZIP 檔
      
## 【 Service 】

* [WoT.City](https://wotcity.com/)
* [Amazon Web Services Cloud](https://aws.amazon.com/tw/)
* [Google Firebase](https://firebase.google.com/)
* [IBM Bluemix](https://console.ng.bluemix.net/)
* [MediaTek Cloud Sandbox](https://mcs.mediatek.com)
* [ThingSpeak](https://thingspeak.com/)
* [ThinkSpeak Data Visualization](nrl.iis.sinica.edu.tw/LASS/PM25.php?site=III&city=台北市&district=信義區&channel=152239&apikey=9ND1FVDPKLQGPDRI)

## 【 Reference 】

* [Get Started with the LinkIt Smart 7688](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-development-board)
* [Get Started with the LinkIt Smart 7688 Duo](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-duo-development-board)
* [LinkIt Smart 7688 Developer’s Guide](https://labs.mediatek.com/en/download/ih80Qtjo)

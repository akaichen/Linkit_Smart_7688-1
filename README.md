# Programs running on LinkIt Smart 7688 Duo that connects to IoT Platform
    
## 【 Overview 】
        
* 物聯網架構與應用
 
![Imgur](http://i.imgur.com/wXvCki9.png)

* 通訊協定與網路服務提供商

| 通訊協定 | 網路服務提供商 |
|---|---|
| HTTP | ThingSpeak、MediaTek Cloud Sandbox (MCS)、Google Firebase |
| MQTT | LASS、MediaTek Cloud Sandbox (MCS)、AWS IoT、IBM Bluemix IoT Platform |
| WebSocket | WoT.City |

* 實作架構
![Imgur](http://i.imgur.com/WFNcC1p.png)

## 【 Board and Sensor 】

* [LinkIt Smart 7688 Duo](https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html)
* [Arduino Breakout for LinkIt Smart 7688 Duo](https://www.seeedstudio.com/Arduino-Breakout-for-LinkIt-Smart-7688-Duo-p-2576.html)
* [Grove - Temperature & Humidity Sensor](https://www.seeedstudio.com/Grove-Temp%26Humi-Sensor-p-745.html)
* [Grove - Dust Sensor](https://www.seeedstudio.com/Grove-Dust-Sensor-p-1050.html)
* [Grove - OLED Display 1.12"](https://www.seeedstudio.com/Grove-OLED-Display-1.12%22-p-824.html)

## 【 Integrated Development Environment - IDE 】

 * Python
   * [Sublime Text](https://www.sublimetext.com/)
   * [Visual Studio Code](https://code.visualstudio.com/b?utm_expid=101350005-27.GqBWbOBuSRqlazQC_nNSRg.1&utm_referrer=https%3A%2F%2Fwww.google.com.tw%2F)
   * [Jupyter](http://jupyter.org/)
     * Command: ipython notebook
 * Arduino
   *  [Arduino IDE v1.6.5](https://www.arduino.cc/en/Main/OldSoftwareReleases)

## 【 Library 】

* [Seeed OLED Display 128*64 library](https://github.com/Seeed-Studio/OLED_Display_128X64)
* DHT

## 【 Service 】

* [WoT.City](https://wotcity.com/)
* [Amazon Web Services Cloud](https://aws.amazon.com/tw/)
* [Google Firebase](https://firebase.google.com/)
* [IBM Bluemix](https://console.ng.bluemix.net/)
* [MediaTek Cloud Sandbox](https://mcs.mediatek.com)
* [ThingSpeak](https://thingspeak.com/)
* [ThinkSpeak Data Visualization](nrl.iis.sinica.edu.tw/LASS/PM25.php?site=III&city=台北市&district=信義區&channel=152239&apikey=9ND1FVDPKLQGPDRI)

## 【 Reference 】

* [MediaTek LinkIt™ Smart 7688](https://labs.mediatek.com/site/global/developer_tools/mediatek_linkit_smart_7688/whatis_7688/index.gsp)
* [MediaTek LinkIt™ Smart 7688 Developer's Guide](http://labs.mediatek.com/fileMedia/download/87c801b5-d1e6-4227-9a29-b5421f2955ac)
* [MediaTek Cloud Sandbox (MCS)](https://mcs.mediatek.com/resources/zh-TW/latest/api_references/)
* [LASS （Location Aware Sensing System）](http://lass-net.org/)
* [LASS - Data specification](https://lass.hackpad.com/LASS-Data-specification-1dYpwINtH8R)
* [LASS - How to get data log from server](https://lass.hackpad.com/How-to-get-data-log-from-server-Ztu9mpUsGL9)

## 【 Firmware and Software 】
 * Linkit Smart 7688
   *  [Firmware](https://labs.mediatek.com/site/global/developer_tools/mediatek_linkit_smart_7688/sdt_intro/index.gsp)

## 【 Tools 】
 * Windows 作業系統
   *  登入
      * Windows 端
        * [Putty](https://the.earth.li/~sgtatham/putty/latest/x86/putty.exe)
   *  傳送檔案 
      * Windows 端
        * [FileZilla Client](https://filezilla-project.org/)
      * Linkit Smart 7688 端
        * ```opkg update```
        * ```opkg install openssh-sftp-server```   
 * macOS 作業系統
   *  登入 / 傳送檔案（本地端到 Linkit Smart 7688 端）- 終端機
      * 登入（在本地端電腦的終端機執行） ➙ ```ssh root@IP```
      * 傳送檔案（在本地端電腦的終端機執行） ➙ ```scp 在電腦中的檔案位置 root@IP:要傳送到 Linkit Smart 7688 中的位置```

## 【 JSON Tools 】
 * [JSON Lint](http://jsonlint.com/)
 * [JSON Editor Online](http://www.jsoneditoronline.org/)

## 【 Troubleshooting 】
 * 如果在瀏覽器輸入所設定的 local domain ( 預設為 ```http://mylinkit.local``` ) 後無法顯示設定頁時
   *  請安裝 [Bonjour Print Services](https://support.apple.com/kb/dl999?locale=zh_TW)
   *  再重新在瀏覽器輸入所設定的 local domain 
 * 當登入時發生 ```WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!``` 錯誤
   * 於終端機輸入 ```ssh-keygen -R IP位置 ```
   * 再重新 Login
   
## 【 Blog 】
* [Archer @ 部落格](https://github.com/ArcherHuang/MyBlog/blob/master/README.md)

## 【 License 】

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# LineBot for my mom
## Introduction
My mom was worked in Central Weather Bureau (Taiwan, R.O.C).    
She resigned in my childhood to take care of me and my brother, but she still cares deeply about the weather.   
Now, She download the [weather card](https://www.cwb.gov.tw/m/sv/ecardFB.php?ecls=5) and push on our family LINE group everyday.   
Real screenshot:    
<a href="https://imgur.com/EiPasSV"><img src="https://i.imgur.com/EiPasSV.png"  width = "300" height = "500" title="source: imgur.com" /></a>

---

Weather Card Example ([Source](https://www.cwb.gov.tw/m/sv/images/st/ecard_mfc01_6300500_20181015171124.jpg)):   
<a href="https://imgur.com/ZuDZMcm"><img src="https://i.imgur.com/ZuDZMcm.jpg" width = "300" height = "250" title="source: imgur.com" /></a>

---

I think this is very complicated and boring job.       
So I use what I have learned to create a LineBot for her. It can automatically reply the weather card when the user enters the city name.   
This project is use Python to create, and complete with [Heroku](https://www.heroku.com).   
Result:   
![result](https://i.imgur.com/TEZndnz.gif)

---

## Method
I can't introduce it in a limited space. I will briefly summarize all the steps, please use [Google](https://www.google.com) for the detailed part.
1. Login [LINE Developers](http://developers.line.me/en/)
2. Register LineBot
3. Get LineBot token
4. write code
5. Register Heroku account
6. push to Heroku
7. Concatenation LineBot to Heroku
8. Done
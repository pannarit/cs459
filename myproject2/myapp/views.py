
from django.shortcuts import render

from django.http import HttpResponse
import datetime
from .models import Item
from django.template import loader

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def item_list(request):
    html='''

<title>Fruit Shop</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<style>
.mySlides {display:none;}
body {margin:25px;}

div.polaroid {
  width: 30%;
  background-color: white;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  margin-bottom: 25px;
}

div.container {
  text-align: center;
  padding: 10px 20px;
}

</style>
<body>

<h1 class="w3-center"><font face="Chilanka" color="green">Welcome to My Fruit Shop</font></h1>

<div class="w3-content w3-display-container">
  <img class="mySlides" src="http://yesofcorsa.com/wp-content/uploads/2015/08/1471_fruit.jpg" style="width:100%">
  <img class="mySlides" src="http://yesofcorsa.com/wp-content/uploads/2015/08/2553_fruit.jpg" style="width:100%">
  <img class="mySlides" src="http://yesofcorsa.com/wp-content/uploads/2015/08/4908_fruit.jpg" style="width:100%">

  <button class="w3-button w3-black w3-display-left" onclick="plusDivs(-1)">&#10094;</button>
  <button class="w3-button w3-black w3-display-right" onclick="plusDivs(1)">&#10095;</button>
</div>

<script>
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}

</script>

<br><br><center>
</body>

'''


    for i in Item.objects.all():
        html = html + '<div><img style="border-top:20px solid black;border-right:1px solid black;border-bottom:20px solid black;border-left:1px solid black;" src="https://cdn-ssl.vidible.tv/prod/2015-04/06/55224e34e4b025fd8795401d_cv1.jpg" width="225" height="151" /><h3>%s </h3>%s %s %s</div>'%(i.name, i.description, i.price, i.expire)
    return HttpResponse(html)
     
   

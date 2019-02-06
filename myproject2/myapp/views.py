
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

<head>
<title>Fruit Shop</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta content="text/html; charset=iso-8859-2" http-equiv="Content-Type">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<style>
.mySlides {display:none;}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
<style>
* {
  box-sizing: border-box;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 50%;
  padding: 10px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
/* Style the buttons */
.btn {
  border: none;
  outline: none;
  padding: 12px 16px;
  background-color: #f1f1f1;
  cursor: pointer;
}

.btn:hover {
  background-color: #ddd;
}

.btn.active {
  background-color: #666;
  color: white;
}
 {
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Style the header */
header {
  background-color: #666;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
}

/* Create two columns/boxes that floats next to each other */
nav {
  float: left;
  width: 30%;
  height: 1260px; /* only for demonstration, should be removed */
  background: #ccc;
  padding: 20px;
}

/* Style the list inside the menu */
nav ul {
  list-style-type: none;
  padding: 0;
}

article {
  float: left;
  padding: 20px;
  width: 70%;
  background-color: #f1f1f1;
  height: auto; /* only for demonstration, should be removed */
}

/* Clear floats after the columns */
section:after {
  content: "";
  display: table;
  clear: both;
  height:auto;
}

/* Style the footer */
footer {
  background-color: #777;
  padding: 10px;
  text-align: center;
  color: white;
}

/* Responsive layout - makes the two columns/boxes stack on top of each other instead of next to each other, on small screens */
@media (max-width: 600px) {
  nav, article {
    width: 100%;
    height: auto;
  }
}
</style>


</style>
</head>

<body>

<h2 class="w3-center"><font face="Chilanka" color="green">Welcome to My Fruit Shop</font></h2>

<div class="w3-content w3-section" style="max-width:800px">
  <img class="mySlides" src="http://yesofcorsa.com/wp-content/uploads/2015/08/1471_fruit.jpg" style="width:100%">
  <img class="mySlides" src="http://yesofcorsa.com/wp-content/uploads/2015/08/2553_fruit.jpg" style="width:100%">
  <img class="mySlides" src="http://yesofcorsa.com/wp-content/uploads/2015/08/4908_fruit.jpg" style="width:100%">
</div>

<script>
var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 2000); // Change image every 2 seconds
}
</script>

<section>
  <nav>
    <ul>
      <li><a href="#">HOME</a></li>
      <li><a href="#">ADMIN</a></li>
      <li><a href="#">SHOP</a></li>
      <li><a href="#">CONTACT</a></li>
    </ul>
  </nav>
  
  <article>
    <h1>Product</h1>
    '''
 


    for i in Item.objects.all():
        html = html + '<center><div><img style="border-top:20px solid black;border-right:1px solid black;border-bottom:20px solid black;border-left:1px solid black;" src="https://cdn-ssl.vidible.tv/prod/2015-04/06/55224e34e4b025fd8795401d_cv1.jpg" width="225" height="151" /><h3>%s </h3>%s %s %s</div> '%(i.name, i.description, i.price, i.expire)
    return HttpResponse(html)
     
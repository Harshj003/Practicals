import 'package:flutter/material.dart'; 
void main() => runApp(MyApp()); 
class MyApp extends StatelessWidget { 
// It is the root widget of your application. 
@override 
Widget build(BuildContext context) { 
return MaterialApp( 
title: 'Flutter Demo Application', theme: 
ThemeData( 
primarySwatch: Colors.green, 
), 
home: MyHomePage(title: 'Complex 
layout example'), 
); 
} 
} 
class MyHomePage extends 
StatelessWidget { MyHomePage({Key? 
key, required this.title}) : super(key: key); 
final String title; 
@override 
Widget build(BuildContext context) { 
return Scaffold( 
appBar: AppBar(title: Text("Product 
List")), body: GridView.count( 
crossAxisCount: 5, 
crossAxisSpacing: 4.0, 
mainAxisSpacing: 8.0, 
padding: const EdgeInsets.fromLTRB(3.0, 
12.0, 3.0, 12.0), children: <Widget>[ 
ProductBox( name: "iPhone", 
description: "iPhone is the top branded 
phone ever", price: 55000, 
image: "download1.jpeg"), ProductBox( 
name: "Android", 
description: "Android is a very stylish 
phone", price: 10000, 
image: "download4.jpeg"), ProductBox( 
name: "Tablet", 
description: "Tablet is a popular device for 
official meetings", 
price: 25000, 
image: "download2.jpeg"), ProductBox( 
name: "Laptop", 
description: "Laptop is most famous 
electronic device", price: 35000, 
image: "download3.jpeg"), ProductBox( 
name: "Desktop", 
description: "Desktop is most popular for 
regular use", price: 10000, 
image: "download5.jpg"), 
], 
)); 
} 
} 
class ProductBox extends StatelessWidget 
{ ProductBox( 
{Key? key, 
required this.name, required 
this.description, required this.price, 
required this.image}) 
: super(key: key); final String name; 
final String description; final int price; 
final String image; 
Widget build(BuildContext context) { 
return Container( 
padding: EdgeInsets.all(2), height: 110, 
child: Card( child: Column( 
mainAxisAlignment: 
MainAxisAlignment.spaceEvenly, 
children: <Widget>[ 
Image.asset("assets/" + image), Expanded( 
child: Container( 
padding: EdgeInsets.all(5), child: Column( 
mainAxisAlignment: 
MainAxisAlignment.spaceEvenly, 
children: <Widget>[ 
Text(this.name, 
style: TextStyle(fontWeight: 
FontWeight.bold)), Text(this.description), 
Text("Price: " + this.price.toString()), 
], 
))) 
]))); 
} 
}

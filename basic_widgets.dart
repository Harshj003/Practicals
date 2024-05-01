import 'package:flutter/material.dart';
void main() => runApp(MaterialApp(
 home: IdCard(),
 ));
class IdCard extends StatelessWidget {
 @override
 Widget build(BuildContext context) {
 return Scaffold(
 backgroundColor: Colors.grey[900],
 appBar: AppBar(
 title: Text('TE-IT ID Card'),
 centerTitle: true,
 backgroundColor: Colors.grey[850],
 elevation: 0.0,
 ),
 body: Padding(
 padding: const EdgeInsets.fromLTRB(30.0, 40.0, 30.0, 0),
 child: Column(
 crossAxisAlignment: CrossAxisAlignment.start,
 children: <Widget>[
 Center(
 child: CircleAvatar(
 radius: 40.0,
 backgroundImage: AssetImage('thumb.jpg'),
 ),
 ),
 Divider(
 color: Colors.grey[800],
 height: 60.0,
 ),
Text(
 'NAME',
 style: TextStyle(
 color: Colors.grey,
 letterSpacing: 2.0,
 ),
 ),
 SizedBox(height: 10.0),
 Text(
 'Sarvesh Suhas Takle',
 style: TextStyle(
 color: Colors.amberAccent[200],
 fontWeight: FontWeight.bold,
 fontSize: 28.0,
 letterSpacing: 2.0,
 ),
 ),
 SizedBox(height: 30.0),
 Text(
 'HOMETOWN',
 style: TextStyle(
 color: Colors.grey,
 letterSpacing: 2.0,
 ),
 ),
 SizedBox(height: 10.0),
 Text(
 'Kalwa -Thane-Maharashtra-India',
 style: TextStyle(
 color: Colors.amberAccent[200],
fontWeight: FontWeight.bold,
 fontSize: 28.0,
 letterSpacing: 2.0,
 ),
 ),
 SizedBox(height: 30.0),
 Text(
 'Current Academic Year',
 style: TextStyle(
 color: Colors.grey,
letterSpacing: 2.0,
 ),
 ),
 SizedBox(height: 10.0),
 Text(
 '2023-2024',
 style: TextStyle(
 color: Colors.amberAccent[200],
 fontWeight: FontWeight.bold,
 fontSize: 28.0,
letterSpacing: 2.0,
 ),
 ),
 SizedBox(height: 30.0),
 Row(
 children: <Widget>[
Icon(
 Icons.email,
color: Colors.grey[400],
 ),
 SizedBox(width: 10.0),
 Text(
 'sarvesh@apsit.edu.in',
style: TextStyle(
 color: Colors.grey[400],
fontSize: 18.0,
letterSpacing: 1.0,
 ),
 )
 ],
 ),
 ],
 ),
 ),
 );
 }
}

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'login_screen.dart';
class HomeScreen extends StatefulWidget {
 const HomeScreen({Key? key}) : super(key: key);
 @override
 _HomeScreenState createState() => _HomeScreenState();
}
class _HomeScreenState extends State<HomeScreen> {
 User? user = FirebaseAuth.instance.currentUser;
 @override
 void initState() {
 super.initState();
 FirebaseFirestore.instance.collection("users").doc(user!.uid).get().then((value) {
 setState(() {});
 });
 }
 @override
 Widget build(BuildContext context) {
 return Scaffold(
 appBar: AppBar(
 title: const Text("Welcome"),
 centerTitle: true,
 ),
 body: Center(
 child: Padding(
 padding: EdgeInsets.all(20),
 child: Column(
 mainAxisAlignment: MainAxisAlignment.center,
 crossAxisAlignment: CrossAxisAlignment.center,
 children: <Widget>[
 SizedBox(
 height: 150,
 child: Image.asset("assets/logo.png", fit: BoxFit.contain),
 ),
 Text(
 "Welcome Back",
 style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
 ),
 SizedBox(
 height: 10,
 ),
 SizedBox(
 height: 15,
 ),
 ActionChip(
 label: Text("Logout"),
 onPressed: () {
 logout(context);
 }),
 ],
 ),
 ),
 ),
 );
 }
 // the logout function
 Future<void> logout(BuildContext context) async {
 await FirebaseAuth.instance.signOut();
 Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (context) => 
LoginScreen()));
 }
}

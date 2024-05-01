import 'package:flutter/material.dart';
void main() => runApp(const MyApp());
class MyApp extends StatelessWidget {
 const MyApp({super.key});
 @override
 Widget build(BuildContext context) {
 const appTitle = 'Form Validation Demo';
 return MaterialApp(
 title: appTitle,
 home: Scaffold(
 appBar: AppBar(
 title: const Text(appTitle),
 ),
 body: const MyCustomForm(),
 ),
 );
 }
}
class MyCustomForm extends StatefulWidget {
 const MyCustomForm({super.key});
 @override
 MyCustomFormState createState() {
 return MyCustomFormState();
 }
}
class MyCustomFormState extends State<MyCustomForm> {
 final _formKey = GlobalKey<FormState>();
 @override
 Widget build(BuildContext context) {
 return Form(
 key: _formKey,
 child: Column(
 crossAxisAlignment: CrossAxisAlignment.start,
 children: [
 Padding(
 padding: const EdgeInsets.all(8.0),
 child: TextFormField(
 decoration: InputDecoration(
 labelText: "Name",
 hintText: "Enter your Name",
 border: OutlineInputBorder(borderRadius: BorderRadius.circular(10.0)),
 ),
 validator: (value) {
 if (value == null || value.isEmpty) {
 return 'Enter your Name: ';
 }
 return null;
 },
 ),
 ),
 Padding(
 padding: const EdgeInsets.all(8.0),
 child: TextFormField(
 decoration: InputDecoration(
 labelText: "Mobile Number",
 hintText: "Enter your Name",
 border: OutlineInputBorder(borderRadius: BorderRadius.circular(10.0)),
 ),
 validator: (value) {
 if (value == null || value.isEmpty) {
 return 'Enter your Mobile Number: ';
 }
 if (value.length != 10) {
 return "Please Enter Correct Digits";
 }
 return null;
 },
 ),
 ),
 Padding(
 padding: const EdgeInsets.all(8.0),
 child: TextFormField(
 obscureText: true,
 validator: (value) {
 if (value == null || value.isEmpty) {
 return 'Enter your Password ';
 }
 return null;
 },
 ),
 ),
 Padding(
 padding: const EdgeInsets.symmetric(vertical: 16.0),
 child: ElevatedButton(
 onPressed: () {
 // Validate returns true if the form is valid, or false otherwise.
 if (_formKey.currentState!.validate()) {
 ScaffoldMessenger.of(context).showSnackBar(
 const SnackBar(content: Text('Login Successful')),
 );
 }
 },
 child: const Text('Submit'),
 ),
